"""
Extractor de Keypoints desde Videos de Señas
Convierte videos en archivos JSON de keypoints para el sistema de animación
"""

import cv2
import json
import numpy as np
from pathlib import Path
from typing import List, Dict
import sys


def extraer_frames_clave(video_path: str, num_keyframes: int = 4) -> List[np.ndarray]:
    """
    Extrae frames clave del video distribuidos uniformemente
    
    Args:
        video_path: Ruta al archivo de video
        num_keyframes: Número de keyframes a extraer
        
    Returns:
        Lista de frames como arrays numpy
    """
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"❌ Error: No se pudo abrir el video {video_path}")
        return []
    
    # Obtener información del video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    print(f"📹 Video: {Path(video_path).name}")
    print(f"   Total frames: {total_frames}")
    print(f"   FPS: {fps:.2f}")
    print(f"   Duración: {total_frames/fps:.2f} segundos")
    
    # Calcular índices de frames clave
    if total_frames < num_keyframes:
        indices = list(range(total_frames))
    else:
        indices = np.linspace(0, total_frames - 1, num_keyframes, dtype=int)
    
    frames = []
    for idx in indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if ret:
            frames.append(frame)
            print(f"   ✓ Frame {idx} extraído")
    
    cap.release()
    return frames, fps, indices


def analizar_pose_simple(frame: np.ndarray, frame_idx: int, fps: float) -> Dict:
    """
    Análisis simple de pose basado en detección de color de piel y geometría
    (Versión simplificada sin MediaPipe/OpenPose)
    
    Args:
        frame: Frame del video
        frame_idx: Índice del frame
        fps: FPS del video
        
    Returns:
        Diccionario con pose estimada
    """
    height, width = frame.shape[:2]
    
    # Convertir a HSV para mejor detección de piel
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Rango de color de piel (ajustable)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    
    # Máscara de piel
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    
    # Encontrar contornos
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Valores por defecto
    hand_x, hand_y = 0.5, 1.2  # Centro, altura del pecho
    hand_z = 0.3
    rotation_x, rotation_y, rotation_z = 0, 0, 0
    elbow_angle, shoulder_angle = 90, 45
    head_rot_x, head_rot_y, head_rot_z = 0, 0, 0
    
    if contours:
        # Encontrar el contorno más grande (probablemente la mano)
        largest_contour = max(contours, key=cv2.contourArea)
        
        # Calcular centro del contorno
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            
            # Normalizar coordenadas (0-1 basado en dimensiones del frame)
            hand_x = cx / width
            hand_y = 1.5 - (cy / height)  # Invertir Y (arriba = mayor valor)
            
            # Estimar profundidad basado en área del contorno
            area = cv2.contourArea(largest_contour)
            hand_z = 0.2 + (area / (width * height)) * 2
            
            # Estimar rotación basado en orientación del contorno
            if len(largest_contour) >= 5:
                ellipse = cv2.fitEllipse(largest_contour)
                angle = ellipse[2]
                rotation_z = angle - 90 if angle > 90 else angle
            
            # Estimar ángulos del brazo basado en posición
            elbow_angle = 60 + (hand_y * 40)
            shoulder_angle = 20 + (hand_x * 60)
    
    # Crear estructura de pose
    pose = {
        "frame": int(frame_idx),
        "time": float(frame_idx / fps),
        "pose": {
            "right_hand": {
                "x": round(hand_x, 2),
                "y": round(hand_y, 2),
                "z": round(hand_z, 2),
                "rotation_x": round(rotation_x, 1),
                "rotation_y": round(rotation_y, 1),
                "rotation_z": round(rotation_z, 1)
            },
            "right_arm": {
                "elbow_angle": round(elbow_angle, 1),
                "shoulder_angle": round(shoulder_angle, 1)
            },
            "head": {
                "rotation_x": round(head_rot_x, 1),
                "rotation_y": round(head_rot_y, 1),
                "rotation_z": round(head_rot_z, 1)
            }
        }
    }
    
    return pose


def procesar_video(video_path: str, sign_name: str, category: str = "pronombre", 
                   num_keyframes: int = 4) -> Dict:
    """
    Procesa un video completo y genera estructura JSON de keypoints
    
    Args:
        video_path: Ruta al video
        sign_name: Nombre de la seña
        category: Categoría de la seña
        num_keyframes: Número de keyframes a extraer
        
    Returns:
        Diccionario con estructura completa de keypoints
    """
    print("\n" + "=" * 60)
    print(f"🎬 Procesando: {sign_name}")
    print("=" * 60)
    
    # Extraer frames clave
    frames, fps, indices = extraer_frames_clave(video_path, num_keyframes)
    
    if not frames:
        return None
    
    # Analizar cada frame
    keyframes = []
    for i, (frame, idx) in enumerate(zip(frames, indices)):
        print(f"\n🔍 Analizando frame {idx}...")
        pose = analizar_pose_simple(frame, idx, fps)
        keyframes.append(pose)
    
    # Calcular duración
    duration = indices[-1] / fps if len(indices) > 0 else 1.0
    
    # Crear estructura JSON
    json_data = {
        "sign_name": sign_name,
        "duration": round(duration, 2),
        "fps": 30,  # FPS estándar para el sistema
        "category": category,
        "keyframes": keyframes
    }
    
    print(f"\n✅ Keypoints extraídos: {len(keyframes)} frames")
    
    return json_data


def procesar_carpeta(input_dir: str, output_dir: str):
    """
    Procesa todos los videos en una carpeta
    
    Args:
        input_dir: Carpeta con videos
        output_dir: Carpeta de salida para JSONs
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    # Buscar videos
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv']
    videos = []
    for ext in video_extensions:
        videos.extend(input_path.glob(f'*{ext}'))
    
    if not videos:
        print("❌ No se encontraron videos en la carpeta")
        return
    
    print(f"\n📂 Encontrados {len(videos)} videos")
    print("=" * 60)
    
    resultados = []
    
    for video_path in videos:
        # Obtener nombre de la seña del archivo
        sign_name = video_path.stem.lower()
        
        # Procesar video
        json_data = procesar_video(str(video_path), sign_name, category="pronombre")
        
        if json_data:
            # Guardar JSON
            output_file = output_path / f"{sign_name}.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, indent=2, ensure_ascii=False)
            
            print(f"💾 Guardado: {output_file}")
            resultados.append({
                'video': video_path.name,
                'json': output_file.name,
                'keyframes': len(json_data['keyframes']),
                'duracion': json_data['duration']
            })
    
    # Resumen
    print("\n" + "=" * 60)
    print("✅ PROCESAMIENTO COMPLETADO")
    print("=" * 60)
    
    for r in resultados:
        print(f"\n📹 {r['video']}")
        print(f"   → {r['json']}")
        print(f"   Keyframes: {r['keyframes']}")
        print(f"   Duración: {r['duracion']:.2f}s")
    
    print(f"\n📁 Archivos JSON guardados en: {output_path}")


def main():
    """
    Función principal
    """
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║  🎬 EXTRACTOR DE KEYPOINTS DESDE VIDEOS                     ║
    ║     Convierte videos de señas en archivos JSON              ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    # Rutas por defecto
    default_input = r"C:\Users\andre\OneDrive\Documentos\tesis\video\videos_segmentados"
    default_output = r"C:\Users\andre\OneDrive\Documentos\tesis\src\data\keypoints"
    
    # Procesar carpeta
    procesar_carpeta(default_input, default_output)
    
    print("\n🎉 ¡Proceso completado!")
    print(f"\n📝 Ahora puedes usar estas señas en el sistema:")
    print(f"   python main.py --mode interactive")
    print(f"   > yo")
    print(f"   > tu")
    print(f"   > el ella nosotros")


if __name__ == "__main__":
    main()
