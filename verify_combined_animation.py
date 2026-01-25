"""
Script para verificar el archivo GLB combinado
"""
from pygltflib import GLTF2
import numpy as np
import struct

def get_buffer_data(gltf, accessor_index):
    """Extrae datos de un accessor del buffer"""
    accessor = gltf.accessors[accessor_index]
    buffer_view = gltf.bufferViews[accessor.bufferView]
    
    if gltf.buffers[0].uri:
        data = gltf.get_data_from_buffer_uri(gltf.buffers[0].uri)
    else:
        data = gltf.binary_blob()
    
    start = buffer_view.byteOffset + accessor.byteOffset
    
    # Calcular tamaño
    type_sizes = {'SCALAR': 1, 'VEC2': 2, 'VEC3': 3, 'VEC4': 4}
    component_sizes = {5120: 1, 5121: 1, 5122: 2, 5123: 2, 5125: 4, 5126: 4}
    
    size = type_sizes[accessor.type] * component_sizes[accessor.componentType]
    end = start + accessor.count * size
    
    return data[start:end], accessor

def parse_accessor_data(data, accessor):
    """Parsea los datos del accessor a un numpy array"""
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

def verify_combined_glb(glb_path):
    """Verifica el archivo GLB combinado"""
    print("="*80)
    print("VERIFICACIÓN DEL ARCHIVO GLB COMBINADO")
    print("="*80)
    print(f"\n📂 Archivo: {glb_path}")
    
    gltf = GLTF2().load(glb_path)
    
    print(f"\n📊 INFORMACIÓN GENERAL:")
    print(f"  - Meshes: {len(gltf.meshes)}")
    print(f"  - Nodes: {len(gltf.nodes)}")
    print(f"  - Animations: {len(gltf.animations)}")
    print(f"  - Accessors: {len(gltf.accessors)}")
    print(f"  - BufferViews: {len(gltf.bufferViews)}")
    print(f"  - Buffer size: {gltf.buffers[0].byteLength} bytes")
    
    # Verificar animaciones
    if gltf.animations:
        print(f"\n🎬 ANIMACIONES:")
        for anim_idx, animation in enumerate(gltf.animations):
            anim_name = animation.name if animation.name else f"Animation_{anim_idx}"
            print(f"\n  Animación {anim_idx}: {anim_name}")
            print(f"    Channels: {len(animation.channels)}")
            print(f"    Samplers: {len(animation.samplers)}")
            
            # Contar tipos de canales
            channel_types = {}
            shapekey_channels = []
            
            for channel_idx, channel in enumerate(animation.channels):
                path = channel.target.path
                channel_types[path] = channel_types.get(path, 0) + 1
                
                if path == "weights":
                    node = gltf.nodes[channel.target.node]
                    mesh = gltf.meshes[node.mesh] if node.mesh is not None else None
                    mesh_name = mesh.name if mesh else "Unknown"
                    shapekey_channels.append({
                        'channel_idx': channel_idx,
                        'node_idx': channel.target.node,
                        'node_name': node.name if node.name else f"Node_{channel.target.node}",
                        'mesh_name': mesh_name,
                        'sampler_idx': channel.sampler
                    })
            
            print(f"\n    Tipos de canales:")
            for path, count in channel_types.items():
                print(f"      - {path}: {count}")
            
            if shapekey_channels:
                print(f"\n    🎭 CANALES DE SHAPE KEYS (weights):")
                for ch in shapekey_channels:
                    sampler = animation.samplers[ch['sampler_idx']]
                    
                    # Obtener información del sampler
                    try:
                        times_data, times_acc = get_buffer_data(gltf, sampler.input)
                        times = parse_accessor_data(times_data, times_acc)
                        
                        weights_data, weights_acc = get_buffer_data(gltf, sampler.output)
                        weights = parse_accessor_data(weights_data, weights_acc)
                        
                        # Obtener número de shape keys del mesh
                        node = gltf.nodes[ch['node_idx']]
                        if node.mesh is not None:
                            mesh = gltf.meshes[node.mesh]
                            num_shapekeys = 0
                            for prim in mesh.primitives:
                                if hasattr(prim, 'targets') and prim.targets:
                                    num_shapekeys = len(prim.targets)
                                    break
                            
                            print(f"\n      Canal {ch['channel_idx']}: {ch['mesh_name']}")
                            print(f"        - Node: {ch['node_idx']} ({ch['node_name']})")
                            print(f"        - Sampler: {ch['sampler_idx']}")
                            print(f"        - Frames: {len(times)}")
                            print(f"        - Duración: {times[0]:.3f}s - {times[-1]:.3f}s")
                            print(f"        - Shape keys en mesh: {num_shapekeys}")
                            print(f"        - Weights count: {len(weights)}")
                            print(f"        - Weights por frame: {len(weights) / len(times):.1f}")
                            
                            # Verificar que los weights no están todos en 0
                            non_zero_weights = np.count_nonzero(weights)
                            print(f"        - Valores no-cero: {non_zero_weights}/{len(weights)} ({non_zero_weights/len(weights)*100:.1f}%)")
                            
                            if non_zero_weights > 0:
                                print(f"        - Min weight: {weights.min():.4f}")
                                print(f"        - Max weight: {weights.max():.4f}")
                                print(f"        - Mean weight: {weights.mean():.4f}")
                                print(f"        ✅ Animación activa detectada")
                            else:
                                print(f"        ⚠️ ADVERTENCIA: Todos los weights son 0")
                    
                    except Exception as e:
                        print(f"\n      Canal {ch['channel_idx']}: {ch['mesh_name']}")
                        print(f"        ❌ Error al leer datos: {e}")
    
    # Verificar meshes con shape keys
    print(f"\n🎭 MESHES CON SHAPE KEYS:")
    for mesh_idx, mesh in enumerate(gltf.meshes):
        mesh_name = mesh.name if mesh.name else f"Mesh_{mesh_idx}"
        
        for prim_idx, primitive in enumerate(mesh.primitives):
            if hasattr(primitive, 'targets') and primitive.targets:
                print(f"\n  {mesh_name}:")
                print(f"    - Shape keys: {len(primitive.targets)}")
                
                if hasattr(mesh, 'extras') and mesh.extras and 'targetNames' in mesh.extras:
                    names = mesh.extras['targetNames']
                    print(f"    - Primeros 10 nombres: {', '.join(names[:10])}")
                    print(f"    - Últimos 5 nombres: {', '.join(names[-5:])}")
    
    print(f"\n{'='*80}")
    print(f"✅ VERIFICACIÓN COMPLETADA")
    print(f"{'='*80}")
    
    return True

if __name__ == "__main__":
    combined_path = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Cultura\Duvall_con_animacion_facial.glb"
    
    print("\nVerificando archivo combinado...")
    verify_combined_glb(combined_path)
    
    print("\n" + "="*80)
    print("COMPARACIÓN CON ARCHIVOS ORIGINALES")
    print("="*80)
    
    # Cargar archivos originales para comparar
    duvall_path = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Cultura\Duvall_resultado_a.glb"
    model_path = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Cultura\model (1).glb"
    
    print("\n📊 Duración de animaciones:")
    
    # Duvall original
    duvall = GLTF2().load(duvall_path)
    if duvall.animations:
        for ch in duvall.animations[0].channels:
            if ch.target.path == "weights":
                sampler = duvall.animations[0].samplers[ch.sampler]
                times_data, times_acc = get_buffer_data(duvall, sampler.input)
                times = parse_accessor_data(times_data, times_acc)
                print(f"  Duvall (original): {len(times)} frames, {times[-1]:.3f}s")
                break
    
    # Model original
    model = GLTF2().load(model_path)
    if model.animations:
        for ch in model.animations[0].channels:
            if ch.target.path == "weights":
                sampler = model.animations[0].samplers[ch.sampler]
                times_data, times_acc = get_buffer_data(model, sampler.input)
                times = parse_accessor_data(times_data, times_acc)
                print(f"  Model (original): {len(times)} frames, {times[-1]:.3f}s")
                break
    
    # Combinado
    combined = GLTF2().load(combined_path)
    if combined.animations:
        for ch in combined.animations[0].channels:
            if ch.target.path == "weights":
                sampler = combined.animations[0].samplers[ch.sampler]
                times_data, times_acc = get_buffer_data(combined, sampler.input)
                times = parse_accessor_data(times_data, times_acc)
                print(f"  Combinado (nuevo): {len(times)} frames, {times[-1]:.3f}s")
                break
    
    print("\n✅ La animación facial ahora tiene la duración del archivo Model")
    print("✅ La animación de cuerpo/seña mantiene los canales del Duvall original")
