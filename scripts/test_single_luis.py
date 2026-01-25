import bpy
from pathlib import Path

BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
LUIS_BASE = BASE_DIR / "Luis" / "Luis.glb"
NINA_FILE = BASE_DIR / "Nina" / "cortesia" / "Nina_resultado_hola.glb"
LUIS_OUTPUT = BASE_DIR / "Luis" / "cortesia" / "Luis_resultado_hola.glb"

LUIS_OUTPUT.parent.mkdir(parents=True, exist_ok=True)

print("="*80)
print("PRUEBA: Nina 'hola' → Luis")
print("="*80)

# 1. Limpiar escena
print("🧹 Limpiando escena...")
bpy.ops.wm.read_homefile(use_empty=True)
for obj in list(bpy.data.objects):
    bpy.data.objects.remove(obj, do_unlink=True)

# 2. Importar Luis
print(f"📦 Importando Luis: {LUIS_BASE}")
bpy.ops.import_scene.gltf(filepath=str(LUIS_BASE))
luis_armature = bpy.data.objects.get("Armature")
print(f"   ✅ Luis Armature: {luis_armature.name if luis_armature else 'NO ENCONTRADO'}")
print(f"   ✅ Huesos: {len(luis_armature.pose.bones) if luis_armature else 0}")

# 3. Importar Nina
print(f"🎬 Importando Nina: {NINA_FILE.name}")
bpy.ops.import_scene.gltf(filepath=str(NINA_FILE))
nina_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE' and obj != luis_armature:
        nina_armature = obj
        break
print(f"   ✅ Nina Armature: {nina_armature.name if nina_armature else 'NO ENCONTRADO'}")

if nina_armature and nina_armature.animation_data:
    nina_action = nina_armature.animation_data.action
    frame_start = int(nina_action.frame_range[0])
    frame_end = int(nina_action.frame_range[1])
    print(f"   ✅ Animación: {nina_action.name}")
    print(f"   ✅ Frames: {frame_start} a {frame_end}")
    
    # 4. Crear constraints
    print("📌 Creando constraints...")
    count = 0
    for luis_bone in luis_armature.pose.bones:
        if luis_bone.name in nina_armature.pose.bones:
            constraint = luis_bone.constraints.new('COPY_TRANSFORMS')
            constraint.target = nina_armature
            constraint.subtarget = luis_bone.name
            count += 1
    print(f"   ✅ {count} constraints creados")
    
    # 5. Bake
    print("🔥 Baking animación...")
    bpy.context.view_layer.objects.active = luis_armature
    luis_armature.select_set(True)
    bpy.ops.nla.bake(
        frame_start=frame_start,
        frame_end=frame_end,
        step=1,
        only_selected=False,
        visual_keying=True,
        clear_constraints=True,
        bake_types={'POSE'}
    )
    print("   ✅ Bakeado")
    
    # 6. Eliminar Nina
    print("🗑️ Eliminando objetos de Nina...")
    objetos_luis = [obj for obj in bpy.data.objects if obj == luis_armature or obj.parent == luis_armature]
    objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_luis]
    for obj in objetos_eliminar:
        bpy.data.objects.remove(obj, do_unlink=True)
    print(f"   ✅ {len(objetos_eliminar)} objetos eliminados")
    
    # 7. Exportar FBX
    print("💾 Exportando a FBX...")
    fbx_temp = LUIS_OUTPUT.with_suffix('.fbx')
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
    print("   ✅ FBX exportado")
    
    # 8. Re-importar y exportar GLB
    print("📦 Re-importando FBX...")
    bpy.ops.wm.read_homefile(use_empty=True)
    bpy.ops.import_scene.fbx(filepath=str(fbx_temp))
    
    print("💾 Exportando a GLB...")
    bpy.ops.export_scene.gltf(
        filepath=str(LUIS_OUTPUT),
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
    
    file_size = LUIS_OUTPUT.stat().st_size / (1024*1024)
    print(f"\n✅ ¡ÉXITO! Archivo: {LUIS_OUTPUT.name} ({file_size:.1f}MB)")
else:
    print("❌ Error: No se encontró animación en Nina")
