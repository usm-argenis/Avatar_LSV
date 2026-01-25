import bpy
from pathlib import Path

# Directorio base
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy")

# Buscar todos los archivos GLB de Nancy (excepto el modelo base)
archivos = []
for glb_file in BASE_DIR.rglob("Nancy_resultado_*.glb"):
    archivos.append(glb_file)

print(f"\n{'='*80}")
print(f"ELIMINANDO ANIMACIÓN DE PIERNAS - BATCH NANCY")
print(f"{'='*80}")
print(f"📂 Encontrados: {len(archivos)} archivos\n")

# Lista de huesos del tren inferior
huesos_piernas = [
    "Hips",
    "LeftUpLeg",
    "LeftLeg",
    "LeftFoot",
    "LeftToeBase",
    "LeftToe_End",
    "RightUpLeg",
    "RightLeg",
    "RightFoot",
    "RightToeBase",
    "RightToe_End"
]

total_procesados = 0
total_fallidos = 0

for idx, archivo in enumerate(archivos, 1):
    categoria = archivo.parent.name
    print(f"[{idx}/{len(archivos)}] {categoria}/{archivo.name}")
    
    try:
        # Limpiar escena
        bpy.ops.wm.read_homefile(use_empty=True)
        
        # Importar GLB
        bpy.ops.import_scene.gltf(filepath=str(archivo))
        
        # Buscar armature
        armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                armature = obj
                break
        
        if not armature or not armature.animation_data or not armature.animation_data.action:
            print(f"   ⚠️ Sin animación")
            continue
        
        action = armature.animation_data.action
        fcurves_iniciales = len(action.fcurves)
        
        # Eliminar FCurves de piernas
        fcurves_a_eliminar = []
        for fcurve in action.fcurves:
            for hueso in huesos_piernas:
                if f'pose.bones["{hueso}"]' in fcurve.data_path:
                    fcurves_a_eliminar.append(fcurve)
                    break
        
        for fcurve in fcurves_a_eliminar:
            action.fcurves.remove(fcurve)
        
        # Resetear pose de piernas
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
        
        # Exportar FBX temporal
        fbx_temp = archivo.with_suffix('.fbx')
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
        
        # Re-importar y exportar GLB
        bpy.ops.wm.read_homefile(use_empty=True)
        bpy.ops.import_scene.fbx(filepath=str(fbx_temp))
        
        bpy.ops.export_scene.gltf(
            filepath=str(archivo),
            export_format='GLB',
            export_animations=True,
            export_frame_range=True,
            export_force_sampling=True,
            export_def_bones=False,
            export_optimize_animation_size=False
        )
        
        # Limpiar FBX
        if fbx_temp.exists():
            fbx_temp.unlink()
        
        file_size = archivo.stat().st_size / (1024*1024)
        fcurves_finales = fcurves_iniciales - len(fcurves_a_eliminar)
        print(f"   ✅ {file_size:.1f}MB | {fcurves_iniciales}→{fcurves_finales} FCurves | -{len(fcurves_a_eliminar)} piernas")
        total_procesados += 1
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        total_fallidos += 1

print(f"\n{'='*80}")
print(f"RESUMEN FINAL")
print(f"{'='*80}")
print(f"✅ Procesados: {total_procesados}/{len(archivos)}")
print(f"❌ Fallidos: {total_fallidos}/{len(archivos)}")
print(f"{'='*80}\n")
