import json
import struct
from pathlib import Path
import os

def verificar_keyframes(glb_path):
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
            for channel in anim.get('channels', []):
                target = channel.get('target', {})
                if target.get('path') == 'weights':
                    node_idx = target.get('node', -1)
                    sampler_idx = channel.get('sampler', -1)
                    
                    node_name = "Unknown"
                    if 'nodes' in gltf and 0 <= node_idx < len(gltf['nodes']):
                        node_name = gltf['nodes'][node_idx].get('name', f'Node_{node_idx}')
                    
                    # Obtener sampler
                    if 'samplers' in anim and 0 <= sampler_idx < len(anim['samplers']):
                        sampler = anim['samplers'][sampler_idx]
                        input_accessor = sampler.get('input', -1)
                        output_accessor = sampler.get('output', -1)
                        
                        # Obtener información de accessors
                        if 'accessors' in gltf:
                            if 0 <= input_accessor < len(gltf['accessors']):
                                time_accessor = gltf['accessors'][input_accessor]
                                num_keyframes = time_accessor.get('count', 0)
                                
                                if 0 <= output_accessor < len(gltf['accessors']):
                                    values_accessor = gltf['accessors'][output_accessor]
                                    num_values = values_accessor.get('count', 0)
                                    
                                    print(f"Track: {node_name}")
                                    print(f"  Keyframes: {num_keyframes}")
                                    print(f"  Valores: {num_values}")
                                    print()

# Verificar
base_dir = Path(__file__).parent

# Buscar hola.glb
for root, dirs, files in os.walk(base_dir / 'output' / 'glb' / 'Duvall'):
    for file in files:
        if file.lower().endswith('.glb') and 'hola' in file.lower():
            hola_glb = Path(root) / file
            verificar_keyframes(hola_glb)
            break
