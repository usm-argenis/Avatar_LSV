#!/usr/bin/env python3
"""
Verificar estructura y transformaciones de Duvall_resultado_vestir.glb
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

# Buscar el archivo vestir
vestir_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_vestir.glb")

if not vestir_path.exists():
    print(f"❌ No se encontró: {vestir_path}")
    # Buscar en otras ubicaciones
    base = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
    encontrado = list(base.rglob("*vestir*.glb"))
    if encontrado:
        print(f"\nArchivos encontrados con 'vestir':")
        for f in encontrado:
            print(f"  {f}")
        vestir_path = encontrado[0]
    else:
        print("\n⚠️  No se encontró ningún archivo con 'vestir'")
        exit(1)

print(f"\n{'='*80}")
print(f"ANÁLISIS DE: {vestir_path.name}")
print(f"{'='*80}\n")

gltf = leer_glb(vestir_path)

print(f"📊 INFORMACIÓN GENERAL")
print(f"  Total nodos: {len(gltf['nodes'])}")
print(f"  Total animaciones: {len(gltf.get('animations', []))}\n")

print(f"🔍 PRIMEROS 5 NODOS:")
for i in range(min(5, len(gltf['nodes']))):
    node = gltf['nodes'][i]
    print(f"  Node {i}: {node.get('name', 'N/A')}")
    if 'rotation' in node:
        print(f"    Rotation: {node['rotation']}")
    if 'scale' in node:
        print(f"    Scale: {node['scale']}")
    if 'translation' in node:
        print(f"    Translation: {node['translation']}")

# Buscar Armature
print(f"\n🎯 ARMATURE:")
for i, node in enumerate(gltf['nodes']):
    if node.get('name') == 'Armature':
        print(f"  Node Index: {i}")
        print(f"  Rotation: {node.get('rotation', [0, 0, 0, 1])}")
        print(f"  Scale: {node.get('scale', [1, 1, 1])}")
        print(f"  Translation: {node.get('translation', [0, 0, 0])}")
        break

# Comparar con agarrar
agarrar_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.glb")
if agarrar_path.exists():
    gltf_agarrar = leer_glb(agarrar_path)
    
    print(f"\n{'='*80}")
    print(f"COMPARACIÓN CON AGARRAR (REFERENCIA)")
    print(f"{'='*80}\n")
    
    print(f"AGARRAR:")
    print(f"  Total nodos: {len(gltf_agarrar['nodes'])}")
    print(f"  Node 0: {gltf_agarrar['nodes'][0].get('name', 'N/A')}")
    print(f"  Node 1: {gltf_agarrar['nodes'][1].get('name', 'N/A')}")
    
    for i, node in enumerate(gltf_agarrar['nodes']):
        if node.get('name') == 'Armature':
            print(f"  Armature Node: {i}")
            print(f"  Armature Rotation: {node.get('rotation', [0, 0, 0, 1])}")
            break
    
    print(f"\nVESTIR:")
    print(f"  Total nodos: {len(gltf['nodes'])}")
    print(f"  Node 0: {gltf['nodes'][0].get('name', 'N/A')}")
    print(f"  Node 1: {gltf['nodes'][1].get('name', 'N/A')}")
    
    if len(gltf_agarrar['nodes']) == len(gltf['nodes']):
        print(f"\n✅ MISMA CANTIDAD DE NODOS")
    else:
        print(f"\n❌ DIFERENTE CANTIDAD DE NODOS ({len(gltf['nodes'])} vs {len(gltf_agarrar['nodes'])})")

print(f"\n{'='*80}\n")
