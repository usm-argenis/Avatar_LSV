#!/usr/bin/env blender --python
"""
Corregir las transformaciones del Armature en agarrar.blend
"""
import bpy
import sys
from pathlib import Path

archivo_blend = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.blend")
archivo_glb = archivo_blend.with_suffix('.glb')

print(f"\n{'='*80}")
print("CORREGIR TRANSFORMACIONES DEL ARMATURE")
print(f"{'='*80}\n")

# Crear backup
import shutil
backup = archivo_blend.with_suffix('.blend.backup_TRANS')
shutil.copy2(archivo_blend, backup)
print(f"💾 Backup creado: {backup.name}\n")

# Abrir archivo
print(f"📂 Abriendo: {archivo_blend.name}")
bpy.ops.wm.open_mainfile(filepath=str(archivo_blend))

# Encontrar armature
armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        armature = obj
        break

if not armature:
    print("❌ No se encontró Armature")
    sys.exit(1)

print(f"\n🦴 Armature encontrado: {armature.name}")
print(f"   ANTES:")
print(f"   - Location: ({armature.location.x:.4f}, {armature.location.y:.4f}, {armature.location.z:.4f})")
print(f"   - Rotation (quat): ({armature.rotation_quaternion.x:.4f}, {armature.rotation_quaternion.y:.4f}, {armature.rotation_quaternion.z:.4f}, {armature.rotation_quaternion.w:.4f})")
print(f"   - Scale: ({armature.scale.x:.4f}, {armature.scale.y:.4f}, {armature.scale.z:.4f})")

# Corregir transformaciones
print(f"\n🔧 Aplicando correcciones...")

# Aplicar la transformación a todo (convertir escala 100 y rotación en poses de los huesos)
bpy.context.view_layer.objects.active = armature
armature.select_set(True)

# Aplicar escala y rotación
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

print(f"\n   DESPUÉS:")
print(f"   - Location: ({armature.location.x:.4f}, {armature.location.y:.4f}, {armature.location.z:.4f})")
print(f"   - Rotation (quat): ({armature.rotation_quaternion.x:.4f}, {armature.rotation_quaternion.y:.4f}, {armature.rotation_quaternion.z:.4f}, {armature.rotation_quaternion.w:.4f})")
print(f"   - Scale: ({armature.scale.x:.4f}, {armature.scale.y:.4f}, {armature.scale.z:.4f})")

# Guardar .blend
print(f"\n💾 Guardando .blend corregido...")
bpy.ops.wm.save_mainfile()

# Exportar a GLB
print(f"\n💾 Exportando a GLB...")
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
print(f"\n✅ CORRECCIÓN COMPLETA")
print(f"   GLB exportado: {tamaño_kb:.2f} KB")
print(f"\n{'='*80}\n")

sys.exit(0)
