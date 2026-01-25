"""
OPTIMIZACIÓN INTELIGENTE - Mejora la animación original existente
NO reemplaza toda la animación, solo corrige/optimiza los dedos
usando MediaPipe como referencia para hacerlos más precisos
"""
import bpy
import json
import mathutils
import math

# ===============================================
# CONFIGURACIÓN
# ===============================================
GLB_INPUT = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_mal.glb"
GLB_OUTPUT = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_OPTIMIZED.glb"
LANDMARKS_JSON = "temp_hands_data.json"

# Factor de mezcla: 0.0 = 100% original, 1.0 = 100% MediaPipe
BLEND_FACTOR = 0.7  # 70% MediaPipe, 30% original

print("\n" + "="*70)
print("# OPTIMIZACIÓN INTELIGENTE - MEJORA ANIMACIÓN ORIGINAL")
print("="*70)
print(f"🎚️  Factor de mezcla: {BLEND_FACTOR*100:.0f}% MediaPipe + {(1-BLEND_FACTOR)*100:.0f}% Original")

# ===============================================
# CARGAR LANDMARKS
# ===============================================
with open(LANDMARKS_JSON, 'r') as f:
    data = json.load(f)

landmarks = data['frames']
fps = data['fps']

print(f"✅ Landmarks cargados: {len(landmarks)} frames")

# ===============================================
# IMPORTAR GLB CON ANIMACIÓN ORIGINAL
# ===============================================
print("\n" + "="*70)
print("🔽 IMPORTANDO GLB CON ANIMACIÓN ORIGINAL")
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

# Verificar que hay animación
if armature.animation_data and armature.animation_data.action:
    print(f"✅ Animación original detectada: {armature.animation_data.action.name}")
    original_frames = int(armature.animation_data.action.frame_range[1])
    print(f"   Frames en animación original: {original_frames}")
else:
    print("⚠️  No se detectó animación original en el GLB")
    original_frames = len(landmarks)

# ===============================================
# CALCULAR ESCALA
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
# EXTRAER ROTACIONES ORIGINALES
# ===============================================
print("\n" + "="*70)
print("📋 EXTRAYENDO ROTACIONES ORIGINALES")
print("="*70)

original_rotations = {}

# Lista de huesos de dedos
hand_bones = []
for hand in ['LeftHand', 'RightHand']:
    for finger in ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']:
        for segment in range(1, 5):
            bone_name = f"{hand}{finger}{segment}"
            if bone_name in armature.pose.bones:
                hand_bones.append(bone_name)

print(f"   Huesos de dedos encontrados: {len(hand_bones)}")

# Extraer rotaciones originales frame por frame
for frame_num in range(1, min(original_frames, len(landmarks)) + 1):
    bpy.context.scene.frame_set(frame_num)
    original_rotations[frame_num] = {}
    
    for bone_name in hand_bones:
        bone = armature.pose.bones[bone_name]
        original_rotations[frame_num][bone_name] = bone.rotation_quaternion.copy()

print(f"✅ Rotaciones originales extraídas: {len(original_rotations)} frames")

# ===============================================
# MAPEO DE LANDMARKS
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
        -rel_z * scale,
        -rel_y * scale
    ))

def calculate_rotation_from_landmarks(bone, start_lm, end_lm, center, scale):
    """Calcula rotación objetivo desde landmarks"""
    start_pos = landmark_to_blender_coords(start_lm, center, scale)
    end_pos = landmark_to_blender_coords(end_lm, center, scale)
    
    target_direction = (end_pos - start_pos).normalized()
    bone_dir_local = (bone.bone.tail_local - bone.bone.head_local).normalized()
    
    rotation_quat = bone_dir_local.rotation_difference(target_direction)
    
    if bone.parent:
        parent_matrix = bone.parent.matrix.to_3x3()
        rot_matrix = rotation_quat.to_matrix()
        local_rot_matrix = parent_matrix.inverted() @ rot_matrix
        rotation_quat = local_rot_matrix.to_quaternion()
    
    return rotation_quat

# ===============================================
# APLICAR OPTIMIZACIÓN (BLEND)
# ===============================================
print("\n" + "="*70)
print("🎨 APLICANDO OPTIMIZACIÓN CON BLEND")
print("="*70)

first_frame = landmarks[0]
centers = {}

for hand_key in ['left_hand', 'right_hand']:
    if first_frame.get(hand_key):
        wrist = first_frame[hand_key][0]
        centers[hand_key] = mathutils.Vector((wrist['x'], wrist['y'], wrist['z']))
    else:
        centers[hand_key] = mathutils.Vector((0, 0, 0))

optimized_bones = set()

for frame_idx, frame_data in enumerate(landmarks):
    frame_num = frame_idx + 1
    
    if frame_num > original_frames:
        break
    
    bpy.context.scene.frame_set(frame_num)
    
    for hand_key, finger_dict in FINGER_MAPPING.items():
        hand_landmarks = frame_data.get(hand_key)
        if not hand_landmarks:
            continue
        
        center = centers[hand_key]
        
        for finger_base, landmark_indices in finger_dict.items():
            for segment in range(1, 5):
                bone_name = f"{finger_base}{segment}"
                
                if bone_name not in armature.pose.bones:
                    continue
                
                bone = armature.pose.bones[bone_name]
                
                # Obtener rotación original
                original_quat = original_rotations[frame_num].get(bone_name)
                if not original_quat:
                    continue
                
                # Calcular rotación desde MediaPipe
                start_idx = landmark_indices[segment - 1]
                end_idx = landmark_indices[segment]
                
                start_lm = hand_landmarks[start_idx]
                end_lm = hand_landmarks[end_idx]
                
                mediapipe_quat = calculate_rotation_from_landmarks(
                    bone, start_lm, end_lm, center, calculated_scale
                )
                
                # BLEND entre original y MediaPipe
                # SLERP = Spherical Linear Interpolation (perfecto para quaterniones)
                blended_quat = original_quat.slerp(mediapipe_quat, BLEND_FACTOR)
                
                # Aplicar rotación blended
                bone.rotation_quaternion = blended_quat
                bone.keyframe_insert(data_path="rotation_quaternion", frame=frame_num)
                
                optimized_bones.add(bone_name)
    
    if frame_num % 10 == 0:
        print(f"   ✔️ Frame {frame_num}/{len(landmarks)}")

print(f"\n✅ Huesos optimizados: {len(optimized_bones)}")

# ===============================================
# EXPORTAR
# ===============================================
print("\n" + "="*70)
print("💾 EXPORTANDO GLB OPTIMIZADO")
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
print(f"🎚️  Blend usado: {BLEND_FACTOR*100:.0f}% MediaPipe + {(1-BLEND_FACTOR)*100:.0f}% Original")
print(f"🦴 Huesos optimizados: {len(optimized_bones)}")
print(f"📏 Escala: {calculated_scale:.4f}")
print("\n💡 Si el resultado no es perfecto, ajusta BLEND_FACTOR en el script:")
print(f"   - Más cercano a original: BLEND_FACTOR = 0.3")
print(f"   - Equilibrado (actual): BLEND_FACTOR = {BLEND_FACTOR}")
print(f"   - Más cercano a MediaPipe: BLEND_FACTOR = 0.9")
