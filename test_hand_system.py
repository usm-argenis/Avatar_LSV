"""
TEST RÁPIDO: Verificar que el sistema funciona
"""

import sys
print("Verificando imports...")

try:
    import cv2
    print("✅ OpenCV importado correctamente")
except Exception as e:
    print(f"❌ Error con OpenCV: {e}")
    sys.exit(1)

try:
    import mediapipe as mp
    print("✅ MediaPipe importado correctamente")
except Exception as e:
    print(f"❌ Error con MediaPipe: {e}")
    sys.exit(1)

try:
    import numpy as np
    print(f"✅ NumPy {np.__version__} importado correctamente")
except Exception as e:
    print(f"❌ Error con NumPy: {e}")
    sys.exit(1)

try:
    from scipy.spatial.transform import Rotation
    print("✅ SciPy Rotation importado correctamente")
except Exception as e:
    print(f"❌ Error con SciPy: {e}")
    sys.exit(1)

# Verificar video
from pathlib import Path
video_path = Path("videos/miercoles.mp4")
if video_path.exists():
    print(f"✅ Video encontrado: {video_path}")
    cap = cv2.VideoCapture(str(video_path))
    if cap.isOpened():
        fps = cap.get(cv2.CAP_PROP_FPS)
        frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f"   FPS: {fps}, Frames: {frames}")
        cap.release()
    else:
        print(f"⚠️  No se puede abrir el video")
else:
    print(f"❌ Video NO encontrado: {video_path}")

print("\n🎉 Todos los componentes están listos!")
print("Ejecuta: python process_hand_video.py")
