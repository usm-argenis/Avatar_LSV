#!/usr/bin/env blender --python
"""
Script de Blender para exportar el archivo .blend limpio a GLB
"""
import bpy
import sys
from pathlib import Path

# Rutas
archivo_blend = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.blend")
archivo_glb = archivo_blend.with_suffix('.glb')

print(f"\n{'='*80}")
print("EXPORTAR .BLEND A .GLB")
print(f"{'='*80}\n")

# Crear backup del GLB actual
import shutil
if archivo_glb.exists():
    backup = archivo_glb.with_suffix('.glb.backup_PRE_EXPORT')
    shutil.copy2(archivo_glb, backup)
    print(f"💾 Backup del GLB actual: {backup.name}\n")

# Abrir el archivo .blend
print(f"📂 Abriendo: {archivo_blend.name}")
bpy.ops.wm.open_mainfile(filepath=str(archivo_blend))

print(f"\n🔍 Objetos en la escena:")
for obj in bpy.data.objects:
    obj_type = obj.type
    parent_info = f" (parent: {obj.parent.name})" if obj.parent else " (root)"
    print(f"  - {obj.name} [{obj_type}]{parent_info}")

# Exportar a GLB
print(f"\n💾 Exportando a: {archivo_glb.name}")
bpy.ops.export_scene.gltf(
    filepath=str(archivo_glb),
    export_format='GLB',
    export_animations=True,
    export_skins=True,
    export_apply=False,
    export_yup=True,
    export_extras=False,
    export_cameras=False,
    export_lights=False,
)

# Verificar tamaño
tamaño_kb = archivo_glb.stat().st_size / 1024
print(f"\n✅ GLB EXPORTADO")
print(f"   Tamaño: {tamaño_kb:.2f} KB")
print(f"\n{'='*80}\n")

sys.exit(0)
