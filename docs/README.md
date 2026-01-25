# Proyecto: Pipeline de conversión a SignAvatar y visualizador

Este repositorio contiene una pipeline para extraer landmarks desde un video, construir un "nano-esqueleto" (16 huesos), convertirlo al formato SignAvatar y visualizarlo con Three.js. Estos documentos explican lo que se hizo, cómo reproducirlo y cómo ajustar parámetros para mejorar la visualización.

Archivos clave
- `test/coordenates.py`: extractor de landmarks usando MediaPipe Holistic + OpenCV. Genera JSON con estructura { fps, frames: [{frame_index, pose, left_hand, right_hand, face}, ...] }.
- `test/build_eskeleton.py`: construye el nano-esqueleto (16 huesos) desde el JSON de poses. Ahora acepta flags para normalizar y suavizar las posiciones.
- `test/convert_to_signavatar.py`: convierte el skeleton al formato SignAvatar (archivo con `bones`, `fps`, `frames`). Evita volver a escalar coordenadas ya convertidas.
- `test/viewer.js` y `test/index.html`: visualizador Three.js con auto-fit y botón "Recenter".
- `test/run_pipeline.py`: script central que ejecuta extractor -> builder -> converter en secuencia para un video.

Resultados logrados
- Extracción de poses desde `estacion.mp4`.
- Generación de `data/skeletons/estacion_skel.json` y `test/output/estacion_signavatar.json`.
- Visualizador funcional que centra y muestra el nano-esqueleto.

Dependencias
- Python 3.8+.
- Paquetes: `opencv-python`, `mediapipe` (solo necesarios para `coordenates.py`).
- Navegador moderno para el viewer (Three.js desde CDN).

Ejecución rápida
1) Activar entorno (si tienes uno):

```powershell
& C:\path\to\venv\Scripts\Activate.ps1
```

2) Ejecutar el pipeline para un video:

```powershell
python test/run_pipeline.py --video "C:\Users\andre\OneDrive\Documentos\tesis\data\reels\estacion.mp4" --max-frames 300 --normalize-hips --smooth-window 3 --inflate 0.02
```

3) Servir y abrir el viewer:

```powershell
cd "C:\Users\andre\OneDrive\Documentos\tesis\test"
python -m http.server 8000
# Abrir: http://localhost:8000/
```

Controles
- Botón "Recenter" en la esquina superior derecha para volver a centrar la cámara.
- Logs en la consola del navegador muestran bones, frames y auto-fit info.

Próximos pasos recomendados
- Añadir UI (sliders) para ajustar escala/inflate/velocidad en tiempo real.
- Añadir modo lado-a-lado con el video sincronizado para comparar movimiento.
- Automatizar el procesamiento batch de una carpeta de videos.

Fin del README
