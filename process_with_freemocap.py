"""
Procesar yo.mp4 con FreeMoCap y exportar para Blender
"""
import os
from pathlib import Path

print("\n" + "="*70)
print("PROCESANDO yo.mp4 CON FREEMOCAP")
print("="*70)

# Rutas
base_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis")
video_path = base_path / "test" / "output" / "videos" / "yo.mp4"
output_folder = base_path / "freemocap_sessions"

if not video_path.exists():
    print(f"\n❌ Error: No se encontró {video_path}")
    exit(1)

print(f"\n📹 Video: {video_path}")
print(f"📁 Output: {output_folder}")

# Crear carpeta
output_folder.mkdir(exist_ok=True)

print("\n⏳ Iniciando procesamiento...")
print("   Esto puede tardar 5-15 minutos dependiendo de tu PC\n")

try:
    from freemocap.system.paths_and_filenames.path_getters import get_recording_session_folder_path
    from freemocap.core_processes.process_motion_capture_videos.process_motion_capture_videos import (
        process_motion_capture_videos
    )
    
    # Crear sesión
    session_id = "yo_motion"
    session_path = output_folder / session_id
    session_path.mkdir(parents=True, exist_ok=True)
    
    # Copiar video a la carpeta de sesión
    synchronized_videos_folder = session_path / "synchronized_videos"
    synchronized_videos_folder.mkdir(exist_ok=True)
    
    import shutil
    video_dest = synchronized_videos_folder / "yo.mp4"
    if not video_dest.exists():
        print(f"📋 Copiando video a sesión...")
        shutil.copy2(video_path, video_dest)
    
    print(f"✓ Sesión creada: {session_path}")
    
    # Procesar con FreeMoCap
    print(f"\n🎬 Procesando motion capture...")
    print(f"   Detectando: Pose + Hands + Face")
    print(f"   Esto tomará varios minutos...\n")
    
    process_motion_capture_videos(
        session_folder_path=str(session_path),
        use_blender_bone_model=True,
        mediapipe_model_complexity=2,
        run_mediapipe_body_3d=True,
        run_mediapipe_hand_3d=True,
        run_mediapipe_face_3d=False,
    )
    
    print(f"\n✅ Procesamiento completado!")
    
    # Buscar archivos de salida
    output_data_folder = session_path / "output_data"
    
    if output_data_folder.exists():
        print(f"\n📦 Archivos generados:")
        for file in output_data_folder.rglob("*.npy"):
            print(f"   - {file.name}")
        for file in output_data_folder.rglob("*.blend"):
            print(f"   - {file.name} (BLENDER)")
        for file in output_data_folder.rglob("*.fbx"):
            print(f"   - {file.name} (FBX)")
    
    print(f"\n{'='*70}")
    print("✅ PROCESO COMPLETO")
    print(f"{'='*70}")
    print(f"\nSesión guardada en:")
    print(f"  {session_path}")
    print(f"\nDatos de salida en:")
    print(f"  {output_data_folder}")
    
    print(f"\n📖 SIGUIENTE PASO:")
    print(f"1. Abre Blender")
    print(f"2. File > Import > FBX")
    print(f"3. Busca archivos .fbx en: {output_data_folder}")
    print(f"4. Importa el FBX con la animación")
    print(f"5. Usa retargeting para aplicarlo a Nancy")
    print(f"{'='*70}\n")

except ImportError as e:
    print(f"\n❌ Error de importación: {e}")
    print("\nIntentando método alternativo...")
    
    # Método alternativo: Usar comando CLI
    import subprocess
    
    cmd = [
        "python", "-m", "freemocap",
        "process",
        str(video_path),
        "--output-folder", str(output_folder)
    ]
    
    print(f"Ejecutando: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("\n✅ Procesamiento completado via CLI")
        print(result.stdout)
    else:
        print(f"\n❌ Error: {result.stderr}")
        
        print(f"\n{'='*70}")
        print("⚠️  SOLUCIÓN ALTERNATIVA")
        print(f"{'='*70}")
        print(f"""
FreeMoCap es complejo de usar programáticamente.
Te recomiendo usar la GUI:

1. Abre una terminal y ejecuta:
   freemocap

2. En la GUI:
   - Create New Session
   - Single Video
   - Selecciona: {video_path}
   - Process
   - Export to Blender

O usa una herramienta online más simple:
- DeepMotion: https://www.deepmotion.com/animate-3d (GRATIS)
- Rokoko Video: https://www.rokoko.com/products/video (pago)
- Plask: https://plask.ai (freemium)

Sube tu video y descarga el FBX/BVH para Blender.
        """)

except Exception as e:
    print(f"\n❌ Error inesperado: {e}")
    import traceback
    traceback.print_exc()
    
    print(f"\n{'='*70}")
    print("💡 RECOMENDACIÓN")
    print(f"{'='*70}")
    print(f"""
FreeMoCap está diseñado para setup multi-cámara.
Para un solo video, es más fácil usar:

OPCIÓN 1: DeepMotion (Recomendado - GRATIS)
────────────────────────────────────────────
1. Ve a: https://www.deepmotion.com/animate-3d
2. Crea cuenta gratis
3. Sube yo.mp4
4. Descarga FBX
5. Importa en Blender
6. Retargeting automático a Nancy

OPCIÓN 2: Usar nuestros scripts mejorados
──────────────────────────────────────────
Podemos ajustar v12 para que los brazos queden 
en mejor posición. El problema es la calibración
de coordenadas 2D→3D, no el código.

¿Qué prefieres?
    """)
