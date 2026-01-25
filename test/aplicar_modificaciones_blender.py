import bpy
import json
import math
from pathlib import Path
from mathutils import Quaternion, Euler

def aplicar_modificaciones_blender(json_config_path):
    """Aplicar modificaciones usando Blender directamente"""
    
    print(f"\n{'='*80}")
    print(f"🎨 APLICANDO MODIFICACIONES CON BLENDER")
    print(f"{'='*80}")
    
    # Cargar configuración
    with open(json_config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    glb_path = list(config.keys())[0]
    modifications = config[glb_path]
    
    print(f"📂 Archivo: {glb_path}")
    
    if not Path(glb_path).exists():
        raise FileNotFoundError(f"Archivo no encontrado: {glb_path}")
    
    # Extraer configuración
    alcance = modifications['alcance']
    frame_min = alcance['min']
    frame_max = alcance['max']
    frame_retencion = alcance['retencion']
    
    # Calcular rangos
    total_frames = frame_max - frame_min
    repeat_start = frame_min + (total_frames - frame_retencion) // 2
    repeat_end = repeat_start + frame_retencion
    
    print(f"⚙️  Rango: {frame_min} → {frame_max}")
    print(f"📊 Repetición: frames {repeat_start}-{repeat_end}")
    print(f"🔄 Transición entrada: {frame_min}→{repeat_start}")
    print(f"🔄 Transición salida: {repeat_end}→{frame_max}")
    
    # Limpiar escena
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    # Importar GLB
    print(f"\n📥 Importando GLB en Blender...")
    bpy.ops.import_scene.gltf(filepath=glb_path)
    
    # Buscar armature
    armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            armature = obj
            break
    
    if not armature:
        raise ValueError("No se encontró armature en el archivo GLB")
    
    print(f"✅ Armature encontrado: {armature.name}")
    
    # Verificar que tiene animación
    if not armature.animation_data or not armature.animation_data.action:
        raise ValueError("El armature no tiene animación")
    
    action = armature.animation_data.action
    print(f"✅ Animación encontrada: {action.name}")
    print(f"   Duración: {action.frame_range[0]:.0f} - {action.frame_range[1]:.0f}")
    
    # Procesar cada hueso
    bones_modified = []
    
    for bone_name in modifications:
        if bone_name == 'alcance':
            continue
        
        target_values = modifications[bone_name]
        print(f"\n🦴 Procesando: {bone_name}")
        print(f"   Valores objetivo: w={target_values['w']:.3f}, x={target_values['x']:.3f}, "
              f"y={target_values['y']:.3f}, z={target_values['z']:.3f}")
        
        # Verificar que el hueso existe
        if bone_name not in armature.pose.bones:
            print(f"   ⚠️  Hueso no encontrado en armature")
            continue
        
        # Crear quaternion objetivo desde JSON (w,x,y,z)
        target_quat = Quaternion((
            target_values['w'],
            target_values['x'],
            target_values['y'],
            target_values['z']
        ))
        
        print(f"   🎯 Quaternion: {target_quat}")
        
        # Buscar fcurves de rotación del hueso
        data_path = f'pose.bones["{bone_name}"].rotation_quaternion'
        
        fcurves = [fc for fc in action.fcurves if fc.data_path == data_path]
        
        if len(fcurves) != 4:
            print(f"   ⚠️  No se encontraron fcurves de rotación quaternion (encontradas: {len(fcurves)})")
            continue
        
        print(f"   ✅ Encontradas 4 fcurves de rotación")
        
        # Ordenar fcurves por array_index (0=W, 1=X, 2=Y, 3=Z)
        fcurves_sorted = sorted(fcurves, key=lambda fc: fc.array_index)
        
        # Obtener valores objetivo por componente
        target_components = [target_quat.w, target_quat.x, target_quat.y, target_quat.z]
        
        # Aplicar en frames de repetición
        for frame in range(repeat_start, repeat_end + 1):
            for i, fc in enumerate(fcurves_sorted):
                # Buscar o crear keyframe
                kf = None
                for k in fc.keyframe_points:
                    if abs(k.co[0] - frame) < 0.01:
                        kf = k
                        break
                
                if kf:
                    kf.co[1] = target_components[i]
                    kf.interpolation = 'LINEAR'
                else:
                    fc.keyframe_points.insert(frame, target_components[i])
        
        print(f"   ✓ Aplicado en frames {repeat_start}-{repeat_end}")
        
        # Interpolación de entrada
        if repeat_start > frame_min:
            for frame in range(frame_min, repeat_start):
                progress = (frame - frame_min) / (repeat_start - frame_min)
                # Ease in-out cubic
                if progress < 0.5:
                    eased = 4 * progress * progress * progress
                else:
                    eased = 1 - pow(-2 * progress + 2, 3) / 2
                
                # Obtener quaternion original en este frame
                bpy.context.scene.frame_set(frame)
                pose_bone = armature.pose.bones[bone_name]
                original_quat = pose_bone.rotation_quaternion.copy()
                
                # Interpolar
                interpolated = original_quat.slerp(target_quat, eased)
                
                # Aplicar
                for i, fc in enumerate(fcurves_sorted):
                    comp_value = [interpolated.w, interpolated.x, interpolated.y, interpolated.z][i]
                    kf = None
                    for k in fc.keyframe_points:
                        if abs(k.co[0] - frame) < 0.01:
                            kf = k
                            break
                    
                    if kf:
                        kf.co[1] = comp_value
                        kf.interpolation = 'LINEAR'
                    else:
                        fc.keyframe_points.insert(frame, comp_value)
            
            print(f"   ✓ Interpolación entrada: {frame_min}-{repeat_start}")
        
        # Interpolación de salida
        if repeat_end < frame_max:
            # Obtener quaternion final original
            bpy.context.scene.frame_set(frame_max)
            pose_bone = armature.pose.bones[bone_name]
            end_quat = pose_bone.rotation_quaternion.copy()
            
            for frame in range(repeat_end + 1, frame_max + 1):
                progress = (frame - repeat_end) / (frame_max - repeat_end)
                # Ease in-out cubic
                if progress < 0.5:
                    eased = 4 * progress * progress * progress
                else:
                    eased = 1 - pow(-2 * progress + 2, 3) / 2
                
                # Interpolar desde target hacia final
                interpolated = target_quat.slerp(end_quat, eased)
                
                # Aplicar
                for i, fc in enumerate(fcurves_sorted):
                    comp_value = [interpolated.w, interpolated.x, interpolated.y, interpolated.z][i]
                    kf = None
                    for k in fc.keyframe_points:
                        if abs(k.co[0] - frame) < 0.01:
                            kf = k
                            break
                    
                    if kf:
                        kf.co[1] = comp_value
                        kf.interpolation = 'LINEAR'
                    else:
                        fc.keyframe_points.insert(frame, comp_value)
            
            print(f"   ✓ Interpolación salida: {repeat_end}-{frame_max}")
        
        # Actualizar fcurves
        for fc in fcurves_sorted:
            fc.update()
        
        bones_modified.append(bone_name)
        print(f"   ✅ Modificaciones aplicadas")
    
    # Exportar GLB modificado
    input_path = Path(glb_path)
    output_path = str(input_path.parent / f"{input_path.stem}_modif{input_path.suffix}")
    
    print(f"\n💾 Exportando GLB modificado...")
    print(f"   Ruta: {output_path}")
    
    bpy.ops.export_scene.gltf(
        filepath=output_path,
        export_format='GLB',
        export_animations=True,
        export_frame_range=False
    )
    
    print(f"\n{'='*80}")
    print(f"✅ PROCESO COMPLETADO CON BLENDER")
    print(f"{'='*80}")
    print(f"📁 Archivo: {output_path}")
    print(f"🦴 Huesos modificados: {len(bones_modified)}")
    for bone in bones_modified:
        print(f"   - {bone}")
    
    # Verificar resultado
    print(f"\n🔍 VERIFICACIÓN:")
    bpy.context.scene.frame_set(30)
    for bone_name in bones_modified:
        pose_bone = armature.pose.bones[bone_name]
        quat = pose_bone.rotation_quaternion
        print(f"   {bone_name} @ frame 30:")
        print(f"      W={quat.w:.3f}, X={quat.x:.3f}, Y={quat.y:.3f}, Z={quat.z:.3f}")
    
    return output_path

if __name__ == "__main__":
    import sys
    
    # Buscar argumento --config en argv
    config_path = "datos.json"  # Default
    
    for i, arg in enumerate(sys.argv):
        if arg == "--config" and i + 1 < len(sys.argv):
            config_path = sys.argv[i + 1]
            break
        elif arg == "--":
            # Después de -- están los argumentos del script
            if i + 1 < len(sys.argv):
                config_path = sys.argv[i + 1]
            break
    
    # Si no se encontró, usar path relativo al script
    if config_path == "datos.json":
        script_dir = Path(__file__).parent
        config_path = str(script_dir / "datos.json")
    
    try:
        output_file = aplicar_modificaciones_blender(str(config_path))
        print(f"\n🎉 Éxito! Archivo listo: {output_file}")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
