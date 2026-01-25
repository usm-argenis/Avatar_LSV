import bpy
from pathlib import Path
import json
import sys

print("="*80)
print("RETARGETING MASIVO: Todas las animaciones de Nina → Nancy")
print("Método: Copiar FCurves → FBX → GLB")
print("="*80)

# Configuración
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_BASE = BASE_DIR / "Nancy" / "Nancy.glb"
NINA_DIR = BASE_DIR / "Nina"
NANCY_DIR = BASE_DIR / "Nancy"

# Buscar todas las animaciones de Nina
print(f"\n🔍 Buscando animaciones de Nina...")
nina_files = list(NINA_DIR.rglob("Nina_resultado_*.glb"))

print(f"   ✅ {len(nina_files)} animaciones encontradas")

# Estadísticas
exitosos = []
fallidos = []

for idx, nina_file in enumerate(nina_files, 1):
    categoria = nina_file.parent.name
    palabra = nina_file.stem.replace("Nina_resultado_", "")
    
    nancy_output_dir = NANCY_DIR / categoria
    nancy_output = nancy_output_dir / f"Nancy_resultado_{palabra}.glb"
    fbx_temp = nancy_output.with_suffix('.fbx')
    
    print(f"\n{'='*80}")
    print(f"[{idx}/{len(nina_files)}] {categoria}/{palabra}")
    print(f"{'='*80}")
    
    try:
        # 1. Limpiar escena
        bpy.ops.wm.read_homefile(use_empty=True)
        
        # 2. Importar Nancy base
        print(f"📦 Importando Nancy base...")
        bpy.ops.import_scene.gltf(filepath=str(NANCY_BASE))
        
        nancy_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                nancy_armature = obj
                break
        
        if not nancy_armature:
            raise Exception("No se encontró Nancy armature")
        
        if nancy_armature.animation_data:
            nancy_armature.animation_data_clear()
        
        # 3. Importar Nina con animación
        print(f"🎬 Importando animación de Nina...")
        bpy.ops.import_scene.gltf(filepath=str(nina_file))
        
        nina_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE' and obj != nancy_armature:
                nina_armature = obj
                break
        
        if not nina_armature or not nina_armature.animation_data or not nina_armature.animation_data.action:
            raise Exception("Nina sin animación")
        
        nina_action = nina_armature.animation_data.action
        frame_start = int(nina_action.frame_range[0])
        frame_end = int(nina_action.frame_range[1])
        
        print(f"   ✅ Frames: {frame_start}-{frame_end}")
        
        # 4. Copiar animación a Nancy
        print(f"🔄 Copiando animación...")
        
        nancy_action = bpy.data.actions.new(name=palabra)
        
        for fcurve in nina_action.fcurves:
            data_path = fcurve.data_path
            
            if 'pose.bones[' in data_path:
                bone_name_start = data_path.find('["') + 2
                bone_name_end = data_path.find('"]')
                bone_name = data_path[bone_name_start:bone_name_end]
                
                if bone_name in nancy_armature.data.bones:
                    new_fcurve = nancy_action.fcurves.new(
                        data_path=data_path,
                        index=fcurve.array_index
                    )
                    
                    for keyframe in fcurve.keyframe_points:
                        new_fcurve.keyframe_points.insert(
                            keyframe.co.x,
                            keyframe.co.y,
                            options={'FAST'}
                        )
        
        if not nancy_armature.animation_data:
            nancy_armature.animation_data_create()
        
        nancy_armature.animation_data.action = nancy_action
        
        print(f"   ✅ {len(nancy_action.fcurves)} FCurves copiadas")
        
        # 5. Eliminar objetos de Nina
        objetos_nancy = [obj for obj in bpy.data.objects if obj == nancy_armature or obj.parent == nancy_armature]
        objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_nancy]
        
        for obj in objetos_eliminar:
            bpy.data.objects.remove(obj, do_unlink=True)
        
        # 6. Exportar a FBX
        print(f"💾 Exportando a FBX...")
        nancy_output_dir.mkdir(parents=True, exist_ok=True)
        
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
            path_mode='COPY',
            embed_textures=True
        )
        
        # 7. Reimportar FBX
        print(f"💾 Reimportando FBX...")
        bpy.ops.wm.read_homefile(use_empty=True)
        bpy.ops.import_scene.fbx(filepath=str(fbx_temp))
        
        # 8. Exportar a GLB
        print(f"💾 Exportando a GLB...")
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
            export_normals=True,
            export_attributes=True
        )
        
        # 9. Verificar resultado
        if nancy_output.exists():
            size_mb = nancy_output.stat().st_size / (1024*1024)
            print(f"   ✅ Generado: {size_mb:.1f} MB")
            exitosos.append(f"{categoria}/{palabra}")
        else:
            raise Exception("Archivo no generado")
        
        # 10. Limpiar FBX temporal
        if fbx_temp.exists():
            fbx_temp.unlink()
        
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        fallidos.append(f"{categoria}/{palabra}: {str(e)}")
        continue

# Resumen final
print(f"\n{'='*80}")
print("RESUMEN FINAL")
print(f"{'='*80}")
print(f"\n✅ EXITOSOS: {len(exitosos)}/{len(nina_files)}")

for item in exitosos:
    print(f"   ✅ {item}")

if fallidos:
    print(f"\n❌ FALLIDOS: {len(fallidos)}")
    for item in fallidos:
        print(f"   ❌ {item}")

print(f"\n{'='*80}")
print("PROCESO COMPLETADO")
print(f"{'='*80}")
