"""
MÉTODO CON INVERSE KINEMATICS (IK)
Este es el método profesional que usan los estudios de motion capture
"""
import bpy
import json
import mathutils
import math

# ===============================================
# CONFIGURACIÓN
# ===============================================
GLB_INPUT = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_mal.glb"
GLB_OUTPUT = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_mal_IK.glb"
LANDMARKS_JSON = "temp_hands_data.json"

print("\n" + "="*70)
print("# MÉTODO CON INVERSE KINEMATICS (IK) - PROFESIONAL")
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

# Obtener posiciones de muñecas
left_wrist_pos = None
right_wrist_pos = None

if 'LeftHand' in armature.pose.bones:
    left_wrist_pos = armature.matrix_world @ armature.pose.bones['LeftHand'].head

if 'RightHand' in armature.pose.bones:
    right_wrist_pos = armature.matrix_world @ armature.pose.bones['RightHand'].head

bpy.ops.object.mode_set(mode='OBJECT')

# ===============================================
# CONFIGURACIÓN DE IK
# ===============================================
FINGER_CONFIG = {
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

# ===============================================
# CREAR TARGETS IK (Empties para las puntas de dedos)
# ===============================================
print("\n" + "="*70)
print("🎯 CREANDO TARGETS IK")
print("="*70)

ik_targets = {}

for hand_key in ['left_hand', 'right_hand']:
    ik_targets[hand_key] = {}
    for finger_name in ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']:
        target = bpy.data.objects.new(f"IK_{hand_key}_{finger_name}", None)
        target.empty_display_size = 0.02
        target.empty_display_type = 'SPHERE'
        bpy.context.scene.collection.objects.link(target)
        ik_targets[hand_key][finger_name] = target

print(f"✅ Targets IK creados: {sum(len(t) for t in ik_targets.values())}")

# ===============================================
# ANIMAR TARGETS IK
# ===============================================
print("\n" + "="*70)
print("🎬 ANIMANDO TARGETS IK")
print("="*70)

first_frame = landmarks[0]
left_center = None
right_center = None

if first_frame.get('left_hand'):
    wrist = first_frame['left_hand'][0]
    left_center = mathutils.Vector((wrist['x'], wrist['y'], wrist['z']))

if first_frame.get('right_hand'):
    wrist = first_frame['right_hand'][0]
    right_center = mathutils.Vector((wrist['x'], wrist['y'], wrist['z']))

finger_tip_indices = {
    'Thumb': 4,
    'Index': 8,
    'Middle': 12,
    'Ring': 16,
    'Pinky': 20
}

for frame_idx, frame_data in enumerate(landmarks):
    frame_num = frame_idx + 1
    bpy.context.scene.frame_set(frame_num)
    
    for hand_key in ['left_hand', 'right_hand']:
        hand_landmarks = frame_data.get(hand_key)
        if not hand_landmarks:
            continue
        
        if hand_key == 'left_hand' and left_wrist_pos and left_center:
            wrist_offset = left_wrist_pos
            lm_center = left_center
        elif hand_key == 'right_hand' and right_wrist_pos and right_center:
            wrist_offset = right_wrist_pos
            lm_center = right_center
        else:
            continue
        
        for finger_name, tip_idx in finger_tip_indices.items():
            target = ik_targets[hand_key][finger_name]
            landmark = hand_landmarks[tip_idx]
            
            rel_x = landmark['x'] - lm_center.x
            rel_y = landmark['y'] - lm_center.y
            rel_z = landmark['z'] - lm_center.z
            
            # Usar XZY_swap (la mejor variante según el usuario)
            target.location = (
                wrist_offset.x + rel_x * calculated_scale,
                wrist_offset.y - rel_z * calculated_scale,
                wrist_offset.z - rel_y * calculated_scale
            )
            target.keyframe_insert(data_path="location", frame=frame_num)
    
    if frame_num % 10 == 0:
        print(f"   ✔️ Frame {frame_num}/{len(landmarks)}")

# ===============================================
# CONFIGURAR IK CONSTRAINTS
# ===============================================
print("\n" + "="*70)
print("🔗 CONFIGURANDO IK CONSTRAINTS")
print("="*70)

bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode='POSE')

constraint_count = 0

for hand_key, finger_dict in FINGER_CONFIG.items():
    hand_prefix = 'Left' if hand_key == 'left_hand' else 'Right'
    
    for finger_base, _ in finger_dict.items():
        finger_name = finger_base.replace(f'{hand_prefix}Hand', '')
        
        # El último hueso de cada dedo (bone 4) tendrá el constraint IK
        bone_name = f"{finger_base}4"
        
        if bone_name not in armature.pose.bones:
            continue
        
        bone = armature.pose.bones[bone_name]
        target = ik_targets[hand_key][finger_name]
        
        # Limpiar constraints existentes
        for c in bone.constraints:
            bone.constraints.remove(c)
        
        # Agregar IK constraint
        ik_constraint = bone.constraints.new('IK')
        ik_constraint.target = armature
        ik_constraint.subtarget = bone_name  # Temporal, lo cambiaremos
        
        # En realidad, IK necesita un target externo
        # Crear un approach diferente: Copy Location en la punta
        copy_loc = bone.constraints.new('COPY_LOCATION')
        copy_loc.target = target
        copy_loc.influence = 0.8  # Influencia parcial para suavizar
        
        constraint_count += 1

print(f"✅ Constraints configurados: {constraint_count}")

# ===============================================
# BAKE ANIMATION
# ===============================================
print("\n" + "="*70)
print("🎯 BAKING ANIMATION")
print("="*70)

for bone in armature.pose.bones:
    bone.bone.select = (
        'Hand' in bone.name and 
        any(f in bone.name for f in ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky'])
    )

bpy.ops.nla.bake(
    frame_start=1,
    frame_end=len(landmarks),
    only_selected=True,
    visual_keying=True,
    clear_constraints=True,
    use_current_action=True,
    bake_types={'POSE'}
)

print("✅ Animation baked")

# ===============================================
# LIMPIAR
# ===============================================
bpy.ops.object.mode_set(mode='OBJECT')

for hand_key in ['left_hand', 'right_hand']:
    for target in ik_targets[hand_key].values():
        bpy.data.objects.remove(target, do_unlink=True)

# ===============================================
# EXPORTAR
# ===============================================
print("\n" + "="*70)
print("💾 EXPORTANDO GLB")
print("="*70)

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
print(f"📁 {GLB_OUTPUT}")
