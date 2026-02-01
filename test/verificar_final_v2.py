"""
Verificar archivo final V2
"""

import bpy
from pathlib import Path

print("="*80)
print("VERIFICACIÓN: Duvall_abril_BRAZOS_FINAL_V2.glb")
print("="*80)

file_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_BRAZOS_FINAL_V2.glb")

bpy.ops.wm.read_homefile(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(file_path))

print(f"\n📦 ARMATURES en la escena:")
armature_count = 0
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        armature_count += 1
        print(f"  - {obj.name} ({len(obj.data.bones)} huesos)")
        
        if obj.animation_data and obj.animation_data.action:
            fcurves = len(obj.animation_data.action.fcurves)
            print(f"    FCurves: {fcurves}")
            print(f"    Frames: {obj.animation_data.action.frame_range}")

if armature_count == 0:
    print(f"  ❌ ERROR: No hay armatures")
elif armature_count == 1:
    print(f"\n  ✅ CORRECTO: Solo 1 armature")
else:
    print(f"\n  ❌ ERROR: Hay {armature_count} armatures (debería ser 1)")

print(f"\n📊 Total de objetos: {len(bpy.data.objects)}")
