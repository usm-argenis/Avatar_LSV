#!/usr/bin/env python3
"""
Verificar qué backup de agarrar tiene 93 nodos (misma estructura que los procesados)
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

base_dir = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos")

print(f"\n{'='*80}")
print("VERIFICANDO BACKUPS DE AGARRAR")
print(f"{'='*80}\n")

# Verificar agarrar actual
archivo_actual = base_dir / "Duvall_resultado_agarrar.glb"
gltf_actual = leer_glb(archivo_actual)
print(f"ACTUAL: {archivo_actual.name}")
print(f"  Total nodos: {len(gltf_actual['nodes'])}")
print(f"  Node 0: {gltf_actual['nodes'][0].get('name', 'N/A')}")
print(f"  Node 1: {gltf_actual['nodes'][1].get('name', 'N/A')}\n")

# Verificar backups
backups = list(base_dir.glob("Duvall_resultado_agarrar.glb.backup*"))
for backup in backups:
    try:
        gltf = leer_glb(backup)
        print(f"BACKUP: {backup.name}")
        print(f"  Total nodos: {len(gltf['nodes'])}")
        print(f"  Node 0: {gltf['nodes'][0].get('name', 'N/A')}")
        print(f"  Node 1: {gltf['nodes'][1].get('name', 'N/A')}")
        
        # Buscar Armature
        for i, node in enumerate(gltf['nodes']):
            if node.get('name') == 'Armature':
                print(f"  Armature Node: {i}")
                print(f"  Armature Rotation: {node.get('rotation', [0,0,0,1])}")
                break
        print()
    except Exception as e:
        print(f"  ERROR: {e}\n")

# Comparar con amar
archivo_amar = base_dir / "Duvall_resultado_amar.glb"
gltf_amar = leer_glb(archivo_amar)
print(f"{'='*80}")
print(f"COMPARACIÓN: {archivo_amar.name}")
print(f"  Total nodos: {len(gltf_amar['nodes'])}")
print(f"  Node 0: {gltf_amar['nodes'][0].get('name', 'N/A')}")
print(f"  Node 1: {gltf_amar['nodes'][1].get('name', 'N/A')}")
for i, node in enumerate(gltf_amar['nodes']):
    if node.get('name') == 'Armature':
        print(f"  Armature Node: {i}")
        print(f"  Armature Rotation: {node.get('rotation', [0,0,0,1])}")
        break

print(f"\n{'='*80}\n")
