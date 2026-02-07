#!/usr/bin/env python3
"""
Analiza en detalle la estructura de agarrar vs amar
"""
import json
import struct
from pathlib import Path

def leer_glb(ruta_glb):
    with open(ruta_glb, 'rb') as f:
        magic = f.read(4)
        version = struct.unpack('<I', f.read(4))[0]
        length = struct.unpack('<I', f.read(4))[0]
        
        chunk_length = struct.unpack('<I', f.read(4))[0]
        chunk_type = f.read(4)
        json_data = f.read(chunk_length).decode('utf-8')
        gltf = json.loads(json_data)
        
        bin_chunk_length = struct.unpack('<I', f.read(4))[0]
        bin_chunk_type = f.read(4)
        bin_data = f.read(bin_chunk_length) if bin_chunk_type == b'BIN\x00' else None
        
        return gltf, bin_data, version

verbos_dir = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos")

agarrar = verbos_dir / "Duvall_resultado_agarrar.glb"
amar = verbos_dir / "Duvall_resultado_amar.glb"

gltf_agarrar, _, _ = leer_glb(agarrar)
gltf_amar, _, _ = leer_glb(amar)

print(f"\n{'='*80}")
print("ANÁLISIS DETALLADO: AGARRAR vs AMAR")
print(f"{'='*80}\n")

print("AGARRAR:")
print(f"  Nodos totales: {len(gltf_agarrar['nodes'])}")
print(f"  Meshes totales: {len(gltf_agarrar.get('meshes', []))}")
print(f"  Scene nodes: {gltf_agarrar['scenes'][0]['nodes']}")
print(f"\n  Primeros 10 nodos:")
for i in range(min(10, len(gltf_agarrar['nodes']))):
    node = gltf_agarrar['nodes'][i]
    mesh_info = f" mesh={node.get('mesh', 'N/A')}" if 'mesh' in node else ""
    skin_info = f" skin={node.get('skin', 'N/A')}" if 'skin' in node else ""
    children = f" children={node.get('children', [])[:3]}" if 'children' in node else ""
    print(f"    {i}: {node.get('name', 'N/A')}{mesh_info}{skin_info}{children}")

print(f"\nAMAR:")
print(f"  Nodos totales: {len(gltf_amar['nodes'])}")
print(f"  Meshes totales: {len(gltf_amar.get('meshes', []))}")
print(f"  Scene nodes: {gltf_amar['scenes'][0]['nodes']}")
print(f"\n  Primeros 10 nodos:")
for i in range(min(10, len(gltf_amar['nodes']))):
    node = gltf_amar['nodes'][i]
    mesh_info = f" mesh={node.get('mesh', 'N/A')}" if 'mesh' in node else""
    skin_info = f" skin={node.get('skin', 'N/A')}" if 'skin' in node else ""
    children = f" children={node.get('children', [])[:3]}" if 'children' in node else ""
    print(f"    {i}: {node.get('name', 'N/A')}{mesh_info}{skin_info}{children}")

# Verificar estructura de skins
print(f"\n{'='*40}")
print("SKINS:")
print(f"{'='*40}")
print(f"\nAGARRAR skins: {len(gltf_agarrar.get('skins', []))}")
if 'skins' in gltf_agarrar:
    for i, skin in enumerate(gltf_agarrar['skins'][:2]):
        print(f"  Skin {i}: skeleton={skin.get('skeleton', 'N/A')}, joints count={len(skin.get('joints', []))}")

print(f"\nAMAR skins: {len(gltf_amar.get('skins', []))}")
if 'skins' in gltf_amar:
    for i, skin in enumerate(gltf_amar['skins'][:2]):
        print(f"  Skin {i}: skeleton={skin.get('skeleton', 'N/A')}, joints count={len(skin.get('joints', []))}")

print(f"\n{'='*80}\n")
