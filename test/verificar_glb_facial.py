"""
Script para verificar que los archivos GLB tienen animaciones faciales correctamente embebidas
"""
import json
import struct
import os

def verificar_animaciones_glb(glb_path):
    """Verifica las animaciones dentro de un archivo GLB"""
    print(f"\n{'='*70}")
    print(f"Verificando: {os.path.basename(glb_path)}")
    print(f"{'='*70}")
    
    with open(glb_path, 'rb') as f:
        # Leer header GLB
        magic = f.read(4)
        version = struct.unpack('<I', f.read(4))[0]
        length = struct.unpack('<I', f.read(4))[0]
        
        # Leer chunk JSON
        json_chunk_length = struct.unpack('<I', f.read(4))[0]
        json_chunk_type = f.read(4)
        json_data = f.read(json_chunk_length)
        
        gltf = json.loads(json_data)
        
        # Verificar animaciones
        if 'animations' in gltf:
            print(f"✅ Animaciones encontradas: {len(gltf['animations'])}")
            
            for idx, anim in enumerate(gltf['animations']):
                print(f"\n  Animación {idx}: {anim.get('name', 'Sin nombre')}")
                print(f"    Canales: {len(anim.get('channels', []))}")
                
                # Buscar canales de morph targets
                morph_channels = []
                for channel in anim.get('channels', []):
                    target = channel.get('target', {})
                    if target.get('path') == 'weights':
                        morph_channels.append(channel)
                        sampler_idx = channel.get('sampler', 0)
                        node_idx = target.get('node', -1)
                        
                        # Obtener nombre del nodo
                        node_name = "Desconocido"
                        if 'nodes' in gltf and node_idx < len(gltf['nodes']):
                            node_name = gltf['nodes'][node_idx].get('name', f'Node_{node_idx}')
                        
                        print(f"      ✅ Morph target channel -> Nodo: {node_name} (sampler: {sampler_idx})")
                
                if morph_channels:
                    print(f"    ✅ Total canales de morph targets: {len(morph_channels)}")
                else:
                    print(f"    ⚠️  No se encontraron canales de morph targets")
        else:
            print("❌ No se encontraron animaciones en el GLB")
        
        # Verificar nodos con morph targets
        if 'nodes' in gltf:
            nodes_with_morphs = []
            for idx, node in enumerate(gltf['nodes']):
                if 'mesh' in node:
                    mesh_idx = node['mesh']
                    if 'meshes' in gltf and mesh_idx < len(gltf['meshes']):
                        mesh = gltf['meshes'][mesh_idx]
                        if 'extras' in mesh and 'targetNames' in mesh['extras']:
                            nodes_with_morphs.append({
                                'name': node.get('name', f'Node_{idx}'),
                                'targets': mesh['extras']['targetNames']
                            })
            
            if nodes_with_morphs:
                print(f"\n✅ Nodos con morph targets: {len(nodes_with_morphs)}")
                for node_info in nodes_with_morphs:
                    print(f"  - {node_info['name']}: {len(node_info['targets'])} targets")
                    print(f"    Primeros targets: {node_info['targets'][:5]}")

# Verificar las 5 palabras de prueba
palabras_prueba = ['hola', 'adios', 'amar', 'bienvenido', 'buenos dias']

for palabra in palabras_prueba:
    # Buscar el archivo GLB
    palabra_normalizada = palabra.lower().replace(' ', '_')
    
    # Buscar en todas las carpetas de Duvall
    for root, dirs, files in os.walk('output/glb/Duvall'):
        for file in files:
            if file.endswith('.glb'):
                # Extraer el nombre base del archivo
                nombre_base = os.path.splitext(file)[0].lower().replace('_', ' ')
                
                if palabra.lower() == nombre_base:
                    glb_path = os.path.join(root, file)
                    verificar_animaciones_glb(glb_path)
                    break

print(f"\n{'='*70}")
print("Verificación completada")
print(f"{'='*70}")
