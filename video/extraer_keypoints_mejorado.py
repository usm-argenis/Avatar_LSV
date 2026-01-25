"""
Extractor de Keypoints Mejorado para Lengua de Señas
Genera animaciones más fluidas con más frames y mejores rotaciones
"""

import cv2
import numpy as np
import json
from pathlib import Path
import math

def calcular_angulo(p1, p2):
    """Calcula ángulo entre dos puntos en grados"""
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return math.degrees(math.atan2(dy, dx))

def calcular_rotacion_3d(pos_actual, pos_anterior):
    """Estima rotación 3D basada en cambio de posición"""
    if pos_anterior is None:
        return 0, 0, 0
    
    dx = pos_actual[0] - pos_anterior[0]
    dy = pos_actual[1] - pos_anterior[1]
    
    # Rotación Z (giro en el plano XY)
    rot_z = math.degrees(math.atan2(dx, dy))
    
    # Rotación X (inclinación vertical)
    rot_x = dy * 30  # Escalar el movimiento vertical
    
    # Rotación Y (giro horizontal)
    rot_y = dx * 30  # Escalar el movimiento horizontal
    
    return rot_x, rot_y, rot_z

def detectar_mano_y_brazo(frame):
    """
    Detecta la posición de mano, codo y hombro usando detección de piel
    Returns: (mano_pos, codo_pos, hombro_pos) o None si no detecta
    """
    height, width = frame.shape[:2]
    
    # Convertir a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Rango de piel mejorado
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    
    # Aplicar operaciones morfológicas
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    
    # Encontrar contornos
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        return None, None, None
    
    # Ordenar contornos por área (de mayor a menor)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    
    mano_pos = None
    codo_pos = None
    hombro_pos = None
    
    # El contorno más grande suele ser la mano o el torso
    # Buscar múltiples regiones de piel
    for i, contour in enumerate(contours[:3]):  # Analizar los 3 contornos más grandes
        area = cv2.contourArea(contour)
        if area < 500:  # Ignorar contornos muy pequeños
            continue
        
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            
            # Normalizar coordenadas
            x = cx / width
            y = 1.5 - (cy / height)  # Invertir Y
            
            # Asignar basado en posición vertical
            if i == 0:
                # Primer contorno (probablemente mano o cara)
                if cy < height * 0.4:  # Parte superior
                    mano_pos = (x, y)
                else:
                    hombro_pos = (x, y)
            elif i == 1 and mano_pos is None:
                mano_pos = (x, y)
            elif i == 2 and codo_pos is None:
                codo_pos = (x, y)
    
    # Estimar posiciones faltantes
    if mano_pos and hombro_pos and codo_pos is None:
        # Codo en punto medio
        codo_pos = ((mano_pos[0] + hombro_pos[0]) / 2, 
                    (mano_pos[1] + hombro_pos[1]) / 2)
    
    if mano_pos and codo_pos is None and hombro_pos is None:
        # Estimar brazo completo basado en mano
        codo_pos = (mano_pos[0] + 0.1, mano_pos[1] - 0.2)
        hombro_pos = (mano_pos[0] + 0.2, mano_pos[1] - 0.4)
    
    return mano_pos, codo_pos, hombro_pos

def extraer_keypoints_video(video_path, fps_extraction=12, output_dir=None):
    """
    Extrae keypoints de un video con mejor densidad de frames
    
    Args:
        video_path: Ruta al video
        fps_extraction: Frames por segundo a extraer (default: 12)
        output_dir: Directorio de salida (default: src/data/keypoints)
    """
    video_path = Path(video_path)
    
    if not video_path.exists():
        print(f"❌ Video no encontrado: {video_path}")
        return None
    
    print(f"\n{'='*60}")
    print(f"🎬 Procesando: {video_path.name}")
    print(f"{'='*60}")
    
    # Abrir video
    cap = cv2.VideoCapture(str(video_path))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = total_frames / fps
    
    print(f"📊 Información del video:")
    print(f"   • Total frames: {total_frames}")
    print(f"   • FPS original: {fps:.2f}")
    print(f"   • Duración: {duration:.2f} segundos")
    
    # Calcular frames a extraer
    num_frames_extract = max(int(duration * fps_extraction), 8)  # Mínimo 8 frames
    frame_interval = max(1, total_frames // num_frames_extract)
    
    print(f"\n🔍 Extracción:")
    print(f"   • FPS objetivo: {fps_extraction}")
    print(f"   • Frames a extraer: {num_frames_extract}")
    print(f"   • Intervalo: cada {frame_interval} frames")
    
    # Extraer keyframes
    keyframes = []
    prev_mano_pos = None
    
    frame_count = 0
    for frame_idx in range(0, total_frames, frame_interval):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()
        
        if not ret:
            continue
        
        time = frame_idx / fps
        
        # Detectar mano y brazo
        mano_pos, codo_pos, hombro_pos = detectar_mano_y_brazo(frame)
        
        if mano_pos is None:
            # Usar valores por defecto si no se detecta
            mano_pos = (0.5, 1.2)
            codo_pos = (0.6, 1.0)
            hombro_pos = (0.7, 0.8)
        
        # Calcular rotaciones
        rot_x, rot_y, rot_z = calcular_rotacion_3d(mano_pos, prev_mano_pos)
        
        # Calcular ángulos del brazo
        if codo_pos and hombro_pos:
            # Ángulo del codo
            elbow_angle = calcular_angulo(codo_pos, mano_pos)
            elbow_angle = abs(elbow_angle) % 180
            
            # Ángulo del hombro
            shoulder_angle = calcular_angulo(hombro_pos, codo_pos)
            shoulder_angle = abs(shoulder_angle) % 180
        else:
            elbow_angle = 90
            shoulder_angle = 45
        
        # Profundidad estimada (z) basada en altura de la mano
        hand_z = 0.3 + (mano_pos[1] - 1.0) * 0.2
        
        keyframe = {
            "frame": frame_count,  # Frame normalizado (0, 1, 2, 3...)
            "time": time,
            "pose": {
                "right_hand": {
                    "x": round(mano_pos[0], 2),
                    "y": round(mano_pos[1], 2),
                    "z": round(hand_z, 2),
                    "rotation_x": round(rot_x, 1),
                    "rotation_y": round(rot_y, 1),
                    "rotation_z": round(rot_z, 1)
                },
                "right_arm": {
                    "elbow_angle": round(elbow_angle, 1),
                    "shoulder_angle": round(shoulder_angle, 1)
                },
                "head": {
                    "rotation_x": 0,
                    "rotation_y": 0,
                    "rotation_z": 0
                }
            }
        }
        
        keyframes.append(keyframe)
        prev_mano_pos = mano_pos
        frame_count += 1
        
        if frame_count % 5 == 0:
            print(f"   ✓ Frame {frame_count}/{num_frames_extract} procesado (t={time:.2f}s)")
    
    cap.release()
    
    print(f"\n✅ Extraídos {len(keyframes)} keyframes")
    
    # Crear estructura JSON
    sign_name = video_path.stem  # Nombre del archivo sin extensión
    
    json_data = {
        "sign_name": sign_name,
        "duration": round(duration, 2),
        "fps": fps_extraction,
        "category": "pronombre",  # Ajustar según corresponda
        "keyframes": keyframes
    }
    
    # Guardar JSON
    if output_dir is None:
        output_dir = Path(__file__).parent.parent / "src" / "data" / "keypoints"
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{sign_name}.json"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Guardado en: {output_path}")
    print(f"\n📈 Resumen:")
    print(f"   • Keyframes: {len(keyframes)}")
    print(f"   • Duración: {duration:.2f}s")
    print(f"   • FPS efectivo: {len(keyframes)/duration:.1f}")
    
    return json_data

def procesar_multiples_videos(videos_dir, fps_extraction=12):
    """Procesa múltiples videos en un directorio"""
    videos_dir = Path(videos_dir)
    
    if not videos_dir.exists():
        print(f"❌ Directorio no encontrado: {videos_dir}")
        return
    
    # Buscar archivos de video
    video_files = list(videos_dir.glob("*.mp4")) + list(videos_dir.glob("*.avi"))
    
    if not video_files:
        print(f"❌ No se encontraron videos en: {videos_dir}")
        return
    
    print(f"\n🎯 Procesando {len(video_files)} videos...")
    print(f"   FPS de extracción: {fps_extraction}")
    
    resultados = []
    for video_file in video_files:
        try:
            result = extraer_keypoints_video(video_file, fps_extraction)
            if result:
                resultados.append(result)
        except Exception as e:
            print(f"❌ Error procesando {video_file.name}: {e}")
    
    print(f"\n{'='*60}")
    print(f"✅ Procesados {len(resultados)} de {len(video_files)} videos")
    print(f"{'='*60}")
    
    return resultados

if __name__ == "__main__":
    import sys
    
    # Directorio de videos segmentados
    videos_dir = Path(__file__).parent / "videos_segmentados"
    
    if len(sys.argv) > 1:
        # Procesar un video específico
        video_path = Path(sys.argv[1])
        fps = int(sys.argv[2]) if len(sys.argv) > 2 else 12
        extraer_keypoints_video(video_path, fps_extraction=fps)
    else:
        # Procesar todos los videos
        print("🚀 Extractor de Keypoints Mejorado")
        print("=" * 60)
        procesar_multiples_videos(videos_dir, fps_extraction=12)
