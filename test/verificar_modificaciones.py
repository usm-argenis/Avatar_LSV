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

def verificar_rango_completo(filepath, bone_name, frame_min, frame_max, valores_esperados):
    """Verificar que los valores se aplicaron en el rango completo"""
    print(f"\n{'='*100}")
    print(f"🔍 VERIFICACIÓN COMPLETA: {bone_name}")
    print(f"{'='*100}")
    
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
            
            print(f"📊 Total keyframes: {len(times)}")
            print(f"⏱️  Duración: {times[-1]:.3f}s")
            print(f"\n🎯 Valores esperados (glTF x,y,z,w):")
            print(f"   x={valores_esperados[0]:.3f}, y={valores_esperados[1]:.3f}, "
                  f"z={valores_esperados[2]:.3f}, w={valores_esperados[3]:.3f}")
            
            print(f"\n📋 ANÁLISIS FRAME POR FRAME (rango {frame_min}-{frame_max}):")
            print(f"{'Frame':>6} | {'Keyframe':>9} | {'Tiempo':>8} | {'X':>8} | {'Y':>8} | {'Z':>8} | {'W':>8} | {'Estado'}")
            print("-" * 100)
            
            modificados_correctos = 0
            modificados_incorrectos = 0
            
            for frame in range(frame_min, frame_max + 1):
                target_time = frame / fps
                
                # Buscar keyframe más cercano
                closest_idx = 0
                min_diff = abs(times[0] - target_time)
                for i, t in enumerate(times):
                    diff = abs(t - target_time)
                    if diff < min_diff:
                        min_diff = diff
                        closest_idx = i
                
                rot = rotations[closest_idx]
                
                # Verificar si coincide con valores esperados (tolerancia 0.001)
                coincide = all(abs(rot[i] - valores_esperados[i]) < 0.001 for i in range(4))
                
                if frame >= 25 and frame <= 30:  # Rango de retención
                    if coincide:
                        estado = "✅ CORRECTO"
                        modificados_correctos += 1
                    else:
                        estado = "❌ ERROR"
                        modificados_incorrectos += 1
                elif frame >= 20 and frame < 25:  # Transición entrada
                    estado = "🔄 Interpolando entrada"
                elif frame > 30 and frame <= 35:  # Transición salida
                    estado = "🔄 Interpolando salida"
                else:
                    estado = "⚪ Original"
                
                print(f"{frame:6d} | {closest_idx:9d} | {times[closest_idx]:8.3f} | "
                      f"{rot[0]:8.3f} | {rot[1]:8.3f} | {rot[2]:8.3f} | {rot[3]:8.3f} | {estado}")
            
            print("-" * 100)
            print(f"\n📊 RESUMEN:")
            print(f"   ✅ Frames modificados correctamente: {modificados_correctos}/6")
            print(f"   ❌ Frames con error: {modificados_incorrectos}/6")
            
            if modificados_incorrectos == 0:
                print(f"\n   🎉 ÉXITO: Todos los frames en el rango de retención (25-30) están correctos")
            else:
                print(f"\n   ⚠️  ADVERTENCIA: Hay frames incorrectos en el rango de retención")
            
            return

if __name__ == "__main__":
    # Cargar configuración
    with open('datos.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    glb_path = list(config.keys())[0]
    modifications = config[glb_path]
    alcance = modifications['alcance']
    
    filepath = "output/glb/Duvall/alfabeto/Duvall_resultado_b_modif.glb"
    
    print("\n" + "="*100)
    print("🔍 VERIFICACIÓN EXHAUSTIVA DE MODIFICACIONES GLB")
    print("="*100)
    print(f"📁 Archivo: {filepath}")
    print(f"🎯 Rango: frames {alcance['min']} - {alcance['max']}")
    print(f"⏱️  Retención: {alcance['retencion']} frames (centro: 25-30)")
    
    # Verificar cada hueso
    for bone_name in modifications:
        if bone_name == 'alcance':
            continue
        
        target_values = modifications[bone_name]
        # Convertir de JSON (w,x,y,z) a glTF (x,y,z,w)
        valores_gltf = [target_values['x'], target_values['y'], target_values['z'], target_values['w']]
        
        verificar_rango_completo(filepath, bone_name, alcance['min'], alcance['max'], valores_gltf)
    
    print("\n" + "="*100)
    print("✅ VERIFICACIÓN COMPLETADA")
    print("="*100)
