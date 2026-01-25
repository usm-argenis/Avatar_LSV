# 🎬 Segmentador de Videos

Script en Python para cortar múltiples segmentos de un video especificando inicio y fin en segundos.

## 📋 Requisitos

- Python 3.7 o superior
- moviepy

## 🚀 Instalación

1. **Instala las dependencias:**

```bash
pip install -r requirements.txt
```

O manualmente:

```bash
pip install moviepy
```

## 💡 Uso

### **Opción 1: Modo Interactivo** (Recomendado)

Ejecuta el script y sigue las instrucciones:

```bash
python segmentar_video.py
```

El script te pedirá:
1. Ruta del video original
2. Carpeta donde guardar los segmentos
3. Cantidad de segmentos a crear
4. Para cada segmento:
   - Segundo de inicio
   - Segundo de fin
   - Nombre del segmento

### **Opción 2: Editar el Script**

Abre `segmentar_video.py` y modifica la función `ejemplo_uso()`:

```python
VIDEO_ORIGINAL = "mi_video.mp4"  # Tu video

segmentos = [
    {"inicio": 0, "fin": 5, "nombre": "letra_a"},
    {"inicio": 10, "fin": 15, "nombre": "letra_b"},
    {"inicio": 20, "fin": 25, "nombre": "letra_c"},
]

CARPETA_SALIDA = "videos_segmentados"
```

Luego ejecuta:

```bash
python segmentar_video.py
```

### **Opción 3: Importar como Módulo**

Crea tu propio script:

```python
from segmentar_video import segmentar_video

segmentar_video(
    video_path="lengua_senas.mp4",
    segmentos=[
        {"inicio": 0, "fin": 3, "nombre": "hola"},
        {"inicio": 5, "fin": 8, "nombre": "adios"},
        {"inicio": 10, "fin": 13, "nombre": "gracias"},
    ],
    carpeta_salida="senas"
)
```

## 📝 Formato de Segmentos

Cada segmento es un diccionario con:

- **inicio** (float): Segundo donde empieza el corte
- **fin** (float): Segundo donde termina el corte
- **nombre** (str): Nombre del archivo de salida (sin extensión)

```python
{
    "inicio": 10.5,    # Inicia en el segundo 10.5
    "fin": 15.0,       # Termina en el segundo 15
    "nombre": "mi_clip" # Se guardará como mi_clip.mp4
}
```

## 📂 Estructura de Salida

```
video/
├── segmentar_video.py
├── requirements.txt
├── README.md
├── mi_video.mp4          # Video original
└── output/               # Carpeta de salida (se crea automáticamente)
    ├── segmento1.mp4
    ├── segmento2.mp4
    └── segmento3.mp4
```

## 🎯 Ejemplos de Uso

### Ejemplo 1: Cortar letras del alfabeto

```python
segmentos = [
    {"inicio": 0, "fin": 2, "nombre": "letra_a"},
    {"inicio": 2, "fin": 4, "nombre": "letra_b"},
    {"inicio": 4, "fin": 6, "nombre": "letra_c"},
    {"inicio": 6, "fin": 8, "nombre": "letra_d"},
    {"inicio": 8, "fin": 10, "nombre": "letra_e"},
]
```

### Ejemplo 2: Cortar palabras completas

```python
segmentos = [
    {"inicio": 0, "fin": 5, "nombre": "hola"},
    {"inicio": 10, "fin": 18, "nombre": "buenos_dias"},
    {"inicio": 25, "fin": 30, "nombre": "gracias"},
]
```

### Ejemplo 3: Con decimales (precisión)

```python
segmentos = [
    {"inicio": 0.5, "fin": 3.2, "nombre": "intro"},
    {"inicio": 5.8, "fin": 12.4, "nombre": "contenido"},
    {"inicio": 15.0, "fin": 18.5, "nombre": "final"},
]
```

## ⚙️ Características

✅ Corta múltiples segmentos de un solo video
✅ Especifica inicio y fin en segundos (admite decimales)
✅ Nombra cada segmento individualmente
✅ Valida automáticamente los tiempos
✅ Crea la carpeta de salida automáticamente
✅ Barra de progreso para cada segmento
✅ Formato de salida: MP4 (H.264 + AAC)

## 🔧 Solución de Problemas

### Error: "No module named 'moviepy'"
```bash
pip install moviepy
```

### El video no se procesa
- Verifica que la ruta del video sea correcta
- Asegúrate de que el formato sea compatible (MP4, AVI, MOV, etc.)

### Los tiempos de corte son incorrectos
- Usa un reproductor de video para verificar los segundos exactos
- Puedes usar decimales para mayor precisión (ej: 10.5 segundos)

## 📊 Formatos Soportados

**Entrada:** MP4, AVI, MOV, MKV, FLV, WMV, etc.
**Salida:** MP4 (H.264 video + AAC audio)

## 🎓 Uso para Lengua de Señas

Ideal para:
- Cortar videos de señas individuales
- Segmentar lecciones largas
- Crear biblioteca de clips de señas
- Preparar material educativo

---

**Creado para el proyecto de tesis de Lengua de Señas Venezolana**
