import json
import numpy as np
from pathlib import Path
import struct
from scipy.spatial.transform import Rotation as R, Slerp

def ease_in_out_cubic(t):
    """Función de suavizado cúbico"""
    if t < 0.5:
        return 4 * t * t * t
    else:
        return 1 - pow(-2 * t + 2, 3) / 2

def slerp_quaternions(q1, q2, t):
    """
    Interpolación esférica entre dos quaternions.
    Input/Output: formato glTF [x, y, z, w]
    """
    from scipy.spatial.transform import Slerp
    
    # Validar que los quaternions son válidos
    if len(q1) != 4 or len(q2) != 4:
        raise ValueError(f"Quaternions inválidos: q1={q1}, q2={q2}")
    
    # Crear Rotation objects (scipy usa x,y,z,w)
    r1 = R.from_quat(q1)  # Ya está en x,y,z,w
    r2 = R.from_quat(q2)
    
    # Crear interpolador SLERP
    key_rots = R.from_quat([q1, q2])
    slerp = Slerp([0, 1], key_rots)
    result_rot = slerp([t])[0]
    result = result_rot.as_quat()  # Retorna x,y,z,w
    
    return list(result)

def load_glb(filepath):
    """Cargar archivo GLB y parsear estructura"""
    with open(filepath, 'rb') as f:
        # Leer header GLB
        magic = f.read(4)
        if magic != b'glTF':
            raise ValueError("No es un archivo GLB válido")
        
        version = struct.unpack('<I', f.read(4))[0]
        length = struct.unpack('<I', f.read(4))[0]
        
        # Leer chunk JSON
        json_length = struct.unpack('<I', f.read(4))[0]
        json_type = f.read(4)
        json_data = json.loads(f.read(json_length).decode('utf-8'))
        
        # Leer chunk BIN
        bin_length = struct.unpack('<I', f.read(4))[0]
        bin_type = f.read(4)
        bin_data = f.read(bin_length)
        
        return {
            'json': json_data,
            'bin': bin_data,
            'version': version,
            'length': length
        }

def save_glb(filepath, glb_data):
    """Guardar archivo GLB modificado"""
    with open(filepath, 'wb') as f:
        json_str = json.dumps(glb_data['json'], separators=(',', ':'))
        json_bytes = json_str.encode('utf-8')
        
        # Padding para alinear a 4 bytes
        json_padding = (4 - len(json_bytes) % 4) % 4
        json_bytes += b' ' * json_padding
        
        bin_data = glb_data['bin']
        bin_padding = (4 - len(bin_data) % 4) % 4
        bin_data += b'\x00' * bin_padding
        
        total_length = 12 + 8 + len(json_bytes) + 8 + len(bin_data)
        
        # Header
        f.write(b'glTF')
        f.write(struct.pack('<I', 2))
        f.write(struct.pack('<I', total_length))
        
        # JSON chunk
        f.write(struct.pack('<I', len(json_bytes)))
        f.write(b'JSON')
        f.write(json_bytes)
        
        # BIN chunk
        f.write(struct.pack('<I', len(bin_data)))
        f.write(b'BIN\x00')
        f.write(bin_data)

def get_accessor_data(glb_data, accessor_index):
    """Obtener datos de un accessor"""
    accessor = glb_data['json']['accessors'][accessor_index]
    buffer_view = glb_data['json']['bufferViews'][accessor['bufferView']]
    
    byte_offset = accessor.get('byteOffset', 0) + buffer_view.get('byteOffset', 0)
    count = accessor['count']
    
    component_types = {
        5126: ('f', 4),  # FLOAT
        5123: ('H', 2),  # UNSIGNED_SHORT
        5125: ('I', 4),  # UNSIGNED_INT
    }
    
    comp_type, comp_size = component_types[accessor['componentType']]
    
    type_sizes = {
        'SCALAR': 1,
        'VEC2': 2,
        'VEC3': 3,
        'VEC4': 4,
        'MAT4': 16
    }
    
    num_components = type_sizes[accessor['type']]
    format_str = '<' + comp_type * num_components
    item_size = comp_size * num_components
    
    data = []
    for i in range(count):
        offset = byte_offset + i * item_size
        values = struct.unpack(format_str, glb_data['bin'][offset:offset + item_size])
        if num_components == 1:
            data.append(values[0])
        else:
            data.append(list(values))
    
    return data

def set_accessor_data(glb_data, accessor_index, data):
    """Modificar datos de un accessor"""
    accessor = glb_data['json']['accessors'][accessor_index]
    buffer_view = glb_data['json']['bufferViews'][accessor['bufferView']]
    
    byte_offset = accessor.get('byteOffset', 0) + buffer_view.get('byteOffset', 0)
    count = accessor['count']
    
    component_types = {
        5126: ('f', 4),  # FLOAT
    }
    
    comp_type, comp_size = component_types[accessor['componentType']]
    
    type_sizes = {
        'SCALAR': 1,
        'VEC2': 2,
        'VEC3': 3,
        'VEC4': 4,
        'MAT4': 16
    }
    
    num_components = type_sizes[accessor['type']]
    format_str = '<' + comp_type * num_components
    item_size = comp_size * num_components
    
    bin_data = bytearray(glb_data['bin'])
    
    for i in range(min(count, len(data))):
        offset = byte_offset + i * item_size
        if num_components == 1:
            values = (data[i],)
        else:
            values = tuple(data[i])
        
        packed = struct.pack(format_str, *values)
        bin_data[offset:offset + item_size] = packed
    
    glb_data['bin'] = bytes(bin_data)

def apply_modifications(json_config_path):
    """Aplicar modificaciones desde archivo JSON"""
    print(f"📂 Cargando configuración: {json_config_path}")
    
    with open(json_config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    # Obtener primera (y única) entrada
    glb_path = list(config.keys())[0]
    modifications = config[glb_path]
    
    print(f"🎯 Archivo GLB: {glb_path}")
    
    # Validar que el archivo existe
    if not Path(glb_path).exists():
        raise FileNotFoundError(f"No se encuentra el archivo: {glb_path}")
    
    # Extraer configuración
    alcance = modifications['alcance']
    frame_min = alcance['min']
    frame_max = alcance['max']
    frame_retencion = alcance['retencion']
    
    print(f"⚙️ Rango de frames: {frame_min} → {frame_max}")
    print(f"⏱️ Retención en centro: {frame_retencion} frames")
    
    # Calcular rangos de interpolación
    total_frames = frame_max - frame_min
    repeat_start = frame_min + (total_frames - frame_retencion) // 2
    repeat_end = repeat_start + frame_retencion
    
    print(f"📊 Repetición: frames {repeat_start}-{repeat_end}")
    print(f"🔄 Transición entrada: {frame_min}→{repeat_start} ({repeat_start - frame_min} frames)")
    print(f"🔄 Transición salida: {repeat_end}→{frame_max} ({frame_max - repeat_end} frames)")
    
    # Cargar GLB
    print(f"\n📥 Cargando GLB...")
    glb_data = load_glb(glb_path)
    
    # Buscar animación
    if 'animations' not in glb_data['json'] or len(glb_data['json']['animations']) == 0:
        raise ValueError("El archivo GLB no contiene animaciones")
    
    animation = glb_data['json']['animations'][0]
    print(f"✅ Animación encontrada: {animation.get('name', 'Sin nombre')}")
    
    # Procesar cada hueso modificado
    bones_modified = []
    for key in modifications:
        if key == 'alcance':
            continue
        
        bone_name = key
        target_values = modifications[bone_name]
        
        print(f"\n🦴 Procesando hueso: {bone_name}")
        print(f"   Valores objetivo (JSON): w={target_values['w']:.3f}, x={target_values['x']:.3f}, y={target_values['y']:.3f}, z={target_values['z']:.3f}")
        
        # Buscar channel del hueso
        channel_found = False
        for channel in animation['channels']:
            sampler = animation['samplers'][channel['sampler']]
            node_index = channel['target']['node']
            node = glb_data['json']['nodes'][node_index]
            
            if node['name'] == bone_name and channel['target']['path'] == 'rotation':
                channel_found = True
                
                # Obtener datos actuales
                time_accessor = sampler['input']
                rotation_accessor = sampler['output']
                
                times = get_accessor_data(glb_data, time_accessor)
                rotations = get_accessor_data(glb_data, rotation_accessor)
                
                # Validar datos
                if not times or not rotations:
                    print(f"   ❌ Datos de animación vacíos")
                    break
                
                fps = 30
                duration = times[-1]
                num_keyframes = len(times)
                
                print(f"   📊 Duración: {duration:.2f}s, {num_keyframes} keyframes, FPS: {fps}")
                print(f"   📊 Formato original (glTF): rotations[0] = {rotations[0]}")
                
                # IMPORTANTE: Convertir de formato JSON (w,x,y,z) a formato glTF (x,y,z,w)
                target_quat_gltf = [
                    target_values['x'],  # x
                    target_values['y'],  # y
                    target_values['z'],  # z
                    target_values['w']   # w
                ]
                
                print(f"   🎯 Quaternion objetivo (glTF): {target_quat_gltf}")
                
                # Copiar rotaciones originales
                new_rotations = [list(rot) for rot in rotations]
                
                # Calcular mapeo de frames a keyframes
                def frame_to_keyframe_index(frame_num):
                    """Convertir número de frame a índice de keyframe"""
                    time_at_frame = frame_num / fps
                    # Buscar el keyframe más cercano
                    closest_idx = 0
                    min_diff = abs(times[0] - time_at_frame)
                    for i, t in enumerate(times):
                        diff = abs(t - time_at_frame)
                        if diff < min_diff:
                            min_diff = diff
                            closest_idx = i
                    return closest_idx
                
                # 1. Aplicar valor objetivo en frames de repetición
                for frame in range(repeat_start, repeat_end + 1):
                    kf_idx = frame_to_keyframe_index(frame)
                    new_rotations[kf_idx] = target_quat_gltf.copy()
                
                print(f"   ✓ Aplicado en frames {repeat_start}-{repeat_end}")
                
                # 2. Interpolación de entrada (suave)
                if repeat_start > frame_min:
                    for frame in range(frame_min, repeat_start):
                        kf_idx = frame_to_keyframe_index(frame)
                        progress = (frame - frame_min) / (repeat_start - frame_min)
                        eased = ease_in_out_cubic(progress)
                        
                        original_quat = rotations[kf_idx]
                        interpolated = slerp_quaternions(original_quat, target_quat_gltf, eased)
                        new_rotations[kf_idx] = interpolated
                    
                    print(f"   ✓ Interpolación entrada: frames {frame_min}-{repeat_start}")
                
                # 3. Interpolación de salida (suave)
                if repeat_end < frame_max:
                    # Obtener quaternion final original
                    end_kf_idx = frame_to_keyframe_index(frame_max)
                    end_quat_original = rotations[end_kf_idx]
                    
                    for frame in range(repeat_end + 1, frame_max + 1):
                        kf_idx = frame_to_keyframe_index(frame)
                        progress = (frame - repeat_end) / (frame_max - repeat_end)
                        eased = ease_in_out_cubic(progress)
                        
                        interpolated = slerp_quaternions(target_quat_gltf, end_quat_original, eased)
                        new_rotations[kf_idx] = interpolated
                    
                    print(f"   ✓ Interpolación salida: frames {repeat_end}-{frame_max}")
                
                # Validar que las rotaciones son correctas
                for i, rot in enumerate(new_rotations):
                    if len(rot) != 4:
                        print(f"   ❌ ERROR: Rotación en índice {i} tiene tamaño incorrecto: {len(rot)}")
                        raise ValueError(f"Rotación inválida en keyframe {i}")
                    
                    # Verificar que es un quaternion válido (norma cercana a 1)
                    norm = sum(x*x for x in rot) ** 0.5
                    if abs(norm - 1.0) > 0.1:
                        print(f"   ⚠️ Advertencia: Quaternion no normalizado en keyframe {i}: norma={norm:.3f}")
                        # Normalizar
                        new_rotations[i] = [x/norm for x in rot]
                
                # Guardar modificaciones
                set_accessor_data(glb_data, rotation_accessor, new_rotations)
                bones_modified.append(bone_name)
                print(f"   ✅ Modificaciones aplicadas correctamente")
                break
        
        if not channel_found:
            print(f"   ⚠️ No se encontró channel de rotación para {bone_name}")
    
    # Generar nombre de salida
    input_path = Path(glb_path)
    output_path = input_path.parent / f"{input_path.stem}_modif{input_path.suffix}"
    
    print(f"\n💾 Guardando archivo modificado: {output_path}")
    save_glb(output_path, glb_data)
    
    print(f"\n✅ PROCESO COMPLETADO")
    print(f"📁 Archivo generado: {output_path}")
    print(f"🦴 Huesos modificados: {len(bones_modified)}")
    for bone in bones_modified:
        print(f"   - {bone}")
    
    return str(output_path)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        config_path = sys.argv[1]
    else:
        config_path = "datos.json"
    
    try:
        output_file = apply_modifications(config_path)
        print(f"\n🎉 Éxito! Archivo listo: {output_file}")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
