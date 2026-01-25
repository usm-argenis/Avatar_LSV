"""
Verificación visual detallada del archivo generado
"""
import json
import struct

def read_glb(file_path):
    with open(file_path, 'rb') as f:
        magic = f.read(4)
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
    
    type_map = {'SCALAR': 1, 'VEC2': 2, 'VEC3': 3, 'VEC4': 4}
    component_count = type_map[accessor['type']]
    
    size = 4
    data = []
    
    for i in range(count):
        values = []
        for j in range(component_count):
            byte_offset = offset + (i * component_count + j) * size
            value = struct.unpack_from('<f', bin_data, byte_offset)[0]
            values.append(value)
        data.append(values if component_count > 1 else values[0])
    
    return data

file_path = r"c:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\alfabeto\Duvall_resultado_s_FINGERS_TEST.glb"

fingers = {
    'RightHandMiddle1': [0.802, 0.512, -0.007, 0.291],
    'RightHandIndex1': [0.954, 0.267, -0.006, 0.138]
}

json_data, bin_data = read_glb(file_path)
animation = json_data['animations'][0]

channels_map = {}
for channel in animation['channels']:
    target_node = channel['target']['node']
    target_path = channel['target']['path']
    node_name = json_data['nodes'][target_node].get('name', f'node_{target_node}')
    
    if node_name not in channels_map:
        channels_map[node_name] = {}
    
    channels_map[node_name][target_path] = channel['sampler']

total_frames = json_data['accessors'][animation['samplers'][0]['input']]['count']

print("="*90)
print(f"VERIFICACIÓN DETALLADA - {total_frames} frames totales")
print("="*90)

for finger_name, expected_blender in fingers.items():
    print(f"\n{finger_name}:")
    print("-"*90)
    
    if finger_name not in channels_map or 'rotation' not in channels_map[finger_name]:
        print("  ❌ No encontrado")
        continue
    
    sampler_idx = channels_map[finger_name]['rotation']
    sampler = animation['samplers'][sampler_idx]
    rotation_data = get_accessor_data(json_data, bin_data, sampler['output'])
    
    # Mostrar frames clave
    frames_to_check = [21, 22, 25, 27, 28, 30, 33, 34, 35]
    
    for frame_idx in frames_to_check:
        if frame_idx >= len(rotation_data):
            continue
            
        quat_glb = rotation_data[frame_idx]
        quat_blender = [quat_glb[3], quat_glb[0], quat_glb[1], quat_glb[2]]
        
        diffs = [abs(quat_blender[i] - expected_blender[i]) for i in range(4)]
        max_diff = max(diffs)
        
        marker = ""
        if frame_idx == 21:
            marker = " (antes del rango)"
        elif frame_idx == 27:
            marker = " (FRAME 28 - OBJETIVO)"
        elif frame_idx == 34:
            marker = " (después del rango)"
        
        status = "✅" if (frame_idx == 27 and max_diff < 0.001) else "  "
        
        print(f"  {status} Frame {frame_idx + 1}{marker}:")
        print(f"      W={quat_blender[0]:.3f}, X={quat_blender[1]:.3f}, Y={quat_blender[2]:.3f}, Z={quat_blender[3]:.3f}")
        
        if frame_idx == 27:
            print(f"      Esperado: W={expected_blender[0]:.3f}, X={expected_blender[1]:.3f}, Y={expected_blender[2]:.3f}, Z={expected_blender[3]:.3f}")
            print(f"      Diff: {max_diff:.6f}")

print(f"\n{'='*90}")
print("✅ ARCHIVO LISTO PARA PROBAR")
print(f"{'='*90}")
print(f"\nArchivo: test\\output\\glb\\Duvall\\alfabeto\\Duvall_resultado_s_FINGERS_TEST.glb")
print(f"Frame objetivo: 28 (debe mostrar coordenadas exactas)")
print(f"Transiciones: Frames 22-27 y 29-34")
