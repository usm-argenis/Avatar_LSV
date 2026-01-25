"""
Script para ajustar la rotación de la cabeza para que mire hacia el frente
"""
import json
import struct
import os
import math

def leer_glb(archivo_path):
    """Lee un archivo GLB y extrae información relevante"""
    with open(archivo_path, 'rb') as f:
        magic = f.read(4)
        if magic != b'glTF':
            raise ValueError("No es un archivo GLB válido")
        
        version = struct.unpack('<I', f.read(4))[0]
        length = struct.unpack('<I', f.read(4))[0]
        
        json_chunk_length = struct.unpack('<I', f.read(4))[0]
        json_chunk_type = f.read(4)
        json_data = f.read(json_chunk_length)
        
        gltf = json.loads(json_data.decode('utf-8'))
        
        binary_data = None
        if f.tell() < length:
            bin_chunk_length = struct.unpack('<I', f.read(4))[0]
            bin_chunk_type = f.read(4)
            binary_data = f.read(bin_chunk_length)
        
        return gltf, binary_data

def escribir_glb(archivo_path, gltf, binary_data):
    """Escribe un archivo GLB con los datos modificados"""
    json_data = json.dumps(gltf, separators=(',', ':')).encode('utf-8')
    json_padding = (4 - (len(json_data) % 4)) % 4
    json_data += b' ' * json_padding
    
    total_length = 12 + 8 + len(json_data)
    if binary_data:
        bin_padding = (4 - (len(binary_data) % 4)) % 4
        binary_data += b'\x00' * bin_padding
        total_length += 8 + len(binary_data)
    
    with open(archivo_path, 'wb') as f:
        f.write(b'glTF')
        f.write(struct.pack('<I', 2))
        f.write(struct.pack('<I', total_length))
        f.write(struct.pack('<I', len(json_data)))
        f.write(b'JSON')
        f.write(json_data)
        
        if binary_data:
            f.write(struct.pack('<I', len(binary_data)))
            f.write(b'BIN\x00')
            f.write(binary_data)

def encontrar_nodo(gltf, nombre_nodo):
    """Encuentra un nodo por su nombre"""
    for i, node in enumerate(gltf['nodes']):
        if node.get('name') == nombre_nodo:
            return i, node
    return None, None

def quaternion_to_euler(quat):
    """Convierte un quaternion [x, y, z, w] a ángulos de Euler en grados"""
    x, y, z, w = quat
    
    # Roll (x-axis rotation)
    sinr_cosp = 2 * (w * x + y * z)
    cosr_cosp = 1 - 2 * (x * x + y * y)
    roll = math.atan2(sinr_cosp, cosr_cosp)
    
    # Pitch (y-axis rotation)
    sinp = 2 * (w * y - z * x)
    if abs(sinp) >= 1:
        pitch = math.copysign(math.pi / 2, sinp)
    else:
        pitch = math.asin(sinp)
    
    # Yaw (z-axis rotation)
    siny_cosp = 2 * (w * z + x * y)
    cosy_cosp = 1 - 2 * (y * y + z * z)
    yaw = math.atan2(siny_cosp, cosy_cosp)
    
    return math.degrees(roll), math.degrees(pitch), math.degrees(yaw)

def euler_to_quaternion(roll, pitch, yaw):
    """Convierte ángulos de Euler (en grados) a quaternion [x, y, z, w]"""
    roll = math.radians(roll)
    pitch = math.radians(pitch)
    yaw = math.radians(yaw)
    
    cy = math.cos(yaw * 0.5)
    sy = math.sin(yaw * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)
    cr = math.cos(roll * 0.5)
    sr = math.sin(roll * 0.5)
    
    w = cr * cp * cy + sr * sp * sy
    x = sr * cp * cy - cr * sp * sy
    y = cr * sp * cy + sr * cp * sy
    z = cr * cp * sy - sr * sp * cy
    
    return [x, y, z, w]

def ajustar_rotacion_cabeza(archivo_origen, archivo_destino, angulo_ajuste=15):
    """
    Ajusta la rotación de la cabeza para que mire hacia el frente
    
    Args:
        archivo_origen: Archivo GLB de origen
        archivo_destino: Archivo GLB de destino
        angulo_ajuste: Ángulo en grados para ajustar el pitch (negativo = mirar hacia arriba)
    """
    print("=" * 80)
    print("AJUSTE DE ROTACIÓN DE CABEZA")
    print("=" * 80)
    
    # Leer modelo
    print(f"\n📖 Leyendo modelo: {os.path.basename(archivo_origen)}")
    gltf, binary_data = leer_glb(archivo_origen)
    
    # Encontrar nodos de cabeza y cuello
    idx_head, node_head = encontrar_nodo(gltf, 'Head')
    idx_neck, node_neck = encontrar_nodo(gltf, 'Neck')
    
    print("\n" + "=" * 80)
    print("ANÁLISIS ACTUAL")
    print("=" * 80)
    
    modificaciones = []
    
    if idx_neck is not None and 'rotation' in node_neck:
        rot_actual = node_neck['rotation']
        euler = quaternion_to_euler(rot_actual)
        
        print(f"\n🦴 Cuello (Neck) - Nodo {idx_neck}")
        print(f"   Rotación actual (quaternion): {rot_actual}")
        print(f"   Ángulos Euler:")
        print(f"      Roll (X):  {euler[0]:.2f}°")
        print(f"      Pitch (Y): {euler[1]:.2f}°")
        print(f"      Yaw (Z):   {euler[2]:.2f}°")
    
    if idx_head is not None and 'rotation' in node_head:
        rot_actual = node_head['rotation']
        euler = quaternion_to_euler(rot_actual)
        
        print(f"\n🦴 Cabeza (Head) - Nodo {idx_head}")
        print(f"   Rotación actual (quaternion): {rot_actual}")
        print(f"   Ángulos Euler:")
        print(f"      Roll (X):  {euler[0]:.2f}°")
        print(f"      Pitch (Y): {euler[1]:.2f}°")
        print(f"      Yaw (Z):   {euler[2]:.2f}°")
        
        # Ajustar la cabeza
        print(f"\n🔧 Ajustando rotación de la cabeza...")
        print(f"   Aplicando ajuste de Pitch: {angulo_ajuste}° (hacia arriba)")
        
        # Convertir a Euler, ajustar pitch, y volver a quaternion
        roll, pitch, yaw = euler
        nuevo_pitch = pitch + angulo_ajuste
        
        nueva_rotacion = euler_to_quaternion(roll, nuevo_pitch, yaw)
        
        print(f"\n   Nueva rotación:")
        print(f"      Roll (X):  {roll:.2f}°")
        print(f"      Pitch (Y): {nuevo_pitch:.2f}° (ajustado desde {pitch:.2f}°)")
        print(f"      Yaw (Z):   {yaw:.2f}°")
        print(f"   Nuevo quaternion: {nueva_rotacion}")
        
        # Aplicar cambio
        node_head['rotation'] = nueva_rotacion
        
        modificaciones.append({
            'nodo': 'Head',
            'indice': idx_head,
            'anterior': rot_actual,
            'nuevo': nueva_rotacion,
            'euler_anterior': euler,
            'euler_nuevo': (roll, nuevo_pitch, yaw)
        })
    
    # Guardar modelo modificado
    print(f"\n💾 Guardando modelo ajustado...")
    escribir_glb(archivo_destino, gltf, binary_data)
    
    print("\n" + "=" * 80)
    print("✅ PROCESO COMPLETADO")
    print("=" * 80)
    print(f"\n📁 Archivo guardado en:")
    print(f"   {archivo_destino}")
    print(f"\n📊 Modificaciones aplicadas: {len(modificaciones)}")
    
    if modificaciones:
        for mod in modificaciones:
            print(f"\n   {mod['nodo']} (Nodo {mod['indice']}):")
            print(f"      Pitch anterior: {mod['euler_anterior'][1]:.2f}°")
            print(f"      Pitch nuevo:    {mod['euler_nuevo'][1]:.2f}°")
            print(f"      Cambio:         +{mod['euler_nuevo'][1] - mod['euler_anterior'][1]:.2f}°")
    
    print("\n" + "=" * 80)
    print("INSTRUCCIONES:")
    print("=" * 80)
    print("\n1. Visualiza el archivo ajustado")
    print("2. Verifica que la cabeza ahora mire hacia el frente")
    print("3. Si necesita más ajuste, modifica el parámetro 'angulo_ajuste'")
    print("   - Valores positivos = mirar más hacia arriba")
    print("   - Valores negativos = mirar más hacia abajo")
    print("4. Si está correcto, confirma para aplicar a todos los modelos")
    
    return modificaciones

if __name__ == "__main__":
    # Rutas de archivos
    archivo_origen = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\saludos\Duvall_resultado_hola_corregido.glb"
    archivo_destino = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\saludos\Duvall_resultado_hola_final.glb"
    
    # Ángulo de ajuste (positivo = mirar hacia arriba)
    # Puedes modificar este valor para ajustar más o menos
    ANGULO_AJUSTE = 15  # Grados
    
    print(f"\n⚙️  Configuración:")
    print(f"   Ángulo de ajuste: {ANGULO_AJUSTE}°")
    print(f"   (Positivo = mirar hacia arriba, Negativo = mirar hacia abajo)")
    
    # Verificar archivo
    if not os.path.exists(archivo_origen):
        print(f"\n❌ Error: No se encuentra el archivo de origen")
        print(f"   {archivo_origen}")
        exit(1)
    
    try:
        modificaciones = ajustar_rotacion_cabeza(archivo_origen, archivo_destino, ANGULO_AJUSTE)
        
    except Exception as e:
        print(f"\n❌ Error durante el proceso: {str(e)}")
        import traceback
        traceback.print_exc()
