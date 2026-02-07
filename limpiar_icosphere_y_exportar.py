#!/usr/bin/env blender --python
"""
Eliminar Icosphere del .blend y re-exportar a GLB
"""
import bpy
import sys
from pathlib import Path

archivo_blend = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.blend")
archivo_glb = archivo_blend.with_suffix('.glb')

print(f"\n{'='*80}")
print("LIMPIAR ICOSPHERE Y RE-EXPORTAR A GLB")
print(f"{'='*80}\n")

# Abrir el archivo .blend
print(f"📂 Abriendo: {archivo_blend.name}")
bpy.ops.wm.open_mainfile(filepath=str(archivo_blend))

# Eliminar Icosphere
if 'Icosphere' in bpy.data.objects:
    obj = bpy.data.objects['Icosphere']
    print(f"🗑️  Eliminando: {obj.name}")
    bpy.data.objects.remove(obj, do_unlink=True)

# Guardar .blend
print(f"💾 Guardando .blend limpio")
bpy.ops.wm.save_mainfile()

print(f"\n🔍 Objetos en la escena:")
for obj in bpy.data.objects:
    obj_type = obj.type
    parent_info = f" (parent: {obj.parent.name})" if obj.parent else " (root)"
    print(f"  - {obj.name} [{obj_type}]{parent_info}")

# Verificar que hay animación
if bpy.data.actions:
    print(f"\n🎬 Animaciones encontradas:")
    for action in bpy.data.actions:
        print(f"   - {action.name}: {len(action.fcurves)} fcurves, frames {action.frame_range[0]:.0f}-{action.frame_range[1]:.0f}")
else:
    print("\n⚠️  No se encontraron animaciones")

# Exportar a GLB
print(f"\n💾 Exportando a: {archivo_glb.name}")
bpy.ops.export_scene.gltf(
    filepath=str(archivo_glb),
    export_format='GLB',
    export_image_format='AUTO',
    export_texcoords=True,
    export_normals=True,
    export_draco_mesh_compression_enable=False,
    export_materials='EXPORT',
    export_cameras=False,
    use_selection=False,
    use_visible=True,
    use_renderable=True,
    use_active_collection=False,
    export_yup=True,
    export_apply=False,
    export_animations=True,
    export_frame_range=True,
    export_frame_step=1,
    export_force_sampling=True,
    export_nla_strips=False,
    export_def_bones=True,
    export_skins=True,
    export_morph=True,
    export_lights=False
)

tamaño_kb = archivo_glb.stat().st_size / 1024
print(f"\n✅ GLB EXPORTADO")
print(f"   Tamaño: {tamaño_kb:.2f} KB")
print(f"\n{'='*80}\n")

sys.exit(0)
