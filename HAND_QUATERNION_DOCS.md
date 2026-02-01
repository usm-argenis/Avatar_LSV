# SISTEMA DE ANÁLISIS DE ORIENTACIÓN DE MANOS CON CUATERNIONES

## 📋 Descripción

Sistema completo en Python que procesa videos de manos usando **MediaPipe Hands** y calcula orientaciones de la mano completa y cada dedo en forma de **cuaterniones** (qx, qy, qz, qw).

---

## 🧮 Matemática de Cuaterniones

### 1. Sistema de Referencia Local de la Mano

Para calcular la orientación de la mano, primero establecemos un sistema de coordenadas local:

```
Origen (O): Muñeca (landmark 0)

Eje Y (principal): 
  - Vector de muñeca (0) → nudillo dedo medio (9)
  - Dirección principal de la mano
  - Y = normalize(landmark[9] - landmark[0])

Vector auxiliar:
  - Vector de muñeca (0) → nudillo índice (5)
  - Aux = normalize(landmark[5] - landmark[0])

Eje Z (normal a la palma):
  - Producto cruz de Y y auxiliar
  - Z = normalize(Y × Aux)
  - Apunta perpendicular a la palma

Eje X (lateral):
  - Completa el sistema ortogonal derecho
  - X = normalize(Y × Z)
  - Apunta hacia el lado de la mano
```

**Matriz de rotación de la mano:**
```
R_hand = [X | Y | Z]  (columnas = ejes)
```

### 2. Rotaciones de Segmentos de Dedos

Para cada segmento entre articulaciones consecutivas:

```
Eje Y del segmento:
  - Dirección del hueso: point2 - point1
  - Y_seg = normalize(point2 - point1)

Sistema perpendicular:
  - Se construyen ejes X y Z perpendiculares
  - Similar al proceso de la mano completa
```

### 3. Conversión Matriz → Cuaternión

**Fórmula de Shepperd** (implementada en SciPy):

Dada una matriz de rotación R:
```
R = [r00  r01  r02]
    [r10  r11  r12]
    [r20  r21  r22]
```

**Caso general (traza positiva):**
```
qw = sqrt(1 + r00 + r11 + r22) / 2
qx = (r21 - r12) / (4*qw)
qy = (r02 - r20) / (4*qw)
qz = (r10 - r01) / (4*qw)
```

**Cuaternión resultante:**
```
q = (qx, qy, qz, qw)

Propiedades:
- Normalizado: qx² + qy² + qz² + qw² = 1
- Representa rotación pura (sin escala ni traslación)
- qw es la componente escalar (parte real)
- (qx, qy, qz) es la componente vectorial (parte imaginaria)
```

**Interpretación física:**
```
θ = 2 * arccos(qw)        # Ángulo de rotación
eje = (qx, qy, qz) / sin(θ/2)  # Eje de rotación
```

El cuaternión representa una rotación de ángulo θ alrededor del eje.

---

## 📦 Requisitos

Instalar dependencias:

```bash
pip install mediapipe opencv-python scipy numpy
```

O desde el entorno virtual de la tesis:
```bash
cd C:\Users\andre\OneDrive\Documentos\tesis
.venv\Scripts\activate
pip install mediapipe opencv-python scipy
```

---

## 🚀 Uso

### Opción 1: Script Rápido

```python
python process_hand_video.py
```

Editar la ruta del video en el script:
```python
VIDEO_PATH = r"videos\miercoles.mp4"
```

### Opción 2: Uso Programático

```python
from hand_quaternion_analyzer import HandQuaternionAnalyzer

# Crear analizador
analyzer = HandQuaternionAnalyzer("videos/miercoles.mp4")

# Procesar video
results = analyzer.process_video(
    output_json="output/hand_analysis/resultado.json",
    output_csv="output/hand_analysis/resultado.csv",
    visualize=True  # Mostrar video durante procesamiento
)
```

---

## 📊 Formato de Salida

### JSON (estructura completa)

```json
{
  "metadata": {
    "video": "videos/miercoles.mp4",
    "total_frames": 1234,
    "processed_date": "2026-01-31T13:10:00"
  },
  "frames": [
    {
      "frame": 0,
      "timestamp": 0.0,
      "hands": [
        {
          "handedness": "Right",
          "hand": {
            "quaternion": [0.123, -0.456, 0.789, 0.321],
            "origin": [0.5, 0.5, 0.0]
          },
          "fingers": {
            "thumb": [
              [qx, qy, qz, qw],  // Segmento 0→1
              [qx, qy, qz, qw],  // Segmento 1→2
              [qx, qy, qz, qw],  // Segmento 2→3
              [qx, qy, qz, qw]   // Segmento 3→4
            ],
            "index": [...],
            "middle": [...],
            "ring": [...],
            "pinky": [...]
          }
        }
      ]
    }
  ]
}
```

### CSV (formato plano para análisis)

```csv
frame,timestamp,hand_index,handedness,hand_qx,hand_qy,hand_qz,hand_qw,finger,segment,seg_qx,seg_qy,seg_qz,seg_qw
0,0.0,0,Right,0.123,-0.456,0.789,0.321,thumb,0,0.1,0.2,0.3,0.9
0,0.0,0,Right,0.123,-0.456,0.789,0.321,thumb,1,0.15,0.25,0.35,0.88
...
```

---

## 🎯 Estructura de Landmarks MediaPipe

```
0:  WRIST (muñeca) - ORIGEN del sistema de coordenadas

THUMB (pulgar):
  1: CMC (carpometacarpiana)
  2: MCP (metacarpofalángica)
  3: IP (interfalángica)
  4: TIP (punta)

INDEX (índice):
  5: MCP
  6: PIP (interfalángica proximal)
  7: DIP (interfalángica distal)
  8: TIP

MIDDLE (medio):
  9: MCP
  10: PIP
  11: DIP
  12: TIP

RING (anular):
  13: MCP
  14: PIP
  15: DIP
  16: TIP

PINKY (meñique):
  17: MCP
  18: PIP
  19: DIP
  20: TIP
```

---

## 🔧 Configuración del Sistema

### Parámetros de MediaPipe

```python
mp_hands.Hands(
    static_image_mode=False,      # False para video, True para imágenes
    max_num_hands=2,               # Máximo de manos a detectar
    min_detection_confidence=0.5,  # Umbral detección inicial
    min_tracking_confidence=0.5,   # Umbral seguimiento entre frames
    model_complexity=1             # 0=lite, 1=full (más preciso)
)
```

### Optimización de Rendimiento

- `visualize=False`: Procesamiento ~2-3x más rápido sin ventana
- `model_complexity=0`: Detección más rápida pero menos precisa
- Reducir resolución del video para procesamiento más rápido

---

## 📐 Validación de Cuaterniones

Los cuaterniones generados cumplen:

1. **Normalización**: qx² + qy² + qz² + qw² ≈ 1.0
2. **Continuidad**: Cambios suaves entre frames consecutivos
3. **Ortogonalidad**: Matrices de rotación son ortogonales (det=1)

Para verificar:
```python
import numpy as np

quat = [qx, qy, qz, qw]
norm = np.linalg.norm(quat)
print(f"Norma del cuaternión: {norm:.6f}")  # Debe ser ≈ 1.0
```

---

## 🐛 Casos Especiales Manejados

1. **Segmentos degenerados**: Si dos puntos son idénticos, retorna cuaternión identidad
2. **Vectores paralelos**: Usa vectores alternativos para evitar divisiones por cero
3. **Frames sin manos**: Genera entrada con cuaternión identidad [0,0,0,1]
4. **Múltiples manos**: Procesa ambas manos independientemente

---

## 📈 Ejemplo de Análisis

```python
# Cargar resultados
import json

with open('output/hand_analysis/miercoles_hands.json') as f:
    data = json.load(f)

# Analizar frame específico
frame_30 = data['frames'][30]
if frame_30['hands']:
    hand = frame_30['hands'][0]
    
    # Cuaternión de la mano completa
    hand_quat = hand['hand']['quaternion']
    print(f"Orientación mano: {hand_quat}")
    
    # Cuaterniones del dedo índice
    index_quats = hand['fingers']['index']
    print(f"Segmentos índice: {len(index_quats)}")
    for i, quat in enumerate(index_quats):
        print(f"  Segmento {i}: {quat}")
```

---

## 🎬 Controles Durante Visualización

- **Q**: Salir del procesamiento
- **ESC**: Salir del procesamiento
- La ventana muestra:
  - Landmarks de la mano dibujados
  - Número de frame actual
  - Cantidad de manos detectadas

---

## 📝 Notas Importantes

1. **Coordenadas de MediaPipe**: 
   - X: [0, 1] de izquierda a derecha
   - Y: [0, 1] de arriba a abajo
   - Z: Profundidad relativa a la muñeca

2. **Handedness**: 
   - "Left" o "Right" desde la perspectiva de la persona en el video
   - No desde la perspectiva de la cámara

3. **Estabilidad**:
   - MediaPipe aplica suavizado temporal automático
   - Los cuaterniones pueden tener pequeñas variaciones entre frames similares

4. **Rendimiento**:
   - ~30 FPS en video 720p con visualización
   - ~60 FPS sin visualización
   - Depende del hardware (GPU recomendada)

---

## 🔗 Referencias

- **MediaPipe Hands**: https://google.github.io/mediapipe/solutions/hands.html
- **Cuaterniones**: https://en.wikipedia.org/wiki/Quaternion
- **SciPy Rotations**: https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Rotation.html
- **Algoritmo de Shepperd**: Shepperd, S.W. (1978). "Quaternion from rotation matrix"
