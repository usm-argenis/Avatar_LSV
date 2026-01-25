"""
Script para procesar videos: ralentizar y mejorar resolución
"""
import os
import subprocess
from pathlib import Path

def process_videos():
    # Rutas
    input_dir = Path(r"c:\Users\andre\OneDrive\Documentos\tesis\test\output\videos")
    output_dir = Path(r"c:\Users\andre\OneDrive\Documentos\tesis\test\output\videos_1")
    
    # Crear carpeta de salida si no existe
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"✓ Carpeta creada: {output_dir}")
    
    # Obtener todos los videos
    video_files = list(input_dir.glob("*.mp4"))
    total = len(video_files)
    
    print(f"\n📹 Encontrados {total} videos para procesar\n")
    
    # Procesar cada video
    for idx, video_path in enumerate(video_files, 1):
        output_path = output_dir / video_path.name
        
        print(f"[{idx}/{total}] Procesando: {video_path.name}")
        
        # FFmpeg command para:
        # 1. Ralentizar video (setpts=1.33*PTS hace 0.75x velocidad = 25% más lento)
        # 2. Mejorar resolución con upscaling a 1920x1080
        # 3. Aumentar bitrate para mejor calidad
        # 4. Aplicar filtros de mejora de imagen
        cmd = [
            'ffmpeg',
            '-i', str(video_path),
            '-vf', 'setpts=1.33*PTS,scale=1920:1080:flags=lanczos,unsharp=5:5:1.0:5:5:0.0',
            '-r', '30',  # 30 fps
            '-c:v', 'libx264',
            '-preset', 'slow',  # Mejor calidad de codificación
            '-crf', '18',  # Calidad alta (menor valor = mejor calidad)
            '-c:a', 'aac',
            '-b:a', '192k',
            '-y',  # Sobrescribir si existe
            str(output_path)
        ]
        
        try:
            # Ejecutar FFmpeg con salida suprimida
            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            if result.returncode == 0:
                print(f"  ✓ Completado: {video_path.name}")
            else:
                print(f"  ✗ Error al procesar {video_path.name}")
                print(f"    {result.stderr[:200]}")
        
        except FileNotFoundError:
            print("\n⚠️  Error: FFmpeg no está instalado o no está en el PATH")
            print("   Instala FFmpeg desde: https://ffmpeg.org/download.html")
            return
        except Exception as e:
            print(f"  ✗ Error inesperado con {video_path.name}: {e}")
    
    print(f"\n✅ Proceso completado!")
    print(f"   Videos originales: {input_dir}")
    print(f"   Videos mejorados: {output_dir}")

if __name__ == "__main__":
    process_videos()
