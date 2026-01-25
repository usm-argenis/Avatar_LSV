import bpy
from pathlib import Path

# Directorios
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_BASE = BASE_DIR / "Nancy" / "Nancy.glb"
NINA_DIR = BASE_DIR / "Nina" / "tiempo"
NANCY_OUTPUT_DIR = BASE_DIR / "Nancy" / "tiempo"

NANCY_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Buscar todos los archivos de Nina
nina_files = list(NINA_DIR.glob("Nina_resultado_*.glb"))
print(f"\n{'='*80}")
print(f"BATCH RETARGETING: Nina → Nancy")
print(f"{'='*80}")
print(f"📂 Encontrados: {len(nina_files)} archivos de Nina")
print(f"📦 Modelo base: {NANCY_BASE.name}")
print(f"💾 Salida: {NANCY_OUTPUT_DIR}")
print()

total = len(nina_files)
exitosos = 0
fallidos = 0

for idx, nina_file in enumerate(nina_files, 1):
    # Nombre de la animación
    anim_name = nina_file.stem.replace("Nina_resultado_", "")
    nancy_output = NANCY_OUTPUT_DIR / f"Nancy_resultado_{anim_name}.glb"
    
    print(f"\n{'─'*80}")
    print(f"[{idx}/{total}] Procesando: {anim_name}")
    print(f"{'─'*80}")
    
    try:
        # 1. Limpiar escena
        bpy.ops.wm.read_homefile(use_empty=True)
        
        # 2. Importar Nancy (destino)
        print(f"📦 Importando Nancy...")
        bpy.ops.import_scene.gltf(filepath=str(NANCY_BASE))
        nancy_armature = bpy.data.objects.get("Nancy_Armature") or bpy.data.objects.get("Armature")
        if not nancy_armature:
            print(f"❌ Error: No se encontró armature de Nancy")
            fallidos += 1
            continue
        
        # 3. Importar Nina con animación
        print(f"🎬 Importando Nina con animación '{anim_name}'...")
        bpy.ops.import_scene.gltf(filepath=str(nina_file))
        nina_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE' and obj != nancy_armature:
                nina_armature = obj
                break
        
        if not nina_armature or not nina_armature.animation_data or not nina_armature.animation_data.action:
            print(f"❌ Error: Nina no tiene animación")
            fallidos += 1
            continue
        
        nina_action = nina_armature.animation_data.action
        frame_start = int(nina_action.frame_range[0])
        frame_end = int(nina_action.frame_range[1])
        print(f"   ✅ Frames: {frame_start} a {frame_end}")
        
        # 4. Crear constraints Copy Transforms
        print(f"📌 Creando constraints...")
        for nancy_bone in nancy_armature.pose.bones:
            if nancy_bone.name in nina_armature.pose.bones:
                constraint = nancy_bone.constraints.new('COPY_TRANSFORMS')
                constraint.target = nina_armature
                constraint.subtarget = nancy_bone.name
        
        # 5. Bakear animación
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
        
        # 6. Eliminar objetos de Nina
        print(f"🗑️ Eliminando objetos de Nina...")
        objetos_nancy = [obj for obj in bpy.data.objects if obj == nancy_armature or obj.parent == nancy_armature]
        objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_nancy]
        
        for obj in objetos_eliminar:
            bpy.data.objects.remove(obj, do_unlink=True)
        
        # 7. Exportar a FBX primero
        fbx_temp = nancy_output.with_suffix('.fbx')
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
        
        # 8. Re-importar FBX y exportar a GLB
        print(f"📦 Re-importando FBX...")
        bpy.ops.wm.read_homefile(use_empty=True)
        bpy.ops.import_scene.fbx(filepath=str(fbx_temp))
        
        print(f"💾 Exportando a GLB final...")
        bpy.ops.export_scene.gltf(
            filepath=str(nancy_output),
            export_format='GLB',
            export_animations=True,
            export_frame_range=True,
            export_force_sampling=True,
            export_def_bones=False,
            export_optimize_animation_size=False
        )
        
        # 9. Eliminar FBX temporal
        if fbx_temp.exists():
            fbx_temp.unlink()
        
        file_size = nancy_output.stat().st_size / (1024*1024)
        print(f"✅ Guardado: {nancy_output.name} ({file_size:.1f} MB)")
        exitosos += 1
        
    except Exception as e:
        print(f"❌ ERROR procesando '{anim_name}': {e}")
        fallidos += 1

# Resumen final
print(f"\n{'='*80}")
print(f"RESUMEN FINAL")
print(f"{'='*80}")
print(f"✅ Exitosos: {exitosos}/{total}")
print(f"❌ Fallidos: {fallidos}/{total}")
print(f"📂 Salida: {NANCY_OUTPUT_DIR}")
print(f"{'='*80}\n")
