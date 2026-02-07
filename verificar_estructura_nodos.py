#!/usr/bin/env python3
"""
Verificar estructura completa de nodos (Node 0, Armature, etc.)
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
        
        return json.loads(json_data)

# Archivo de referencia
ref_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.glb")
gltf_ref = leer_glb(ref_path)

print(f"\n{'='*80}")
print(f"ESTRUCTURA DE NODOS - REFERENCIA: {ref_path.name}")
print(f"{'='*80}\n")

print(f"Total nodos: {len(gltf_ref['nodes'])}\n")

# Mostrar los primeros 5 nodos
for i in range(min(5, len(gltf_ref['nodes']))):
    node = gltf_ref['nodes'][i]
    print(f"Node {i}: {node.get('name', 'N/A')}")
    if 'rotation' in node:
        print(f"  Rotation: {node['rotation']}")
    if 'scale' in node:
        print(f"  Scale: {node['scale']}")
    if 'translation' in node:
        print(f"  Translation: {node['translation']}")

# Buscar Armature
for i, node in enumerate(gltf_ref['nodes']):
    if node.get('name') == 'Armature':
        print(f"\nNode {i} (Armature):")
        print(f"  Rotation: {node.get('rotation', [0,0,0,1])}")
        print(f"  Scale: {node.get('scale', [1,1,1])}")
        print(f"  Translation: {node.get('translation', [0,0,0])}")
        break

# Comparar con uno de los procesados
comp_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_amar.glb")
gltf_comp = leer_glb(comp_path)

print(f"\n{'='*80}")
print(f"COMPARACIÓN CON: {comp_path.name}")
print(f"{'='*80}\n")

print(f"Total nodos: {len(gltf_comp['nodes'])}\n")

# Mostrar los primeros 5 nodos
for i in range(min(5, len(gltf_comp['nodes']))):
    node = gltf_comp['nodes'][i]
    print(f"Node {i}: {node.get('name', 'N/A')}")
    if 'rotation' in node:
        print(f"  Rotation: {node['rotation']}")
    if 'scale' in node:
        print(f"  Scale: {node['scale']}")
    if 'translation' in node:
        print(f"  Translation: {node['translation']}")

# Buscar Armature
for i, node in enumerate(gltf_comp['nodes']):
    if node.get('name') == 'Armature':
        print(f"\nNode {i} (Armature):")
        print(f"  Rotation: {node.get('rotation', [0,0,0,1])}")
        print(f"  Scale: {node.get('scale', [1,1,1])}")
        print(f"  Translation: {node.get('translation', [0,0,0])}")
        break

print(f"\n{'='*80}\n")
