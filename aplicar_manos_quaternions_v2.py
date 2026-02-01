import bpy
import json
import sys
from pathlib import Path
from mathutils import Quaternion, Euler
import math

def aplicar_manos_quaternions_v2(hand_json_path, glb_input_path, glb_output_path):
    """
    Aplica cuaterniones de manos desde JSON de MediaPipe a un archivo GLB.
    Versión 2: Aplica rotaciones relativas, no absolutas
    
    Args:
        hand_json_path: Ruta al JSON con cuaterniones de MediaPipe
        glb_input_path: Ruta al GLB de entrada
        glb_output_path: Ruta al GLB de salida modificado
    """
    
    print(f"\n{'='*80}")
    print(f"🖐️  APLICANDO CUATERNIONES DE MANOS A GLB (V2 - Relativo)")
    print(f"{'='*80}")
    
    # Cargar JSON de cuaterniones
    print(f"\n📂 Cargando datos de manos...")
    with open(hand_json_path, 'r', encoding='utf-8') as f:
        hand_data = json.load(f)
    
    frames_data = hand_data['frames']
    total_frames = len(frames_data)
    print(f"✅ Cargados {total_frames} frames de datos de manos")
    
    # Verificar archivos
    if not Path(glb_input_path).exists():
        raise FileNotFoundError(f"Archivo GLB no encontrado: {glb_input_path}")
    
    print(f"\n📥 Importando GLB: {Path(glb_input_path).name}")
    
    # Limpiar escena
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    # Importar GLB
    bpy.ops.import_scene.gltf(filepath=str(glb_input_path))
    
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
    print(f"   Duración original: {action.frame_range[0]:.0f} - {action.frame_range[1]:.0f}")
    
    # Mapeo de dedos MediaPipe a huesos de Duvall (RIGHT HAND)
    finger_mapping = {
        'thumb': {
            1: 'RightHandThumb2',   # Proximal
            2: 'RightHandThumb3',   # Middle
            3: 'RightHandThumb4'    # Distal
        },
        'index': {
            1: 'RightHandIndex2',
            2: 'RightHandIndex3',
            3: 'RightHandIndex4'
        },
        'middle': {
            1: 'RightHandMiddle2',
            2: 'RightHandMiddle3',
            3: 'RightHandMiddle4'
        },
        'ring': {
            1: 'RightHandRing2',
            2: 'RightHandRing3',
            3: 'RightHandRing4'
        },
        'pinky': {
            1: 'RightHandPinky2',
            2: 'RightHandPinky3',
            3: 'RightHandPinky4'
        }
    }
    
    print(f"\n🦴 Preparando modificación de huesos de mano...")
    
    # Guardar rotaciones originales de cada hueso en el primer frame
    bpy.context.scene.frame_set(1)
    original_rotations = {}
    
    for finger_name, segments in finger_mapping.items():
        for segment_idx, bone_name in segments.items():
            if bone_name in armature.pose.bones:
                pose_bone = armature.pose.bones[bone_name]
                original_rotations[bone_name] = pose_bone.rotation_quaternion.copy()
    
    print(f"✅ Guardadas {len(original_rotations)} rotaciones originales")
    
    # Obtener el primer frame de MediaPipe como referencia
    first_frame = frames_data[0]
    if 'hands' not in first_frame or len(first_frame['hands']) == 0:
        raise ValueError("No hay datos de manos en el primer frame")
    
    first_hand = first_frame['hands'][0]
    reference_quats = {}
    
    for finger_name in ['thumb', 'index', 'middle', 'ring', 'pinky']:
        reference_quats[finger_name] = {}
        for segment_idx in [1, 2, 3]:
            quat_data = first_hand['fingers'][finger_name][segment_idx]
            # Guardar como Quaternion de Blender
            reference_quats[finger_name][segment_idx] = Quaternion((
                quat_data[3],  # w
                quat_data[0],  # x
                quat_data[1],  # y
                quat_data[2]   # z
            ))
    
    print(f"✅ Cuaterniones de referencia guardados (frame 0)")
    
    # Procesar cada frame
    print(f"\n🎬 Aplicando rotaciones relativas frame por frame...")
    
    frames_modified = 0
    
    for frame_idx, frame_data in enumerate(frames_data):
        frame_number = frame_idx + 1
        
        if frame_idx % 10 == 0:
            print(f"   Frame {frame_idx + 1}/{total_frames}...", end='\r')
        
        # Verificar que hay datos de manos
        if 'hands' not in frame_data or len(frame_data['hands']) == 0:
            continue
        
        hand_info = frame_data['hands'][0]
        
        # Procesar cada dedo
        for finger_name in ['thumb', 'index', 'middle', 'ring', 'pinky']:
            finger_data = hand_info['fingers'][finger_name]
            
            # Solo segmentos 1, 2, 3 (excluyendo metacarpo/base)
            for segment_idx in [1, 2, 3]:
                if finger_name not in finger_mapping or segment_idx not in finger_mapping[finger_name]:
                    continue
                
                bone_name = finger_mapping[finger_name][segment_idx]
                
                if bone_name not in original_rotations:
                    continue
                
                # Obtener cuaternión actual de MediaPipe
                quat_data = finger_data[segment_idx]
                current_mp_quat = Quaternion((
                    quat_data[3],  # w
                    quat_data[0],  # x
                    quat_data[1],  # y
                    quat_data[2]   # z
                ))
                
                # Calcular la rotación relativa desde el frame de referencia
                reference_quat = reference_quats[finger_name][segment_idx]
                
                # Delta = current * reference^-1
                delta_quat = current_mp_quat @ reference_quat.inverted()
                
                # Convertir a ángulos de Euler para análisis y limitación
                delta_euler = delta_quat.to_euler('XYZ')
                
                # Escalar la rotación (reducir intensidad para evitar deformaciones)
                scale_factor = 0.5  # Usar solo 50% de la rotación detectada
                
                scaled_euler = Euler((
                    delta_euler.x * scale_factor,
                    delta_euler.y * scale_factor,
                    delta_euler.z * scale_factor
                ), 'XYZ')
                
                scaled_delta = scaled_euler.to_quaternion()
                
                # Aplicar a la rotación original
                original_rot = original_rotations[bone_name]
                final_quat = scaled_delta @ original_rot
                
                # Normalizar
                final_quat.normalize()
                
                # Buscar o crear fcurves
                data_path = f'pose.bones["{bone_name}"].rotation_quaternion'
                fcurves = [fc for fc in action.fcurves if fc.data_path == data_path]
                
                if len(fcurves) == 0:
                    for i in range(4):
                        fc = action.fcurves.new(data_path=data_path, index=i)
                        fcurves.append(fc)
                
                fcurves_sorted = sorted(fcurves, key=lambda fc: fc.array_index)
                
                # Aplicar valores
                target_components = [final_quat.w, final_quat.x, final_quat.y, final_quat.z]
                
                for i, fc in enumerate(fcurves_sorted):
                    kf = None
                    for k in fc.keyframe_points:
                        if abs(k.co[0] - frame_number) < 0.01:
                            kf = k
                            break
                    
                    if kf:
                        kf.co[1] = target_components[i]
                        kf.interpolation = 'LINEAR'
                    else:
                        fc.keyframe_points.insert(frame_number, target_components[i])
                        fc.update()
        
        frames_modified += 1
    
    print(f"\n✅ Procesados {frames_modified} frames")
    
    # Actualizar rango de frames
    if total_frames > action.frame_range[1]:
        action.frame_range = (action.frame_range[0], total_frames)
        print(f"📊 Rango de animación actualizado: {action.frame_range[0]:.0f} - {action.frame_range[1]:.0f}")
    
    # Exportar GLB modificado
    print(f"\n💾 Exportando GLB modificado...")
    print(f"   Destino: {glb_output_path}")
    
    bpy.ops.export_scene.gltf(
        filepath=str(glb_output_path),
        export_format='GLB',
        export_animations=True,
        export_nla_strips=False
    )
    
    output_size = Path(glb_output_path).stat().st_size / (1024 * 1024)
    print(f"✅ Exportación completa: {output_size:.2f} MB")
    
    print(f"\n{'='*80}")
    print(f"✨ PROCESO COMPLETADO EXITOSAMENTE")
    print(f"{'='*80}")
    print(f"📊 Resumen:")
    print(f"   • Método: Rotaciones relativas con escala 0.5x")
    print(f"   • Frames procesados: {frames_modified}")
    print(f"   • Huesos modificados: {len(original_rotations)}")
    print(f"   • Archivo salida: {Path(glb_output_path).name}")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    argv = sys.argv
    
    if "--" in argv:
        argv = argv[argv.index("--") + 1:]
    else:
        argv = []
    
    if len(argv) < 3:
        print("❌ Error: Se requieren 3 argumentos")
        print("Uso: blender --background --python aplicar_manos_quaternions_v2.py -- <hand_json> <input_glb> <output_glb>")
        sys.exit(1)
    
    hand_json = argv[0]
    input_glb = argv[1]
    output_glb = argv[2]
    
    aplicar_manos_quaternions_v2(hand_json, input_glb, output_glb)
