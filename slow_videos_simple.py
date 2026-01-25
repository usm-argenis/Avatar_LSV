"""
Script simple para ralentizar videos sin cambiar resolución
"""
import cv2
from pathlib import Path

def slow_video(input_path, output_path, speed_factor=0.75):
    """Ralentiza un video sin cambiar su resolución"""
    cap = cv2.VideoCapture(str(input_path))
    
    if not cap.isOpened():
        print(f"  ✗ Error al abrir: {input_path.name}")
        return False
    
    # Obtener propiedades originales
    original_fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Nueva tasa de frames (más lenta)
    new_fps = original_fps * speed_factor
    
    # Configurar writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(str(output_path), fourcc, new_fps, (width, height))
    
    processed = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        out.write(frame)
        processed += 1
        
        if processed % 30 == 0:
            progress = (processed / frame_count) * 100
            print(f"    {progress:.1f}%", end='\r')
    
    cap.release()
    out.release()
    print(f"    100.0%")
    return True

def main():
    input_dir = Path(r"c:\Users\andre\OneDrive\Documentos\tesis\test\output\videos")
    output_dir = Path(r"c:\Users\andre\OneDrive\Documentos\tesis\test\output\videos_1")
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    video_files = sorted(input_dir.glob("*.mp4"))
    total = len(video_files)
    
    print(f"📹 {total} videos - velocidad reducida al 75%\n")
    
    for idx, video_path in enumerate(video_files, 1):
        output_path = output_dir / video_path.name
        print(f"[{idx}/{total}] {video_path.name}")
        
        if slow_video(video_path, output_path, speed_factor=0.75):
            print(f"  ✓ Listo\n")
        else:
            print(f"  ✗ Error\n")
    
    print(f"✅ Completado - {output_dir}")

if __name__ == "__main__":
    main()
