import bpy
from pathlib import Path

# Limpiar escena
bpy.ops.wm.read_factory_settings(use_empty=True)

NANCY_BASE = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy\Nancy.glb")
archivo = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy\cortesia\Nancy_resultado_cortesia.glb")

huesos_piernas = [
    "Hips", "LeftUpLeg", "LeftLeg", "LeftFoot", "LeftToeBase", "LeftToe_End",
    "RightUpLeg", "RightLeg", "RightFoot", "RightToeBase", "RightToe_End"
]

print(f"\n{'='*80}")
print(f"PRUEBA: {archivo.name}")
print(f"{'='*80}")

# Importar Nancy base (CON texturas)
bpy.ops.import_scene.gltf(filepath=str(NANCY_BASE))
nancy_armature = bpy.data.objects.get("Nancy_Armature") or bpy.data.objects.get("Armature")
print(f"✅ Nancy base importada: {nancy_armature.name}")

# Guardar texturas originales
texturas_originales = {img.name: img for img in bpy.data.images}
print(f"✅ Texturas originales: {len(texturas_originales)}")

# Importar archivo con animación
bpy.ops.import_scene.gltf(filepath=str(archivo))
anim_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE' and obj != nancy_armature:
        anim_armature = obj
        break

print(f"✅ Armature animado importado: {anim_armature.name}")

# Copiar la animación
action_original = anim_armature.animation_data.action
action = action_original.copy()
action.name = "AnimacionLimpia"
print(f"✅ Action copiada: {action.name} ({len(action.fcurves)} FCurves)")

# Obtener rango de frames
frame_start = min([min([kf.co[0] for kf in fc.keyframe_points]) for fc in action.fcurves])
frame_end = max([max([kf.co[0] for kf in fc.keyframe_points]) for fc in action.fcurves])
print(f"✅ Frame range: {frame_start} - {frame_end}")

# Eliminar FCurves de piernas
fcurves_a_eliminar = []
for fcurve in action.fcurves:
    for hueso in huesos_piernas:
        if f'pose.bones["{hueso}"]' in fcurve.data_path:
            fcurves_a_eliminar.append(fcurve)
            break

for fcurve in fcurves_a_eliminar:
    action.fcurves.remove(fcurve)
print(f"✅ FCurves eliminadas: {len(fcurves_a_eliminar)}")
print(f"✅ FCurves restantes: {len(action.fcurves)}")

# Eliminar objetos del segundo import
objetos_nancy = [obj for obj in bpy.data.objects if obj == nancy_armature or obj.parent == nancy_armature]
objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_nancy]
for obj in objetos_eliminar:
    bpy.data.objects.remove(obj, do_unlink=True)
print(f"✅ Objetos eliminados: {len(objetos_eliminar)}")

# CRÍTICO: Limpiar animation_data completamente y reasignar
if nancy_armature.animation_data:
    print(f"⚠️ Limpiando animation_data existente...")
    # Remover todos los NLA tracks uno por uno
    while len(nancy_armature.animation_data.nla_tracks) > 0:
        nancy_armature.animation_data.nla_tracks.remove(nancy_armature.animation_data.nla_tracks[0])
    print(f"✅ NLA tracks limpiados: {len(nancy_armature.animation_data.nla_tracks)}")

# CRÍTICO: Eliminar TODAS las acciones no utilizadas de bpy.data.actions ANTES de asignar
# Esto previene que el exportador GLTF cree NLA tracks automáticamente
acciones_a_mantener = {action.name}
acciones_a_eliminar = []
for act in bpy.data.actions:
    if act.name not in acciones_a_mantener:
        acciones_a_eliminar.append(act)

print(f"⚠️ Eliminando {len(acciones_a_eliminar)} acciones no utilizadas...")
for act in acciones_a_eliminar:
    bpy.data.actions.remove(act)

print(f"✅ Acciones restantes en bpy.data.actions: {len(bpy.data.actions)}")

# Ahora asignar la acción limpia
if not nancy_armature.animation_data:
    nancy_armature.animation_data_create()

# Proteger la acción con fake_user para que no se elimine
action.use_fake_user = True

nancy_armature.animation_data.action = action
nancy_armature.animation_data.use_nla = False

print(f"✅ Action asignada a Nancy: {nancy_armature.animation_data.action.name}")
print(f"✅ fake_user: {action.use_fake_user}")

# Configurar rango de frames
bpy.context.scene.frame_start = int(frame_start)
bpy.context.scene.frame_end = int(frame_end)

# Resetear pose de piernas
bpy.context.view_layer.objects.active = nancy_armature
bpy.ops.object.mode_set(mode='POSE')
for bone_name in huesos_piernas:
    if bone_name in nancy_armature.pose.bones:
        pose_bone = nancy_armature.pose.bones[bone_name]
        pose_bone.location = (0, 0, 0)
        pose_bone.rotation_quaternion = (1, 0, 0, 0)
        pose_bone.rotation_euler = (0, 0, 0)
        pose_bone.scale = (1, 1, 1)
bpy.ops.object.mode_set(mode='OBJECT')

# Verificar texturas finales
texturas_finales = len([img for img in bpy.data.images if img.packed_file])
print(f"✅ Texturas finales: {texturas_finales}")

# Verificar estado antes de exportar
print(f"\n--- VERIFICACIÓN PRE-EXPORT ---")
print(f"Action asignada: {nancy_armature.animation_data.action.name}")
print(f"FCurves en action: {len(nancy_armature.animation_data.action.fcurves)}")
print(f"NLA tracks: {len(nancy_armature.animation_data.nla_tracks)}")
print(f"use_nla: {nancy_armature.animation_data.use_nla}")

# Exportar
archivo_test = archivo.parent / f"{archivo.stem}_TEST3.glb"
bpy.ops.export_scene.gltf(
    filepath=str(archivo_test),
    use_selection=False,
    export_format='GLB',
    export_animations=True,
    export_nla_strips=False,  # NO exportar NLA strips, solo la action
    export_frame_range=False,
    export_force_sampling=False,
    export_def_bones=False,
    export_optimize_animation_size=False,
    export_image_format='AUTO'
)

print(f"\n✅ EXPORTADO: {archivo_test.name}")
print(f"   Tamaño: {archivo_test.stat().st_size / (1024*1024):.1f}MB")

print(f"\n{'='*80}\n")
