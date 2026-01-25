"""
MÉTODO CON CONSTRAINTS - Solución Profesional
En lugar de calcular rotaciones manualmente, usamos constraints de Blender
que hacen que los huesos apunten automáticamente a las posiciones objetivo
"""
import bpy
import json
import mathutils

# ===============================================
# CONFIGURACIÓN
# ===============================================
GLB_INPUT = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_mal.glb"
GLB_OUTPUT = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_mal_constraints.glb"
LANDMARKS_JSON = "temp_hands_data.json"

print("\n" + "="*70)
print("# MÉTODO CON CONSTRAINTS - SOLUCIÓN PROFESIONAL")
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

bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode='OBJECT')

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
print("🎬 ANIMANDO EMPTIES CON LANDMARKS")
print("="*70)

for frame_idx, frame_data in enumerate(landmarks):
    frame_num = frame_idx + 1
    bpy.context.scene.frame_set(frame_num)
    
    for hand_key in ['left_hand', 'right_hand']:
        hand_landmarks = frame_data.get(hand_key)
        if not hand_landmarks:
            continue
        
        for i, landmark in enumerate(hand_landmarks):
            empty = empties[hand_key][i]
            
            # Posicionar el empty en el landmark
            # Escalar y ajustar coordenadas
            scale = 5.0  # Ajustar según el tamaño del modelo
            empty.location = (
                landmark['x'] * scale,
                landmark['y'] * scale,
                landmark['z'] * scale
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
            constraint.track_axis = 'TRACK_Y'  # El hueso apunta en Y
            constraint.influence = 1.0
            
            constraint_count += 1

print(f"✅ Constraints aplicados: {constraint_count}")

# ===============================================
# BAKE ANIMATION (Convertir constraints a keyframes)
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
print("✅ CONSTRAINTS METHOD COMPLETADO")
print("="*70)
print(f"📁 Archivo: {GLB_OUTPUT}")
print("\n💡 Este método usa constraints nativos de Blender")
print("   que son más precisos que cálculos manuales")
