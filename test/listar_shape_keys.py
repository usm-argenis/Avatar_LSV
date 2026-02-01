"""
Script para extraer los nombres de shape keys disponibles en un GLB de ReadyPlayerMe
"""

import bpy
import sys

# Limpiar la escena
bpy.ops.wm.read_homefile(use_empty=True)

# Importar un GLB de ejemplo
glb_path = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\numero\Duvall_resultado_0.glb"
bpy.ops.import_scene.gltf(filepath=glb_path)

# Buscar el objeto Wolf3D_Head
for obj in bpy.data.objects:
    if 'Wolf3D_Head' in obj.name and obj.type == 'MESH':
        if obj.data.shape_keys:
            print("Shape keys encontrados en", obj.name)
            print("=" * 70)
            for i, sk in enumerate(obj.data.shape_keys.key_blocks):
                print(f"{i}: {sk.name}")
            print("=" * 70)
            print(f"Total: {len(obj.data.shape_keys.key_blocks)}")
        break
