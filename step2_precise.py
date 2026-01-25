"""
MÉTODO CONSTRAINTS MEJORADO - Con cálculo automático de escala y transformación correcta
"""
import bpy
import json
import mathutils
import math

# ===============================================
# CONFIGURACIÓN
# ===============================================
GLB_INPUT = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_mal.glb"
GLB_OUTPUT = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_mal_precise.glb"
LANDMARKS_JSON = "temp_hands_data.json"

print("\n" + "="*70)
print("# CONSTRAINTS MEJORADO - CÁLCULO AUTOMÁTICO DE ESCALA")
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
# CALCULAR ESCALA AUTOMÁTICAMENTE
# ===============================================
print("\n" + "="*70)
print("📏 CALCULANDO ESCALA AUTOMÁTICA")
print("="*70)

bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode='POSE')

# Encontrar huesos de referencia para calcular escala
left_wrist = armature.pose.bones.get('LeftHand')
left_middle1 = armature.pose.bones.get('LeftHandMiddle1')

if left_wrist and left_middle1:
    # Distancia en el modelo 3D
    wrist_pos = armature.matrix_world @ left_wrist.head
    middle_pos = armature.matrix_world @ left_middle1.head
    model_hand_size = (wrist_pos - middle_pos).length
    
    print(f"📐 Tamaño de mano en modelo: {model_hand_size:.4f}")
    
    # Distancia promedio en landmarks de MediaPipe
    # Calcular distancia promedio entre landmark 0 (muñeca) y 9 (base medio)
    mediapipe_distances = []
    for frame_data in landmarks[:10]:  # Usar primeros 10 frames
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
        print(f"📐 Distancia promedio en MediaPipe: {avg_mediapipe_dist:.4f}")
        print(f"✅ Escala calculada: {calculated_scale:.4f}")
    else:
        calculated_scale = 1.0
        print("⚠️ No se pudo calcular escala, usando 1.0")
else:
    calculated_scale = 1.0
    print("⚠️ No se encontraron huesos de referencia, usando escala 1.0")

# ===============================================
# OBTENER POSICIONES DE MUÑECAS PARA OFFSET
# ===============================================
left_wrist_pos = None
right_wrist_pos = None

if 'LeftHand' in armature.pose.bones:
    left_wrist_pos = armature.matrix_world @ armature.pose.bones['LeftHand'].head
    print(f"📍 Muñeca izquierda en modelo: {left_wrist_pos}")

if 'RightHand' in armature.pose.bones:
    right_wrist_pos = armature.matrix_world @ armature.pose.bones['RightHand'].head
    print(f"📍 Muñeca derecha en modelo: {right_wrist_pos}")

bpy.ops.object.mode_set(mode='OBJECT')

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

# ===============================================
# CREAR EMPTIES PARA LOS LANDMARKS
# ===============================================
print("\n" + "="*70)
print("📍 CREANDO EMPTIES PARA LANDMARKS")
print("="*70)

empties = {}

for hand_key in ['left_hand', 'right_hand']:
    empties[hand_key] = {}
    for i in range(21):
        empty = bpy.data.objects.new(f"Target_{hand_key}_{i}", None)
        empty.empty_display_size = 0.01
        empty.empty_display_type = 'SPHERE'
        bpy.context.scene.collection.objects.link(empty)
        empties[hand_key][i] = empty

print(f"✅ Empties creados: {len(empties['left_hand']) + len(empties['right_hand'])}")

# ===============================================
# ANIMAR EMPTIES CON LANDMARKS
# ===============================================
print("\n" + "="*70)
print("🎬 ANIMANDO EMPTIES CON TRANSFORMACIÓN CORRECTA")
print("="*70)

# Obtener centro de landmarks del primer frame para calcular offset
first_frame = landmarks[0]
left_center = None
right_center = None

if first_frame.get('left_hand'):
    wrist = first_frame['left_hand'][0]
    left_center = mathutils.Vector((wrist['x'], wrist['y'], wrist['z']))

if first_frame.get('right_hand'):
    wrist = first_frame['right_hand'][0]
    right_center = mathutils.Vector((wrist['x'], wrist['y'], wrist['z']))

for frame_idx, frame_data in enumerate(landmarks):
    frame_num = frame_idx + 1
    bpy.context.scene.frame_set(frame_num)
    
    for hand_key in ['left_hand', 'right_hand']:
        hand_landmarks = frame_data.get(hand_key)
        if not hand_landmarks:
            continue
        
        # Determinar offset y centro
        if hand_key == 'left_hand' and left_wrist_pos and left_center:
            wrist_offset = left_wrist_pos
            lm_center = left_center
        elif hand_key == 'right_hand' and right_wrist_pos and right_center:
            wrist_offset = right_wrist_pos
            lm_center = right_center
        else:
            wrist_offset = mathutils.Vector((0, 0, 0))
            lm_center = mathutils.Vector((0, 0, 0))
        
        for i, landmark in enumerate(hand_landmarks):
            empty = empties[hand_key][i]
            
            # Transformar coordenadas de MediaPipe a Blender
            # MediaPipe: X right, Y down, Z forward (hacia cámara es negativo)
            # Blender: X right, Y forward, Z up
            
            # Restar el centro para hacer relativo a la muñeca
            rel_x = landmark['x'] - lm_center.x
            rel_y = landmark['y'] - lm_center.y
            rel_z = landmark['z'] - lm_center.z
            
            # Aplicar transformación de coordenadas y escala
            # MediaPipe Y (down) -> Blender -Z (up invertido)
            # MediaPipe Z (depth, negativo hacia cámara) -> Blender Y (forward)
            # MediaPipe X (right) -> Blender X (right)
            empty.location = (
                wrist_offset.x + rel_x * calculated_scale,
                wrist_offset.y - rel_z * calculated_scale,  # Z de MediaPipe -> Y de Blender (invertido)
                wrist_offset.z - rel_y * calculated_scale   # Y de MediaPipe -> Z de Blender (invertido)
            )
            empty.keyframe_insert(data_path="location", frame=frame_num)
    
    if (frame_num) % 10 == 0:
        print(f"   ✔️ Frame {frame_num}/{len(landmarks)}")

# ===============================================
# APLICAR CONSTRAINTS A HUESOS
# ===============================================
print("\n" + "="*70)
print("🔗 APLICANDO CONSTRAINTS A HUESOS")
print("="*70)

bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode='POSE')

constraint_count = 0

for hand_key, finger_dict in FINGER_MAPPING.items():
    for finger_base, landmark_indices in finger_dict.items():
        for segment in range(1, 5):  # 4 segmentos por dedo
            bone_name = f"{finger_base}{segment}"
            
            if bone_name not in armature.pose.bones:
                continue
            
            bone = armature.pose.bones[bone_name]
            
            # El hueso debe apuntar hacia el landmark final del segmento
            target_idx = landmark_indices[segment]
            target_empty = empties[hand_key][target_idx]
            
            # Limpiar constraints existentes
            for c in bone.constraints:
                bone.constraints.remove(c)
            
            # Agregar constraint "Damped Track"
            constraint = bone.constraints.new('DAMPED_TRACK')
            constraint.target = target_empty
            constraint.track_axis = 'TRACK_Y'  # Ajustar según orientación del hueso
            constraint.influence = 1.0
            
            constraint_count += 1

print(f"✅ Constraints aplicados: {constraint_count}")

# ===============================================
# BAKE ANIMATION
# ===============================================
print("\n" + "="*70)
print("🎯 BAKING ANIMATION")
print("="*70)

# Seleccionar todos los huesos de manos
for bone in armature.pose.bones:
    bone.bone.select = (
        'Hand' in bone.name and 
        any(f in bone.name for f in ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky'])
    )

# Bake la animación
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
# LIMPIAR EMPTIES
# ===============================================
print("\n" + "="*70)
print("🧹 LIMPIANDO EMPTIES")
print("="*70)

bpy.ops.object.mode_set(mode='OBJECT')

for hand_key in ['left_hand', 'right_hand']:
    for empty in empties[hand_key].values():
        bpy.data.objects.remove(empty, do_unlink=True)

print("✅ Empties eliminados")

# ===============================================
# EXPORTAR GLB
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

print("\n" + "="*70)
print("✅ MÉTODO PRECISO COMPLETADO")
print("="*70)
print(f"📁 Archivo: {GLB_OUTPUT}")
print(f"📏 Escala usada: {calculated_scale:.4f}")
