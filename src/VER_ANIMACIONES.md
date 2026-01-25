# 🎬 Cómo Ver Tu Animación con el Avatar Remy

## ✅ Visualizador 3D con Avatar Remy (Recomendado)

### 🆕 NUEVO: Visualizador con tu modelo FBX

Ahora puedes ver tus animaciones con tu avatar personalizado **Remy.fbx**!

**URL:** `http://localhost:8080/visualizador_remy.html`

### Características:
- ✅ Carga tu modelo FBX (Remy.fbx)
- ✅ Renderizado 3D con Three.js
- ✅ Controles de cámara (Frente, Lado, Arriba)
- ✅ Grid y ejes de referencia
- ✅ Iluminación profesional
- ✅ Auto-rotación opcional

---

## ✅ Visualizador Web Básico (SVG)

### Paso 1: Iniciar el Servidor

```powershell
cd c:\Users\andre\OneDrive\Documentos\tesis\src
python -m http.server 8080
```

### Paso 2: Abrir en el Navegador

Abre tu navegador y ve a:
```
http://localhost:8080/visualizador_animacion.html
```

### Paso 3: Cargar tu Animación

Tienes **2 opciones**:

**Opción A - Carga Rápida:**
- En el menú desplegable "🎨 Opciones Rápidas"
- Selecciona: "YO"
- ¡La animación se carga automáticamente!

**Opción B - Cargar Archivo:**
- Click en "📁 Seleccionar Archivo"
- Busca: `output_yo.json`
- La animación se cargará

### Paso 4: Reproducir

- Click en **▶ Reproducir** para ver la animación
- Usa **⏸ Pausar** para pausar
- Arrastra la barra de tiempo para ir a un frame específico

---

## 🎯 Animaciones Disponibles

Puedes cargar cualquiera de estas:

- `output_yo.json` - Seña de "YO" (de tu video)
- `output_hola.json` - Seña de "HOLA"
- `output_gracias.json` - Seña de "GRACIAS"
- `output_hola_gracias.json` - Combinación con interpolación

---

## 📊 Información que Verás

El visualizador muestra:

- **Frame Actual**: El frame que se está mostrando
- **Total Frames**: Cuántos frames tiene la animación
- **Duración**: Tiempo total en segundos
- **FPS**: Frames por segundo (normalmente 30)

---

## 🎨 Avatar

El avatar SVG muestra:
- ✅ Cabeza (con rotación)
- ✅ Cuerpo
- ✅ Brazos (izquierdo y derecho)
- ✅ Manos (se mueven según los keypoints)
- ✅ Piernas

La **mano derecha** se mueve según las coordenadas del JSON.

---

## 🚀 Método Alternativo: Usar el Visualizador Existente

También puedes usar el visualizador que ya tienes en GitHub Pages:

```
https://usm-argenis.github.io/STT_LSV/
```

Necesitarías subir tus archivos JSON allí.

---

## 🛠️ Método 3: Integrar con la App Móvil

Tu app React Native ya tiene WebView configurado. Puedes:

1. **Subir el visualizador a GitHub Pages**
2. **Agregar endpoint a tu backend** para generar animaciones
3. **Llamar desde HomeScreen** y mostrar en WebView

---

## 💡 Tips

### Ver Varias Animaciones

Para probar diferentes señas:
1. Genera más animaciones con `main.py --mode interactive`
2. Los archivos se guardan como `output_*.json`
3. Cárgalos en el visualizador con el botón de archivo

### Ver Animaciones de Pronombres

Ya tienes los videos procesados:
- tu, el, ella, nosotros

Genera sus animaciones:
```powershell
cd src
python -c "from ai.motion_generator import MotionGenerator; g = MotionGenerator('data/keypoints'); g.generate_from_text('tu', 'output_tu.json')"
python -c "from ai.motion_generator import MotionGenerator; g = MotionGenerator('data/keypoints'); g.generate_from_text('el', 'output_el.json')"
python -c "from ai.motion_generator import MotionGenerator; g = MotionGenerator('data/keypoints'); g.generate_from_text('ella', 'output_ella.json')"
```

Luego cárgalas en el visualizador.

---

## ⚙️ Personalizar el Avatar

Si quieres cambiar colores o tamaño del avatar:

Abre `visualizador_animacion.html` y modifica los estilos CSS:

```css
.avatar-head {
    fill: #ffd6a5;  /* Color de piel */
}

.avatar-body-part {
    fill: #4a90e2;  /* Color de ropa */
}
```

---

## 🎓 Resumen Rápido

```bash
# 1. Iniciar servidor
cd c:\Users\andre\OneDrive\Documentos\tesis\src
python -m http.server 8080

# 2. Abrir navegador
http://localhost:8080/visualizador_animacion.html

# 3. Seleccionar "YO" en el menú

# 4. Click en "▶ Reproducir"

# ¡Listo! Tu animación está corriendo 🎉
```

---

**¡Ahora puedes ver tus animaciones con el avatar en tiempo real!** 🎬
