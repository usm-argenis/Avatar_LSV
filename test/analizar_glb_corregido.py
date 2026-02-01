"""
Verificar si el GLB exportado contiene los tracks de morph targets faciales
"""
import json
from pathlib import Path
import struct

glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\test_hola_corregido.glb")

with open(glb_path, 'rb') as f:
    # Header GLB
    magic = f.read(4)
    version = struct.unpack('<I', f.read(4))[0]
    length = struct.unpack('<I', f.read(4))[0]
    
    # JSON chunk
    chunk_length = struct.unpack('<I', f.read(4))[0]
    chunk_type = f.read(4)
    json_data = f.read(chunk_length).decode('utf-8')
    
    gltf = json.loads(json_data)
    
    print("📊 ANÁLISIS DE ANIMACIONES EN GLB:")
    print(f"\nTotal de animaciones: {len(gltf.get('animations', []))}")
    
    for i, anim in enumerate(gltf.get('animations', [])):
        print(f"\n{'='*60}")
        print(f"Animación #{i}: {anim.get('name', 'sin nombre')}")
        print(f"Channels: {len(anim.get('channels', []))}")
        print(f"Samplers: {len(anim.get('samplers', []))}")
        
        # Analizar channels
        morph_channels = []
        bone_channels = []
        
        for ch in anim.get('channels', []):
            path = ch['target'].get('path', '')
            node_idx = ch['target'].get('node')
            
            if path == 'weights':
                morph_channels.append((node_idx, ch))
            elif path in ['translation', 'rotation', 'scale']:
                bone_channels.append((node_idx, ch, path))
        
        print(f"\n  Channels de morphs (weights): {len(morph_channels)}")
        print(f"  Channels de huesos: {len(bone_channels)}")
        
        if morph_channels:
            print(f"\n  MORPH TARGET TRACKS:")
            for node_idx, ch in morph_channels:
                node_name = gltf['nodes'][node_idx].get('name', f'Node_{node_idx}')
                sampler_idx = ch['sampler']
                sampler = anim['samplers'][sampler_idx]
                
                # Obtener datos del accessor para saber cuántos valores
                output_accessor_idx = sampler['output']
                output_accessor = gltf['accessors'][output_accessor_idx]
                count = output_accessor['count']
                
                print(f"    - Node: {node_name} (#{node_idx})")
                print(f"      Keyframes: {count}")
                print(f"      Tipo: {output_accessor['type']}")
                print(f"      Componentes: {output_accessor.get('count', 'N/A')}")

print("\n✅ Análisis completado")
