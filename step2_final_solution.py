"""
SOLUCIÓN DEFINITIVA - Cálculo correcto de rotaciones con jerarquía
Calcula la rotación de cada hueso basándose en la dirección entre landmarks
y respetando el espacio local y la jerarquía de huesos
"""
import bpy
import json
import mathutils
import math

# ===============================================
# CONFIGURACIÓN
# ===============================================
GLB_INPUT = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_mal.glb"
GLB_OUTPUT = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_FINAL.glb"
LANDMARKS_JSON = "temp_hands_data.json"

print("\n" + "="*70)
print("# SOLUCIÓN DEFINITIVA - ROTACIONES CON JERARQUÍA")
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

armature = None
for obj in bpy.context.scene.objects:
    if obj.type == 'ARMATURE':
        armature = obj
        break

if not armature:
    print("❌ ERROR: No se encontró armature")
    exit()

print(f"✅ Armature: {armature.name}")

# ===============================================
# CALCULAR ESCALA Y OFFSETS
# ===============================================
bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode='POSE')

left_wrist = armature.pose.bones.get('LeftHand')
left_middle1 = armature.pose.bones.get('LeftHandMiddle1')

if left_wrist and left_middle1:
    wrist_pos = armature.matrix_world @ left_wrist.head
    middle_pos = armature.matrix_world @ left_middle1.head
    model_hand_size = (wrist_pos - middle_pos).length
    
    mediapipe_distances = []
    for frame_data in landmarks[:10]:
        if frame_data.get('left_hand'):
            wrist_lm = frame_data['left_hand'][0]
            middle_lm = frame_data['left_hand'][9]
            dist = math.sqrt(
                (wrist_lm['x'] - middle_lm['x'])**2 +
                (wrist_lm['y'] - middle_lm['y'])**2 +
                (wrist_lm['z'] - middle_lm['z'])**2
            )
            mediapipe_distances.append(dist)
    
    if mediapipe_distances:
        avg_mediapipe_dist = sum(mediapipe_distances) / len(mediapipe_distances)
        calculated_scale = model_hand_size / avg_mediapipe_dist
    else:
        calculated_scale = 1.0
else:
    calculated_scale = 1.0

print(f"📏 Escala calculada: {calculated_scale:.4f}")

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

def landmark_to_blender_coords(lm, center, scale):
    """Convierte coordenadas de MediaPipe a Blender (XZY_swap)"""
    rel_x = lm['x'] - center.x
    rel_y = lm['y'] - center.y
    rel_z = lm['z'] - center.z
    
    return mathutils.Vector((
        rel_x * scale,
        -rel_z * scale,  # Z de MediaPipe -> Y de Blender (invertido)
        -rel_y * scale   # Y de MediaPipe -> Z de Blender (invertido)
    ))

def calculate_bone_rotation_from_direction(bone, target_direction):
    """
    Calcula la rotación necesaria para que un hueso apunte en una dirección específica
    considerando su espacio local y jerarquía
    """
    # Obtener la dirección original del hueso en espacio local
    bone_dir_local = (bone.bone.tail_local - bone.bone.head_local).normalized()
    
    # Normalizar la dirección objetivo
    target_dir_normalized = target_direction.normalized()
    
    # Calcular la rotación necesaria (quaternion)
    rotation_quat = bone_dir_local.rotation_difference(target_dir_normalized)
    
    # Si tiene padre, convertir a espacio local
    if bone.parent:
        # Obtener la rotación del padre
        parent_matrix = bone.parent.matrix.to_3x3()
        # Convertir el quaternion a matriz
        rot_matrix = rotation_quat.to_matrix()
        # Aplicar la transformación inversa del padre
        local_rot_matrix = parent_matrix.inverted() @ rot_matrix
        # Convertir de vuelta a quaternion
        rotation_quat = local_rot_matrix.to_quaternion()
    
    return rotation_quat

# ===============================================
# APLICAR ROTACIONES FRAME POR FRAME
# ===============================================
print("\n" + "="*70)
print("🎬 APLICANDO ROTACIONES CON JERARQUÍA")
print("="*70)

# Obtener centros iniciales
first_frame = landmarks[0]
centers = {}

for hand_key in ['left_hand', 'right_hand']:
    if first_frame.get(hand_key):
        wrist = first_frame[hand_key][0]
        centers[hand_key] = mathutils.Vector((wrist['x'], wrist['y'], wrist['z']))
    else:
        centers[hand_key] = mathutils.Vector((0, 0, 0))

modified_bones = set()

for frame_idx, frame_data in enumerate(landmarks):
    frame_num = frame_idx + 1
    bpy.context.scene.frame_set(frame_num)
    
    for hand_key, finger_dict in FINGER_MAPPING.items():
        hand_landmarks = frame_data.get(hand_key)
        if not hand_landmarks:
            continue
        
        center = centers[hand_key]
        
        for finger_base, landmark_indices in finger_dict.items():
            # Procesar cada segmento del dedo
            for segment in range(1, 5):  # 4 segmentos por dedo
                bone_name = f"{finger_base}{segment}"
                
                if bone_name not in armature.pose.bones:
                    continue
                
                bone = armature.pose.bones[bone_name]
                
                # Obtener landmarks para este segmento
                start_idx = landmark_indices[segment - 1]
                end_idx = landmark_indices[segment]
                
                start_lm = hand_landmarks[start_idx]
                end_lm = hand_landmarks[end_idx]
                
                # Convertir a coordenadas Blender
                start_pos = landmark_to_blender_coords(start_lm, center, calculated_scale)
                end_pos = landmark_to_blender_coords(end_lm, center, calculated_scale)
                
                # Calcular dirección objetivo
                target_direction = (end_pos - start_pos).normalized()
                
                # Calcular rotación necesaria
                rotation_quat = calculate_bone_rotation_from_direction(bone, target_direction)
                
                # Aplicar rotación
                bone.rotation_quaternion = rotation_quat
                bone.keyframe_insert(data_path="rotation_quaternion", frame=frame_num)
                
                modified_bones.add(bone_name)
    
    if frame_num % 10 == 0:
        print(f"   ✔️ Frame {frame_num}/{len(landmarks)}")

print(f"\n✅ Huesos modificados: {len(modified_bones)}")

# ===============================================
# EXPORTAR
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
print("✅ PROCESO COMPLETADO")
print("="*70)
print(f"📁 Archivo: {GLB_OUTPUT}")
print(f"📏 Escala usada: {calculated_scale:.4f}")
print(f"🔄 Transform: XZY_swap (la mejor variante)")
print(f"🦴 Huesos modificados: {len(modified_bones)}")
