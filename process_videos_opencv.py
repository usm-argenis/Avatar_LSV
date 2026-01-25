"""
Script para procesar videos usando OpenCV: ralentizar y mejorar resolución
"""
import cv2
import os
from pathlib import Path
import numpy as np

def upscale_frame(frame, target_width=1920, target_height=1080):
    """Mejora la resolución del frame usando interpolación"""
    return cv2.resize(frame, (target_width, target_height), interpolation=cv2.INTER_LANCZOS4)

def sharpen_frame(frame):
    """Aplica un filtro de nitidez al frame"""
    kernel = np.array([[-1,-1,-1],
                       [-1, 9,-1],
                       [-1,-1,-1]])
    sharpened = cv2.filter2D(frame, -1, kernel)
    # Mezcla el frame original con el nitidizado (50/50)
    return cv2.addWeighted(frame, 0.5, sharpened, 0.5, 0)

def process_video(input_path, output_path, speed_factor=0.75):
    """
    Procesa un video ralentizándolo y mejorando su resolución
    speed_factor: 0.75 = 25% más lento, 0.5 = 50% más lento
    """
    cap = cv2.VideoCapture(str(input_path))
    
    if not cap.isOpened():
        print(f"  ✗ No se pudo abrir: {input_path.name}")
        return False
    
    # Obtener propiedades del video original
    original_fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Nueva tasa de frames (más baja = más lento)
    new_fps = original_fps * speed_factor
    
    # Configurar el writer para el video de salida
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(
        str(output_path),
        fourcc,
        new_fps,
        (1920, 1080)  # Resolución mejorada
    )
    
    frame_idx = 0
    processed = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Mejorar resolución
        frame_upscaled = upscale_frame(frame)
        
        # Aplicar mejoras de nitidez
        frame_enhanced = sharpen_frame(frame_upscaled)
        
        # Escribir frame
        out.write(frame_enhanced)
        
        frame_idx += 1
        processed += 1
        
        # Mostrar progreso cada 30 frames
        if processed % 30 == 0:
            progress = (processed / frame_count) * 100
            print(f"    Progreso: {progress:.1f}%", end='\r')
    
    cap.release()
    out.release()
    
    print(f"    Progreso: 100.0%")
    return True

def main():
    # Rutas
    input_dir = Path(r"c:\Users\andre\OneDrive\Documentos\tesis\test\output\videos")
    output_dir = Path(r"c:\Users\andre\OneDrive\Documentos\tesis\test\output\videos_1")
    
    # Crear carpeta de salida
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"✓ Carpeta creada: {output_dir}\n")
    
    # Obtener todos los videos
    video_files = sorted(input_dir.glob("*.mp4"))
    total = len(video_files)
    
    print(f"📹 Encontrados {total} videos para procesar")
    print(f"⚙️  Configuración:")
    print(f"   - Velocidad: 75% (25% más lento)")
    print(f"   - Resolución: 1920x1080 (Full HD)")
    print(f"   - Mejoras: Nitidez y suavizado\n")
    
    # Procesar cada video
    for idx, video_path in enumerate(video_files, 1):
        output_path = output_dir / video_path.name
        
        print(f"[{idx}/{total}] {video_path.name}")
        
        success = process_video(video_path, output_path, speed_factor=0.75)
        
        if success:
            print(f"  ✓ Completado\n")
        else:
            print(f"  ✗ Error\n")
    
    print(f"✅ Proceso completado!")
    print(f"   Videos originales: {input_dir}")
    print(f"   Videos mejorados: {output_dir}")

if __name__ == "__main__":
    main()
