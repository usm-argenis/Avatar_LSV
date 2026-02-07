#!/usr/bin/env blender --python
"""
Comparar agarrar CORREGIDO (funciona bien) vs atraer (no funciona)
"""
import bpy
import sys
from pathlib import Path
import json
import struct

def leer_glb_estructura(ruta_glb):
    """Lee la estructura JSON del GLB"""
    with open(ruta_glb, 'rb') as f:
        f.read(4)  # magic
        f.read(4)  # version
        f.read(4)  # length
        chunk_length = struct.unpack('<I', f.read(4))[0]
        f.read(4)  # chunk_type
        json_data = f.read(chunk_length).decode('utf-8')
        return json.loads(json_data)

archivos = [
    (Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.glb"), "AGARRAR (funciona bien)"),
    (Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_atraer.glb"), "ATRAER (volteado)"),
]

print(f"\n{'='*80}")
print("COMPARACIÓN: AGARRAR (bien) vs ATRAER (volteado)")
print(f"{'='*80}\n")

for archivo, descripcion in archivos:
    if not archivo.exists():
        print(f"⚠️  No existe: {descripcion}\n")
        continue
    
    print(f"📂 {descripcion}")
    print(f"{'='*80}")
    
    # Leer estructura GLB
    gltf = leer_glb_estructura(archivo)
    print(f"📊 Estructura GLB:")
    print(f"   Total nodos: {len(gltf['nodes'])}")
    print(f"   Node 0: {gltf['nodes'][0].get('name')}")
    if len(gltf['nodes']) > 1:
        print(f"   Node 1: {gltf['nodes'][1].get('name')}")
    
    # Verificar si Node 0 o Node 1 tiene rotación/escala
    for i in range(min(2, len(gltf['nodes']))):
        node = gltf['nodes'][i]
        if 'rotation' in node or 'scale' in node:
            rot = node.get('rotation', [0, 0, 0, 1])
            scale = node.get('scale', [1, 1, 1])
            print(f"   Node {i} ({node.get('name')}):")
            print(f"      Rotation: {rot}")
            print(f"      Scale: {scale}")
    
    # Importar en Blender para verificar
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(archivo))
    
    # Buscar armature
    armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            armature = obj
            break
    
    if armature:
        print(f"\n🦴 Armature en Blender:")
        print(f"   Rotation (quat): ({armature.rotation_quaternion.x:.4f}, {armature.rotation_quaternion.y:.4f}, {armature.rotation_quaternion.z:.4f}, {armature.rotation_quaternion.w:.4f})")
        print(f"   Scale: ({armature.scale.x:.4f}, {armature.scale.y:.4f}, {armature.scale.z:.4f})")
    
    print()

print(f"{'='*80}\n")
sys.exit(0)
