"""
Script de diagnóstico para ver cómo se nombran los objetos en el GLB exportado
"""
import json
import struct
import os
from pathlib import Path

def analizar_glb(glb_path):
    """Analiza la estructura de nombres en un archivo GLB"""
    print(f"\n{'='*70}")
    print(f"Analizando: {glb_path.name}")
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
        
        # Listar todos los nodos
        print("\n📦 NODOS EN EL GLB:")
        if 'nodes' in gltf:
            for idx, node in enumerate(gltf['nodes']):
                name = node.get('name', f'Node_{idx}')
                node_type = []
                if 'mesh' in node:
                    node_type.append('MESH')
                if 'skin' in node:
                    node_type.append('SKIN')
                if 'camera' in node:
                    node_type.append('CAMERA')
                if not node_type:
                    node_type.append('EMPTY')
                
                type_str = ', '.join(node_type)
                print(f"  [{idx:3d}] {name:30s} ({type_str})")
        
        # Analizar animaciones
        print("\n🎬 ANIMACIONES:")
        if 'animations' in gltf:
            for anim_idx, anim in enumerate(gltf['animations']):
                anim_name = anim.get('name', f'Animation_{anim_idx}')
                print(f"\n  Animación {anim_idx}: {anim_name}")
                print(f"  Canales: {len(anim.get('channels', []))}")
                
                # Analizar canales
                channels_by_type = {}
                for channel in anim.get('channels', []):
                    target = channel.get('target', {})
                    path = target.get('path', 'unknown')
                    node_idx = target.get('node', -1)
                    
                    if path not in channels_by_type:
                        channels_by_type[path] = []
                    
                    # Obtener nombre del nodo
                    node_name = "Unknown"
                    if 'nodes' in gltf and 0 <= node_idx < len(gltf['nodes']):
                        node_name = gltf['nodes'][node_idx].get('name', f'Node_{node_idx}')
                    
                    channels_by_type[path].append({
                        'node_idx': node_idx,
                        'node_name': node_name
                    })
                
                # Mostrar resumen por tipo
                for path, channels in channels_by_type.items():
                    print(f"\n    {path.upper()} tracks: {len(channels)}")
                    for ch in channels[:5]:  # Mostrar solo los primeros 5
                        print(f"      - Node[{ch['node_idx']:3d}]: {ch['node_name']}")
                    if len(channels) > 5:
                        print(f"      ... y {len(channels)-5} más")
        
        # Analizar meshes con morph targets
        print("\n🎭 MESHES CON MORPH TARGETS:")
        if 'meshes' in gltf:
            for mesh_idx, mesh in enumerate(gltf['meshes']):
                mesh_name = mesh.get('name', f'Mesh_{mesh_idx}')
                
                # Verificar si tiene morph targets
                has_morphs = False
                if 'extras' in mesh and 'targetNames' in mesh['extras']:
                    has_morphs = True
                    target_names = mesh['extras']['targetNames']
                    print(f"\n  Mesh {mesh_idx}: {mesh_name}")
                    print(f"    Morph targets: {len(target_names)}")
                    print(f"    Primeros targets: {target_names[:5]}")

# Analizar el archivo hola.glb
base_dir = Path(__file__).parent
hola_glb = None

# Buscar hola.glb
for root, dirs, files in os.walk(base_dir / 'output' / 'glb' / 'Duvall'):
    for file in files:
        if file.lower().endswith('.glb') and 'hola' in file.lower():
            hola_glb = Path(root) / file
            break
    if hola_glb:
        break

if hola_glb and hola_glb.exists():
    import os
    analizar_glb(hola_glb)
else:
    print("❌ No se encontró hola.glb")
