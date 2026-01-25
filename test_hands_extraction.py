"""
Script de prueba para verificar extracción de landmarks antes de aplicar a Blender
"""
import cv2
import mediapipe as mp
import json
from pathlib import Path

VIDEO_PATH = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\videos\mal.mp4")
OUTPUT_JSON = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test_hands_landmarks.json")

def test_extraction():
    print("="*70)
    print("PRUEBA DE EXTRACCIÓN DE LANDMARKS")
    print("="*70)
    print(f"\nVideo: {VIDEO_PATH.name}")
    
    if not VIDEO_PATH.exists():
        print(f"❌ ERROR: Video no encontrado")
        return False
    
    cap = cv2.VideoCapture(str(VIDEO_PATH))
    if not cap.isOpened():
        print(f"❌ ERROR: No se pudo abrir el video")
        return False
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    print(f"📊 FPS: {fps:.2f}")
    print(f"📊 Total frames: {total_frames}")
    
    mp_holistic = mp.solutions.holistic
    hands_data = {'fps': fps, 'frames': []}
    
    frame_count = 0
    left_count = 0
    right_count = 0
    
    print(f"\n🔍 Procesando...")
    
    with mp_holistic.Holistic(
        static_image_mode=False,
        model_complexity=2,
        smooth_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as holistic:
        
        while cap.isOpened() and frame_count < total_frames:
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
                left_count += 1
            
            if results.right_hand_landmarks:
                frame_data['right_hand'] = [
                    {'x': lm.x, 'y': lm.y, 'z': lm.z}
                    for lm in results.right_hand_landmarks.landmark
                ]
                right_count += 1
            
            hands_data['frames'].append(frame_data)
            frame_count += 1
    
    cap.release()
    
    print(f"\n✅ Extracción completada: {frame_count} frames")
    print(f"\n📊 Detecciones:")
    print(f"   Mano izquierda: {left_count}/{frame_count} ({left_count/frame_count*100:.1f}%)")
    print(f"   Mano derecha: {right_count}/{frame_count} ({right_count/frame_count*100:.1f}%)")
    
    # Guardar JSON
    print(f"\n💾 Guardando: {OUTPUT_JSON.name}")
    with open(OUTPUT_JSON, 'w') as f:
        json.dump(hands_data, f, indent=2)
    
    # Mostrar muestra de datos
    print(f"\n📋 Muestra del primer frame con datos:")
    for frame in hands_data['frames']:
        if frame['left_hand'] or frame['right_hand']:
            print(f"   Frame {frame['frame']}:")
            if frame['left_hand']:
                print(f"      Mano izq: {len(frame['left_hand'])} landmarks")
                print(f"         Muestra (punto 0): x={frame['left_hand'][0]['x']:.3f}, y={frame['left_hand'][0]['y']:.3f}, z={frame['left_hand'][0]['z']:.3f}")
            if frame['right_hand']:
                print(f"      Mano der: {len(frame['right_hand'])} landmarks")
                print(f"         Muestra (punto 0): x={frame['right_hand'][0]['x']:.3f}, y={frame['right_hand'][0]['y']:.3f}, z={frame['right_hand'][0]['z']:.3f}")
            break
    
    print(f"\n{'='*70}")
    print(f"✅ PRUEBA EXITOSA - Los datos se extrajeron correctamente")
    print(f"{'='*70}")
    print(f"📁 Archivo guardado: {OUTPUT_JSON}")
    
    return True

if __name__ == "__main__":
    try:
        test_extraction()
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
