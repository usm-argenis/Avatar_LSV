# 🚀 Sistema de Generación de Animaciones 3D para Lengua de Señas Venezolana

Sistema inteligente que genera automáticamente animaciones 3D de señas a partir de texto en español.

## 📋 Características

- ✅ **Traducción automática**: Convierte texto en español a secuencias de señas
- ✅ **Generación de animaciones**: Crea animaciones 3D fluidas con interpolación
- ✅ **Suavizado inteligente**: Aplica filtros Savitzky-Golay para transiciones naturales
- ✅ **Coincidencia difusa**: Encuentra señas similares usando distancia de Levenshtein
- ✅ **Extensible**: Fácil de agregar nuevas señas al diccionario
- ✅ **Pipeline completo**: Texto → Señas → Keyframes → Animación → Exportación

## 🏗️ Arquitectura

```
src/
├── ai/
│   └── motion_generator.py    # Motor de generación de animaciones
├── api/
│   └── translator.py          # Traductor español → LSV
├── data/
│   └── keypoints/             # Base de datos de señas
│       ├── hola.json
│       └── gracias.json
├── render/                     # Renderizador Three.js (futuro)
├── main.py                     # Script principal
└── requirements.txt           # Dependencias
```

## 🚦 Inicio Rápido

### 1. Instalación

```bash
# Instalar dependencias
pip install -r requirements.txt
```

**Dependencias principales:**
- numpy >= 1.24.0
- scipy >= 1.10.0
- pandas >= 2.0.0
- matplotlib >= 3.7.0

### 2. Uso Básico

#### Modo Prueba (automático)
```bash
python main.py
```

#### Modo Interactivo
```bash
python main.py --mode interactive
```

O simplemente ejecutar:
```bash
ejecutar_interactivo.bat   # Windows
```

### 3. Uso desde Código

```python
from ai.motion_generator import MotionGenerator
from api.translator import SignTranslator

# Inicializar
translator = SignTranslator()
generator = MotionGenerator(keypoints_dir="data/keypoints")

# Generar animación
animation = generator.generate_from_text(
    "hola gracias",
    output_path="mi_animacion.json"
)
```

## 📊 Pipeline de Procesamiento

```
Texto de entrada
      ↓
[SignTranslator]
      ↓
Secuencia de señas
      ↓
[MotionGenerator.sequence_to_keyframes]
      ↓
Keyframes base
      ↓
[MotionGenerator._create_blend]
      ↓
Interpolación cúbica
      ↓
[MotionGenerator.generate_animation]
      ↓
Suavizado Savitzky-Golay
      ↓
[MotionGenerator.export_glb]
      ↓
Archivo JSON/GLB
```

## 🎯 Componentes Principales

### 1. MotionGenerator

Clase principal para generación de animaciones 3D.

**Métodos:**
- `text_to_sign_sequence(text)`: Texto → lista de señas
- `sequence_to_keyframes(signs)`: Señas → keyframes 3D
- `_create_blend(kf1, kf2, frames)`: Interpolación entre keyframes
- `generate_animation(keyframes, smooth)`: Genera animación suavizada
- `export_glb(animation, path)`: Exporta a JSON/GLB
- `generate_from_text(text, output_path)`: Pipeline completo

**Características:**
- FPS: 30 frames por segundo
- Blend frames: 10 frames de transición entre señas
- Interpolación: Spline cúbica
- Suavizado: Savitzky-Golay (ventana=5, orden=2)

### 2. SignTranslator

Traductor de español a Lengua de Señas Venezolana.

**Métodos:**
- `translate(text)`: Traduce texto completo
- `add_word(word, sign, category)`: Agrega nueva seña
- `save_dictionary(path)`: Guarda diccionario personalizado

**Diccionario base (39 palabras):**
- **Saludos**: hola, buenos, dias, tardes, noches, adios
- **Cortesía**: gracias, favor, por, perdon, disculpa
- **Pronombres**: yo, tu, el, ella, nosotros, ustedes
- **Familia**: mama, papa, hermano, hermana, hijo, hija, abuelo, abuela
- **Verbos**: ir, venir, hacer, ver, comer, beber, dormir, trabajar
- **Números**: 0-10 (cero, uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez)

## 📁 Formato de Keypoints

Los archivos JSON de keypoints siguen esta estructura:

```json
{
  "sign_name": "hola",
  "duration": 1.5,
  "fps": 30,
  "category": "saludo",
  "keyframes": [
    {
      "frame": 0,
      "time": 0.0,
      "pose": {
        "right_hand": {
          "x": 0.0, "y": 1.2, "z": 0.3,
          "rotation_x": 0.0, "rotation_y": 0.0, "rotation_z": 0.0
        },
        "right_arm": {
          "elbow_angle": 90.0,
          "shoulder_angle": 45.0
        },
        "head": {
          "rotation_x": 0.0,
          "rotation_y": 0.0,
          "rotation_z": 0.0
        }
      }
    }
  ]
}
```

## ➕ Agregar Nuevas Señas

### 1. Crear archivo de keypoints

```bash
# Crear archivo en data/keypoints/
data/keypoints/adios.json
```

### 2. Definir keyframes

```json
{
  "sign_name": "adios",
  "duration": 2.0,
  "fps": 30,
  "category": "saludo",
  "keyframes": [
    // ... definir poses en frames clave
  ]
}
```

### 3. Actualizar diccionario

```python
translator = SignTranslator()
translator.add_word("adios", "adios", "saludo")
translator.save_dictionary("mi_diccionario.json")
```

## 🔧 Configuración Avanzada

### Ajustar parámetros de suavizado

```python
generator = MotionGenerator(
    keypoints_dir="data/keypoints",
    fps=60,                    # Mayor FPS = más fluido
    blend_frames=15            # Más frames de transición
)
```

### Personalizar interpolación

```python
# En motion_generator.py, línea 245
from scipy.interpolate import CubicSpline

# Cambiar por otras opciones:
# - interp1d (lineal, cuadrática)
# - PchipInterpolator (monotónica)
# - Akima1DInterpolator (suave)
```

## 📈 Resultados de Prueba

```
✅ "hola"          → 4 frames, 0.13s
✅ "gracias"       → 4 frames, 0.13s
✅ "hola gracias"  → 18 frames, 0.60s (con interpolación)
```

## 🚀 Próximos Pasos

### Fase 1: Expansión de Datos
- [ ] Agregar alfabeto completo (A-Z)
- [ ] Agregar números (11-100)
- [ ] Agregar 100+ palabras comunes
- [ ] Frases completas pre-definidas

### Fase 2: Exportación GLB
- [ ] Instalar pygltflib o trimesh
- [ ] Implementar conversión JSON → GLB
- [ ] Agregar modelo 3D de avatar
- [ ] Optimizar tamaño de archivos

### Fase 3: Visualización
- [ ] Crear renderizador Three.js
- [ ] Integrar con WebView de app móvil
- [ ] Controles de reproducción (play, pause, velocidad)
- [ ] Cambio de avatar

### Fase 4: Deep Learning
- [ ] Entrenar modelo seq2seq para generar keypoints
- [ ] Dataset: 1000+ señas anotadas
- [ ] Transfer learning desde ASL/LSM
- [ ] Generación automática sin keypoints manuales

### Fase 5: Integración
- [ ] API REST con FastAPI
- [ ] Endpoint: POST /generate {"text": "hola"}
- [ ] Conectar con app React Native
- [ ] Cache de animaciones generadas
- [ ] CDN para archivos GLB

## 🛠️ Solución de Problemas

### Error: "No module named 'numpy'"
```bash
pip install numpy scipy pandas matplotlib tqdm
```

### Error: "Seña no encontrada"
El sistema usa coincidencia difusa. Si una palabra no existe:
1. Se busca la más similar
2. Si no hay coincidencia cercana, se deletrea letra por letra

### Error: "Archivo GLB no se genera"
Actualmente el sistema exporta a JSON. Para GLB:
```bash
pip install pygltflib
# Descomentar código GLB en motion_generator.py línea 295
```

## 📚 Recursos Adicionales

- **Documentación LSV**: [Instituto Venezolano de la Audición y el Lenguaje](https://ival.org.ve)
- **Three.js Docs**: https://threejs.org/docs/
- **Scipy Interpolation**: https://docs.scipy.org/doc/scipy/tutorial/interpolate.html
- **GLB Format**: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html

## 📄 Licencia

Este proyecto es parte de una tesis de grado para la Universidad Santa María.

## 🤝 Contribuciones

Para agregar nuevas señas al diccionario, por favor:
1. Crear archivo JSON con keypoints
2. Validar formato con `main.py`
3. Documentar movimiento de la seña
4. Probar con frases de ejemplo

## 📞 Soporte

Para preguntas o problemas:
1. Verificar que todas las dependencias estén instaladas
2. Ejecutar `python main.py` para pruebas básicas
3. Revisar archivos de salida en la carpeta `src/`

---

**Versión:** 1.0.0  
**Última actualización:** 2024  
**Mantenedor:** @usm-argenis
