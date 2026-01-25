# Detalles técnicos

Este documento describe los formatos intermedios, las transformaciones aplicadas y las opciones disponibles en los scripts.

1) Formato de salida de `coordenates.py` (pose JSON)
- Estructura principal:

```json
{
  "fps": 30.0,
  "frames": [
    {"frame_index": 0, "pose": [[x,y,z],...], "left_hand": [...], "right_hand": [...], "face": [...]},
    ...
  ],
  "frames_extracted": 123
}
```

- `pose` es una lista de hasta 33 landmarks de MediaPipe, cada uno [x,y,z] en coordenadas normalizadas (x,y en 0..1 respecto imagen, z es relativo).

2) `build_eskeleton.py` — mapeo y transformaciones
- Mapea landmarks de MediaPipe a 16 huesos (ver `MP` dictionary dentro del script).
- Transformación aplicada por defecto (convert_coord):
  - x' = (x - 0.5) * scale
  - y' = -(y - 0.5) * scale
  - z' = -z * scale

- Opciones nuevas:
  - `--normalize-hips`: traslada todas las posiciones para que `hips` (bone 0) del primer frame tenga Y=0.
  - `--smooth-window N`: aplica media móvil de ventana N sobre cada joint para suavizar movimientos.
  - `--inflate F`: desplaza cada joint una fracción F adicional en la dirección desde su padre hacia él.

3) `convert_to_signavatar.py`
- Toma un skeleton JSON (con `frames` y `positions`) y crea un objeto SignAvatar con `bones`, `fps` y `frames`.
- Evita volver a escalar si detecta que las posiciones ya están en unidades de mundo (magnitud > 1.5).

4) Viewer (`test/viewer.js`)
- Espera un JSON SignAvatar con estructura:

```json
{
  "bones": [{"name":"hips","parent":-1}, ...],
  "fps": 30.0,
  "frames": [{"time":0.0, "positions":[[x,y,z], ...]}, ...]
}
```

- `autoFitCamera()` calcula el bounding box de un muestreo de frames y sitúa la cámara para que la caja entre en vista. Esto ayuda cuando el esqueleto estaba fuera o muy alejado.

5) Recomendaciones para ajustes
- Si el movimiento parece "aplastado" en Y o invertido, revisa la función `convert_coord` en `build_eskeleton.py` y la convención del viewer; podemos cambiar la señal de `z` o `y` si hace falta.
- Para evitar que las articulaciones se crucen o queden pegadas, usa `--inflate 0.01` a `0.05` según tu preferencia.
- Para suavizar ruido en landmarks, `--smooth-window 3` o `5` suele ayudar.

6) Ejemplo de pipeline para procesar una carpeta completa
- Puedes ejecutar un pequeño bucle PowerShell para procesar todos los mp4 en `data/reels`:

```powershell
Get-ChildItem -Path .\data\reels -Filter *.mp4 | ForEach-Object {
  python test/run_pipeline.py --video $_.FullName --max-frames 300 --normalize-hips --smooth-window 3 --inflate 0.02
}
```

7) Archivo `.env`
- Opcionalmente `convert_to_signavatar.py` lee `TEST_VIDEO_PATH` desde `.env` y usa el basename para escoger `data/skeletons/<basename>_skel.json`.

Si quieres que añada un CSV de resumen por video (frames, ranges, fps), lo genero automáticamente cuando ejecutes el pipeline.

Fin del documento técnico.
