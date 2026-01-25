"""
Verificar el archivo recién generado
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

test_file = r"c:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\alfabeto\Duvall_TEST_REWRITE.glb"

expected_blender = {
    'LeftArm': [0.896, -0.195, 0.356, -0.181],
    'RightArm': [0.896, 0.195, -0.356, -0.181],
    'RightForeArm': [-0.786, 0.020, -0.078, 0.613],
    'LeftForeArm': [0.751, 0.004, -0.045, 0.658]
}

json_data, bin_data = read_glb(test_file)
animation = json_data['animations'][0]

channels_map = {}
for channel in animation['channels']:
    target_node = channel['target']['node']
    target_path = channel['target']['path']
    node_name = json_data['nodes'][target_node].get('name', f'node_{target_node}')
    
    if node_name not in channels_map:
        channels_map[node_name] = {}
    
    channels_map[node_name][target_path] = channel['sampler']

print("="*90)
print("VERIFICACIÓN DEL ARCHIVO GENERADO: Duvall_TEST_REWRITE.glb")
print("="*90)

all_ok = True

for bone_name, exp_blender in expected_blender.items():
    if bone_name in channels_map and 'rotation' in channels_map[bone_name]:
        sampler_idx = channels_map[bone_name]['rotation']
        sampler = animation['samplers'][sampler_idx]
        rotation_data = get_accessor_data(json_data, bin_data, sampler['output'])
        
        quat_glb = rotation_data[0]
        quat_blender = [quat_glb[3], quat_glb[0], quat_glb[1], quat_glb[2]]
        
        diffs = [abs(quat_blender[i] - exp_blender[i]) for i in range(4)]
        max_diff = max(diffs)
        
        ok = max_diff < 0.001
        all_ok = all_ok and ok
        status = "✅" if ok else "❌"
        
        print(f"\n{status} {bone_name} (Frame 1):")
        print(f"    Esperado: W={exp_blender[0]:.3f}, X={exp_blender[1]:.3f}, Y={exp_blender[2]:.3f}, Z={exp_blender[3]:.3f}")
        print(f"    Actual:   W={quat_blender[0]:.3f}, X={quat_blender[1]:.3f}, Y={quat_blender[2]:.3f}, Z={quat_blender[3]:.3f}")
        if not ok:
            print(f"    Diff: {max_diff:.6f}")

print(f"\n{'='*90}")
if all_ok:
    print("✅ ARCHIVO CORRECTO - LISTO PARA PROBAR EN BLENDER")
    print("\nAbre: test\\output\\glb\\Duvall\\alfabeto\\Duvall_TEST_REWRITE.glb")
else:
    print("❌ HAY ERRORES EN EL ARCHIVO")
print(f"{'='*90}")
