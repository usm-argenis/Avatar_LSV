"""
Verificar qué contiene el archivo compensado
"""

import bpy
from pathlib import Path

print("="*80)
print("VERIFICACIÓN: Qué contiene Duvall_abril_BRAZOS_COMPENSADO.glb")
print("="*80)

file_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_BRAZOS_COMPENSADO.glb")

bpy.ops.wm.read_homefile(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(file_path))

print(f"\n📦 Objetos en la escena:")
for obj in bpy.data.objects:
    print(f"  - {obj.name} (tipo: {obj.type})")
    if obj.type == 'ARMATURE':
        print(f"    Huesos: {len(obj.data.bones)}")
        print(f"    Nombre: {obj.name}")
