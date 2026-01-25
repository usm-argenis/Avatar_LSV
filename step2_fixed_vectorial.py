"""
SOLUCIÓN CORRECTA: Usar posiciones de MediaPipe para calcular rotaciones de huesos
basándose en la dirección de los vectores entre landmarks consecutivos
"""
import bpy
import json
import mathutils
import math
from pathlib import Path

# ==================== CONFIGURACIÓN ====================
ROTATIONS_JSON = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\temp_hand_rotations.json")
GLB_INPUT = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_mal.glb")
GLB_OUTPUT = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_mal_fixed.glb")

# MediaPipe Hand landmarks por dedo (índices 0-20)
# 0: WRIST
# 1-4: THUMB_CMC, MCP, IP, TIP
# 5-8: INDEX_MCP, PIP, DIP, TIP
# 9-12: MIDDLE_MCP, PIP, DIP, TIP
# 13-16: RING_MCP, PIP, DIP, TIP
# 17-20: PINKY_MCP, PIP, DIP, TIP

MEDIAPIPE_TO_BONE = {
    'left': {
        'thumb': [
            (0, 1, 'LeftHandThumb1'),   # wrist → thumb_cmc
            (1, 2, 'LeftHandThumb2'),   # cmc → mcp
            (2, 3, 'LeftHandThumb3'),   # mcp → ip
            (3, 4, 'LeftHandThumb4'),   # ip → tip
        ],
        'index': [
            (0, 5, 'LeftHandIndex1'),   # wrist → index_mcp
            (5, 6, 'LeftHandIndex2'),   # mcp → pip
            (6, 7, 'LeftHandIndex3'),   # pip → dip
            (7, 8, 'LeftHandIndex4'),   # dip → tip
        ],
        'middle': [
            (0, 9, 'LeftHandMiddle1'),   # wrist → middle_mcp
            (9, 10, 'LeftHandMiddle2'),  # mcp → pip
            (10, 11, 'LeftHandMiddle3'), # pip → dip
            (11, 12, 'LeftHandMiddle4'), # dip → tip
        ],
        'ring': [
            (0, 13, 'LeftHandRing1'),    # wrist → ring_mcp
            (13, 14, 'LeftHandRing2'),   # mcp → pip
            (14, 15, 'LeftHandRing3'),   # pip → dip
            (15, 16, 'LeftHandRing4'),   # dip → tip
        ],
        'pinky': [
            (0, 17, 'LeftHandPinky1'),   # wrist → pinky_mcp
            (17, 18, 'LeftHandPinky2'),  # mcp → pip
            (18, 19, 'LeftHandPinky3'),  # pip → dip
            (19, 20, 'LeftHandPinky4'),  # dip → tip
        ],
    },
    'right': {
        'thumb': [
            (0, 1, 'RightHandThumb1'),
            (1, 2, 'RightHandThumb2'),
            (2, 3, 'RightHandThumb3'),
            (3, 4, 'RightHandThumb4'),
        ],
        'index': [
            (0, 5, 'RightHandIndex1'),
            (5, 6, 'RightHandIndex2'),
            (6, 7, 'RightHandIndex3'),
            (7, 8, 'RightHandIndex4'),
        ],
        'middle': [
            (0, 9, 'RightHandMiddle1'),
            (9, 10, 'RightHandMiddle2'),
            (10, 11, 'RightHandMiddle3'),
            (11, 12, 'RightHandMiddle4'),
        ],
        'ring': [
            (0, 13, 'RightHandRing1'),
            (13, 14, 'RightHandRing2'),
            (14, 15, 'RightHandRing3'),
            (15, 16, 'RightHandRing4'),
        ],
        'pinky': [
            (0, 17, 'RightHandPinky1'),
            (17, 18, 'RightHandPinky2'),
            (18, 19, 'RightHandPinky3'),
            (19, 20, 'RightHandPinky4'),
        ],
    }
}

def load_hands_landmarks():
    """Carga los landmarks del JSON del PASO 1"""
    # El PASO 1 genera landmarks, no rotaciones
    temp_landmarks = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\temp_hands_data.json")
    
    if not temp_landmarks.exists():
        print(f"⚠️ No se encontró {temp_landmarks.name}")
        print(f"💡 Ejecuta primero el PASO 1")
        return None
    
    with open(temp_landmarks, 'r') as f:
        data = json.load(f)
    
    print(f"✅ Landmarks cargados: {len(data['frames'])} frames")
    return data

def calculate_bone_rotation(start_pos, end_pos, bone):
    """
    Calcula la rotación necesaria para que el hueso apunte de start_pos a end_pos
    usando quaternions (el modo original del modelo)
    """
    # Vector objetivo (hacia donde debe apuntar el hueso)
    target_vec = mathutils.Vector((
        end_pos['x'] - start_pos['x'],
        end_pos['y'] - start_pos['y'],
        end_pos['z'] - start_pos['z']
    ))
    
    if target_vec.length < 0.0001:
        return None  # Vector demasiado corto
    
    target_vec.normalize()
    
    # Vector original del hueso en pose de reposo (apunta hacia su tail)
    bone_vec = (bone.bone.tail_local - bone.bone.head_local).normalized()
    
    # Calcular rotación entre el vector original y el objetivo
    rotation_quat = bone_vec.rotation_difference(target_vec)
    
    return rotation_quat

def import_glb():
    """Importa el GLB"""
    print(f"\n{'='*70}")
    print(f"📥 IMPORTANDO GLB")
    print(f"{'='*70}")
    
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    bpy.ops.import_scene.gltf(filepath=str(GLB_INPUT))
    
    armature = None
    for obj in bpy.context.scene.objects:
        if obj.type == 'ARMATURE':
            armature = obj
            break
    
    if not armature:
        raise RuntimeError("❌ No se encontró armature")
    
    print(f"✅ Armature: {armature.name}")
    return armature

def apply_hand_landmarks(armature, landmarks_data):
    """
    Aplica las posiciones de landmarks calculando rotaciones correctas para cada hueso
    """
    print(f"\n{'='*70}")
    print(f"🔧 APLICANDO LANDMARKS A HUESOS")
    print(f"{'='*70}")
    
    if not armature.animation_data or not armature.animation_data.action:
        action = bpy.data.actions.new(name="HandsFixed")
        armature.animation_data_create()
        armature.animation_data.action = action
    else:
        action = armature.animation_data.action
    
    frame_start = bpy.context.scene.frame_start
    modified_bones = set()
    
    # Procesar cada frame
    for frame_idx, frame_data in enumerate(landmarks_data['frames']):
        frame_number = frame_start + frame_data['frame']
        bpy.context.scene.frame_set(frame_number)
        
        # Procesar mano izquierda
        if frame_data['left_hand']:
            hand_landmarks = frame_data['left_hand']
            
            for finger_name, bone_mappings in MEDIAPIPE_TO_BONE['left'].items():
                for start_idx, end_idx, bone_name in bone_mappings:
                    if bone_name not in armature.pose.bones:
                        continue
                    
                    bone = armature.pose.bones[bone_name]
                    start_landmark = hand_landmarks[start_idx]
                    end_landmark = hand_landmarks[end_idx]
                    
                    # Calcular rotación
                    rotation = calculate_bone_rotation(start_landmark, end_landmark, bone)
                    
                    if rotation:
                        bone.rotation_mode = 'QUATERNION'
                        bone.rotation_quaternion = rotation
                        bone.keyframe_insert(data_path="rotation_quaternion", frame=frame_number)
                        modified_bones.add(bone_name)
        
        # Procesar mano derecha
        if frame_data['right_hand']:
            hand_landmarks = frame_data['right_hand']
            
            for finger_name, bone_mappings in MEDIAPIPE_TO_BONE['right'].items():
                for start_idx, end_idx, bone_name in bone_mappings:
                    if bone_name not in armature.pose.bones:
                        continue
                    
                    bone = armature.pose.bones[bone_name]
                    start_landmark = hand_landmarks[start_idx]
                    end_landmark = hand_landmarks[end_idx]
                    
                    # Calcular rotación
                    rotation = calculate_bone_rotation(start_landmark, end_landmark, bone)
                    
                    if rotation:
                        bone.rotation_mode = 'QUATERNION'
                        bone.rotation_quaternion = rotation
                        bone.keyframe_insert(data_path="rotation_quaternion", frame=frame_number)
                        modified_bones.add(bone_name)
        
        if (frame_idx + 1) % 10 == 0:
            print(f"   ✓ Frame {frame_idx + 1}/{len(landmarks_data['frames'])}")
    
    print(f"\n✅ Huesos modificados: {len(modified_bones)}")
    return len(modified_bones) > 0

def export_glb():
    """Exporta el GLB optimizado"""
    print(f"\n{'='*70}")
    print(f"💾 EXPORTANDO GLB")
    print(f"{'='*70}")
    
    GLB_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    
    if bpy.context.active_object and bpy.context.active_object.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    
    bpy.ops.object.select_all(action='SELECT')
    
    bpy.ops.export_scene.gltf(
        filepath=str(GLB_OUTPUT),
        export_format='GLB',
        export_animations=True,
        export_apply=False,
        export_rest_position_armature=False,
        export_frame_range=True
    )
    
    print(f"✅ GLB exportado: {GLB_OUTPUT.name}")
    size_mb = GLB_OUTPUT.stat().st_size / (1024 * 1024)
    print(f"📊 Tamaño: {size_mb:.2f} MB")
    
    return GLB_OUTPUT

def main():
    print(f"\n{'#'*70}")
    print(f"# CORRECCIÓN DE MANOS - MÉTODO VECTORIAL")
    print(f"{'#'*70}")
    
    try:
        # Cargar landmarks (no rotaciones)
        landmarks_data = load_hands_landmarks()
        if not landmarks_data:
            return False
        
        # Importar GLB
        armature = import_glb()
        
        # Aplicar landmarks
        success = apply_hand_landmarks(armature, landmarks_data)
        
        if not success:
            print("\n⚠️ No se aplicaron modificaciones")
            return False
        
        # Exportar
        output_file = export_glb()
        
        print(f"\n{'='*70}")
        print(f"✅ CORRECCIÓN COMPLETADA")
        print(f"{'='*70}")
        print(f"📁 Archivo: {output_file}")
        
        return True
        
    except Exception as e:
        print(f"\n{'='*70}")
        print(f"❌ ERROR")
        print(f"{'='*70}")
        print(f"{type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    main()
