import bpy
import json
import sys
from pathlib import Path
from mathutils import Quaternion, Euler

def aplicar_manos_quaternions_escalable(hand_json_path, glb_input_path, glb_output_path, scale_factor=0.5):
    """
    Aplica cuaterniones de manos con factor de escala ajustable
    
    Args:
        scale_factor: Factor de escala (0.0 = sin cambio, 1.0 = cambio completo)
    """
    
    print(f"\n{'='*80}")
    print(f"🖐️  APLICANDO MANOS - Escala: {scale_factor}x")
    print(f"{'='*80}")
    
    # Cargar JSON
    with open(hand_json_path, 'r', encoding='utf-8') as f:
        hand_data = json.load(f)
    
    frames_data = hand_data['frames']
    total_frames = len(frames_data)
    print(f"✅ Cargados {total_frames} frames")
    
    if not Path(glb_input_path).exists():
        raise FileNotFoundError(f"Archivo GLB no encontrado: {glb_input_path}")
    
    # Limpiar e importar
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    bpy.ops.import_scene.gltf(filepath=str(glb_input_path))
    
    # Buscar armature
    armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            armature = obj
            break
    
    if not armature or not armature.animation_data or not armature.animation_data.action:
        raise ValueError("No se encontró armature o animación")
    
    action = armature.animation_data.action
    print(f"✅ Armature: {armature.name}, Animación: {action.name}")
    
    # Mapeo (solo segmentos 1-3, no el metacarpo)
    finger_mapping = {
        'thumb': {1: 'RightHandThumb2', 2: 'RightHandThumb3', 3: 'RightHandThumb4'},
        'index': {1: 'RightHandIndex2', 2: 'RightHandIndex3', 3: 'RightHandIndex4'},
        'middle': {1: 'RightHandMiddle2', 2: 'RightHandMiddle3', 3: 'RightHandMiddle4'},
        'ring': {1: 'RightHandRing2', 2: 'RightHandRing3', 3: 'RightHandRing4'},
        'pinky': {1: 'RightHandPinky2', 2: 'RightHandPinky3', 3: 'RightHandPinky4'}
    }
    
    # Guardar rotaciones originales (frame 1)
    bpy.context.scene.frame_set(1)
    original_rotations = {}
    
    for finger_name, segments in finger_mapping.items():
        for segment_idx, bone_name in segments.items():
            if bone_name in armature.pose.bones:
                original_rotations[bone_name] = armature.pose.bones[bone_name].rotation_quaternion.copy()
    
    print(f"✅ Guardadas {len(original_rotations)} rotaciones originales")
    
    # Frame de referencia (frame 0 de MediaPipe)
    first_frame = frames_data[0]
    if 'hands' not in first_frame or len(first_frame['hands']) == 0:
        raise ValueError("No hay datos de manos en frame 0")
    
    first_hand = first_frame['hands'][0]
    reference_quats = {}
    
    for finger_name in ['thumb', 'index', 'middle', 'ring', 'pinky']:
        reference_quats[finger_name] = {}
        for segment_idx in [1, 2, 3]:
            quat_data = first_hand['fingers'][finger_name][segment_idx]
            reference_quats[finger_name][segment_idx] = Quaternion((
                quat_data[3], quat_data[0], quat_data[1], quat_data[2]
            ))
    
    print(f"✅ Referencia guardada (frame 0)")
    
    # Procesar frames
    print(f"\n🎬 Aplicando rotaciones (escala {scale_factor}x)...")
    
    for frame_idx, frame_data in enumerate(frames_data):
        frame_number = frame_idx + 1
        
        if frame_idx % 10 == 0:
            print(f"   Frame {frame_idx + 1}/{total_frames}...", end='\r')
        
        if 'hands' not in frame_data or len(frame_data['hands']) == 0:
            continue
        
        hand_info = frame_data['hands'][0]
        
        for finger_name in ['thumb', 'index', 'middle', 'ring', 'pinky']:
            finger_data = hand_info['fingers'][finger_name]
            
            for segment_idx in [1, 2, 3]:
                if finger_name not in finger_mapping or segment_idx not in finger_mapping[finger_name]:
                    continue
                
                bone_name = finger_mapping[finger_name][segment_idx]
                
                if bone_name not in original_rotations:
                    continue
                
                # Cuaternión actual
                quat_data = finger_data[segment_idx]
                current_mp_quat = Quaternion((
                    quat_data[3], quat_data[0], quat_data[1], quat_data[2]
                ))
                
                # Delta desde referencia
                reference_quat = reference_quats[finger_name][segment_idx]
                delta_quat = current_mp_quat @ reference_quat.inverted()
                
                # Convertir a Euler y escalar
                delta_euler = delta_quat.to_euler('XYZ')
                scaled_euler = Euler((
                    delta_euler.x * scale_factor,
                    delta_euler.y * scale_factor,
                    delta_euler.z * scale_factor
                ), 'XYZ')
                
                scaled_delta = scaled_euler.to_quaternion()
                
                # Aplicar a rotación original
                original_rot = original_rotations[bone_name]
                final_quat = scaled_delta @ original_rot
                final_quat.normalize()
                
                # Guardar en fcurves
                data_path = f'pose.bones["{bone_name}"].rotation_quaternion'
                fcurves = [fc for fc in action.fcurves if fc.data_path == data_path]
                
                if len(fcurves) == 0:
                    for i in range(4):
                        fcurves.append(action.fcurves.new(data_path=data_path, index=i))
                
                fcurves_sorted = sorted(fcurves, key=lambda fc: fc.array_index)
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
    
    print(f"\n✅ Procesados {total_frames} frames")
    
    # Exportar
    print(f"\n💾 Exportando GLB...")
    bpy.ops.export_scene.gltf(
        filepath=str(glb_output_path),
        export_format='GLB',
        export_animations=True,
        export_nla_strips=False
    )
    
    output_size = Path(glb_output_path).stat().st_size / (1024 * 1024)
    print(f"✅ Exportación completa: {output_size:.2f} MB")
    print(f"   Archivo: {Path(glb_output_path).name}")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    argv = sys.argv
    
    if "--" in argv:
        argv = argv[argv.index("--") + 1:]
    else:
        argv = []
    
    if len(argv) < 3:
        print("❌ Error: Se requieren al menos 3 argumentos")
        print("Uso: blender --background --python script.py -- <hand_json> <input_glb> <output_glb> [scale_factor]")
        sys.exit(1)
    
    hand_json = argv[0]
    input_glb = argv[1]
    output_glb = argv[2]
    scale_factor = float(argv[3]) if len(argv) > 3 else 0.5
    
    aplicar_manos_quaternions_escalable(hand_json, input_glb, output_glb, scale_factor)
