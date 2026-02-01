import bpy
import json
from pathlib import Path
from mathutils import Quaternion, Vector

def verificar_dedos():
    """Verificar las rotaciones de los dedos en el GLB modificado"""
    
    print(f"\n{'='*80}")
    print(f"🔍 VERIFICACIÓN DE DEDOS EN GLB")
    print(f"{'='*80}")
    
    glb_path = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\dias_semana\Duvall_resultado_miercoles_MANOS.glb"
    
    # Limpiar escena
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    # Importar GLB
    print(f"\n📥 Importando GLB...")
    bpy.ops.import_scene.gltf(filepath=glb_path)
    
    # Buscar armature
    armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            armature = obj
            break
    
    if not armature:
        raise ValueError("No se encontró armature")
    
    print(f"✅ Armature: {armature.name}")
    
    action = armature.animation_data.action
    print(f"✅ Animación: {action.name}")
    print(f"   Rango: {action.frame_range[0]:.0f} - {action.frame_range[1]:.0f}")
    
    # Huesos de mano a verificar
    hand_bones = [
        'RightHandThumb1', 'RightHandThumb2', 'RightHandThumb3', 'RightHandThumb4',
        'RightHandIndex1', 'RightHandIndex2', 'RightHandIndex3', 'RightHandIndex4',
        'RightHandMiddle1', 'RightHandMiddle2', 'RightHandMiddle3', 'RightHandMiddle4',
    ]
    
    print(f"\n🦴 Analizando huesos de mano...")
    
    # Verificar en frame 1, 30, 60
    test_frames = [1, 30, 60]
    
    for frame_num in test_frames:
        print(f"\n{'─'*80}")
        print(f"📊 Frame {frame_num}:")
        print(f"{'─'*80}")
        
        bpy.context.scene.frame_set(frame_num)
        
        for bone_name in hand_bones:
            if bone_name not in armature.pose.bones:
                continue
            
            pose_bone = armature.pose.bones[bone_name]
            quat = pose_bone.rotation_quaternion
            
            # Calcular magnitud del cuaternión
            magnitude = (quat.w**2 + quat.x**2 + quat.y**2 + quat.z**2)**0.5
            
            # Convertir a ángulo de rotación
            angle_rad = 2 * abs(quat.w)
            if angle_rad > 1.0:
                angle_rad = 1.0
            import math
            angle_deg = math.degrees(math.acos(angle_rad))
            
            print(f"  {bone_name:25s} | Quat: ({quat.w:7.3f}, {quat.x:7.3f}, {quat.y:7.3f}, {quat.z:7.3f}) | Mag: {magnitude:.3f} | Ángulo: {angle_deg:6.1f}°")
    
    # Verificar fcurves
    print(f"\n{'='*80}")
    print(f"📈 FCurves de huesos de mano:")
    print(f"{'='*80}")
    
    for bone_name in hand_bones:
        data_path = f'pose.bones["{bone_name}"].rotation_quaternion'
        fcurves = [fc for fc in action.fcurves if fc.data_path == data_path]
        
        if fcurves:
            print(f"\n{bone_name}:")
            for fc in sorted(fcurves, key=lambda x: x.array_index):
                component = ['W', 'X', 'Y', 'Z'][fc.array_index]
                num_keys = len(fc.keyframe_points)
                
                # Obtener rango de valores
                if num_keys > 0:
                    values = [kf.co[1] for kf in fc.keyframe_points]
                    min_val = min(values)
                    max_val = max(values)
                    print(f"  {component}: {num_keys} keyframes | Rango: [{min_val:7.3f}, {max_val:7.3f}]")
    
    # Comparar con JSON original
    print(f"\n{'='*80}")
    print(f"📊 Comparando con JSON original (Frame 1):")
    print(f"{'='*80}")
    
    json_path = r"C:\Users\andre\OneDrive\Documentos\tesis\output\hand_analysis\miercoles_hands.json"
    with open(json_path, 'r') as f:
        hand_data = json.load(f)
    
    frame_0 = hand_data['frames'][0]
    if 'hands' in frame_0 and len(frame_0['hands']) > 0:
        hand_info = frame_0['hands'][0]
        
        print("\n🖐️ JSON - Cuaterniones originales (Frame 0):")
        
        finger_names = ['thumb', 'index', 'middle']
        for finger in finger_names:
            print(f"\n  {finger.upper()}:")
            for seg_idx in range(4):
                quat_data = hand_info['fingers'][finger][seg_idx]
                # JSON: [qx, qy, qz, qw]
                magnitude = (quat_data[0]**2 + quat_data[1]**2 + quat_data[2]**2 + quat_data[3]**2)**0.5
                print(f"    Seg {seg_idx}: [{quat_data[0]:7.3f}, {quat_data[1]:7.3f}, {quat_data[2]:7.3f}, {quat_data[3]:7.3f}] | Mag: {magnitude:.3f}")
    
    print(f"\n{'='*80}")
    print(f"✅ VERIFICACIÓN COMPLETA")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    verificar_dedos()
