"""
Verificar qué animaciones tiene el GLB importado
"""
import bpy
from pathlib import Path

# Limpiar
bpy.ops.wm.read_homefile(use_empty=True)

# Importar
glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\saludos\Duvall_resultado_hola.glb")
bpy.ops.import_scene.gltf(filepath=str(glb_path))

print("\n=== ACCIONES EN EL ARCHIVO ===")
for action in bpy.data.actions:
    print(f"\nAcción: {action.name}")
    print(f"  F-Curves: {len(action.fcurves)}")
    if action.fcurves:
        print(f"  Primeros data paths:")
        for fcurve in list(action.fcurves)[:5]:
            print(f"    - {fcurve.data_path}")

print("\n=== OBJETOS CON ANIMACIÓN ===")
for obj in bpy.data.objects:
    if obj.animation_data and obj.animation_data.action:
        print(f"\nObjeto: {obj.name}")
        print(f"  Tipo: {obj.type}")
        print(f"  Acción: {obj.animation_data.action.name}")
