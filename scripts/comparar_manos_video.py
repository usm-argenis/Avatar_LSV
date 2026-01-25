"""
Script para comparar posiciones de manos entre video y modelo GLB
Extrae frames del video y analiza posiciones manualmente
"""

import cv2
import numpy as np
import json
from pathlib import Path
import sys

def extraer_frames_video(video_path, output_dir):
    """
    Extrae frames del video para análisis manual
    """
    print(f"📹 Extrayendo frames de: {video_path}")
    
    cap = cv2.VideoCapture(str(video_path))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duracion = total_frames / fps
    
    print(f"   📊 FPS: {fps:.2f}")
    print(f"   📊 Frames totales: {total_frames}")
    print(f"   📊 Duración: {duracion:.2f}s")
    
    # Crear directorio de salida
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Extraer un frame cada 0.1 segundos (10 fps)
    intervalo_frames = max(1, int(fps / 10))
    
    frames_info = []
    frame_idx = 0
    frames_guardados = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Guardar frame cada intervalo
        if frame_idx % intervalo_frames == 0:
            tiempo = frame_idx / fps
            frame_filename = f"frame_{frame_idx:04d}_t{tiempo:.2f}s.jpg"
            frame_path = output_dir / frame_filename
            
            cv2.imwrite(str(frame_path), frame)
            
            frames_info.append({
                'frame': frame_idx,
                'tiempo': tiempo,
                'archivo': frame_filename
            })
            
            frames_guardados += 1
            
            # Mostrar progreso
            if frames_guardados % 10 == 0:
                progreso = (frame_idx / total_frames) * 100
                print(f"   ⏳ Extrayendo: {progreso:.1f}% ({frames_guardados} frames)")
        
        frame_idx += 1
    
    cap.release()
    
    # Guardar información
    info_file = output_dir / "frames_info.json"
    with open(info_file, 'w') as f:
        json.dump({
            'video_info': {
                'fps': fps,
                'total_frames': total_frames,
                'duracion': duracion,
                'intervalo_extraccion': intervalo_frames
            },
            'frames': frames_info
        }, f, indent=2)
    
    print(f"✅ {frames_guardados} frames extraídos en: {output_dir}")
    print(f"✅ Info guardada en: {info_file}")
    
    return frames_info

def main():
    # Rutas
    video_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\r.mp4")
    output_dir = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\output\frames_r")
    
    # Extraer frames
    frames_info = extraer_frames_video(video_path, output_dir)
    
    print("\n" + "="*60)
    print("✅ EXTRACCIÓN COMPLETADA")
    print("="*60)
    print(f"📁 Frames en: {output_dir}")
    print(f"📊 Total de frames: {len(frames_info)}")
    print("\n💡 Siguiente paso:")
    print("   1. Revisa los frames extraídos")
    print("   2. Compara visualmente con la animación del GLB")
    print("   3. Anota las correcciones necesarias")

if __name__ == "__main__":
    main()
