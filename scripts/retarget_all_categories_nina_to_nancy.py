import bpy
from pathlib import Path

print("="*80)
print("BATCH RETARGETING: Nina → Nancy (FBX method)")
print("="*80)

# Directorios base
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_BASE = BASE_DIR / "Nancy" / "Nancy.glb"
NINA_DIR = BASE_DIR / "Nina"
NANCY_OUTPUT_DIR = BASE_DIR / "Nancy"

# Categorías a procesar
categorias = [
    "alfabeto",
    "cortesia", 
    "dias_semana",
    "expresiones",
    "preguntas",
    "pronombres",
    "saludos",
    "tiempo"
]

print(f"\n{'='*80}")
print(f"BATCH RETARGETING COMPLETO: Nina → Nancy")
print(f"{'='*80}")
print(f"📦 Modelo base: {NANCY_BASE.name}")
print(f"📂 Categorías: {len(categorias)}")
print(f"{'='*80}\n")

total_general = 0
exitosos_general = 0
fallidos_general = 0

for categoria in categorias:
    print(f"\n{'█'*80}")
    print(f"CATEGORÍA: {categoria.upper()}")
    print(f"{'█'*80}\n")
    
    nina_categoria_dir = NINA_DIR / categoria
    nancy_categoria_dir = NANCY_OUTPUT_DIR / categoria
    nancy_categoria_dir.mkdir(parents=True, exist_ok=True)
    
    # Buscar archivos de esta categoría
    nina_files = list(nina_categoria_dir.glob("Nina_resultado_*.glb"))
    print(f"📂 Encontrados: {len(nina_files)} archivos")
    
    if not nina_files:
        print(f"⚠️ No hay archivos en {categoria}")
        continue
    
    total_general += len(nina_files)
    exitosos = 0
    fallidos = 0
    
    for idx, nina_file in enumerate(nina_files, 1):
        anim_name = nina_file.stem.replace("Nina_resultado_", "")
        nancy_output = nancy_categoria_dir / f"Nancy_resultado_{anim_name}.glb"
        
        print(f"[{idx}/{len(nina_files)}] {anim_name}...", end=" ", flush=True)
        
        try:
            # 1. Limpiar escena
            bpy.ops.wm.read_homefile(use_empty=True)
            
            # 2. Importar Nancy
            bpy.ops.import_scene.gltf(filepath=str(NANCY_BASE))
            nancy_armature = bpy.data.objects.get("Nancy_Armature") or bpy.data.objects.get("Armature")
            if not nancy_armature:
                print(f"❌ No armature Nancy")
                fallidos += 1
                continue
            
            # 3. Importar Nina con animación
            bpy.ops.import_scene.gltf(filepath=str(nina_file))
            nina_armature = None
            for obj in bpy.data.objects:
                if obj.type == 'ARMATURE' and obj != nancy_armature:
                    nina_armature = obj
                    break
            
            if not nina_armature or not nina_armature.animation_data or not nina_armature.animation_data.action:
                print(f"❌ Sin animación")
                fallidos += 1
                continue
            
            nina_action = nina_armature.animation_data.action
            frame_start = int(nina_action.frame_range[0])
            frame_end = int(nina_action.frame_range[1])
            
            # 4. Crear constraints
            for nancy_bone in nancy_armature.pose.bones:
                if nancy_bone.name in nina_armature.pose.bones:
                    constraint = nancy_bone.constraints.new('COPY_TRANSFORMS')
                    constraint.target = nina_armature
                    constraint.subtarget = nancy_bone.name
            
            # 5. Bake
            bpy.context.view_layer.objects.active = nancy_armature
            nancy_armature.select_set(True)
            
            # CRÍTICO: Configurar frame range ANTES del bake
            bpy.context.scene.frame_start = frame_start
            bpy.context.scene.frame_end = frame_end
            
            bpy.ops.nla.bake(
                frame_start=frame_start,
                frame_end=frame_end,
                step=1,
                only_selected=False,
                visual_keying=True,
                clear_constraints=True,
                bake_types={'POSE'}
            )
            
            # Verificar que la animación se bakeó
            if not nancy_armature.animation_data or not nancy_armature.animation_data.action:
                print(f"❌ Bake falló")
                fallidos += 1
                continue
            
            # 6. Eliminar objetos de Nina
            objetos_nancy = [obj for obj in bpy.data.objects if obj == nancy_armature or obj.parent == nancy_armature]
            objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_nancy]
            for obj in objetos_eliminar:
                bpy.data.objects.remove(obj, do_unlink=True)
            
            # 7. MÉTODO FBX → GLB (preserva animación funcional)
            fbx_temp = nancy_output.with_suffix('.fbx')
            
            # Exportar a FBX
            bpy.ops.export_scene.fbx(
                filepath=str(fbx_temp),
                use_selection=False,
                bake_anim=True,
                bake_anim_use_all_bones=True,
                bake_anim_step=1.0,
                add_leaf_bones=False,
                path_mode='COPY',
                embed_textures=True
            )
            
            # Reimportar FBX
            bpy.ops.wm.read_homefile(use_empty=True)
            bpy.ops.import_scene.fbx(filepath=str(fbx_temp))
            
            # Exportar a GLB desde FBX
            bpy.ops.export_scene.gltf(
                filepath=str(nancy_output),
                export_format='GLB',
                export_animations=True,
                export_frame_range=True,
                export_force_sampling=True,
                export_def_bones=False,
                export_optimize_animation_size=False,
                export_materials='EXPORT',
                export_image_format='AUTO',
                export_texcoords=True,
                export_normals=True
            )
            
            # Limpiar FBX temporal
            if fbx_temp.exists():
                fbx_temp.unlink()
            
            file_size = nancy_output.stat().st_size / (1024*1024)
            print(f"✅ {file_size:.1f}MB")
            exitosos += 1
            
        except Exception as e:
            print(f"❌ {e}")
            fallidos += 1
    
    print(f"\n{'─'*80}")
    print(f"Categoría '{categoria}': ✅ {exitosos}/{len(nina_files)} exitosos")
    print(f"{'─'*80}")
    
    exitosos_general += exitosos
    fallidos_general += fallidos

# Resumen final
print(f"\n{'='*80}")
print(f"RESUMEN FINAL COMPLETO")
print(f"{'='*80}")
print(f"✅ Exitosos: {exitosos_general}/{total_general}")
print(f"❌ Fallidos: {fallidos_general}/{total_general}")
print(f"📂 Salida base: {NANCY_OUTPUT_DIR}")
print(f"{'='*80}\n")
