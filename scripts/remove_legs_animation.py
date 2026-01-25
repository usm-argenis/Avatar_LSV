import bpy
from pathlib import Path

# Archivo a procesar
archivo = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy\tiempo\Nancy_resultado_ayer.glb")

print(f"\n{'='*80}")
print(f"ELIMINANDO ANIMACIÓN DE PIERNAS Y PIES")
print(f"{'='*80}")
print(f"📂 Archivo: {archivo.name}\n")

# Limpiar escena
bpy.ops.wm.read_homefile(use_empty=True)

# Importar GLB
print("📦 Importando archivo...")
bpy.ops.import_scene.gltf(filepath=str(archivo))

# Buscar armature
armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        armature = obj
        break

if not armature or not armature.animation_data or not armature.animation_data.action:
    print("❌ No se encontró armature con animación")
    exit()

action = armature.animation_data.action
print(f"✅ Action encontrada: {action.name}")
print(f"✅ FCurves totales: {len(action.fcurves)}")

# Lista de huesos de piernas y pies que NO queremos animar
huesos_piernas = [
    "Hips",           # Cadera - la raíz del movimiento
    "LeftUpLeg",      # Muslo izquierdo
    "LeftLeg",        # Pantorrilla izquierda
    "LeftFoot",       # Pie izquierdo
    "LeftToeBase",    # Base dedos izquierdo
    "LeftToe_End",    # Punta dedos izquierdo
    "RightUpLeg",     # Muslo derecho
    "RightLeg",       # Pantorrilla derecha
    "RightFoot",      # Pie derecho
    "RightToeBase",   # Base dedos derecho
    "RightToe_End"    # Punta dedos derecho
]

print(f"\n🗑️ Eliminando FCurves de huesos del tren inferior...")

# Crear lista de FCurves a eliminar
fcurves_a_eliminar = []
for fcurve in action.fcurves:
    # El data_path tiene formato: pose.bones["NombreHueso"].rotation_quaternion
    for hueso in huesos_piernas:
        if f'pose.bones["{hueso}"]' in fcurve.data_path:
            fcurves_a_eliminar.append(fcurve)
            print(f"   ❌ Marcando: {hueso} - {fcurve.data_path}")
            break

# Eliminar las FCurves marcadas
print(f"\n🔥 Eliminando {len(fcurves_a_eliminar)} FCurves...")
for fcurve in fcurves_a_eliminar:
    action.fcurves.remove(fcurve)

print(f"✅ FCurves restantes: {len(action.fcurves)}")

# Resetear pose de piernas a rest pose
print(f"\n🦴 Reseteando pose de piernas a rest pose...")
bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode='POSE')

for bone_name in huesos_piernas:
    if bone_name in armature.pose.bones:
        pose_bone = armature.pose.bones[bone_name]
        pose_bone.location = (0, 0, 0)
        pose_bone.rotation_quaternion = (1, 0, 0, 0)
        pose_bone.rotation_euler = (0, 0, 0)
        pose_bone.scale = (1, 1, 1)

bpy.ops.object.mode_set(mode='OBJECT')

# Exportar usando flujo FBX->GLB
backup_file = archivo.with_name(archivo.stem + "_BACKUP.glb")
print(f"\n💾 Creando backup: {backup_file.name}")
import shutil
if archivo.exists():
    shutil.copy(archivo, backup_file)

fbx_temp = archivo.with_suffix('.fbx')
print(f"💾 Exportando a FBX temporal...")
bpy.ops.export_scene.fbx(
    filepath=str(fbx_temp),
    use_selection=False,
    bake_anim=True,
    bake_anim_use_all_bones=True,
    bake_anim_use_nla_strips=False,
    bake_anim_use_all_actions=False,
    bake_anim_step=1.0,
    bake_anim_simplify_factor=0.0,
    add_leaf_bones=False,
    path_mode='AUTO'
)

print(f"📦 Re-importando FBX...")
bpy.ops.wm.read_homefile(use_empty=True)
bpy.ops.import_scene.fbx(filepath=str(fbx_temp))

print(f"💾 Exportando a GLB final...")
bpy.ops.export_scene.gltf(
    filepath=str(archivo),
    export_format='GLB',
    export_animations=True,
    export_frame_range=True,
    export_force_sampling=True,
    export_def_bones=False,
    export_optimize_animation_size=False
)

# Limpiar FBX temporal
if fbx_temp.exists():
    fbx_temp.unlink()

file_size = archivo.stat().st_size / (1024*1024)
print(f"✅ Guardado: {archivo.name} ({file_size:.1f} MB)")

print(f"\n{'='*80}")
print(f"✅ COMPLETADO")
print(f"   - Piernas y pies en rest pose")
print(f"   - Animación del tren superior preservada")
print(f"   - Backup creado: {backup_file.name}")
print(f"{'='*80}\n")
