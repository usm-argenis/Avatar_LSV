import json
import struct
from pathlib import Path
import os

def verificar_tracks_animacion(glb_path):
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
        
        print(f"\nArchivo: {os.path.basename(glb_path)}\n")
        
        # Analizar animaciones
        if 'animations' in gltf and gltf['animations']:
            anim = gltf['animations'][0]
            
            # Buscar channels de tipo weights
            weight_channels = []
            for channel in anim.get('channels', []):
                target = channel.get('target', {})
                if target.get('path') == 'weights':
                    node_idx = target.get('node', -1)
                    node_name = "Unknown"
                    if 'nodes' in gltf and 0 <= node_idx < len(gltf['nodes']):
                        node_name = gltf['nodes'][node_idx].get('name', f'Node_{node_idx}')
                    weight_channels.append(node_name)
            
            print(f"TRACKS DE MORPH TARGETS ({len(weight_channels)}):")
            for name in weight_channels:
                print(f"  - {name}")

# Verificar
base_dir = Path(__file__).parent
hola_glb = None

for root, dirs, files in os.walk(base_dir / 'output' / 'glb' / 'Duvall'):
    for file in files:
        if file.lower().endswith('.glb') and 'hola' in file.lower():
            hola_glb = Path(root) / file
            break
    if hola_glb:
        break

if hola_glb and hola_glb.exists():
    verificar_tracks_animacion(hola_glb)
