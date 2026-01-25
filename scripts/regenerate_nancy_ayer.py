import bpy
from pathlib import Path

# Archivos
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_BASE = BASE_DIR / "Nancy" / "Nancy.glb"
NINA_FILE = BASE_DIR / "Nina" / "tiempo" / "Nina_resultado_ayer.glb"
NANCY_OUTPUT = BASE_DIR / "Nancy" / "tiempo" / "Nancy_resultado_ayer.glb"

print(f"\n{'='*80}")
print(f"REGENERANDO: Nancy_resultado_ayer.glb")
print(f"{'='*80}\n")

# 1. Limpiar escena
bpy.ops.wm.read_homefile(use_empty=True)

# 2. Importar Nancy
print(f"📦 Importando Nancy...")
bpy.ops.import_scene.gltf(filepath=str(NANCY_BASE))
nancy_armature = bpy.data.objects.get("Nancy_Armature") or bpy.data.objects.get("Armature")

# 3. Importar Nina con animación
print(f"🎬 Importando Nina con animación 'ayer'...")
bpy.ops.import_scene.gltf(filepath=str(NINA_FILE))
nina_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE' and obj != nancy_armature:
        nina_armature = obj
        break

nina_action = nina_armature.animation_data.action
frame_start = int(nina_action.frame_range[0])
frame_end = int(nina_action.frame_range[1])
print(f"   ✅ Frames: {frame_start} a {frame_end}")

# 4. Crear constraints
print(f"📌 Creando constraints...")
for nancy_bone in nancy_armature.pose.bones:
    if nancy_bone.name in nina_armature.pose.bones:
        constraint = nancy_bone.constraints.new('COPY_TRANSFORMS')
        constraint.target = nina_armature
        constraint.subtarget = nancy_bone.name

# 5. Bake
print(f"🔥 Baking animación...")
bpy.context.view_layer.objects.active = nancy_armature
nancy_armature.select_set(True)
bpy.ops.nla.bake(
    frame_start=frame_start,
    frame_end=frame_end,
    step=1,
    only_selected=False,
    visual_keying=True,
    clear_constraints=True,
    bake_types={'POSE'}
)

# 6. Eliminar Nina
print(f"🗑️ Eliminando objetos de Nina...")
objetos_nancy = [obj for obj in bpy.data.objects if obj == nancy_armature or obj.parent == nancy_armature]
objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_nancy]
for obj in objetos_eliminar:
    bpy.data.objects.remove(obj, do_unlink=True)

# 7. Exportar FBX
fbx_temp = NANCY_OUTPUT.with_suffix('.fbx')
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

# 8. Re-importar y exportar GLB
print(f"📦 Re-importando FBX...")
bpy.ops.wm.read_homefile(use_empty=True)
bpy.ops.import_scene.fbx(filepath=str(fbx_temp))

print(f"💾 Exportando a GLB final...")
bpy.ops.export_scene.gltf(
    filepath=str(NANCY_OUTPUT),
    export_format='GLB',
    export_animations=True,
    export_frame_range=True,
    export_force_sampling=True,
    export_def_bones=False,
    export_optimize_animation_size=False
)

# 9. Limpiar FBX
if fbx_temp.exists():
    fbx_temp.unlink()

file_size = NANCY_OUTPUT.stat().st_size / (1024*1024)
print(f"✅ Guardado: {NANCY_OUTPUT.name} ({file_size:.1f} MB)")
print(f"\n{'='*80}")
print(f"✅ COMPLETADO")
print(f"{'='*80}\n")
