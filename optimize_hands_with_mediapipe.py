"""
Script optimizado para mejorar las manos de un modelo GLB usando MediaPipe Holistic
- Extrae landmarks de manos del video usando MediaPipe Holistic (con Z depth)
- Aplica las rotaciones SOLO a los huesos de las manos del modelo GLB
- Usa ángulos de Euler (NO quaternions)
- Modifica el GLB preservando el resto de la animación
"""

import bpy
import sys
import json
import numpy as np
import mathutils
from pathlib import Path
from scipy.spatial.transform import Rotation as R

# Añadir path para importar cv2 y mediapipe
sys.path.append(r"C:\Users\andre\OneDrive\Documentos\tesis\.venv\Lib\site-packages")

import cv2
import mediapipe as mp

# ==================== CONFIGURACIÓN ====================
VIDEO_PATH = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\videos\mal.mp4")
GLB_INPUT = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_mal.glb")
GLB_OUTPUT = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_mal_optimizado.glb")
TEMP_JSON = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\temp_hands_data.json")

# Mapeo de dedos MediaPipe Hand a huesos del modelo
# MediaPipe Hand tiene 21 landmarks (0=wrist, 1-4=thumb, 5-8=index, etc.)
FINGER_BONES_MAP = {
    'left': {
        'thumb': ['LeftHandThumb1', 'LeftHandThumb2', 'LeftHandThumb3'],
        'index': ['LeftHandIndex1', 'LeftHandIndex2', 'LeftHandIndex3'],
        'middle': ['LeftHandMiddle1', 'LeftHandMiddle2', 'LeftHandMiddle3'],
        'ring': ['LeftHandRing1', 'LeftHandRing2', 'LeftHandRing3'],
        'pinky': ['LeftHandPinky1', 'LeftHandPinky2', 'LeftHandPinky3']
    },
    'right': {
        'thumb': ['RightHandThumb1', 'RightHandThumb2', 'RightHandThumb3'],
        'index': ['RightHandIndex1', 'RightHandIndex2', 'RightHandIndex3'],
        'middle': ['RightHandMiddle1', 'RightHandMiddle2', 'RightHandMiddle3'],
        'ring': ['RightHandRing1', 'RightHandRing2', 'RightHandRing3'],
        'pinky': ['RightHandPinky1', 'RightHandPinky2', 'RightHandPinky3']
    }
}

# Landmarks de MediaPipe Hand por dedo
MEDIAPIPE_FINGER_INDICES = {
    'thumb': [1, 2, 3, 4],
    'index': [5, 6, 7, 8],
    'middle': [9, 10, 11, 12],
    'ring': [13, 14, 15, 16],
    'pinky': [17, 18, 19, 20]
}

# ==================== PASO 1: EXTRAER LANDMARKS DEL VIDEO ====================

def extract_hands_from_video():
    """
    Extrae landmarks de manos del video usando MediaPipe Holistic
    Incluye coordenadas 3D (x, y, z) donde z es la profundidad
    """
    print(f"\n{'='*70}")
    print(f"📹 PASO 1: Extrayendo landmarks del video")
    print(f"{'='*70}")
    print(f"Video: {VIDEO_PATH.name}")
    
    if not VIDEO_PATH.exists():
        raise FileNotFoundError(f"❌ Video no encontrado: {VIDEO_PATH}")
    
    cap = cv2.VideoCapture(str(VIDEO_PATH))
    if not cap.isOpened():
        raise RuntimeError(f"❌ No se pudo abrir el video")
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print(f"📊 FPS: {fps:.2f}")
    print(f"📊 Total frames: {total_frames}")
    print(f"📊 Resolución: {width}x{height}")
    
    # Inicializar MediaPipe Holistic
    mp_holistic = mp.solutions.holistic
    hands_data = {
        'fps': fps,
        'total_frames': total_frames,
        'frames': []
    }
    
    frame_count = 0
    
    print(f"\n🔍 Procesando frames...")
    
    with mp_holistic.Holistic(
        static_image_mode=False,
        model_complexity=2,  # Máxima precisión
        smooth_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as holistic:
        
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break
            
            # Convertir BGR a RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_rgb.flags.writeable = False
            
            # Procesar frame
            results = holistic.process(frame_rgb)
            
            frame_data = {
                'frame': frame_count,
                'left_hand': None,
                'right_hand': None
            }
            
            # Extraer mano izquierda
            if results.left_hand_landmarks:
                frame_data['left_hand'] = [
                    {
                        'x': lm.x,
                        'y': lm.y,
                        'z': lm.z,
                        'visibility': lm.visibility if hasattr(lm, 'visibility') else 1.0
                    }
                    for lm in results.left_hand_landmarks.landmark
                ]
            
            # Extraer mano derecha
            if results.right_hand_landmarks:
                frame_data['right_hand'] = [
                    {
                        'x': lm.x,
                        'y': lm.y,
                        'z': lm.z,
                        'visibility': lm.visibility if hasattr(lm, 'visibility') else 1.0
                    }
                    for lm in results.right_hand_landmarks.landmark
                ]
            
            hands_data['frames'].append(frame_data)
            
            frame_count += 1
            if frame_count % 10 == 0:
                print(f"   ✓ Frame {frame_count}/{total_frames}")
    
    cap.release()
    
    # Guardar datos temporales
    print(f"\n💾 Guardando datos temporales: {TEMP_JSON.name}")
    with open(TEMP_JSON, 'w') as f:
        json.dump(hands_data, f, indent=2)
    
    print(f"✅ Extracción completada: {frame_count} frames procesados")
    
    # Estadísticas de detección
    left_detected = sum(1 for f in hands_data['frames'] if f['left_hand'])
    right_detected = sum(1 for f in hands_data['frames'] if f['right_hand'])
    
    print(f"\n📊 Estadísticas de detección:")
    print(f"   Mano izquierda: {left_detected}/{frame_count} frames ({left_detected/frame_count*100:.1f}%)")
    print(f"   Mano derecha: {right_detected}/{frame_count} frames ({right_detected/frame_count*100:.1f}%)")
    
    return hands_data

# ==================== PASO 2: CALCULAR ROTACIONES EULER ====================

def calculate_euler_rotation(point1, point2, point3):
    """
    Calcula rotación Euler basándose en 3 puntos consecutivos (ej: base, mid, tip)
    Usa el vector entre point1-point2 y point2-point3
    Retorna rotación en Euler (XYZ) en radianes
    """
    # Convertir a numpy arrays
    p1 = np.array([point1['x'], point1['y'], point1['z']])
    p2 = np.array([point2['x'], point2['y'], point2['z']])
    p3 = np.array([point3['x'], point3['y'], point3['z']])
    
    # Vectores
    v1 = p2 - p1  # Vector base a medio
    v2 = p3 - p2  # Vector medio a punta
    
    # Normalizar
    v1_norm = v1 / (np.linalg.norm(v1) + 1e-6)
    v2_norm = v2 / (np.linalg.norm(v2) + 1e-6)
    
    # Calcular ángulo de flexión
    dot_product = np.clip(np.dot(v1_norm, v2_norm), -1.0, 1.0)
    bend_angle = np.arccos(dot_product)
    
    # Calcular vector perpendicular (eje de rotación)
    cross = np.cross(v1_norm, v2_norm)
    
    if np.linalg.norm(cross) > 1e-6:
        axis = cross / np.linalg.norm(cross)
        
        # Crear rotación usando scipy
        rotation = R.from_rotvec(bend_angle * axis)
        euler = rotation.as_euler('xyz', degrees=False)
    else:
        # Si los vectores son paralelos, no hay rotación
        euler = np.array([0.0, 0.0, 0.0])
    
    return euler

def process_finger_rotations(hand_landmarks, finger_name):
    """
    Procesa las rotaciones de un dedo completo
    Retorna lista de rotaciones Euler para cada segmento del dedo
    """
    if not hand_landmarks:
        return None
    
    indices = MEDIAPIPE_FINGER_INDICES[finger_name]
    rotations = []
    
    # Para cada segmento del dedo (necesitamos 3 puntos para calcular rotación)
    for i in range(len(indices) - 2):
        p1 = hand_landmarks[indices[i]]
        p2 = hand_landmarks[indices[i + 1]]
        p3 = hand_landmarks[indices[i + 2]]
        
        euler = calculate_euler_rotation(p1, p2, p3)
        rotations.append(euler.tolist())
    
    return rotations

def process_all_frames(hands_data):
    """
    Procesa todos los frames y calcula rotaciones Euler para cada hueso
    """
    print(f"\n{'='*70}")
    print(f"🧮 PASO 2: Calculando rotaciones Euler")
    print(f"{'='*70}")
    
    processed_data = {
        'fps': hands_data['fps'],
        'frames': []
    }
    
    for frame_idx, frame in enumerate(hands_data['frames']):
        frame_rotations = {
            'frame': frame['frame'],
            'left_hand': {},
            'right_hand': {}
        }
        
        # Procesar mano izquierda
        if frame['left_hand']:
            for finger_name in ['thumb', 'index', 'middle', 'ring', 'pinky']:
                rotations = process_finger_rotations(frame['left_hand'], finger_name)
                if rotations:
                    frame_rotations['left_hand'][finger_name] = rotations
        
        # Procesar mano derecha
        if frame['right_hand']:
            for finger_name in ['thumb', 'index', 'middle', 'ring', 'pinky']:
                rotations = process_finger_rotations(frame['right_hand'], finger_name)
                if rotations:
                    frame_rotations['right_hand'][finger_name] = rotations
        
        processed_data['frames'].append(frame_rotations)
        
        if (frame_idx + 1) % 10 == 0:
            print(f"   ✓ Procesado frame {frame_idx + 1}/{len(hands_data['frames'])}")
    
    print(f"✅ Rotaciones calculadas para {len(processed_data['frames'])} frames")
    
    return processed_data

# ==================== PASO 3: APLICAR ROTACIONES EN BLENDER ====================

def import_glb():
    """Importa el GLB en Blender"""
    print(f"\n📥 Importando GLB: {GLB_INPUT.name}")
    
    # Limpiar escena
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    
    # Importar GLB
    bpy.ops.import_scene.gltf(filepath=str(GLB_INPUT))
    
    # Buscar armature
    armature = None
    for obj in bpy.context.scene.objects:
        if obj.type == 'ARMATURE':
            armature = obj
            break
    
    if not armature:
        raise RuntimeError("❌ No se encontró armature en el GLB")
    
    print(f"✅ Armature encontrado: {armature.name}")
    
    # Listar huesos de manos
    hand_bones = []
    for bone in armature.pose.bones:
        bone_lower = bone.name.lower()
        if any(kw in bone_lower for kw in ['hand', 'finger', 'thumb', 'index', 'middle', 'ring', 'pinky']):
            hand_bones.append(bone.name)
    
    print(f"🦴 Huesos de manos encontrados: {len(hand_bones)}")
    for bone_name in sorted(hand_bones):
        print(f"   - {bone_name}")
    
    return armature, hand_bones

def apply_hand_rotations(armature, rotations_data):
    """
    Aplica las rotaciones Euler SOLO a los huesos de las manos
    Preserva el resto de la animación
    """
    print(f"\n{'='*70}")
    print(f"🔧 PASO 3: Aplicando rotaciones a los huesos")
    print(f"{'='*70}")
    
    if not armature.animation_data or not armature.animation_data.action:
        # Crear nueva acción si no existe
        action = bpy.data.actions.new(name="HandsOptimized")
        armature.animation_data_create()
        armature.animation_data.action = action
    else:
        action = armature.animation_data.action
    
    print(f"📊 Acción: {action.name}")
    
    fps = bpy.context.scene.render.fps
    frame_start = bpy.context.scene.frame_start
    
    modified_bones = set()
    
    # Procesar cada frame
    for frame_data in rotations_data['frames']:
        frame_number = frame_start + frame_data['frame']
        bpy.context.scene.frame_set(frame_number)
        
        # Aplicar rotaciones de mano izquierda
        for finger_name, rotations in frame_data['left_hand'].items():
            bone_names = FINGER_BONES_MAP['left'].get(finger_name, [])
            
            for i, bone_name in enumerate(bone_names):
                if i >= len(rotations):
                    continue
                
                if bone_name not in armature.pose.bones:
                    continue
                
                bone = armature.pose.bones[bone_name]
                euler_rot = rotations[i]
                
                # Convertir a Euler Blender
                bone.rotation_mode = 'XYZ'
                bone.rotation_euler = mathutils.Euler(euler_rot, 'XYZ')
                
                # Insertar keyframe
                bone.keyframe_insert(data_path="rotation_euler", frame=frame_number)
                modified_bones.add(bone_name)
        
        # Aplicar rotaciones de mano derecha
        for finger_name, rotations in frame_data['right_hand'].items():
            bone_names = FINGER_BONES_MAP['right'].get(finger_name, [])
            
            for i, bone_name in enumerate(bone_names):
                if i >= len(rotations):
                    continue
                
                if bone_name not in armature.pose.bones:
                    continue
                
                bone = armature.pose.bones[bone_name]
                euler_rot = rotations[i]
                
                # Convertir a Euler Blender
                bone.rotation_mode = 'XYZ'
                bone.rotation_euler = mathutils.Euler(euler_rot, 'XYZ')
                
                # Insertar keyframe
                bone.keyframe_insert(data_path="rotation_euler", frame=frame_number)
                modified_bones.add(bone_name)
    
    print(f"\n✅ Huesos modificados: {len(modified_bones)}")
    for bone_name in sorted(modified_bones):
        print(f"   ✓ {bone_name}")
    
    return len(modified_bones) > 0

def export_optimized_glb():
    """Exporta el GLB optimizado"""
    print(f"\n{'='*70}")
    print(f"💾 PASO 4: Exportando GLB optimizado")
    print(f"{'='*70}")
    
    # Crear directorio de salida
    GLB_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    
    # Asegurarse de estar en Object Mode
    if bpy.context.active_object and bpy.context.active_object.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    
    # Seleccionar todos los objetos
    bpy.ops.object.select_all(action='SELECT')
    
    # Exportar GLB
    bpy.ops.export_scene.gltf(
        filepath=str(GLB_OUTPUT),
        export_format='GLB',
        export_animations=True,
        export_apply=False,
        export_rest_position_armature=False,
        export_frame_range=True
    )
    
    print(f"✅ GLB exportado: {GLB_OUTPUT.name}")
    
    # Verificar tamaño
    size_mb = GLB_OUTPUT.stat().st_size / (1024 * 1024)
    print(f"📊 Tamaño: {size_mb:.2f} MB")
    
    return GLB_OUTPUT

# ==================== EJECUCIÓN PRINCIPAL ====================

def main():
    """Función principal que ejecuta todo el pipeline"""
    print(f"\n{'#'*70}")
    print(f"# OPTIMIZACIÓN DE MANOS CON MEDIAPIPE HOLISTIC")
    print(f"{'#'*70}")
    print(f"\n📋 Configuración:")
    print(f"   Video: {VIDEO_PATH.name}")
    print(f"   GLB entrada: {GLB_INPUT.name}")
    print(f"   GLB salida: {GLB_OUTPUT.name}")
    
    try:
        # PASO 1: Extraer landmarks del video
        hands_data = extract_hands_from_video()
        
        # PASO 2: Calcular rotaciones Euler
        rotations_data = process_all_frames(hands_data)
        
        # PASO 3: Importar GLB y aplicar rotaciones
        armature, hand_bones = import_glb()
        success = apply_hand_rotations(armature, rotations_data)
        
        if not success:
            print("\n⚠️ No se aplicaron rotaciones (posible problema con nombres de huesos)")
            return False
        
        # PASO 4: Exportar GLB optimizado
        output_file = export_optimized_glb()
        
        # Limpiar archivo temporal
        if TEMP_JSON.exists():
            TEMP_JSON.unlink()
            print(f"\n🗑️ Archivo temporal eliminado")
        
        print(f"\n{'='*70}")
        print(f"✅ OPTIMIZACIÓN COMPLETADA EXITOSAMENTE")
        print(f"{'='*70}")
        print(f"📁 Archivo generado: {output_file}")
        print(f"\n💡 Puedes abrir el archivo en Blender o tu visualizador 3D")
        
        return True
        
    except Exception as e:
        print(f"\n{'='*70}")
        print(f"❌ ERROR EN EL PROCESO")
        print(f"{'='*70}")
        print(f"{type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    # Verificar que estamos en Blender
    if not hasattr(bpy, 'data'):
        print("❌ Este script debe ejecutarse dentro de Blender")
        print("\nUso:")
        print('   blender --background --python optimize_hands_with_mediapipe.py')
        sys.exit(1)
    
    # Ejecutar
    success = main()
    sys.exit(0 if success else 1)
