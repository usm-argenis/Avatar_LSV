"""
Script para recortar animación de un GLB específico
Elimina frames después de un frame específico
"""

import bpy
import sys
from pathlib import Path

# Configuración
GLB_FILE = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\alfabeto\Duvall_resultado_a.glb")
MAX_FRAME = 56

print("="*80)
print(f"🔪 RECORTANDO ANIMACIÓN")
print(f"📁 Archivo: {GLB_FILE.name}")
print(f"📊 Frame máximo: {MAX_FRAME}")
print("="*80)

if not GLB_FILE.exists():
    print(f"❌ ERROR: No existe {GLB_FILE}")
    sys.exit(1)

# Limpiar escena
bpy.ops.wm.read_factory_settings(use_empty=True)

# Importar GLB
print(f"\n📥 Importando GLB...")
bpy.ops.import_scene.gltf(filepath=str(GLB_FILE))

# Buscar armature
armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        armature = obj
        break

if not armature:
    print("❌ No se encontró armature")
    sys.exit(1)

if not armature.animation_data or not armature.animation_data.action:
    print("❌ No hay animación en el armature")
    sys.exit(1)

action = armature.animation_data.action
frame_start, frame_end = action.frame_range

print(f"✅ Animación encontrada: {action.name}")
print(f"   Frames originales: {frame_start:.0f} - {frame_end:.0f}")

if frame_end <= MAX_FRAME:
    print(f"⚠️ La animación ya termina en frame {frame_end:.0f}, no necesita recorte")
    sys.exit(0)

# Recortar animación eliminando keyframes después del frame máximo
print(f"\n✂️ Recortando frames después de {MAX_FRAME}...")

removed_keyframes = 0
for fcurve in action.fcurves:
    # Crear lista de índices a eliminar (en orden inverso)
    indices_to_remove = []
    for i, keyframe in enumerate(fcurve.keyframe_points):
        if keyframe.co[0] > MAX_FRAME:
            indices_to_remove.append(i)
    
    # Eliminar de atrás hacia adelante para no desincronizar índices
    for i in reversed(indices_to_remove):
        fcurve.keyframe_points.remove(fcurve.keyframe_points[i])
        removed_keyframes += 1

print(f"   🗑️ Eliminados {removed_keyframes} keyframes")

# Actualizar frame range de la acción
action.frame_range = (frame_start, MAX_FRAME)
bpy.context.scene.frame_start = int(frame_start)
bpy.context.scene.frame_end = MAX_FRAME

print(f"   📊 Nueva duración: {frame_start:.0f} - {MAX_FRAME}")

# Crear backup
backup_file = GLB_FILE.parent / f"{GLB_FILE.stem}_BACKUP_ANTES_RECORTE.glb"
if not backup_file.exists():
    import shutil
    shutil.copy2(GLB_FILE, backup_file)
    print(f"\n💾 Backup creado: {backup_file.name}")

# Exportar GLB
print(f"\n📤 Exportando GLB recortado...")

temp_file = Path(f"/tmp/{GLB_FILE.name}")
bpy.ops.object.select_all(action='SELECT')

bpy.ops.export_scene.gltf(
    filepath=str(temp_file),
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

# Reemplazar archivo original
if temp_file.exists():
    import shutil
    shutil.copy2(temp_file, GLB_FILE)
    temp_file.unlink()
    
    size_kb = GLB_FILE.stat().st_size / 1024
    print(f"✅ Archivo actualizado: {size_kb:.1f} KB")
    print(f"\n🎉 COMPLETADO - Animación recortada a {MAX_FRAME} frames")
else:
    print("❌ Error al exportar")
    sys.exit(1)

print("="*80)
