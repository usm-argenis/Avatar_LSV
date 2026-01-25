"""
Script para actualizar animaciones de archivos FBX existentes usando los datos
de landmarks de MediaPipe (JSONs SignAvatar v2.0).

Toma los FBX procesados y ajusta las posiciones de los huesos de las manos
para que coincidan exactamente con los landmarks detectados en los videos.

Uso:
    blender --background --python update_fbx_from_json.py
"""

import bpy
import json
import sys
from pathlib import Path
from mathutils import Vector, Quaternion, Matrix
import math

# Rutas del proyecto
PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_ROOT / 'output'
TEST_OUTPUT = PROJECT_ROOT / 'test' / 'output'

# Videos a procesar
VIDEOS = ['b', 'c', 'd', 'e']

# Mapeo de landmarks de MediaPipe a huesos de Mixamo
# MediaPipe hand tiene 21 landmarks, Mixamo tiene estructura de dedos
HAND_BONE_MAPPING = {
    # Mano izquierda - MediaPipe index -> Mixamo bone name
    'left': {
        0: 'mixamorig:LeftHand',  # wrist
        # Pulgar
        1: 'mixamorig:LeftHandThumb1',
        2: 'mixamorig:LeftHandThumb2',
        3: 'mixamorig:LeftHandThumb3',
        4: 'mixamorig:LeftHandThumb4',
        # Índice
        5: 'mixamorig:LeftHandIndex1',
        6: 'mixamorig:LeftHandIndex2',
        7: 'mixamorig:LeftHandIndex3',
        8: 'mixamorig:LeftHandIndex4',
        # Medio
        9: 'mixamorig:LeftHandMiddle1',
        10: 'mixamorig:LeftHandMiddle2',
        11: 'mixamorig:LeftHandMiddle3',
        12: 'mixamorig:LeftHandMiddle4',
        # Anular
        13: 'mixamorig:LeftHandRing1',
        14: 'mixamorig:LeftHandRing2',
        15: 'mixamorig:LeftHandRing3',
        16: 'mixamorig:LeftHandRing4',
        # Meñique
        17: 'mixamorig:LeftHandPinky1',
        18: 'mixamorig:LeftHandPinky2',
        19: 'mixamorig:LeftHandPinky3',
        20: 'mixamorig:LeftHandPinky4',
    },
    # Mano derecha
    'right': {
        0: 'mixamorig:RightHand',
        # Pulgar
        1: 'mixamorig:RightHandThumb1',
        2: 'mixamorig:RightHandThumb2',
        3: 'mixamorig:RightHandThumb3',
        4: 'mixamorig:RightHandThumb4',
        # Índice
        5: 'mixamorig:RightHandIndex1',
        6: 'mixamorig:RightHandIndex2',
        7: 'mixamorig:RightHandIndex3',
        8: 'mixamorig:RightHandIndex4',
        # Medio
        9: 'mixamorig:RightHandMiddle1',
        10: 'mixamorig:RightHandMiddle2',
        11: 'mixamorig:RightHandMiddle3',
        12: 'mixamorig:RightHandMiddle4',
        # Anular
        13: 'mixamorig:RightHandRing1',
        14: 'mixamorig:RightHandRing2',
        15: 'mixamorig:RightHandRing3',
        16: 'mixamorig:RightHandRing4',
        # Meñique
        17: 'mixamorig:RightHandPinky1',
        18: 'mixamorig:RightHandPinky2',
        19: 'mixamorig:RightHandPinky3',
        20: 'mixamorig:RightHandPinky4',
    }
}

def clear_scene():
    """Limpia la escena de Blender"""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

def load_signavatar_json(json_path):
    """Carga archivo SignAvatar JSON v2.0"""
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    print(f"📄 JSON cargado: {json_path.name}")
    print(f"   Versión: {data.get('version', '1.0')}")
    print(f"   Huesos: {data.get('total_bones', len(data.get('bones', [])))} ")
    print(f"   Frames: {len(data.get('frames', []))}")
    print(f"   FPS: {data.get('fps', 30)}")
    
    return data

def get_hand_landmarks_from_frame(frame_data, hand='left'):
    """
    Extrae landmarks de una mano específica de un frame
    
    Retorna lista de 21 posiciones [x, y, z]
    """
    positions = frame_data.get('positions', [])
    
    if hand == 'left':
        # Índices 16-36 para mano izquierda
        return positions[16:37] if len(positions) >= 37 else []
    else:
        # Índices 37-57 para mano derecha
        return positions[37:58] if len(positions) >= 58 else []

def calculate_bone_rotation(bone, target_pos):
    """
    Calcula la rotación necesaria para que un hueso apunte hacia una posición objetivo
    
    Args:
        bone: Pose bone de Blender
        target_pos: Vector3 de posición objetivo
    
    Returns:
        Quaternion de rotación
    """
    # Obtener posición actual del hueso en espacio mundo
    bone_head = bone.head
    bone_tail = bone.tail
    
    # Vector dirección actual del hueso
    current_dir = (bone_tail - bone_head).normalized()
    
    # Vector dirección deseada
    target_vec = Vector(target_pos)
    desired_dir = (target_vec - bone_head).normalized()
    
    # Calcular rotación entre vectores
    rotation = current_dir.rotation_difference(desired_dir)
    
    return rotation

def calculate_bone_curl(current_pos, next_pos, parent_pos):
    """
    Calcula el ángulo de flexión (curl) de un hueso del dedo
    Retorna ángulo en radianes para rotación Z
    """
    # Vector desde parent al current
    v1 = (current_pos - parent_pos).normalized()
    # Vector desde current al next
    v2 = (next_pos - current_pos).normalized()
    
    # Ángulo entre vectores
    angle = v1.angle(v2)
    
    # Convertir a curl: ángulo de flexión natural del dedo
    # Si angle es pequeño, el dedo está extendido
    # Si angle es grande, el dedo está flexionado
    curl = math.pi - angle
    
    return curl

def apply_hand_animation(armature, json_data, hand='left'):
    """
    Aplica animación de mano desde JSON a armature de Blender
    OPTIMIZADO: Enfoque híbrido - pulgar libre, dedos con curl Z
    """
    if not armature or armature.type != 'ARMATURE':
        print(f"⚠️ No es un armature válido")
        return
    
    frames = json_data.get('frames', [])
    fps = json_data.get('fps', 30)
    bone_mapping = HAND_BONE_MAPPING[hand]
    
    print(f"\n🖐️ Aplicando animación de mano {hand}...")
    print(f"   Frames a procesar: {len(frames)}")
    print(f"   Modo: Híbrido (pulgar libre, dedos Z-curl optimizado)")
    
    # Definir cadenas de dedos
    finger_chains = {
        'thumb': [1, 2, 3, 4],
        'index': [5, 6, 7, 8],
        'middle': [9, 10, 11, 12],
        'ring': [13, 14, 15, 16],
        'pinky': [17, 18, 19, 20]
    }
    
    # Establecer modo pose
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='POSE')
    
    keyframes_added = 0
    
    for frame_idx, frame in enumerate(frames):
        bpy.context.scene.frame_set(frame_idx + 1)
        
        hand_landmarks = get_hand_landmarks_from_frame(frame, hand)
        
        if not hand_landmarks or len(hand_landmarks) < 21:
            continue
        
        # Procesar cada dedo
        for finger_name, chain in finger_chains.items():
            is_thumb = (finger_name == 'thumb')
            
            for i, landmark_idx in enumerate(chain):
                bone_name = bone_mapping.get(landmark_idx)
                
                if not bone_name or bone_name not in armature.pose.bones:
                    continue
                
                pose_bone = armature.pose.bones[bone_name]
                
                # Posiciones
                current_pos = Vector(hand_landmarks[landmark_idx])
                
                # Parent position (wrist o hueso anterior)
                if i == 0:  # Primer hueso del dedo
                    parent_pos = Vector(hand_landmarks[0])  # Muñeca
                else:
                    parent_pos = Vector(hand_landmarks[chain[i-1]])
                
                # Next position
                if i < len(chain) - 1:
                    next_pos = Vector(hand_landmarks[chain[i+1]])
                else:
                    # Último hueso: extrapolar dirección
                    next_pos = current_pos + (current_pos - parent_pos)
                
                if is_thumb:
                    # PULGAR: Rotación completa con límite en twist
                    bone_direction = (next_pos - current_pos).normalized()
                    
                    if pose_bone.parent:
                        parent_matrix = armature.matrix_world @ pose_bone.parent.matrix
                        local_direction = parent_matrix.inverted().to_3x3() @ bone_direction
                    else:
                        local_direction = armature.matrix_world.inverted().to_3x3() @ bone_direction
                    
                    rest_direction = Vector((0, 1, 0))
                    rotation_quat = rest_direction.rotation_difference(local_direction)
                    
                    # Limitar twist (Y-axis) para evitar deformaciones
                    euler = rotation_quat.to_euler()
                    euler.y *= 0.3  # Reducir twist
                    rotation_quat = euler.to_quaternion()
                    
                    pose_bone.rotation_mode = 'QUATERNION'
                    pose_bone.rotation_quaternion = rotation_quat
                    pose_bone.keyframe_insert(data_path="rotation_quaternion", frame=frame_idx + 1)
                    
                else:
                    # DEDOS (Index, Middle, Ring, Pinky): Solo curl Z
                    curl_angle = calculate_bone_curl(current_pos, next_pos, parent_pos)
                    
                    # Limites suaves
                    max_curl = math.radians(110)  # Flexión máxima
                    min_curl = math.radians(-20)  # Ligera hiperextensión
                    
                    curl_angle = max(min(curl_angle, max_curl), min_curl)
                    
                    # Factor de suavizado moderado
                    curl_angle *= 0.75  # Balance entre precisión y skinning
                    
                    pose_bone.rotation_mode = 'XYZ'
                    pose_bone.rotation_euler = (0, 0, curl_angle)
                    pose_bone.keyframe_insert(data_path="rotation_euler", frame=frame_idx + 1)
                
                keyframes_added += 1
    
    print(f"   ✅ Keyframes agregados: {keyframes_added}")
    print(f"   📊 Pulgar: quaternion libre | Dedos: Z-curl 0.75x")
    
    bpy.ops.object.mode_set(mode='OBJECT')

def update_fbx_with_hand_data(video_name):
    """
    Actualiza un archivo FBX con datos de manos del JSON correspondiente
    """
    fbx_path = OUTPUT_DIR / f"Remy_resultado_{video_name}.fbx"
    json_path = TEST_OUTPUT / f"{video_name}_signavatar.json"
    output_path = OUTPUT_DIR / f"Remy_resultado_{video_name}_updated.fbx"
    
    print(f"\n{'='*70}")
    print(f"🎬 Procesando: {video_name.upper()}")
    print(f"{'='*70}")
    
    # Verificar archivos
    if not fbx_path.exists():
        print(f"❌ FBX no encontrado: {fbx_path}")
        return False
    
    if not json_path.exists():
        print(f"❌ JSON no encontrado: {json_path}")
        return False
    
    # Limpiar escena
    clear_scene()
    
    # Importar FBX con escala correcta
    print(f"📦 Importando FBX: {fbx_path.name}")
    bpy.ops.import_scene.fbx(
        filepath=str(fbx_path),
        global_scale=1.0,
        use_custom_normals=True
    )
    
    # Encontrar armature
    armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            armature = obj
            break
    
    if not armature:
        print(f"❌ No se encontró armature en el FBX")
        return False
    
    print(f"✅ Armature encontrado: {armature.name}")
    print(f"   Huesos: {len(armature.pose.bones)}")
    print(f"   Escala: {armature.scale}")
    
    # Cargar datos del JSON
    json_data = load_signavatar_json(json_path)
    
    # Obtener el rango de frames original del FBX
    original_action = None
    original_frame_start = 1
    original_frame_end = len(json_data.get('frames', []))
    
    if armature.animation_data and armature.animation_data.action:
        original_action = armature.animation_data.action
        original_frame_start = int(original_action.frame_range[0])
        original_frame_end = int(original_action.frame_range[1])
        print(f"   Animación original: frames {original_frame_start}-{original_frame_end}")
    
    # Ajustar el rango de la escena al número de frames del JSON
    num_json_frames = len(json_data.get('frames', []))
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = num_json_frames
    
    print(f"   Ajustando rango a {num_json_frames} frames")
    
    # Aplicar animación de manos
    apply_hand_animation(armature, json_data, hand='left')
    apply_hand_animation(armature, json_data, hand='right')
    
    # Exportar FBX actualizado
    print(f"\n💾 Exportando FBX actualizado...")
    
    # Seleccionar todo para exportar
    bpy.ops.object.select_all(action='SELECT')
    
    # Exportar con configuración que preserva materiales, texturas Y ESCALA
    bpy.ops.export_scene.fbx(
        filepath=str(output_path),
        use_selection=True,
        # Mantener escala original (sin aplicar transformaciones)
        global_scale=1.0,
        apply_unit_scale=False,
        apply_scale_options='FBX_SCALE_NONE',
        bake_space_transform=False,
        # Animación
        bake_anim=True,
        bake_anim_use_all_bones=True,
        bake_anim_use_nla_strips=False,
        bake_anim_use_all_actions=False,
        bake_anim_step=1.0,
        bake_anim_simplify_factor=0.0,
        # Rango correcto de frames
        bake_anim_force_startend_keying=True,
        # Materiales y texturas
        path_mode='COPY',
        embed_textures=True,
        # Otros
        add_leaf_bones=False,
        use_custom_props=True
    )
    
    print(f"✅ FBX actualizado guardado: {output_path.name}")
    
    # Verificar tamaño
    size_mb = output_path.stat().st_size / (1024 * 1024)
    print(f"   Tamaño: {size_mb:.2f} MB")
    
    return True

def main():
    print("="*70)
    print("🔄 ACTUALIZACIÓN DE FBX CON DATOS DE MANOS")
    print("="*70)
    print("\nEste script:")
    print("  1. Carga el FBX existente")
    print("  2. Lee los landmarks de manos del JSON SignAvatar")
    print("  3. Actualiza las animaciones de los dedos")
    print("  4. Exporta el FBX con animación mejorada")
    print()
    
    success_count = 0
    
    for video_name in VIDEOS:
        try:
            if update_fbx_with_hand_data(video_name):
                success_count += 1
        except Exception as e:
            print(f"❌ Error procesando {video_name}: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n{'='*70}")
    print(f"✅ Proceso completado: {success_count}/{len(VIDEOS)} FBX actualizados")
    print(f"{'='*70}")
    
    if success_count > 0:
        print(f"\n📁 Archivos generados:")
        for video_name in VIDEOS:
            output_file = OUTPUT_DIR / f"Remy_resultado_{video_name}_updated.fbx"
            if output_file.exists():
                size_mb = output_file.stat().st_size / (1024 * 1024)
                print(f"   ✅ {output_file.name} ({size_mb:.2f} MB)")

if __name__ == "__main__":
    # Verificar que estamos en Blender
    try:
        import bpy
        main()
    except ImportError:
        print("❌ Este script debe ejecutarse desde Blender:")
        print("   blender --background --python update_fbx_from_json.py")
        sys.exit(1)
