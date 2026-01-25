import json
import struct
from pathlib import Path

def load_glb(filepath):
    """Cargar archivo GLB y parsear estructura"""
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
    """Obtener datos de un accessor"""
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

def diagnosticar_archivo(filepath, bone_name, frame_num=30):
    """Diagnosticar valores de un hueso en un frame específico"""
    print(f"\n{'='*80}")
    print(f"📋 DIAGNÓSTICO: {Path(filepath).name}")
    print(f"{'='*80}")
    
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
            
            duration = times[-1]
            num_keyframes = len(times)
            
            print(f"🦴 Hueso: {bone_name}")
            print(f"⏱️  Duración: {duration:.3f}s")
            print(f"📊 Total keyframes: {num_keyframes}")
            print(f"🎯 FPS: {fps}")
            
            # Calcular qué keyframe corresponde al frame solicitado
            target_time = frame_num / fps
            
            # Método 1: Buscar keyframe más cercano
            closest_idx = 0
            min_diff = abs(times[0] - target_time)
            for i, t in enumerate(times):
                diff = abs(t - target_time)
                if diff < min_diff:
                    min_diff = diff
                    closest_idx = i
            
            print(f"\n🎬 Frame solicitado: {frame_num}")
            print(f"   Tiempo esperado: {target_time:.3f}s")
            print(f"   Keyframe más cercano: {closest_idx}")
            print(f"   Tiempo real del keyframe: {times[closest_idx]:.3f}s")
            print(f"   Diferencia: {abs(times[closest_idx] - target_time):.3f}s")
            
            rotation = rotations[closest_idx]
            print(f"\n📐 Rotación en keyframe {closest_idx} (formato glTF x,y,z,w):")
            print(f"   x = {rotation[0]:.6f}")
            print(f"   y = {rotation[1]:.6f}")
            print(f"   z = {rotation[2]:.6f}")
            print(f"   w = {rotation[3]:.6f}")
            
            # Calcular norma
            norm = sum(x*x for x in rotation) ** 0.5
            print(f"   Norma: {norm:.6f} {'✓' if abs(norm - 1.0) < 0.01 else '⚠️ NO NORMALIZADO'}")
            
            # Mostrar algunos keyframes alrededor
            print(f"\n📋 Keyframes cercanos al frame {frame_num}:")
            for i in range(max(0, closest_idx - 2), min(num_keyframes, closest_idx + 3)):
                frame_num_calc = int(times[i] * fps)
                rot = rotations[i]
                marker = " 👉" if i == closest_idx else ""
                print(f"   KF {i:3d} | Frame ~{frame_num_calc:3d} | t={times[i]:.3f}s | "
                      f"x={rot[0]:7.3f} y={rot[1]:7.3f} z={rot[2]:7.3f} w={rot[3]:7.3f}{marker}")
            
            return
    
    print(f"❌ No se encontró el hueso '{bone_name}' con rotación")

if __name__ == "__main__":
    # Archivos a comparar
    original = "output/glb/Duvall/alfabeto/Duvall_resultado_b.glb"
    modificado = "output/glb/Duvall/alfabeto/Duvall_resultado_b_modif.glb"
    
    hueso = "RightHandPinky1"
    frame = 30
    
    print("\n" + "="*80)
    print("🔍 COMPARACIÓN DE ARCHIVOS GLB")
    print("="*80)
    
    diagnosticar_archivo(original, hueso, frame)
    diagnosticar_archivo(modificado, hueso, frame)
    
    print(f"\n{'='*80}")
    print("📝 VALORES ESPERADOS (del JSON):")
    print("="*80)
    print(f"   Frame objetivo: {frame}")
    print(f"   Hueso: {hueso}")
    print(f"   Valores JSON (w,x,y,z): w=0.966, x=0.092, y=0.210, z=-0.121")
    print(f"   Valores glTF (x,y,z,w): x=0.092, y=0.210, z=-0.121, w=0.966")
    print("="*80)
