# 🎯 INSTRUCCIONES: Ajustar Animación de Manos

## Objetivo
Ajustar la animación del archivo `Remy_resultado_r.glb` para que coincida con el video de referencia `r.mp4`

---

## Método 1: Blender (Recomendado)

### Paso 1: Abrir Blender
1. Abre **Blender** (versión 3.0 o superior)
2. Ve a `Scripting` en la barra superior

### Paso 2: Cargar el Script
1. En el editor de texto, haz clic en `Open`
2. Navega a: `C:\Users\andre\OneDrive\Documentos\tesis\scripts\ajustar_manos_blender.py`
3. Abre el archivo

### Paso 3: Ejecutar
1. Haz clic en el botón `▶ Run Script` o presiona `Alt + P`
2. Espera a que termine (verás logs en la consola)

### Paso 4: Verificar Resultado
- Archivo generado: `C:\Users\andre\OneDrive\Documentos\tesis\output\Remy_resultado_r_ajustado.glb`
- Verifica el tamaño del archivo (debería ser similar al original ~27 MB)

---

## Método 2: Ajuste Manual en Blender

Si el script automático no funciona, puedes ajustar manualmente:

### Paso 1: Importar GLB
1. Abre Blender
2. `File > Import > glTF 2.0 (.glb/.gltf)`
3. Selecciona `Remy_resultado_r.glb`

### Paso 2: Preparar Comparación
1. Abre carpeta `output\frames_r\` en el explorador de archivos
2. En Blender, ve a la vista `Animation`
3. En el panel derecho, cambia a `Image Editor`
4. Carga la primera imagen: `frame_0000_t0.00s.jpg`

### Paso 3: Sincronizar Timeline
1. Establece FPS a **29.47** (en Timeline)
2. El video dura **2.75 segundos** (81 frames a 29.47 FPS)
3. Ajusta el rango de frames en Blender para que coincida

### Paso 4: Comparación Frame por Frame
Para cada frame clave del video:

1. **Frame 0 (t=0.00s)**
   - Carga `frame_0000_t0.00s.jpg`
   - Observa posición de manos en la imagen
   - Ajusta huesos correspondientes en Blender:
     - `LeftHand`, `RightHand`
     - `LeftHandThumb1-3`, `RightHandThumb1-3`
     - `LeftHandIndex1-3`, `RightHandIndex1-3`
     - etc.

2. **Frame ~20 (t=0.68s)**
   - Carga `frame_0020_t0.68s.jpg`
   - Repite ajustes

3. **Continúa para cada frame extraído** (41 en total)

### Paso 5: Exportar GLB Ajustado
1. Selecciona el armature
2. `File > Export > glTF 2.0 (.glb/.gltf)`
3. Configuración:
   - Format: **GLB**
   - Include: **Selected Objects** ✓
   - Animations: **✓**
   - Apply Modifiers: **✓**
4. Guarda como: `output\Remy_resultado_r_ajustado.glb`

---

## Método 3: MotionBuilder (Alternativo)

### Paso 1: Convertir GLB a FBX
```powershell
# En la terminal de VS Code:
cd C:\Users\andre\OneDrive\Documentos\tesis
# Necesitarás un script de conversión o usar Blender:
# File > Export > FBX (.fbx)
```

### Paso 2: Abrir en MotionBuilder
1. Abre MotionBuilder
2. `File > Open` → Selecciona el FBX exportado
3. Ve a `Story` para edición no-lineal de animación

### Paso 3: Ajustar con Referencia Visual
1. Carga imágenes de `output\frames_r\` como referencia
2. Usa `Keying Mode` para ajustar poses de manos
3. Sincroniza con timestamps del video

### Paso 4: Exportar
1. `File > Save As` → FBX
2. Convertir FBX a GLB usando Blender

---

## 📊 Frames Extraídos del Video

Total: **41 frames** de 81 totales (cada ~3 frames)

| Frame | Timestamp | Archivo |
|-------|-----------|---------|
| 0 | 0.00s | frame_0000_t0.00s.jpg |
| 3 | 0.10s | frame_0003_t0.10s.jpg |
| 6 | 0.20s | frame_0006_t0.20s.jpg |
| ... | ... | ... |
| 78 | 2.65s | frame_0078_t2.65s.jpg |
| 81 | 2.75s | frame_0081_t2.75s.jpg |

(Ver `output\frames_r\frames_info.json` para lista completa)

---

## 🎯 Huesos Clave de Manos

Busca estos huesos en el armature:

**Mano Izquierda:**
- `LeftHand`
- `LeftHandThumb1`, `LeftHandThumb2`, `LeftHandThumb3`
- `LeftHandIndex1`, `LeftHandIndex2`, `LeftHandIndex3`
- `LeftHandMiddle1`, `LeftHandMiddle2`, `LeftHandMiddle3`
- `LeftHandRing1`, `LeftHandRing2`, `LeftHandRing3`
- `LeftHandPinky1`, `LeftHandPinky2`, `LeftHandPinky3`

**Mano Derecha:**
- `RightHand`
- `RightHandThumb1-3`
- `RightHandIndex1-3`
- `RightHandMiddle1-3`
- `RightHandRing1-3`
- `RightHandPinky1-3`

---

## 💡 Tips

1. **Prioridad**: Enfócate en las poses más evidentes del video
2. **Interpolación**: Blender interpolará automáticamente entre keyframes
3. **Verificación**: Reproduce la animación después de cada ajuste
4. **Backup**: Guarda versiones intermedias por si acaso

---

## ❓ Problemas Comunes

**"No veo los huesos de las manos"**
- Selecciona el armature
- Presiona `Tab` para entrar en Edit Mode
- Activa `X-Ray` para ver huesos a través del mesh

**"La animación se ve rara después de exportar"**
- Asegúrate de exportar con "Bake Animation" activado
- Verifica que FPS esté en 29.47

**"El archivo GLB es muy grande"**
- Usa compresión Draco en opciones de exportación
- Verifica que no se estén exportando objetos innecesarios
