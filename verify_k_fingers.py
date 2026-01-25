"""
Verifica que las coordenadas de los dedos en el frame 28 sean exactas
"""

import json
import struct

TARGET_COORDS_BLENDER = {
    'RightHandMiddle1': [0.802, 0.512, -0.007, 0.291],
    'RightHandIndex1': [0.954, 0.267, -0.006, 0.138]
}

BONE_SAMPLERS = {
    'RightHandMiddle1': 136,
    'RightHandIndex1': 124
}

def read_glb(file_path):
    with open(file_path, 'rb') as f:
        magic = f.read(4)
        version = struct.unpack('<I', f.read(4))[0]
        length = struct.unpack('<I', f.read(4))[0]
        json_chunk_length = struct.unpack('<I', f.read(4))[0]
        json_chunk_type = f.read(4)
        json_data = json.loads(f.read(json_chunk_length).decode('utf-8'))
        bin_chunk_length = struct.unpack('<I', f.read(4))[0]
        bin_chunk_type = f.read(4)
        bin_data = f.read(bin_chunk_length)
    return json_data, bin_data

def get_accessor_data(json_data, bin_data, accessor_index):
    accessor = json_data['accessors'][accessor_index]
    buffer_view = json_data['bufferViews'][accessor['bufferView']]
    byte_offset = buffer_view.get('byteOffset', 0) + accessor.get('byteOffset', 0)
    count = accessor['count']
    type_str = accessor['type']
    type_map = {'SCALAR': 1, 'VEC2': 2, 'VEC3': 3, 'VEC4': 4}
    components = type_map[type_str]
    format_char = 'f'
    bytes_per_component = struct.calcsize(format_char)
    values = []
    for i in range(count):
        offset = byte_offset + i * components * bytes_per_component
        data = struct.unpack(f'<{components}{format_char}', bin_data[offset:offset + components * bytes_per_component])
        values.append(list(data))
    return values

file_path = r'test\output\glb\Duvall\alfabeto\Duvall_resultado_k_FINGERS_MODIFIED.glb'
print("=" * 80)
print("VERIFICACIÓN DE COORDENADAS EN FRAME 28")
print("=" * 80)

json_data, bin_data = read_glb(file_path)
animation = json_data['animations'][0]

for bone_name, target_blender in TARGET_COORDS_BLENDER.items():
    print(f"\n{bone_name}:")
    print(f"  Objetivo Blender (W,X,Y,Z): {target_blender}")
    
    # Convertir a GLB
    target_glb = [target_blender[1], target_blender[2], target_blender[3], target_blender[0]]
    print(f"  Objetivo GLB (X,Y,Z,W): {target_glb}")
    
    # Leer frame 28 (índice 27)
    sampler_idx = BONE_SAMPLERS[bone_name]
    sampler = animation['samplers'][sampler_idx]
    output_accessor = sampler['output']
    quats = get_accessor_data(json_data, bin_data, output_accessor)
    
    frame_28 = quats[27]
    print(f"  Frame 28 GLB actual: {frame_28}")
    
    # Convertir a Blender para mostrar
    frame_28_blender = [frame_28[3], frame_28[0], frame_28[1], frame_28[2]]
    print(f"  Frame 28 Blender: {frame_28_blender}")
    
    # Calcular diferencia
    diff = sum((a - b) ** 2 for a, b in zip(target_glb, frame_28)) ** 0.5
    print(f"  Diferencia: {diff:.10f}")
    
    if diff < 0.0001:
        print(f"  ✅ COORDENADAS EXACTAS")
    else:
        print(f"  ❌ DIFERENCIA DETECTADA")

print("\n" + "=" * 80)
print("VERIFICACIÓN COMPLETADA")
print("=" * 80)
