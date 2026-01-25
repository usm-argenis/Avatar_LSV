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
print(f"PRUEBA FINAL: {archivo.name}")
print(f"{'='*80}")

# Importar Nancy base (CON texturas)
bpy.ops.import_scene.gltf(filepath=str(NANCY_BASE))
nancy_armature = bpy.data.objects.get("Nancy_Armature") or bpy.data.objects.get("Armature")
print(f"✅ Nancy base importada")

# Importar archivo con animación
bpy.ops.import_scene.gltf(filepath=str(archivo))
anim_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE' and obj != nancy_armature:
        anim_armature = obj
        break

print(f"✅ Armature animado importado")

# Copiar la animación
action_original = anim_armature.animation_data.action
action = action_original.copy()
action.name = "cortesia"
print(f"✅ Action copiada: {len(action.fcurves)} FCurves")

# Obtener rango de frames
frame_start = min([min([kf.co[0] for kf in fc.keyframe_points]) for fc in action.fcurves])
frame_end = max([max([kf.co[0] for kf in fc.keyframe_points]) for fc in action.fcurves])

# Eliminar FCurves de piernas
fcurves_a_eliminar = []
for fcurve in action.fcurves:
    for hueso in huesos_piernas:
        if f'pose.bones["{hueso}"]' in fcurve.data_path:
            fcurves_a_eliminar.append(fcurve)
            break

for fcurve in fcurves_a_eliminar:
    action.fcurves.remove(fcurve)
print(f"✅ FCurves restantes: {len(action.fcurves)}")

# Eliminar objetos del segundo import
objetos_nancy = [obj for obj in bpy.data.objects if obj == nancy_armature or obj.parent == nancy_armature]
objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_nancy]
for obj in objetos_eliminar:
    bpy.data.objects.remove(obj, do_unlink=True)

# Eliminar TODAS las acciones no utilizadas
acciones_a_eliminar = [act for act in bpy.data.actions if act != action]
for act in acciones_a_eliminar:
    bpy.data.actions.remove(act)
print(f"✅ Solo queda 1 acción: {action.name}")

# Crear animation_data si no existe
if not nancy_armature.animation_data:
    nancy_armature.animation_data_create()

# Limpiar NLA tracks existentes
while len(nancy_armature.animation_data.nla_tracks) > 0:
    nancy_armature.animation_data.nla_tracks.remove(nancy_armature.animation_data.nla_tracks[0])

# CLAVE: Crear NLA track como lo hace Nina
nla_track = nancy_armature.animation_data.nla_tracks.new()
nla_track.name = action.name

# Crear NLA strip con la acción
strip = nla_track.strips.new(action.name, int(frame_start), action)
strip.action = action

# NO asignar action directamente, solo via NLA
nancy_armature.animation_data.action = None

print(f"✅ NLA track creado: {nla_track.name}")
print(f"✅ NLA strip creado: {strip.name}")

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

# Configurar rango de frames
bpy.context.scene.frame_start = int(frame_start)
bpy.context.scene.frame_end = int(frame_end)

# Verificar
print(f"\n--- VERIFICACIÓN PRE-EXPORT ---")
print(f"NLA tracks: {len(nancy_armature.animation_data.nla_tracks)}")
print(f"NLA strips: {len(nla_track.strips)}")
print(f"Action directa: {nancy_armature.animation_data.action}")
print(f"Acciones en bpy.data.actions: {len(bpy.data.actions)}")

# Exportar
archivo_final = archivo.parent / f"{archivo.stem}_FINAL.glb"
bpy.ops.export_scene.gltf(
    filepath=str(archivo_final),
    export_format='GLB',
    export_animations=True,
    export_image_format='AUTO'
)

print(f"\n✅ EXPORTADO: {archivo_final.name} ({archivo_final.stat().st_size / (1024*1024):.1f}MB)")
print(f"{'='*80}\n")
