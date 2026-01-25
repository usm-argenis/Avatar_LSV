"""
Verificar que el frame 1 y el último frame tengan las coordenadas exactas de Blender
"""
import json
import struct
from pathlib import Path
import numpy as np

# Coordenadas de Blender en formato (W, X, Y, Z)
BLENDER_EXPECTED = {
    'RightArm': [0.896, 0.195, -0.356, -0.181],
    'RightForeArm': [-0.786, 0.020, -0.078, 0.613],
    'LeftForeArm': [0.751, 0.004, -0.045, 0.658]
}

# Convertir a formato GLB (X, Y, Z, W) para comparación
EXPECTED_POSE = {
    name: [quat[1], quat[2], quat[3], quat[0]]  # X, Y, Z, W
    for name, quat in BLENDER_EXPECTED.items()
}

def read_glb(file_path):
    with open(file_path, 'rb') as f:
        magic = f.read(4)
        if magic != b'glTF':
            raise ValueError("No es GLB")
        
        version = struct.unpack('<I', f.read(4))[0]
        length = struct.unpack('<I', f.read(4))[0]
        
        json_len = struct.unpack('<I', f.read(4))[0]
        json_type = f.read(4)
        json_data = json.loads(f.read(json_len).decode('utf-8'))
        
        bin_len = struct.unpack('<I', f.read(4))[0]
        bin_type = f.read(4)
        bin_data = f.read(bin_len)
        
        return json_data, bin_data

def get_accessor_data(json_data, bin_data, accessor_idx):
    accessor = json_data['accessors'][accessor_idx]
    buffer_view = json_data['bufferViews'][accessor['bufferView']]
    
    offset = buffer_view.get('byteOffset', 0) + accessor.get('byteOffset', 0)
    count = accessor['count']
    
    type_map = {'SCALAR': 1, 'VEC2': 2, 'VEC3': 3, 'VEC4': 4, 'MAT4': 16}
    component_count = type_map[accessor['type']]
    
    component_type = accessor['componentType']
    format_map = {5126: 'f', 5123: 'H', 5125: 'I'}
    fmt = format_map[component_type]
    
    size = struct.calcsize(fmt)
    data = []
    
    for i in range(count):
        values = []
        for j in range(component_count):
            byte_offset = offset + (i * component_count + j) * size
            value = struct.unpack_from(f'<{fmt}', bin_data, byte_offset)[0]
            values.append(value)
        data.append(values if component_count > 1 else values[0])
    
    return data

def verify_frame(json_data, bin_data, frame_idx):
    """Verifica las coordenadas de un frame específico"""
    animation = json_data['animations'][0]
    
    # Mapear canales
    channels_map = {}
    for channel in animation['channels']:
        target_node = channel['target']['node']
        target_path = channel['target']['path']
        node_name = json_data['nodes'][target_node].get('name', f'node_{target_node}')
        
        if node_name not in channels_map:
            channels_map[node_name] = {}
        
        channels_map[node_name][target_path] = channel['sampler']
    
    print(f"\n--- FRAME {frame_idx + 1} ---")
    
    all_ok = True
    for bone_name, expected_quat in EXPECTED_POSE.items():
        if bone_name not in channels_map or 'rotation' not in channels_map[bone_name]:
            print(f"  ❌ {bone_name}: NO ENCONTRADO")
            all_ok = False
            continue
        
        sampler_idx = channels_map[bone_name]['rotation']
        sampler = animation['samplers'][sampler_idx]
        
        rotation_data = get_accessor_data(json_data, bin_data, sampler['output'])
        actual_quat = rotation_data[frame_idx]  # En formato GLB: (X, Y, Z, W)
        
        # expected_quat ya está en formato GLB (X, Y, Z, W)
        # Convertir a formato Blender (W, X, Y, Z) para mostrar
        actual_blender = [actual_quat[3], actual_quat[0], actual_quat[1], actual_quat[2]]
        expected_blender = [expected_quat[3], expected_quat[0], expected_quat[1], expected_quat[2]]
        
        # Calcular diferencia
        diff = [abs(actual_quat[i] - expected_quat[i]) for i in range(4)]
        max_diff = max(diff)
        
        status = "✅" if max_diff < 0.001 else "❌"
        
        print(f"  {status} {bone_name}:")
        print(f"      Esperado (Blender W,X,Y,Z): W={expected_blender[0]:.3f}, X={expected_blender[1]:.3f}, Y={expected_blender[2]:.3f}, Z={expected_blender[3]:.3f}")
        print(f"      Actual   (Blender W,X,Y,Z): W={actual_blender[0]:.3f}, X={actual_blender[1]:.3f}, Y={actual_blender[2]:.3f}, Z={actual_blender[3]:.3f}")
        print(f"      Diferencia máxima: {max_diff:.6f}")
        
        if max_diff >= 0.001:
            all_ok = False
    
    return all_ok

def main():
    glb_path = r"c:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\alfabeto\Duvall_resultado_ss.glb"
    
    print("="*60)
    print("VERIFICACIÓN DE POSE DE REPOSO")
    print("="*60)
    print(f"Archivo: {Path(glb_path).name}")
    
    json_data, bin_data = read_glb(glb_path)
    
    # Contar frames
    animation = json_data['animations'][0]
    first_sampler = animation['samplers'][0]
    time_data = get_accessor_data(json_data, bin_data, first_sampler['input'])
    total_frames = len(time_data)
    
    print(f"Total frames: {total_frames}")
    
    # Verificar primer frame (índice 0)
    frame1_ok = verify_frame(json_data, bin_data, 0)
    
    # Verificar último frame
    last_frame_ok = verify_frame(json_data, bin_data, total_frames - 1)
    
    print("\n" + "="*60)
    if frame1_ok and last_frame_ok:
        print("✅ VERIFICACIÓN EXITOSA")
        print("El frame 1 y el último frame tienen las coordenadas correctas")
    else:
        print("❌ VERIFICACIÓN FALLIDA")
        print("Algunos frames no tienen las coordenadas esperadas")
    print("="*60)

if __name__ == "__main__":
    main()
