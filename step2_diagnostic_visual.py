"""
VERSIÓN DE DIAGNÓSTICO VISUAL
Mantiene los empties visibles para ver exactamente dónde están los landmarks
"""
import bpy
import json
import mathutils
import math

# ===============================================
# CONFIGURACIÓN
# ===============================================
GLB_INPUT = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_mal.glb"
BLEND_OUTPUT = r"C:\Users\andre\OneDrive\Documentos\tesis\diagnostic_hands.blend"
LANDMARKS_JSON = "temp_hands_data.json"

print("\n" + "="*70)
print("# DIAGNÓSTICO VISUAL - VER LANDMARKS Y HUESOS")
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
# ANÁLISIS DE ORIENTACIÓN DE HUESOS
# ===============================================
print("\n" + "="*70)
print("🔍 ANALIZANDO ORIENTACIÓN DE HUESOS")
print("="*70)

bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode='POSE')

# Analizar algunos huesos para ver su orientación
test_bones = ['LeftHandIndex1', 'LeftHandIndex2', 'LeftHandThumb1']
for bone_name in test_bones:
    if bone_name in armature.pose.bones:
        bone = armature.pose.bones[bone_name]
        head = armature.matrix_world @ bone.head
        tail = armature.matrix_world @ bone.tail
        direction = (tail - head).normalized()
        
        print(f"\n🦴 {bone_name}:")
        print(f"   Head: ({head.x:.4f}, {head.y:.4f}, {head.z:.4f})")
        print(f"   Tail: ({tail.x:.4f}, {tail.y:.4f}, {tail.z:.4f})")
        print(f"   Direction: ({direction.x:.4f}, {direction.y:.4f}, {direction.z:.4f})")

# Calcular escala automáticamente
left_wrist = armature.pose.bones.get('LeftHand')
left_middle1 = armature.pose.bones.get('LeftHandMiddle1')

if left_wrist and left_middle1:
    wrist_pos = armature.matrix_world @ left_wrist.head
    middle_pos = armature.matrix_world @ left_middle1.head
    model_hand_size = (wrist_pos - middle_pos).length
    
    print(f"\n📐 Tamaño de mano en modelo: {model_hand_size:.4f}")
    
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
        print(f"📐 Distancia promedio en MediaPipe: {avg_mediapipe_dist:.4f}")
        print(f"✅ Escala calculada: {calculated_scale:.4f}")
    else:
        calculated_scale = 1.0
else:
    calculated_scale = 1.0

# Obtener posiciones de muñecas
left_wrist_pos = None
right_wrist_pos = None

if 'LeftHand' in armature.pose.bones:
    left_wrist_pos = armature.matrix_world @ armature.pose.bones['LeftHand'].head

if 'RightHand' in armature.pose.bones:
    right_wrist_pos = armature.matrix_world @ armature.pose.bones['RightHand'].head

bpy.ops.object.mode_set(mode='OBJECT')

# ===============================================
# CREAR EMPTIES CON COLORES
# ===============================================
print("\n" + "="*70)
print("📍 CREANDO EMPTIES VISIBLES CON COLORES")
print("="*70)

empties = {}
colors = {
    'left_hand': (0.0, 1.0, 0.0),   # Verde
    'right_hand': (1.0, 0.0, 0.0)    # Rojo
}

for hand_key in ['left_hand', 'right_hand']:
    empties[hand_key] = {}
    for i in range(21):
        empty = bpy.data.objects.new(f"LM_{hand_key}_{i}", None)
        empty.empty_display_size = 0.02  # Más grande para ver
        empty.empty_display_type = 'SPHERE'
        bpy.context.scene.collection.objects.link(empty)
        empties[hand_key][i] = empty

print(f"✅ Empties creados: {len(empties['left_hand']) + len(empties['right_hand'])}")

# ===============================================
# ANIMAR EMPTIES
# ===============================================
print("\n" + "="*70)
print("🎬 ANIMANDO EMPTIES")
print("="*70)

# Frame de referencia para análisis
REFERENCE_FRAME = 1
bpy.context.scene.frame_set(REFERENCE_FRAME)

first_frame = landmarks[0]
left_center = None
right_center = None

if first_frame.get('left_hand'):
    wrist = first_frame['left_hand'][0]
    left_center = mathutils.Vector((wrist['x'], wrist['y'], wrist['z']))

if first_frame.get('right_hand'):
    wrist = first_frame['right_hand'][0]
    right_center = mathutils.Vector((wrist['x'], wrist['y'], wrist['z']))

print(f"\n🎯 Frame de referencia: {REFERENCE_FRAME}")
print(f"   Configurando posiciones para visualización...")

for frame_idx, frame_data in enumerate(landmarks[:1]):  # Solo primer frame para diagnóstico
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
            wrist_offset = mathutils.Vector((0, 0, 0))
            lm_center = mathutils.Vector((0, 0, 0))
        
        print(f"\n🖐️ {hand_key.upper()}:")
        print(f"   Offset de muñeca: ({wrist_offset.x:.4f}, {wrist_offset.y:.4f}, {wrist_offset.z:.4f})")
        
        for i, landmark in enumerate(hand_landmarks):
            empty = empties[hand_key][i]
            
            rel_x = landmark['x'] - lm_center.x
            rel_y = landmark['y'] - lm_center.y
            rel_z = landmark['z'] - lm_center.z
            
            # Probar diferentes transformaciones
            # OPCIÓN 1: MediaPipe directo con escala
            loc1 = (
                wrist_offset.x + rel_x * calculated_scale,
                wrist_offset.y - rel_z * calculated_scale,
                wrist_offset.z - rel_y * calculated_scale
            )
            
            empty.location = loc1
            
            if i == 0:  # Muñeca
                print(f"   Landmark {i} (muñeca):")
                print(f"      MediaPipe: ({landmark['x']:.4f}, {landmark['y']:.4f}, {landmark['z']:.4f})")
                print(f"      Relativo: ({rel_x:.4f}, {rel_y:.4f}, {rel_z:.4f})")
                print(f"      Blender: ({loc1[0]:.4f}, {loc1[1]:.4f}, {loc1[2]:.4f})")

# ===============================================
# GUARDAR ARCHIVO .BLEND
# ===============================================
print("\n" + "="*70)
print("💾 GUARDANDO ARCHIVO .BLEND")
print("="*70)

bpy.ops.ww3d.save(filepath=BLEND_OUTPUT)

print(f"✅ Archivo guardado: {BLEND_OUTPUT}")
print("\n" + "="*70)
print("✅ DIAGNÓSTICO COMPLETADO")
print("="*70)
print("\n💡 INSTRUCCIONES:")
print("   1. Abre el archivo diagnostic_hands.blend en Blender")
print("   2. Verás los empties (esferas) en las posiciones de los landmarks")
print("   3. Verde = mano izquierda, Rojo = mano derecha")
print("   4. Compara si los empties están alineados con los huesos")
print("   5. Si no están alineados, necesitamos ajustar la transformación")
