import json
import struct
from pathlib import Path

def load_glb(filepath):
    with open(filepath, 'rb') as f:
        magic = f.read(4)
        if magic != b'glTF':
            raise ValueError("No es un archivo GLB válido")
        version = struct.unpack('<I', f.read(4))[0]
        length = struct.unpack('<I', f.read(4))[0]
        json_length = struct.unpack('<I', f.read(4))[0]
        json_type = f.read(4)
        json_data = json.loads(f.read(json_length).decode('utf-8'))
        bin_length = struct.unpack('<I', f.read(4))[0]
        bin_type = f.read(4)
        bin_data = f.read(bin_length)
        return {'json': json_data, 'bin': bin_data}

def get_accessor_data(glb_data, accessor_index):
    accessor = glb_data['json']['accessors'][accessor_index]
    buffer_view = glb_data['json']['bufferViews'][accessor['bufferView']]
    byte_offset = accessor.get('byteOffset', 0) + buffer_view.get('byteOffset', 0)
    count = accessor['count']
    component_types = {5126: ('f', 4), 5123: ('H', 2), 5125: ('I', 4)}
    comp_type, comp_size = component_types[accessor['componentType']]
    type_sizes = {'SCALAR': 1, 'VEC2': 2, 'VEC3': 3, 'VEC4': 4, 'MAT4': 16}
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

def verificar_frame(filepath, bone_name, frame_num):
    glb_data = load_glb(filepath)
    animation = glb_data['json']['animations'][0]
    fps = 30
    
    for channel in animation['channels']:
        node_index = channel['target']['node']
        node = glb_data['json']['nodes'][node_index]
        
        if node['name'] == bone_name and channel['target']['path'] == 'rotation':
            sampler = animation['samplers'][channel['sampler']]
            times = get_accessor_data(glb_data, sampler['input'])
            rotations = get_accessor_data(glb_data, sampler['output'])
            
            target_time = frame_num / fps
            closest_idx = 0
            min_diff = abs(times[0] - target_time)
            for i, t in enumerate(times):
                diff = abs(t - target_time)
                if diff < min_diff:
                    min_diff = diff
                    closest_idx = i
            
            rotation = rotations[closest_idx]
            return rotation
    return None

# Verificar en frame 25 (centro de repetición 19-28)
carla_file = "output/glb/Carla/alfabeto/Carla_resultado_b_modif.glb"
duvall_file = "output/glb/Duvall/alfabeto/Duvall_resultado_b_modif.glb"

print("VERIFICACIÓN EN FRAME 25 (centro de repetición 19-28):")
print("="*80)

bones = ["RightHandThumb2", "RightHandPinky1", "RightHandRing1"]

for bone in bones:
    carla_rot = verificar_frame(carla_file, bone, 25)
    duvall_rot = verificar_frame(duvall_file, bone, 25)
    
    print(f"\n{bone}:")
    print(f"  Carla:  x={carla_rot[0]:.3f}, y={carla_rot[1]:.3f}, z={carla_rot[2]:.3f}, w={carla_rot[3]:.3f}")
    print(f"  Duvall: x={duvall_rot[0]:.3f}, y={duvall_rot[1]:.3f}, z={duvall_rot[2]:.3f}, w={duvall_rot[3]:.3f}")
    
    # Verificar si son iguales
    if all(abs(carla_rot[i] - duvall_rot[i]) < 0.001 for i in range(4)):
        print(f"  ✅ IGUALES")
    else:
        print(f"  ❌ DIFERENTES")

print("\n" + "="*80)
print("Valores esperados del JSON (en formato glTF x,y,z,w):")
print("  RightHandThumb2: x=-0.068, y=0.310, z=0.008, w=0.948")
print("  RightHandPinky1: x=0.092, y=0.210, z=-0.121, w=0.966")
print("  RightHandRing1: x=0.183, y=0.029, z=-0.023, w=0.982")
