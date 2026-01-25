"""
Verificar que el fade out se aplicó correctamente
"""
from pygltflib import GLTF2
import numpy as np
import struct

def get_buffer_data(gltf, accessor_index):
    accessor = gltf.accessors[accessor_index]
    buffer_view = gltf.bufferViews[accessor.bufferView]
    
    if gltf.buffers[0].uri:
        data = gltf.get_data_from_buffer_uri(gltf.buffers[0].uri)
    else:
        data = gltf.binary_blob()
    
    start = buffer_view.byteOffset + accessor.byteOffset
    type_sizes = {'SCALAR': 1, 'VEC2': 2, 'VEC3': 3, 'VEC4': 4}
    component_sizes = {5120: 1, 5121: 1, 5122: 2, 5123: 2, 5125: 4, 5126: 4}
    size = type_sizes[accessor.type] * component_sizes[accessor.componentType]
    end = start + accessor.count * size
    
    return data[start:end], accessor

def parse_accessor_data(data, accessor):
    component_type_map = {
        5120: ('b', np.int8),
        5121: ('B', np.uint8),
        5122: ('h', np.int16),
        5123: ('H', np.uint16),
        5125: ('I', np.uint32),
        5126: ('f', np.float32)
    }
    type_sizes = {'SCALAR': 1, 'VEC2': 2, 'VEC3': 3, 'VEC4': 4}
    fmt_char, dtype = component_type_map[accessor.componentType]
    components = type_sizes[accessor.type]
    values = struct.unpack(f'{accessor.count * components}{fmt_char}', data)
    
    if components > 1:
        return np.array(values, dtype=dtype).reshape(accessor.count, components)
    else:
        return np.array(values, dtype=dtype)

combined_path = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Cultura\Duvall_con_animacion_facial.glb"

print("="*80)
print("VERIFICACIÓN DEL FADE OUT EN ANIMACIÓN FACIAL")
print("="*80)

gltf = GLTF2().load(combined_path)

if gltf.animations:
    anim = gltf.animations[0]
    
    print(f"\n🎬 Animación: {anim.name}")
    
    # Analizar cada canal de shape keys
    for channel in anim.channels:
        if channel.target.path == "weights":
            node = gltf.nodes[channel.target.node]
            node_name = node.name if node.name else f"Node_{channel.target.node}"
            
            sampler = anim.samplers[channel.sampler]
            
            # Obtener times y weights
            times_data, times_acc = get_buffer_data(gltf, sampler.input)
            times = parse_accessor_data(times_data, times_acc)
            
            weights_data, weights_acc = get_buffer_data(gltf, sampler.output)
            weights = parse_accessor_data(weights_data, weights_acc)
            
            # Obtener número de shape keys
            mesh = gltf.meshes[node.mesh]
            num_shapekeys = 0
            for prim in mesh.primitives:
                if hasattr(prim, 'targets') and prim.targets:
                    num_shapekeys = len(prim.targets)
                    break
            
            # Reshape weights
            weights_2d = weights.reshape(len(times), num_shapekeys)
            
            print(f"\n📊 {node_name}:")
            print(f"  Frames totales: {len(times)}")
            print(f"  Shape keys: {num_shapekeys}")
            
            # Analizar valores en diferentes puntos
            print(f"\n  Análisis de valores:")
            
            # Encontrar el frame alrededor de 2.122s (inicio del fade out)
            fade_start_time = 2.122
            fade_end_time = 2.292
            
            # Frames antes del fade out (alrededor de 2.0s)
            before_idx = np.argmin(np.abs(times - 2.0))
            print(f"\n    Frame {before_idx} (t={times[before_idx]:.3f}s) - ANTES del fade out:")
            non_zero = np.count_nonzero(weights_2d[before_idx, :])
            max_val = np.max(weights_2d[before_idx, :])
            mean_val = np.mean(weights_2d[before_idx, :])
            print(f"      Valores no-cero: {non_zero}/{num_shapekeys}")
            print(f"      Max: {max_val:.4f}, Mean: {mean_val:.4f}")
            
            # Frame al inicio del fade out (2.122s)
            start_idx = np.argmin(np.abs(times - fade_start_time))
            print(f"\n    Frame {start_idx} (t={times[start_idx]:.3f}s) - INICIO del fade out:")
            non_zero = np.count_nonzero(weights_2d[start_idx, :])
            max_val = np.max(weights_2d[start_idx, :])
            mean_val = np.mean(weights_2d[start_idx, :])
            print(f"      Valores no-cero: {non_zero}/{num_shapekeys}")
            print(f"      Max: {max_val:.4f}, Mean: {mean_val:.4f}")
            
            # Frame a mitad del fade out
            mid_time = (fade_start_time + fade_end_time) / 2
            mid_idx = np.argmin(np.abs(times - mid_time))
            print(f"\n    Frame {mid_idx} (t={times[mid_idx]:.3f}s) - MITAD del fade out:")
            non_zero = np.count_nonzero(weights_2d[mid_idx, :])
            max_val = np.max(weights_2d[mid_idx, :])
            mean_val = np.mean(weights_2d[mid_idx, :])
            print(f"      Valores no-cero: {non_zero}/{num_shapekeys}")
            print(f"      Max: {max_val:.4f}, Mean: {mean_val:.4f}")
            
            # Frame al final del fade out (2.292s)
            end_idx = np.argmin(np.abs(times - fade_end_time))
            print(f"\n    Frame {end_idx} (t={times[end_idx]:.3f}s) - FIN del fade out:")
            non_zero = np.count_nonzero(weights_2d[end_idx, :])
            max_val = np.max(weights_2d[end_idx, :])
            mean_val = np.mean(weights_2d[end_idx, :])
            print(f"      Valores no-cero: {non_zero}/{num_shapekeys}")
            print(f"      Max: {max_val:.4f}, Mean: {mean_val:.4f}")
            
            # Frames después del fade out
            if len(times) > end_idx + 5:
                after_idx = end_idx + 5
                print(f"\n    Frame {after_idx} (t={times[after_idx]:.3f}s) - DESPUÉS del fade out:")
                non_zero = np.count_nonzero(weights_2d[after_idx, :])
                max_val = np.max(weights_2d[after_idx, :])
                mean_val = np.mean(weights_2d[after_idx, :])
                print(f"      Valores no-cero: {non_zero}/{num_shapekeys}")
                print(f"      Max: {max_val:.4f}, Mean: {mean_val:.4f}")
                
                if non_zero == 0:
                    print(f"      ✅ Todos los valores son 0 después del fade out")
                else:
                    print(f"      ⚠️ Hay valores no-cero después del fade out")
            
            # Verificar últimos frames
            print(f"\n    Frame {len(times)-1} (t={times[-1]:.3f}s) - ÚLTIMO FRAME:")
            non_zero = np.count_nonzero(weights_2d[-1, :])
            max_val = np.max(weights_2d[-1, :])
            print(f"      Valores no-cero: {non_zero}/{num_shapekeys}")
            print(f"      Max: {max_val:.4f}")
            
            if non_zero == 0:
                print(f"      ✅ El último frame está correctamente en 0")
            else:
                print(f"      ⚠️ El último frame tiene valores no-cero")

print("\n" + "="*80)
print("✅ VERIFICACIÓN COMPLETADA")
print("="*80)
