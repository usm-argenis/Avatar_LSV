"""
PASO 2 MEJORADO - Con normalización y estabilización de movimientos
Aplica rotaciones a los huesos de las manos usando el método vectorial
con suavizado y control de movimientos excesivos
"""
import bpy
import json
import mathutils
import math

# ===============================================
# CONFIGURACIÓN
# ===============================================
GLB_INPUT = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_mal.glb"
GLB_OUTPUT = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_mal_optimized.glb"
LANDMARKS_JSON = "temp_hands_data.json"

# Factor de suavizado (0.0 = sin suavizado, 1.0 = suavizado máximo)
SMOOTHING_FACTOR = 0.3

# Factor de escala para limitar movimientos excesivos
MAX_ROTATION_ANGLE = math.radians(30)  # 30 grados máximo por frame

print("\n" + "="*70)
print("# OPTIMIZACIÓN DE MANOS - MÉTODO MEJORADO")
print("="*70)

# ===============================================
# CARGAR LANDMARKS
# ===============================================
with open(LANDMARKS_JSON, 'r') as f:
    data = json.load(f)

landmarks = data['frames']
fps = data['fps']

print(f"✅ Landmarks cargados: {len(landmarks)} frames")

# ===============================================
# IMPORTAR GLB
# ===============================================
print("\n" + "="*70)
print("🔽 IMPORTANDO GLB")
print("="*70)

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

bpy.ops.import_scene.gltf(filepath=GLB_INPUT)

# Encontrar la armature
armature = None
for obj in bpy.context.scene.objects:
    if obj.type == 'ARMATURE':
        armature = obj
        break

if not armature:
    print("❌ ERROR: No se encontró armature en el GLB")
    exit()

print(f"✅ Armature: {armature.name}")

# ===============================================
# FUNCIÓN DE SUAVIZADO
# ===============================================
def smooth_rotation(current_quat, target_quat, factor):
    """Interpola suavemente entre la rotación actual y la objetivo"""
    return current_quat.slerp(target_quat, 1.0 - factor)

def limit_rotation_change(new_quat, old_quat, max_angle):
    """Limita el cambio de rotación máximo por frame"""
    angle = new_quat.rotation_difference(old_quat).angle
    if angle > max_angle:
        # Limitar el ángulo de cambio
        limited_quat = old_quat.slerp(new_quat, max_angle / angle)
        return limited_quat
    return new_quat

# ===============================================
# MAPEO DE LANDMARKS A HUESOS
# ===============================================
FINGER_MAPPING = {
    'left_hand': {
        'LeftHandThumb': [0, 1, 2, 3, 4],
        'LeftHandIndex': [0, 5, 6, 7, 8],
        'LeftHandMiddle': [0, 9, 10, 11, 12],
        'LeftHandRing': [0, 13, 14, 15, 16],
        'LeftHandPinky': [0, 17, 18, 19, 20]
    },
    'right_hand': {
        'RightHandThumb': [0, 1, 2, 3, 4],
        'RightHandIndex': [0, 5, 6, 7, 8],
        'RightHandMiddle': [0, 9, 10, 11, 12],
        'RightHandRing': [0, 13, 14, 15, 16],
        'RightHandPinky': [0, 17, 18, 19, 20]
    }
}

def calculate_bone_rotation(start_pos, end_pos, bone):
    """Calcula la rotación del hueso basada en la dirección del vector entre landmarks"""
    # Vector objetivo (de landmark inicial a final)
    target_vec = mathutils.Vector((
        end_pos['x'] - start_pos['x'],
        end_pos['y'] - start_pos['y'],
        end_pos['z'] - start_pos['z']
    ))
    
    if target_vec.length < 0.0001:
        return bone.rotation_quaternion.copy()
    
    target_vec.normalize()
    
    # Vector del hueso en su estado original (pose rest)
    bone_vec = (bone.bone.tail_local - bone.bone.head_local).normalized()
    
    # Calcular la rotación necesaria
    rotation_quat = bone_vec.rotation_difference(target_vec)
    
    return rotation_quat

# ===============================================
# APLICAR LANDMARKS A HUESOS
# ===============================================
print("\n" + "="*70)
print("🖐️ APLICANDO LANDMARKS A HUESOS CON OPTIMIZACIÓN")
print("="*70)

bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode='POSE')

# Diccionario para almacenar rotaciones previas
previous_rotations = {}

modified_bones = set()

for frame_idx, frame_data in enumerate(landmarks):
    frame_num = frame_idx + 1
    bpy.context.scene.frame_set(frame_num)
    
    for hand_key, finger_dict in FINGER_MAPPING.items():
        hand_landmarks = frame_data.get(hand_key)
        if not hand_landmarks:
            continue
        
        for finger_base, landmark_indices in finger_dict.items():
            for segment in range(1, 5):  # 4 segmentos por dedo
                bone_name = f"{finger_base}{segment}"
                
                if bone_name not in armature.pose.bones:
                    continue
                
                bone = armature.pose.bones[bone_name]
                
                # Obtener los landmarks para este segmento
                start_idx = landmark_indices[segment - 1]
                end_idx = landmark_indices[segment]
                
                start_pos = hand_landmarks[start_idx]
                end_pos = hand_landmarks[end_idx]
                
                # Calcular rotación objetivo
                target_rotation = calculate_bone_rotation(start_pos, end_pos, bone)
                
                # Aplicar suavizado si hay rotación previa
                bone_key = f"{hand_key}_{bone_name}"
                if bone_key in previous_rotations:
                    old_rotation = previous_rotations[bone_key]
                    
                    # Limitar cambio excesivo
                    target_rotation = limit_rotation_change(target_rotation, old_rotation, MAX_ROTATION_ANGLE)
                    
                    # Suavizar
                    target_rotation = smooth_rotation(old_rotation, target_rotation, SMOOTHING_FACTOR)
                
                # Aplicar rotación
                bone.rotation_quaternion = target_rotation
                bone.keyframe_insert(data_path="rotation_quaternion", frame=frame_num)
                
                # Guardar para el siguiente frame
                previous_rotations[bone_key] = target_rotation.copy()
                
                modified_bones.add(bone_name)
    
    if (frame_num) % 10 == 0:
        print(f"   ✔️ Frame {frame_num}/{len(landmarks)}")

print(f"\n✅ Huesos modificados: {len(modified_bones)}")

# ===============================================
# EXPORTAR GLB
# ===============================================
print("\n" + "="*70)
print("💾 EXPORTANDO GLB")
print("="*70)

bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.export_scene.gltf(
    filepath=GLB_OUTPUT,
    export_format='GLB',
    export_animations=True,
    export_frame_range=True,
    export_frame_step=1,
    export_force_sampling=True,
    export_current_frame=False
)

import os
file_size = os.path.getsize(GLB_OUTPUT) / (1024 * 1024)
print(f"✅ GLB exportado: {os.path.basename(GLB_OUTPUT)}")
print(f"🎯 Tamaño: {file_size:.2f} MB")

print("\n" + "="*70)
print("✅ OPTIMIZACIÓN COMPLETADA")
print("="*70)
print(f"📁 Archivo: {GLB_OUTPUT}")
