"""
Mostrar coordenadas EXACTAS antes y después de la modificación
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

def get_bone_rotation(file_path, bone_name, frame_idx):
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
    
    if bone_name in channels_map and 'rotation' in channels_map[bone_name]:
        sampler_idx = channels_map[bone_name]['rotation']
        sampler = animation['samplers'][sampler_idx]
        rotation_data = get_accessor_data(json_data, bin_data, sampler['output'])
        
        # GLB format (X, Y, Z, W) -> Blender format (W, X, Y, Z)
        quat_glb = rotation_data[frame_idx]
        quat_blender = [quat_glb[3], quat_glb[0], quat_glb[1], quat_glb[2]]
        
        return quat_blender
    
    return None

# Archivos
original = r"c:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\alfabeto\Duvall_resultado_ss.glb.backup_original"
modified = r"c:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\alfabeto\Duvall_resultado_ss.glb"

# Huesos a verificar
bones = ['LeftArm', 'RightArm', 'LeftForeArm', 'RightForeArm']

# COORDENADAS QUE EL USUARIO MOSTRÓ EN LAS CAPTURAS DE BLENDER
user_screenshots = {
    'RightArm': [0.896, 0.195, -0.356, -0.181],
    'RightForeArm': [-0.786, 0.020, -0.078, 0.613],
    'LeftForeArm': [0.751, 0.004, -0.045, 0.658]
}

print("="*90)
print("COORDENADAS EXACTAS - ANTES Y DESPUÉS")
print("="*90)

for bone_name in bones:
    print(f"\n{'='*90}")
    print(f"{bone_name}")
    print(f"{'='*90}")
    
    # Obtener coordenadas del archivo ORIGINAL (frame 1)
    orig_frame1 = get_bone_rotation(original, bone_name, 0)
    
    # Obtener coordenadas del archivo MODIFICADO (frame 1)
    mod_frame1 = get_bone_rotation(modified, bone_name, 0)
    
    # Obtener coordenadas del archivo MODIFICADO (último frame)
    json_data, _ = read_glb(modified)
    total_frames = json_data['accessors'][json_data['animations'][0]['samplers'][0]['input']]['count']
    mod_last = get_bone_rotation(modified, bone_name, total_frames - 1)
    
    if orig_frame1 and mod_frame1 and mod_last:
        print(f"\nARCHIVO ORIGINAL (Frame 1):")
        print(f"  W = {orig_frame1[0]:.6f}")
        print(f"  X = {orig_frame1[1]:.6f}")
        print(f"  Y = {orig_frame1[2]:.6f}")
        print(f"  Z = {orig_frame1[3]:.6f}")
        
        print(f"\nARCHIVO MODIFICADO (Frame 1):")
        print(f"  W = {mod_frame1[0]:.6f}")
        print(f"  X = {mod_frame1[1]:.6f}")
        print(f"  Y = {mod_frame1[2]:.6f}")
        print(f"  Z = {mod_frame1[3]:.6f}")
        
        print(f"\nARCHIVO MODIFICADO (Frame {total_frames}):")
        print(f"  W = {mod_last[0]:.6f}")
        print(f"  X = {mod_last[1]:.6f}")
        print(f"  Y = {mod_last[2]:.6f}")
        print(f"  Z = {mod_last[3]:.6f}")
        
        # Comparar con capturas del usuario (si existe)
        if bone_name in user_screenshots:
            expected = user_screenshots[bone_name]
            print(f"\nCOORDENADAS DE TU CAPTURA DE BLENDER:")
            print(f"  W = {expected[0]:.6f}")
            print(f"  X = {expected[1]:.6f}")
            print(f"  Y = {expected[2]:.6f}")
            print(f"  Z = {expected[3]:.6f}")
            
            # Calcular diferencia
            diff_frame1 = [abs(mod_frame1[i] - expected[i]) for i in range(4)]
            max_diff_frame1 = max(diff_frame1)
            
            diff_last = [abs(mod_last[i] - expected[i]) for i in range(4)]
            max_diff_last = max(diff_last)
            
            if max_diff_frame1 < 0.0001:
                print(f"\n  ✅ Frame 1 COINCIDE con tu captura (diff: {max_diff_frame1:.8f})")
            else:
                print(f"\n  ❌ Frame 1 NO COINCIDE con tu captura (diff: {max_diff_frame1:.8f})")
                print(f"     Diferencias por componente:")
                print(f"       W: {diff_frame1[0]:.8f}")
                print(f"       X: {diff_frame1[1]:.8f}")
                print(f"       Y: {diff_frame1[2]:.8f}")
                print(f"       Z: {diff_frame1[3]:.8f}")
            
            if max_diff_last < 0.0001:
                print(f"  ✅ Frame {total_frames} COINCIDE con tu captura (diff: {max_diff_last:.8f})")
            else:
                print(f"  ❌ Frame {total_frames} NO COINCIDE con tu captura (diff: {max_diff_last:.8f})")
        else:
            print(f"\n  ⚠️  NO HAY CAPTURA DE BLENDER PARA {bone_name}")
            print(f"     Se aplicó simetría basada en RightArm")

print(f"\n{'='*90}")
print("RESUMEN:")
print(f"{'='*90}")
print("\nSi algún hueso NO COINCIDE con tu captura, significa que:")
print("  1. Las coordenadas esperadas son incorrectas, O")
print("  2. Falta una captura de Blender para ese hueso")
print(f"\n{'='*90}")
