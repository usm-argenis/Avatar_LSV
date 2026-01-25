import bpy
import sys
from pathlib import Path

# Rutas
base_dir = Path(r"C:\Users\andre\OneDrive\Documentos\tesis")
nancy_base = base_dir / "test/output/glb/Nancy/Nancy.glb"

categoria = "saludos"
animacion = "hola"
archivo_nina = base_dir / f"test/output/glb/Nina/{categoria}/Nina_resultado_{animacion}.glb"
archivo_fbx_temp = base_dir / f"test/output/temp_{animacion}.fbx"
archivo_salida = base_dir / f"test/output/glb/Nancy/{categoria}/Nancy_resultado_{animacion}.glb"

print(f"\n{'='*80}")
print(f"PRUEBA: FBX → GLB para preservar animación + texturas")
print(f"{'='*80}\n")

try:
    # PASO 1: Crear FBX con animación (sin texturas)
    print("="*80)
    print("PASO 1: Crear FBX con animación")
    print("="*80)
    
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
    print(f"📥 Importando Nancy base...")
    bpy.ops.import_scene.gltf(filepath=str(nancy_base))
    nancy_objs = list(bpy.data.objects)
    nancy_armature = next((obj for obj in nancy_objs if obj.type == 'ARMATURE'), None)
    
    print(f"📥 Importando animación de Nina ({animacion})...")
    bpy.ops.import_scene.gltf(filepath=str(archivo_nina))
    nina_objs = [obj for obj in bpy.data.objects if obj not in nancy_objs]
    nina_armature = next((obj for obj in nina_objs if obj.type == 'ARMATURE'), None)
    
    action_original = nina_armature.animation_data.action
    
    print(f"🔄 Copiando y limpiando animación...")
    action = action_original.copy()
    action.name = f"{action_original.name}_limpia"
    
    frame_start = action.frame_range[0]
    frame_end = action.frame_range[1]
    
    huesos_piernas = [
        'Hips', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase',
        'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase'
    ]
    
    fcurves_eliminadas = [fc for fc in action.fcurves if any(bone in fc.data_path for bone in huesos_piernas)]
    for fc in fcurves_eliminadas:
        action.fcurves.remove(fc)
    
    print(f"   Eliminadas {len(fcurves_eliminadas)} FCurves de piernas")
    
    # Eliminar objetos de Nina
    for obj in nina_objs:
        if obj != nina_armature:
            bpy.data.objects.remove(obj, do_unlink=True)
    
    # Eliminar acciones no usadas
    acciones_a_eliminar = [act for act in bpy.data.actions if act != action]
    for act in acciones_a_eliminar:
        bpy.data.actions.remove(act)
    
    # Asignar acción a Nancy
    if not nancy_armature.animation_data:
        nancy_armature.animation_data_create()
    
    nancy_armature.animation_data.action = action
    bpy.context.scene.frame_start = int(frame_start)
    bpy.context.scene.frame_end = int(frame_end)
    
    print(f"💾 Exportando a FBX temporal...")
    bpy.ops.export_scene.fbx(
        filepath=str(archivo_fbx_temp),
        use_selection=False,
        bake_anim=True,
        bake_anim_use_all_actions=False,
        bake_anim_use_nla_strips=False,
        add_leaf_bones=False
    )
    
    print(f"   ✅ FBX creado con {len(action.fcurves)} FCurves\n")
    
    # PASO 2: Importar FBX + Nancy base para combinar animación + texturas
    print("="*80)
    print("PASO 2: Combinar animación (FBX) + texturas (Nancy base)")
    print("="*80)
    
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
    print(f"📥 Importando Nancy base (texturas)...")
    bpy.ops.import_scene.gltf(filepath=str(nancy_base))
    nancy_objs = list(bpy.data.objects)
    nancy_armature = next((obj for obj in nancy_objs if obj.type == 'ARMATURE'), None)
    texturas_nancy = len(bpy.data.images)
    print(f"   ✅ {texturas_nancy} texturas importadas")
    
    print(f"📥 Importando FBX con animación...")
    bpy.ops.import_scene.fbx(filepath=str(archivo_fbx_temp))
    fbx_objs = [obj for obj in bpy.data.objects if obj not in nancy_objs]
    fbx_armature = next((obj for obj in fbx_objs if obj.type == 'ARMATURE'), None)
    
    if fbx_armature and fbx_armature.animation_data and fbx_armature.animation_data.action:
        fbx_action = fbx_armature.animation_data.action
        print(f"   ✅ Animación importada: {len(fbx_action.fcurves)} FCurves")
        
        # Transferir animación a Nancy
        print(f"🔄 Transfiriendo animación a Nancy...")
        if not nancy_armature.animation_data:
            nancy_armature.animation_data_create()
        
        # Copiar la acción
        accion_limpia = fbx_action.copy()
        accion_limpia.name = "AnimacionLimpia"
        
        # Eliminar objetos del FBX
        for obj in fbx_objs:
            bpy.data.objects.remove(obj, do_unlink=True)
        
        # CRÍTICO: Eliminar TODAS las otras acciones
        print(f"🗑️  Limpiando acciones...")
        acciones_a_eliminar = [act for act in bpy.data.actions if act != accion_limpia]
        print(f"   Eliminando: {[act.name for act in acciones_a_eliminar]}")
        for act in acciones_a_eliminar:
            bpy.data.actions.remove(act)
        
        # Limpiar NLA tracks existentes
        if nancy_armature.animation_data:
            while len(nancy_armature.animation_data.nla_tracks) > 0:
                nancy_armature.animation_data.nla_tracks.remove(nancy_armature.animation_data.nla_tracks[0])
        
        # NO asignar como acción activa, sino crear NLA strip para export
        # GLTF solo exporta desde NLA strips cuando export_nla_strips=True
        print(f"🎬 Creando NLA strip para exportación...")
        if not nancy_armature.animation_data:
            nancy_armature.animation_data_create()
        
        nla_track = nancy_armature.animation_data.nla_tracks.new()
        nla_track.name = accion_limpia.name
        nla_strip = nla_track.strips.new(accion_limpia.name, int(frame_start), accion_limpia)
        
        print(f"   ✅ NLA track: {nla_track.name}")
        print(f"   ✅ NLA strip frames: {int(frame_start)}-{int(frame_end)}")
        
        # Configurar timeline
        bpy.context.scene.frame_start = int(frame_start)
        bpy.context.scene.frame_end = int(frame_end)
        
        print(f"💾 Exportando GLB final con NLA strips...")
        archivo_salida.parent.mkdir(parents=True, exist_ok=True)
        
        bpy.ops.export_scene.gltf(
            filepath=str(archivo_salida),
            export_format='GLB',
            export_animations=True,
            export_nla_strips=True,  # CRÍTICO: Exportar desde NLA strips
            export_image_format='AUTO'
        )
        
        file_size = archivo_salida.stat().st_size / (1024*1024)
        texturas_finales = len(bpy.data.images)
        acciones_finales = len(bpy.data.actions)
        if nancy_armature.animation_data and nancy_armature.animation_data.action:
            fcurves_finales = len(nancy_armature.animation_data.action.fcurves)
        else:
            fcurves_finales = 0
        
        print(f"   ✅ {file_size:.1f}MB | {texturas_finales} texturas | {acciones_finales} acciones | {fcurves_finales} FCurves")
        
        # Limpiar archivo temporal
        archivo_fbx_temp.unlink()
        
        print(f"\n{'='*80}")
        print(f"✅ EXPORTACIÓN EXITOSA")
        print(f"{'='*80}\n")
    else:
        raise Exception("FBX no tiene animación")
        
except Exception as e:
    print(f"\n{'='*80}")
    print(f"❌ ERROR: {e}")
    print(f"{'='*80}\n")
    import traceback
    traceback.print_exc()
    sys.exit(1)
