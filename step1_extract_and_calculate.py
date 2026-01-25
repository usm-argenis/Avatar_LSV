"""
PASO 1: Extraer landmarks y calcular rotaciones Euler
Este script se ejecuta con el Python del sistema (que tiene mediapipe y cv2)
"""
import cv2
import mediapipe as mp
import json
import numpy as np
from pathlib import Path
from scipy.spatial.transform import Rotation as R

# ==================== CONFIGURACIÓN ====================
VIDEO_PATH = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\videos\mal.mp4")
OUTPUT_JSON = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\temp_hand_rotations.json")
LANDMARKS_JSON = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\temp_hands_data.json")

# Landmarks de MediaPipe Hand por dedo
MEDIAPIPE_FINGER_INDICES = {
    'thumb': [1, 2, 3, 4],
    'index': [5, 6, 7, 8],
    'middle': [9, 10, 11, 12],
    'ring': [13, 14, 15, 16],
    'pinky': [17, 18, 19, 20]
}

# ==================== FUNCIONES ====================

def extract_hands_from_video():
    """Extrae landmarks de manos del video"""
    print(f"\n{'='*70}")
    print(f"📹 EXTRAYENDO LANDMARKS DEL VIDEO")
    print(f"{'='*70}")
    print(f"Video: {VIDEO_PATH.name}")
    
    if not VIDEO_PATH.exists():
        raise FileNotFoundError(f"❌ Video no encontrado: {VIDEO_PATH}")
    
    cap = cv2.VideoCapture(str(VIDEO_PATH))
    if not cap.isOpened():
        raise RuntimeError(f"❌ No se pudo abrir el video")
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    print(f"📊 FPS: {fps:.2f}")
    print(f"📊 Total frames: {total_frames}")
    
    mp_holistic = mp.solutions.holistic
    hands_data = {'fps': fps, 'frames': []}
    
    frame_count = 0
    
    print(f"\n🔍 Procesando frames...")
    
    with mp_holistic.Holistic(
        static_image_mode=False,
        model_complexity=2,
        smooth_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as holistic:
        
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break
            
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_rgb.flags.writeable = False
            results = holistic.process(frame_rgb)
            
            frame_data = {
                'frame': frame_count,
                'left_hand': None,
                'right_hand': None
            }
            
            if results.left_hand_landmarks:
                frame_data['left_hand'] = [
                    {'x': lm.x, 'y': lm.y, 'z': lm.z}
                    for lm in results.left_hand_landmarks.landmark
                ]
            
            if results.right_hand_landmarks:
                frame_data['right_hand'] = [
                    {'x': lm.x, 'y': lm.y, 'z': lm.z}
                    for lm in results.right_hand_landmarks.landmark
                ]
            
            hands_data['frames'].append(frame_data)
            frame_count += 1
            
            if frame_count % 10 == 0:
                print(f"   ✓ Frame {frame_count}/{total_frames}")
    
    cap.release()
    
    left_detected = sum(1 for f in hands_data['frames'] if f['left_hand'])
    right_detected = sum(1 for f in hands_data['frames'] if f['right_hand'])
    
    print(f"\n📊 Detecciones:")
    print(f"   Mano izquierda: {left_detected}/{frame_count} ({left_detected/frame_count*100:.1f}%)")
    print(f"   Mano derecha: {right_detected}/{frame_count} ({right_detected/frame_count*100:.1f}%)")
    
    return hands_data

def calculate_euler_rotation(p1, p2, p3):
    """Calcula rotación Euler entre 3 puntos consecutivos"""
    p1_arr = np.array([p1['x'], p1['y'], p1['z']])
    p2_arr = np.array([p2['x'], p2['y'], p2['z']])
    p3_arr = np.array([p3['x'], p3['y'], p3['z']])
    
    v1 = p2_arr - p1_arr
    v2 = p3_arr - p2_arr
    
    v1_norm = v1 / (np.linalg.norm(v1) + 1e-6)
    v2_norm = v2 / (np.linalg.norm(v2) + 1e-6)
    
    dot_product = np.clip(np.dot(v1_norm, v2_norm), -1.0, 1.0)
    bend_angle = np.arccos(dot_product)
    
    cross = np.cross(v1_norm, v2_norm)
    
    if np.linalg.norm(cross) > 1e-6:
        axis = cross / np.linalg.norm(cross)
        rotation = R.from_rotvec(bend_angle * axis)
        euler = rotation.as_euler('xyz', degrees=False)
    else:
        euler = np.array([0.0, 0.0, 0.0])
    
    return euler.tolist()

def process_finger_rotations(hand_landmarks, finger_name):
    """Procesa rotaciones de un dedo completo"""
    if not hand_landmarks:
        return None
    
    indices = MEDIAPIPE_FINGER_INDICES[finger_name]
    rotations = []
    
    for i in range(len(indices) - 2):
        p1 = hand_landmarks[indices[i]]
        p2 = hand_landmarks[indices[i + 1]]
        p3 = hand_landmarks[indices[i + 2]]
        
        euler = calculate_euler_rotation(p1, p2, p3)
        rotations.append(euler)
    
    return rotations

def calculate_all_rotations(hands_data):
    """Calcula rotaciones Euler para todos los frames"""
    print(f"\n{'='*70}")
    print(f"🧮 CALCULANDO ROTACIONES EULER")
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
        
        # Mano izquierda
        if frame['left_hand']:
            for finger_name in ['thumb', 'index', 'middle', 'ring', 'pinky']:
                rotations = process_finger_rotations(frame['left_hand'], finger_name)
                if rotations:
                    frame_rotations['left_hand'][finger_name] = rotations
        
        # Mano derecha
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

def main():
    """Función principal"""
    print(f"\n{'#'*70}")
    print(f"# PASO 1: EXTRACCIÓN Y CÁLCULO DE ROTACIONES")
    print(f"{'#'*70}")
    
    try:
        # Extraer landmarks
        hands_data = extract_hands_from_video()
        
        # Guardar landmarks PRIMERO (para el método vectorial)
        print(f"\n💾 Guardando landmarks: {LANDMARKS_JSON.name}")
        with open(LANDMARKS_JSON, 'w') as f:
            json.dump(hands_data, f, indent=2)
        
        # Calcular rotaciones (método alternativo)
        rotations_data = calculate_all_rotations(hands_data)
        
        # Guardar rotaciones
        print(f"💾 Guardando rotaciones: {OUTPUT_JSON.name}")
        with open(OUTPUT_JSON, 'w') as f:
            json.dump(rotations_data, f, indent=2)
        
        print(f"\n{'='*70}")
        print(f"✅ PASO 1 COMPLETADO")
        print(f"{'='*70}")
        print(f"📁 Landmarks: {LANDMARKS_JSON}")
        print(f"📁 Rotaciones: {OUTPUT_JSON}")
        print(f"\n💡 Ahora ejecuta el PASO 2 con Blender para aplicar las rotaciones")
        
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
    success = main()
    exit(0 if success else 1)
