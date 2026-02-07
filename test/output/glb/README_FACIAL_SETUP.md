# 🎭 Sistema de Animación Facial ARKit para Blender 4.5+

Scripts de Python para agregar controles de emociones faciales a personajes importados desde DeepMotion (formato GLB).

---

## 📁 Archivos

```
test/output/glb/
├── setup_facial_emotions_arkit.py    # Script principal: configura emociones
├── inspect_arkit_shapekeys.py        # Script auxiliar: inspecciona blendshapes
├── README_FACIAL_SETUP.md            # Esta guía
└── [Archivos GLB de DeepMotion]      # Modelos animados
```

---

## 🎯 ¿Qué hace este sistema?

Agrega **6 controles maestros** (sliders) al Armature de tu personaje para controlar expresiones faciales de manera intuitiva:

| Control Maestro       | Emoción              | Blendshapes Controlados                                    |
|-----------------------|----------------------|------------------------------------------------------------|
| `EMOTION_SORPRESA`    | Pregunta/Asombro     | BrowInnerUp, BrowOuterUpLeft/Right, EyeWideLeft/Right      |
| `EMOTION_IRA`         | Enojo/Tensión        | BrowDownLeft/Right, MouthFrownLeft/Right                   |
| `EMOTION_ALEGRIA`     | Sonrisa/Risa         | MouthSmileLeft/Right, CheekPuff                            |
| `EMOTION_ASCO`        | Desaprobación        | NoseSneerLeft/Right, MouthUpperUpLeft/Right                |
| `EMOTION_TRISTEZA`    | Pena/Preocupación    | MouthDimpleLeft/Right, MouthLowerDownLeft/Right            |
| `BLINK_CONTROL`       | Parpadeo             | EyeBlinkLeft/Right                                         |

**Valor de cada control**: 0.0 (sin efecto) a 1.0 (efecto completo)

---

## 🚀 GUÍA PASO A PASO

### PASO 1: Verificar tu Modelo GLB (OPCIONAL)

Antes de configurar emociones, puedes inspeccionar qué blendshapes tiene tu modelo:

**1. Abrir Blender 4.5+**

**2. Importar modelo GLB:**
   - File → Import → glTF 2.0 (.glb/.gltf)
   - Seleccionar cualquier archivo de esta carpeta (ej: `Remy_resultado_b.glb`)
   - Import

**3. Abrir Scripting workspace:**
   - Clic en pestaña "Scripting" (arriba)

**4. Cargar script de inspección:**
   - Text → Open
   - Seleccionar: `inspect_arkit_shapekeys.py`

**5. Ejecutar:**
   - Alt+P o botón "Run Script"

**6. Ver reporte en consola:**
   - Window → Toggle System Console (en Windows)
   - O ver output en Blender Console

**Resultado esperado:**
```
🔍 INSPECTOR DE SHAPE KEYS ARKit - DeepMotion GLB
==================================================================
✅ Malla encontrada: 'Wolf3D_Head'

📊 SHAPE KEYS ENCONTRADOS
==================================================================
Total: 52 Shape Keys

✅ ARKit Shape Keys (48):
  1. BrowDownLeft
  2. BrowDownRight
  3. BrowInnerUp
  ...

📊 VERIFICACIÓN DE EMOCIONES
==================================================================
EMOTION_SORPRESA:
  Estado: ✅ COMPLETO (100%)
  Presentes: 5/5
...
```

---

### PASO 2: Configurar Controles de Emociones

**1. Si no lo hiciste en PASO 1, importar modelo GLB:**
   - File → Import → glTF 2.0
   - Seleccionar archivo GLB
   - Import

**2. Abrir Scripting workspace**

**3. Cargar script principal:**
   - Text → Open
   - Seleccionar: `setup_facial_emotions_arkit.py`

**4. Ejecutar script:**
   - Alt+P o "Run Script"

**5. Ver confirmación en consola:**
```
🎭 SETUP DE EMOCIONES FACIALES - ARKit Blendshapes
==================================================================
✅ Armature encontrado: 'Armature'
🎉 Malla facial encontrada: 'Wolf3D_Head'

📝 Creando propiedades personalizadas...
  ✓ Creada: EMOTION_SORPRESA (Pregunta/Asombro)
  ✓ Creada: EMOTION_IRA (Enojo/Tensión)
  ✓ Creada: EMOTION_ALEGRIA (Sonrisa/Risa)
  ✓ Creada: EMOTION_ASCO (Desaprobación)
  ✓ Creada: EMOTION_TRISTEZA (Pena/Preocupación)
  ✓ Creada: BLINK_CONTROL (Parpadeo)

🔗 Configurando drivers...
  Control: EMOTION_SORPRESA
    ✓ BrowInnerUp
    ✓ BrowOuterUpLeft
    ✓ BrowOuterUpRight
    ✓ EyeWideLeft
    ✓ EyeWideRight
  Conectados: 5/5
...

✅ SETUP COMPLETADO
Drivers creados: 24
```

---

### PASO 3: Usar los Controles

**1. Seleccionar el Armature:**
   - Clic en "Armature" en el Outliner (panel derecho)

**2. Abrir Object Properties:**
   - Panel derecho → Ícono de cubo naranja (Object Properties)

**3. Scroll down hasta "Custom Properties"**

**4. Verás los 6 sliders:**
   - EMOTION_SORPRESA
   - EMOTION_IRA
   - EMOTION_ALEGRIA
   - EMOTION_ASCO
   - EMOTION_TRISTEZA
   - BLINK_CONTROL

**5. Ajustar valores (0.0 a 1.0):**
   - Arrastra los sliders
   - O haz clic para ingresar valor numérico
   - ¡Los cambios se ven en tiempo real en el viewport!

**Ejemplo:**
```
EMOTION_ALEGRIA = 0.8  → Sonrisa amplia
BLINK_CONTROL = 1.0    → Ojos cerrados
EMOTION_SORPRESA = 0.5 → Cejas levemente levantadas
```

---

### PASO 4: Animar las Emociones (OPCIONAL)

Puedes animar estos controles con keyframes:

**1. Seleccionar Armature**

**2. En Custom Properties, hacer hover sobre un slider:**
   - Clic derecho → "Insert Keyframe"

**3. Mover en el Timeline (frame 30 por ejemplo)**

**4. Cambiar valor del slider**

**5. Clic derecho → "Insert Keyframe" de nuevo**

**6. ¡Ahora la emoción se anima suavemente!**

**7. Presionar ESPACIO para reproducir**

---

## 🎬 Casos de Uso

### Caso 1: Personaje sorprendido

```
EMOTION_SORPRESA = 1.0
BLINK_CONTROL = 0.0
(Resto en 0.0)
```

### Caso 2: Sonrisa feliz

```
EMOTION_ALEGRIA = 0.9
EMOTION_SORPRESA = 0.2  (ojos levemente abiertos)
(Resto en 0.0)
```

### Caso 3: Expresión triste

```
EMOTION_TRISTEZA = 0.8
EMOTION_IRA = 0.2  (cejas levemente caídas)
(Resto en 0.0)
```

### Caso 4: Disgusto

```
EMOTION_ASCO = 1.0
EMOTION_IRA = 0.3
(Resto en 0.0)
```

### Caso 5: Parpadeo rápido

**Animar BLINK_CONTROL:**
```
Frame 0:  BLINK_CONTROL = 0.0
Frame 2:  BLINK_CONTROL = 1.0
Frame 4:  BLINK_CONTROL = 0.0
```

---

## 🔧 Detalles Técnicos

### Cómo funciona

1. **Custom Properties**: Se crean 6 propiedades flotantes en el Armature (rango 0.0-1.0)

2. **Drivers**: Cada propiedad controla múltiples Shape Keys vía drivers
   - Driver Type: `AVERAGE`
   - Expression: `emotion_value` (1:1 mapping)
   - Cuando slider = 1.0 → Shape Key value = 1.0

3. **ARKit Blendshapes**: El script asume que el modelo GLB tiene blendshapes compatibles con ARKit Face Tracking

### Requisitos del Modelo GLB

Para que el script funcione correctamente, el modelo debe:

- ✅ Estar importado desde DeepMotion
- ✅ Tener un Armature
- ✅ Tener una malla con Shape Keys ARKit
- ✅ La malla debe llamarse con "Face" o "Head" en el nombre (o tener Shape Keys)

### Shape Keys ARKit Utilizados

El script usa estos 24 blendshapes del estándar ARKit:

**Cejas (7):**
- BrowInnerUp, BrowDownLeft, BrowDownRight
- BrowOuterUpLeft, BrowOuterUpRight

**Ojos (4):**
- EyeWideLeft, EyeWideRight
- EyeBlinkLeft, EyeBlinkRight

**Boca (11):**
- MouthSmileLeft, MouthSmileRight
- MouthFrownLeft, MouthFrownRight
- MouthDimpleLeft, MouthDimpleRight
- MouthUpperUpLeft, MouthUpperUpRight
- MouthLowerDownLeft, MouthLowerDownRight

**Mejillas (1):**
- CheekPuff

**Nariz (2):**
- NoseSneerLeft, NoseSneerRight

---

## 🐛 Troubleshooting

### "No se encontró Armature"

**Problema**: El modelo no tiene un objeto de tipo Armature

**Solución**: 
- Verificar en Outliner que existe "Armature"
- Si está oculto, hacerlo visible
- Si no existe, el modelo no tiene rig

### "No se encontró malla facial"

**Problema**: No hay mesh con Shape Keys

**Solución**:
- Ejecutar `inspect_arkit_shapekeys.py` primero
- Verificar que el mesh tenga Shape Keys
- En Outliner → Mesh → Shape Keys panel

### "Shape Key 'XXX' no encontrado"

**Problema**: El modelo no tiene todos los blendshapes ARKit

**Solución**:
- Esto es normal, algunos modelos no tienen todos
- El script crea drivers solo para los presentes
- Ejecutar inspector para ver coverage

### "Los sliders no cambian la cara"

**Problema**: Drivers no funcionan

**Solución**:
1. Verificar que estás viendo la malla facial en viewport
2. Seleccionar mesh facial → Shape Keys panel
3. Ver si los valores de Shape Keys cambian al mover sliders
4. Si no, ejecutar script de nuevo

### "No veo Custom Properties"

**Problema**: Armature no seleccionado o panel cerrado

**Solución**:
1. Seleccionar "Armature" en Outliner
2. Panel derecho → Object Properties (cubo naranja)
3. Scroll down
4. Expandir "Custom Properties"

---

## 📊 Verificación Rápida

Para verificar que el setup funcionó:

**1. Seleccionar Armature**

**2. Object Properties → Custom Properties**

**3. Mover slider BLINK_CONTROL a 1.0**
   - Los ojos deben cerrarse

**4. Mover EMOTION_ALEGRIA a 1.0**
   - Debe aparecer sonrisa

**Si ambos funcionan:** ✅ Setup exitoso

**Si no funcionan:** Ver Troubleshooting arriba

---

## 🎯 Modelos GLB Disponibles

En esta carpeta tienes ~40 modelos GLB de Remy con diferentes animaciones LSV:

- `Remy_resultado_b.glb` (letra B)
- `Remy_resultado_c.glb` (letra C)
- `Remy_resultado_yo.glb` (pronombre YO)
- `Remy_resultado_ustedes.glb` (pronombre USTEDES)
- ... y más

**Puedes aplicar el setup a cualquiera:**
1. Importar GLB
2. Ejecutar `setup_facial_emotions_arkit.py`
3. ¡Listo!

---

## 💡 Tips Avanzados

### Combinar emociones

Puedes mezclar múltiples emociones:
```
EMOTION_ALEGRIA = 0.5    (sonrisa leve)
EMOTION_SORPRESA = 0.7   (ojos abiertos)
= Expresión de sorpresa feliz
```

### Animar sincronización labial

Para habla:
1. Importar audio: Add → Sound → Sound
2. Animar BLINK_CONTROL para parpadeos naturales
3. Usar otros controles para emociones durante diálogo

### Exportar con emociones

1. Configurar keyframes en las emociones
2. File → Export → FBX
3. ✅ Bake Animation
4. El FBX tendrá las animaciones faciales

### Crear presets de emociones

Guardar combinaciones comunes:
- En Custom Properties, guardar valores
- Tomar screenshot para referencia
- O crear poses guardadas con Pose Library addon

---

## 📚 Referencias

- **ARKit Face Tracking**: Estándar de Apple para blendshapes faciales
- **DeepMotion**: Servicio de retargeting de animaciones
- **Blender Shape Keys**: Sistema de deformación por morfología
- **Blender Drivers**: Sistema de animación procedural

---

## 🔄 Flujo de Trabajo Completo

```
1. DeepMotion → Exportar GLB con ARKit blendshapes
                    ↓
2. Blender → Import GLB
                    ↓
3. Ejecutar inspect_arkit_shapekeys.py (opcional)
                    ↓
4. Ejecutar setup_facial_emotions_arkit.py
                    ↓
5. Ajustar sliders en Custom Properties
                    ↓
6. Animar con keyframes (opcional)
                    ↓
7. Export FBX para uso en juegos/web
```

---

## ✅ Checklist de Setup

- [ ] Importar modelo GLB en Blender
- [ ] Verificar Armature presente
- [ ] Verificar malla con Shape Keys
- [ ] Ejecutar `setup_facial_emotions_arkit.py`
- [ ] Ver confirmación en consola
- [ ] Seleccionar Armature
- [ ] Abrir Object Properties → Custom Properties
- [ ] Ver 6 sliders creados
- [ ] Probar BLINK_CONTROL = 1.0
- [ ] Probar EMOTION_ALEGRIA = 1.0
- [ ] ✅ Setup completo

---

**Autor**: Sistema LSV de Animación Facial  
**Fecha**: Noviembre 2025  
**Versión**: 1.0  
**Compatible con**: Blender 4.5+  
**Formato**: GLB desde DeepMotion con ARKit
