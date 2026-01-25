import bpy
import sys
from pathlib import Path

# Archivos base (rutas absolutas)
base_dir = Path(r"C:\Users\andre\OneDrive\Documentos\tesis")
nancy_base = base_dir / "test/output/glb/Nancy/Nancy.glb"

# Archivo de prueba
categoria = "saludos"
animacion = "hola"
archivo_nina = base_dir / f"test/output/glb/Nina/{categoria}/Nina_resultado_{animacion}.glb"
archivo_salida = base_dir / f"test/output/glb/Nancy/{categoria}/Nancy_resultado_{animacion}.glb"

print(f"\n{'='*80}")
print(f"PRUEBA UNITARIA: {animacion}")
print(f"{'='*80}\n")

try:
    # Limpiar escena
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
    # 1. Importar Nancy base
    print(f"📥 Importando Nancy base...")
    bpy.ops.import_scene.gltf(filepath=str(nancy_base))
    
    nancy_objs = list(bpy.data.objects)
    nancy_armature = next((obj for obj in nancy_objs if obj.type == 'ARMATURE'), None)
    
    if not nancy_armature:
        raise Exception("No se encontró armature de Nancy")
    
    texturas_nancy = len(bpy.data.images)
    print(f"   ✅ Nancy importada: {len(nancy_objs)} objetos, {texturas_nancy} texturas")
    
    # 2. Importar animación de Nina
    print(f"📥 Importando animación de Nina ({animacion})...")
    bpy.ops.import_scene.gltf(filepath=str(archivo_nina))
    
    nina_objs = [obj for obj in bpy.data.objects if obj not in nancy_objs]
    nina_armature = next((obj for obj in nina_objs if obj.type == 'ARMATURE'), None)
    
    if not nina_armature or not nina_armature.animation_data:
        raise Exception("Nina no tiene animación")
    
    action_original = nina_armature.animation_data.action
    print(f"   ✅ Nina importada: {action_original.name} con {len(action_original.fcurves)} FCurves")
    
    # 3. Copiar y limpiar acción
    print(f"🔄 Copiando y limpiando animación...")
    action = action_original.copy()
    action.name = f"{action_original.name}_fixed"
    
    frame_start = action.frame_range[0]
    frame_end = action.frame_range[1]
    
    huesos_piernas = [
        'Hips', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 
        'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase'
    ]
    
    fcurves_a_eliminar = [fc for fc in action.fcurves if any(bone in fc.data_path for bone in huesos_piernas)]
    for fc in fcurves_a_eliminar:
        action.fcurves.remove(fc)
    
    print(f"   ✅ Eliminadas {len(fcurves_a_eliminar)} FCurves de piernas ({len(action.fcurves)} restantes)")
    
    # 4. Eliminar objetos de Nina
    print(f"🗑️ Eliminando objetos de Nina...")
    objetos_eliminar = [obj for obj in nina_objs if obj != nina_armature]
    for obj in objetos_eliminar:
        bpy.data.objects.remove(obj, do_unlink=True)
    
    # CRÍTICO: Eliminar TODAS las otras acciones PRIMERO
    print(f"🗑️ Eliminando acciones no utilizadas...")
    acciones_a_eliminar = [act for act in bpy.data.actions if act != action]
    print(f"   Eliminando: {[act.name for act in acciones_a_eliminar]}")
    for act in acciones_a_eliminar:
        bpy.data.actions.remove(act)
    
    print(f"   ✅ Acciones en bpy.data.actions: {[act.name for act in bpy.data.actions]}")
    
    # 5. Configurar animation_data
    print(f"🎬 Configurando animación en Nancy...")
    if not nancy_armature.animation_data:
        nancy_armature.animation_data_create()
    
    # Limpiar NLA tracks existentes
    while len(nancy_armature.animation_data.nla_tracks) > 0:
        nancy_armature.animation_data.nla_tracks.remove(nancy_armature.animation_data.nla_tracks[0])
    
    # Asignar la acción directamente
    nancy_armature.animation_data.action = action
    action.use_fake_user = True  # Proteger la acción
    
    print(f"   ✅ Acción asignada: {action.name}")
    print(f"   ✅ FCurves: {len(action.fcurves)}")
    print(f"   ✅ Frame range: {action.frame_range}")
    
    # Configurar timeline
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
    
    # 6. Exportar a FBX (prueba)
    print(f"💾 Exportando a FBX...")
    archivo_fbx = archivo_salida.with_suffix('.fbx')
    archivo_fbx.parent.mkdir(parents=True, exist_ok=True)
    
    bpy.ops.export_scene.fbx(
        filepath=str(archivo_fbx),
        use_selection=False,
        bake_anim=True,
        bake_anim_use_all_actions=False,
        bake_anim_use_nla_strips=False,
        add_leaf_bones=False
    )
    
    file_size_fbx = archivo_fbx.stat().st_size / (1024*1024)
    print(f"   ✅ FBX: {file_size_fbx:.1f}MB")
    
    # 7. Exportar a GLB también para comparar
    print(f"💾 Exportando a GLB...")
    archivo_salida.parent.mkdir(parents=True, exist_ok=True)
    
    bpy.ops.export_scene.gltf(
        filepath=str(archivo_salida),
        export_format='GLB',
        export_animations=True,
        export_current_frame=False,
        export_anim_single_armature=True,
        export_image_format='AUTO'
    )
    
    file_size = archivo_salida.stat().st_size / (1024*1024)
    texturas_finales = len(bpy.data.images)
    
    print(f"   ✅ {file_size:.1f}MB | {texturas_finales} texturas | {len(action.fcurves)} FCurves")
    print(f"\n{'='*80}")
    print(f"✅ EXPORTACIÓN EXITOSA")
    print(f"{'='*80}\n")
    
except Exception as e:
    print(f"\n{'='*80}")
    print(f"❌ ERROR: {e}")
    print(f"{'='*80}\n")
    import traceback
    traceback.print_exc()
    sys.exit(1)
