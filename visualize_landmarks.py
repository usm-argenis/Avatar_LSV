"""
Script para visualizar los landmarks de MediaPipe extraídos del video
Genera una visualización 2D de los landmarks frame por frame
"""
import json
import cv2
import numpy as np
from pathlib import Path

MOTION_JSON = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\motion_data_yo.json")
VIDEO_PATH = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\videos\yo.mp4")
OUTPUT_VIDEO = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\yo_landmarks_overlay.mp4")

# Conexiones de MediaPipe Pose
POSE_CONNECTIONS = [
    # Cara
    (0, 1), (1, 2), (2, 3), (3, 7),  # Izquierda
    (0, 4), (4, 5), (5, 6), (6, 8),  # Derecha
    (9, 10),  # Boca
    
    # Torso
    (11, 12),  # Hombros
    (11, 23), (12, 24),  # Hombros a caderas
    (23, 24),  # Caderas
    
    # Brazo izquierdo
    (11, 13), (13, 15), (15, 17), (15, 19), (15, 21),
    
    # Brazo derecho
    (12, 14), (14, 16), (16, 18), (16, 20), (16, 22),
    
    # Pierna izquierda
    (23, 25), (25, 27), (27, 29), (27, 31),
    
    # Pierna derecha
    (24, 26), (26, 28), (28, 30), (28, 32),
]

def load_motion_data():
    """Carga el JSON de movimiento"""
    with open(MOTION_JSON, 'r') as f:
        return json.load(f)

def draw_landmarks_on_frame(frame, landmarks, width, height):
    """Dibuja landmarks y conexiones en el frame"""
    overlay = frame.copy()
    
    # Dibujar conexiones
    for connection in POSE_CONNECTIONS:
        start_idx, end_idx = connection
        if start_idx < len(landmarks) and end_idx < len(landmarks):
            start = landmarks[start_idx]
            end = landmarks[end_idx]
            
            # Convertir coordenadas normalizadas a píxeles
            start_x = int(start['x'] * width)
            start_y = int(start['y'] * height)
            end_x = int(end['x'] * width)
            end_y = int(end['y'] * height)
            
            # Color basado en visibilidad
            vis = (start.get('visibility', 1.0) + end.get('visibility', 1.0)) / 2
            if vis > 0.5:
                color = (0, 255, 0)  # Verde para alta visibilidad
                thickness = 2
            else:
                color = (0, 128, 0)  # Verde oscuro para baja visibilidad
                thickness = 1
            
            cv2.line(overlay, (start_x, start_y), (end_x, end_y), color, thickness)
    
    # Dibujar puntos
    for idx, lm in enumerate(landmarks):
        x = int(lm['x'] * width)
        y = int(lm['y'] * height)
        vis = lm.get('visibility', 1.0)
        
        # Color según tipo de landmark
        if idx in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:  # Cara
            color = (255, 255, 0)  # Cian
        elif idx in [11, 12, 13, 14, 15, 16]:  # Brazos
            color = (0, 0, 255)  # Rojo
        elif idx in [23, 24, 25, 26, 27, 28]:  # Piernas
            color = (255, 0, 0)  # Azul
        else:
            color = (255, 255, 255)  # Blanco para manos/pies
        
        # Tamaño según visibilidad
        radius = 5 if vis > 0.7 else 3
        cv2.circle(overlay, (x, y), radius, color, -1)
        
        # Borde
        cv2.circle(overlay, (x, y), radius + 1, (0, 0, 0), 1)
    
    # Mezclar overlay con transparencia
    alpha = 0.7
    frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)
    
    return frame

def create_visualization():
    """Crea video con landmarks superpuestos"""
    print("Cargando datos...")
    motion_data = load_motion_data()
    
    # Abrir video original
    cap = cv2.VideoCapture(str(VIDEO_PATH))
    
    if not cap.isOpened():
        print(f"ERROR: No se pudo abrir el video {VIDEO_PATH}")
        return
    
    # Configuración del video de salida
    fps = motion_data['fps']
    width = motion_data['width']
    height = motion_data['height']
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(str(OUTPUT_VIDEO), fourcc, fps, (width, height))
    
    print(f"\nGenerando visualización...")
    print(f"  Video: {VIDEO_PATH.name}")
    print(f"  Resolución: {width}x{height}")
    print(f"  FPS: {fps:.2f}")
    print(f"  Frames: {len(motion_data['frames'])}")
    
    frame_idx = 0
    total_frames = len(motion_data['frames'])
    
    while cap.isOpened() and frame_idx < total_frames:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Obtener landmarks del frame actual
        frame_data = motion_data['frames'][frame_idx]
        landmarks = frame_data.get('pose', [])
        
        if landmarks:
            # Dibujar landmarks
            frame = draw_landmarks_on_frame(frame, landmarks, width, height)
            
            # Agregar información
            info_text = f"Frame: {frame_idx + 1}/{total_frames} | Landmarks: {len(landmarks)}"
            cv2.putText(frame, info_text, (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        out.write(frame)
        frame_idx += 1
        
        if frame_idx % 10 == 0:
            print(f"  Procesado {frame_idx}/{total_frames} frames...")
    
    cap.release()
    out.release()
    
    print(f"\n✓ Video generado: {OUTPUT_VIDEO}")
    print(f"  Tamaño: {OUTPUT_VIDEO.stat().st_size / (1024*1024):.2f} MB")
    print(f"\nPuedes reproducir el video para ver los landmarks detectados:")
    print(f"  {OUTPUT_VIDEO}")

if __name__ == "__main__":
    print("\n" + "="*70)
    print("  VISUALIZACIÓN DE LANDMARKS DE MEDIAPIPE")
    print("="*70 + "\n")
    
    create_visualization()
    
    print("\n" + "="*70)
