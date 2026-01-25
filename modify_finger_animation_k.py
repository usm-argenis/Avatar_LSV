"""
Script para modificar animación de huesos en archivos GLB
CONFIGURABLE: Define huesos, frames y coordenadas en la sección de configuración
"""

import json
import struct
import math
from pathlib import Path

# ============================================================================
# CONFIGURACIÓN - MODIFICAR AQUÍ
# ============================================================================

# Lista de archivos a procesar
# Puedes agregar todos los avatares que necesites
INPUT_FILES = [
    r'test\output\glb\Duvall\alfabeto\Duvall_resultado_c.glb',
    r'test\output\glb\Luis\alfabeto\Luis_resultado_c.glb',
    # Agrega más archivos aquí:
    # r'test\output\glb\Nancy\alfabeto\Nancy_resultado_a.glb',
    # r'test\output\glb\Carla\alfabeto\Carla_resultado_a.glb',
]

# Rango de frames a modificar (1-indexed, como en Blender)
FRAME_START = 20  # Primer frame a modificar
FRAME_END = 35    # Último frame a modificar
FRAME_CENTER = 27 # Frame central con coordenadas exactas

# Huesos a modificar con sus coordenadas objetivo en formato Blender (W, X, Y, Z)
# Puedes agregar o quitar huesos según necesites
TARGET_COORDS_BLENDER = {
    'RightHandIndex1': [0.987, 0.002, -0.042, 0.155],
    'RightHandPinky2': [0.964, 0.072, 0.222, 0.087],
    'RightHandPinky1': [0.923, 0.266, -0.139, -0.239],
    'RightHandPinky3': [0.985, 0.141, 0.074, 0.062],
    # Agrega más huesos aquí si necesitas:
    # 'RightHandThumb1': [W, X, Y, Z],
    # 'LeftArm': [W, X, Y, Z],
}


# Sufijo para el archivo de salida (se agrega antes de .glb)
OUTPUT_SUFFIX = '_MODIFIED'

# ============================================================================
# FIN DE CONFIGURACIÓN
# ============================================================================

def read_glb(file_path):
    """Lee un archivo GLB y extrae el JSON y los datos binarios."""
    with open(file_path, 'rb') as f:
        # Leer encabezado GLB
        magic = f.read(4)
        version = struct.unpack('<I', f.read(4))[0]
        length = struct.unpack('<I', f.read(4))[0]
        
        # Leer chunk JSON
        json_chunk_length = struct.unpack('<I', f.read(4))[0]
        json_chunk_type = f.read(4)
        json_data = json.loads(f.read(json_chunk_length).decode('utf-8'))
        
        # Leer chunk binario
        bin_chunk_length = struct.unpack('<I', f.read(4))[0]
        bin_chunk_type = f.read(4)
        bin_data = bytearray(f.read(bin_chunk_length))
    
    return json_data, bin_data

def write_glb(file_path, json_data, bin_data):
    """Escribe un archivo GLB."""
    json_str = json.dumps(json_data, separators=(',', ':'))
    json_bytes = json_str.encode('utf-8')
    json_padding = (4 - len(json_bytes) % 4) % 4
    json_bytes += b' ' * json_padding
    
    bin_padding = (4 - len(bin_data) % 4) % 4
    bin_data = bytes(bin_data) + b'\x00' * bin_padding
    
    total_length = 12 + 8 + len(json_bytes) + 8 + len(bin_data)
    
    with open(file_path, 'wb') as f:
        f.write(b'glTF')
        f.write(struct.pack('<I', 2))
        f.write(struct.pack('<I', total_length))
        f.write(struct.pack('<I', len(json_bytes)))
        f.write(b'JSON')
        f.write(json_bytes)
        f.write(struct.pack('<I', len(bin_data)))
        f.write(b'BIN\x00')
        f.write(bin_data)

def get_accessor_data(json_data, bin_data, accessor_index):
    """Obtiene los datos de un accessor."""
    accessor = json_data['accessors'][accessor_index]
    buffer_view = json_data['bufferViews'][accessor['bufferView']]
    
    byte_offset = buffer_view.get('byteOffset', 0) + accessor.get('byteOffset', 0)
    count = accessor['count']
    
    component_type = accessor['componentType']
    type_str = accessor['type']
    
    type_map = {'SCALAR': 1, 'VEC2': 2, 'VEC3': 3, 'VEC4': 4}
    components = type_map[type_str]
    
    format_map = {5126: 'f'}
    format_char = format_map.get(component_type, 'f')
    
    values = []
    bytes_per_component = struct.calcsize(format_char)
    for i in range(count):
        offset = byte_offset + i * components * bytes_per_component
        data = struct.unpack(f'<{components}{format_char}', bin_data[offset:offset + components * bytes_per_component])
        values.append(list(data))
    
    return values

def set_accessor_data(json_data, bin_data, accessor_index, values):
    """Escribe datos en un accessor."""
    accessor = json_data['accessors'][accessor_index]
    buffer_view = json_data['bufferViews'][accessor['bufferView']]
    
    byte_offset = buffer_view.get('byteOffset', 0) + accessor.get('byteOffset', 0)
    
    type_str = accessor['type']
    type_map = {'SCALAR': 1, 'VEC2': 2, 'VEC3': 3, 'VEC4': 4}
    components = type_map[type_str]
    
    format_char = 'f'
    bytes_per_component = struct.calcsize(format_char)
    
    for i, value in enumerate(values):
        offset = byte_offset + i * components * bytes_per_component
        packed = struct.pack(f'<{components}{format_char}', *value)
        bin_data[offset:offset + len(packed)] = packed

def slerp(q1, q2, t):
    """Interpolación esférica entre dos quaternions."""
    dot = sum(a * b for a, b in zip(q1, q2))
    
    if dot < 0.0:
        q2 = [-x for x in q2]
        dot = -dot
    
    if dot > 0.9995:
        result = [q1[i] + t * (q2[i] - q1[i]) for i in range(4)]
        mag = math.sqrt(sum(x * x for x in result))
        return [x / mag for x in result]
    
    dot = max(-1.0, min(1.0, dot))
    theta = math.acos(dot)
    sin_theta = math.sin(theta)
    
    w1 = math.sin((1.0 - t) * theta) / sin_theta
    w2 = math.sin(t * theta) / sin_theta
    
    result = [w1 * q1[i] + w2 * q2[i] for i in range(4)]
    return result

def find_bone_rotation_sampler(json_data, bone_name):
    """Encuentra el sampler de rotación para un hueso específico."""
    animation = json_data['animations'][0]
    
    for channel_idx, channel in enumerate(animation['channels']):
        node_idx = channel['target']['node']
        node = json_data['nodes'][node_idx]
        
        if node.get('name') == bone_name and channel['target']['path'] == 'rotation':
            sampler_idx = channel['sampler']
            sampler = animation['samplers'][sampler_idx]
            
            # Verificar que tenga suficientes frames
            accessor = json_data['accessors'][sampler['input']]
            frame_count = accessor['count']
            
            return sampler_idx, frame_count
    
    return None, 0

def modify_finger_animation(input_file, output_file):
    """Modifica la animación de los huesos especificados."""
    print(f"Leyendo: {input_file}")
    json_data, bin_data = read_glb(input_file)
    
    animation = json_data['animations'][0]
    
    # Convertir frames de Blender (1-indexed) a índices de array (0-indexed)
    frame_start_idx = FRAME_START - 1
    frame_center_idx = FRAME_CENTER - 1
    frame_end_idx = FRAME_END - 1
    
    print(f"\n{'=' * 80}")
    print(f"CONFIGURACIÓN:")
    print(f"{'=' * 80}")
    print(f"Rango de frames: {FRAME_START} a {FRAME_END} (frame central: {FRAME_CENTER})")
    print(f"Frames a modificar (índices): {frame_start_idx} a {frame_end_idx} (centro: {frame_center_idx})")
    print(f"Total de huesos a modificar: {len(TARGET_COORDS_BLENDER)}")
    
    for bone_name, target_blender in TARGET_COORDS_BLENDER.items():
        print(f"\n{'=' * 80}")
        print(f"Modificando: {bone_name}")
        print(f"{'=' * 80}")
        
        # Buscar sampler automáticamente
        sampler_idx, frame_count = find_bone_rotation_sampler(json_data, bone_name)
        
        if sampler_idx is None:
            print(f"❌ ERROR: No se encontró el hueso '{bone_name}' en la animación")
            continue
        
        if frame_count <= frame_end_idx:
            print(f"❌ ERROR: El hueso '{bone_name}' solo tiene {frame_count} frames, pero necesita al menos {frame_end_idx + 1}")
            continue
        
        print(f"✅ Sampler encontrado: {sampler_idx} ({frame_count} frames)")
        
        sampler = animation['samplers'][sampler_idx]
        output_accessor = sampler['output']
        
        # Leer datos actuales
        current_quats = get_accessor_data(json_data, bin_data, output_accessor)
        
        # Convertir de Blender (W,X,Y,Z) a GLB (X,Y,Z,W)
        target_glb = [target_blender[1], target_blender[2], target_blender[3], target_blender[0]]
        print(f"Objetivo Blender (W,X,Y,Z): {target_blender}")
        print(f"Objetivo GLB (X,Y,Z,W): {target_glb}")
        
        # Guardar valores originales para transiciones
        # Frame anterior al inicio (para transición suave desde animación original)
        frame_before_idx = max(0, frame_start_idx - 1)
        # Frame posterior al final (para transición suave hacia animación original)
        frame_after_idx = min(len(current_quats) - 1, frame_end_idx + 1)
        
        original_before = current_quats[frame_before_idx].copy()
        original_after = current_quats[frame_after_idx].copy()
        
        print(f"\nFrame {frame_before_idx + 1} original (antes de transición): {original_before}")
        print(f"Frame {frame_after_idx + 1} original (después de transición): {original_after}")
        
        new_quats = current_quats.copy()
        
        # Definir 4 frames exactos consecutivos centrados en frame_center_idx
        exact_frame_start = frame_center_idx - 1  # 2 frames antes del centro
        exact_frame_end = frame_center_idx + 2    # 2 frames después del centro (total = 4 frames)
        
        # Transición desde frame_start hasta el primer frame exacto
        steps_to_exact = exact_frame_start - frame_start_idx
        if steps_to_exact > 0:
            for i in range(frame_start_idx, exact_frame_start):
                t = (i - frame_start_idx) / steps_to_exact
                new_quats[i] = slerp(original_before, target_glb, t)
                print(f"  Frame {i + 1} (índice {i}): t={t:.3f}, transición a coordenada exacta")
        
        # 4 frames consecutivos con coordenada exacta
        for i in range(exact_frame_start, exact_frame_end + 1):
            new_quats[i] = target_glb.copy()
            print(f"  Frame {i + 1} (índice {i}): EXACTO ✅")
        
        # Transición desde el último frame exacto hasta frame_end
        steps_from_exact = frame_end_idx - exact_frame_end
        if steps_from_exact > 0:
            for i in range(exact_frame_end + 1, frame_end_idx + 1):
                t = (i - exact_frame_end) / steps_from_exact
                new_quats[i] = slerp(target_glb, original_after, t)
                print(f"  Frame {i + 1} (índice {i}): t={t:.3f}, transición desde coordenada exacta")
        
        # Escribir datos modificados
        set_accessor_data(json_data, bin_data, output_accessor, new_quats)
        print(f"✅ {bone_name} modificado exitosamente")
    
    # Guardar archivo
    print(f"\n{'=' * 80}")
    print(f"Guardando: {output_file}")
    write_glb(output_file, json_data, bin_data)
    print(f"✅ Archivo guardado exitosamente")

if __name__ == '__main__':
    # Validar configuración
    if FRAME_CENTER < FRAME_START or FRAME_CENTER > FRAME_END:
        print("❌ ERROR: FRAME_CENTER debe estar entre FRAME_START y FRAME_END")
        exit(1)
    
    if not TARGET_COORDS_BLENDER:
        print("❌ ERROR: Debes especificar al menos un hueso en TARGET_COORDS_BLENDER")
        exit(1)
    
    if not INPUT_FILES:
        print("❌ ERROR: Debes especificar al menos un archivo en INPUT_FILES")
        exit(1)
    
    print("=" * 80)
    print("SCRIPT DE MODIFICACIÓN DE ANIMACIÓN GLB")
    print("=" * 80)
    print(f"Total de archivos a procesar: {len(INPUT_FILES)}")
    print(f"Rango de frames: {FRAME_START} - {FRAME_END} (centro: {FRAME_CENTER})")
    print(f"Huesos a modificar: {', '.join(TARGET_COORDS_BLENDER.keys())}")
    
    # Procesar cada archivo
    resultados_exitosos = []
    resultados_fallidos = []
    
    for idx, input_file in enumerate(INPUT_FILES, 1):
        print(f"\n{'=' * 80}")
        print(f"PROCESANDO ARCHIVO {idx}/{len(INPUT_FILES)}")
        print(f"{'=' * 80}")
        
        input_path = Path(input_file)
        
        # Validar que el archivo existe
        if not input_path.exists():
            print(f"❌ ERROR: El archivo no existe: {input_file}")
            resultados_fallidos.append(input_file)
            continue
        
        # Generar nombre de archivo de salida
        output_file = str(input_path.parent / f"{input_path.stem}{OUTPUT_SUFFIX}{input_path.suffix}")
        
        print(f"Archivo entrada: {input_file}")
        print(f"Archivo salida: {output_file}")
        
        try:
            modify_finger_animation(input_file, output_file)
            resultados_exitosos.append((input_file, output_file))
            print(f"✅ Archivo procesado exitosamente")
        except Exception as e:
            print(f"❌ ERROR al procesar archivo: {e}")
            resultados_fallidos.append(input_file)
    
    # Resumen final
    print(f"\n{'=' * 80}")
    print("RESUMEN FINAL")
    print(f"{'=' * 80}")
    print(f"\n✅ Archivos procesados exitosamente: {len(resultados_exitosos)}")
    for input_file, output_file in resultados_exitosos:
        print(f"  • {Path(input_file).name} → {Path(output_file).name}")
    
    if resultados_fallidos:
        print(f"\n❌ Archivos con errores: {len(resultados_fallidos)}")
        for input_file in resultados_fallidos:
            print(f"  • {input_file}")
    
    print(f"\n{'=' * 80}")
    print("PROCESO COMPLETADO")
    print(f"{'=' * 80}")
    if resultados_exitosos:
        print(f"\nAbre los archivos modificados en Blender y verifica el frame {FRAME_CENTER}")

    
    print(f"\n{'=' * 80}")
    print("PROCESO COMPLETADO")
    print(f"{'=' * 80}")
    print(f"\nAbre el archivo en Blender:")
    print(f"  {output_file}")
    print(f"\nVerifica el frame {FRAME_CENTER} para ver las coordenadas exactas")
