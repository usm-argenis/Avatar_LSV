# 👀 Visualizador de Señas LSV - Versión 2

## 🎯 Descripción

Visualizador web interactivo para animaciones de Lengua de Señas Venezolana (LSV) con soporte para múltiples avatares.

---

## ✨ Características Nuevas v3.0

### 🆕 Selector Dual de Avatar y Seña
- **Selector de Avatar** (👤): Cambia entre diferentes personajes 3D
- **Selector de Seña** (🤟): Cambia entre diferentes animaciones
- **Carga automática**: Al cambiar cualquier selector, se carga la combinación inmediatamente

### 🎨 Interfaz Mejorada
- Diseño moderno con degradados
- Controles de reproducción intuitivos
- Panel de información en tiempo real
- Timeline interactivo
- Control de velocidad (0.25x - 2.0x)
- Modo loop activable

### 🛠️ Funcionalidades
- ▶️ Play/Pause
- ⏹ Stop
- ⏮ Restart
- 🔄 Loop
- ⚡ Control de velocidad
- 📊 Información de frame actual
- 🦴 Contador de huesos
- ⏱️ Duración de animación

---

## 🚀 Inicio Rápido

### 1. Iniciar servidor web
```powershell
python -m http.server 8000
```

### 2. Abrir visualizador
```
http://localhost:8000/test/viewer_senas_v2.html
```

### 3. Seleccionar combinación
```
👤 Avatar: Remy o JH
🤟 Seña: Letra B
```

### 4. Reproducir
```
Presiona ▶️ para ver la animación
```

---

## 📂 Archivos Disponibles

### Avatares:
- **Remy**: Avatar masculino base
- **JH**: Avatar alternativo

### Señas:
- **Letra B**: Primera letra del alfabeto LSV

### Combinaciones Actuales:
```
output/
├── Remy_b_deepmotion.fbx (27.4 MB) ✅
├── JH_b_deepmotion.fbx (51.5 MB) ✅
└── Remy_resultado_b.fbx (27.4 MB) ✅ Legacy
```

---

## ➕ Agregar Nuevas Combinaciones

### Opción A: Nuevo Avatar con Señas Existentes

```powershell
# 1. Descargar avatar de Mixamo → avatars/Amy.fbx

# 2. Procesar con animación existente
blender --background --python scripts\apply_animation_to_avatars.py -- "animations_library\alphabet\b_deepmotion.fbx"

# 3. Actualizar HTML (viewer_senas_v2.html línea ~355)
<select id="avatar-select">
    <option value="Remy">Remy</option>
    <option value="JH">JH</option>
    <option value="Amy">Amy</option>  <!-- NUEVO -->
</select>

# 4. Recargar navegador (F5)
```

### Opción B: Nueva Seña con Avatares Existentes

```powershell
# 1. Generar en DeepMotion → resultado_c.fbx (1 crédito)

# 2. Guardar en biblioteca
Copy-Item "Downloads\resultado_c.fbx" "animations_library\alphabet\c_deepmotion.fbx"

# 3. Procesar con todos los avatares
blender --background --python scripts\apply_animation_to_avatars.py -- "animations_library\alphabet\c_deepmotion.fbx"

# 4. Actualizar HTML (viewer_senas_v2.html línea ~360)
<select id="sign-select">
    <option value="b_deepmotion">Letra B</option>
    <option value="c_deepmotion">Letra C</option>  <!-- NUEVO -->
</select>

# 5. Recargar navegador (F5)
```

---

## 🎨 Controles

### Teclado (futuras versiones):
```
Espacio  : Play/Pause
R        : Restart
L        : Toggle Loop
↑/↓      : Velocidad ±0.25x
←/→      : Frame anterior/siguiente
```

### Mouse:
```
Clic izquierdo + arrastrar : Rotar cámara
Clic derecho + arrastrar   : Pan (mover cámara)
Scroll                     : Zoom
```

---

## 🔧 Configuración Técnica

### Dependencias:
- **Three.js** v0.160.0 (CDN)
- **FBXLoader** (Three.js addon)
- **OrbitControls** (Three.js addon)

### Formato de archivos:
```
Entrada esperada:
output/{Avatar}_{Seña}.fbx

Ejemplo:
output/Remy_b_deepmotion.fbx
       ^^^^^  ^^^^^^^^^^^
       |      └── Nombre de seña
       └── Nombre de avatar
```

### Renderizado:
- **Background**: Blanco (#ffffff)
- **Escala FBX**: 0.01x
- **Luces**: 5 direccionales (ambiente + 4 direccionales)
- **Sombras**: Activadas (PCF Soft)
- **Grid**: 10x10 unidades
- **FPS**: 30 (para cálculo de frames)

---

## 🐛 Troubleshooting

### Error: "No se puede cargar FBX"

#### Causa 1: Archivo no existe
```powershell
# Verificar archivos disponibles
Get-ChildItem output\*.fbx

# Si falta la combinación, procesar:
blender --background --python scripts\apply_animation_to_avatars.py -- "animations_library\alphabet\[letra]_deepmotion.fbx"
```

#### Causa 2: Servidor web no está corriendo
```powershell
# Verificar puerto 8000
netstat -an | findstr :8000

# Si no está activo, iniciar:
python -m http.server 8000
```

#### Causa 3: Ruta incorrecta en buildFBXPath()
```javascript
// Abrir consola del navegador (F12)
// Ver mensajes de error
// Formato debe ser: output/{Avatar}_{Seña}.fbx
```

### Modal de Error Mejorado

El visualizador ahora muestra un modal detallado cuando hay error:
- ❌ Nombre del archivo que falló
- 🔍 4 causas posibles diagnosticadas
- 💡 Soluciones sugeridas
- ⏰ Auto-cierra en 10 segundos

---

## 📊 Métricas de Rendimiento

### Archivos Actuales:
```
JH_b_deepmotion.fbx      : 51.47 MB
Remy_b_deepmotion.fbx    : 27.44 MB
Remy_resultado_b.fbx     : 27.36 MB
```

### Tiempo de Carga:
- **Primera carga**: 2-5 segundos (según conexión)
- **Cambio de avatar**: 2-3 segundos
- **Cambio de seña**: 2-3 segundos

### Optimizaciones:
- Mesh culling (lower body hidden via JS)
- Texture compression automática
- Shadow map: 2048x2048
- Anti-aliasing activado

---

## 🎓 Mejores Prácticas

### ✅ HACER:
1. Iniciar servidor web ANTES de abrir HTML
2. Verificar archivos FBX existen en output/
3. Usar nombres consistentes en selectores y archivos
4. Cerrar servidor al terminar (Ctrl+C)
5. Recargar página después de cambios (F5)

### ❌ EVITAR:
1. Abrir HTML directamente (file://) → Usa servidor HTTP
2. Cambiar selectores muy rápido (espera carga completa)
3. Usar archivos FBX muy pesados (>100 MB)
4. Olvidar actualizar HTML después de agregar archivos

---

## 🔮 Roadmap Futuro

### v3.1 - Auto-Discovery:
- [ ] Escanear carpeta `output/` automáticamente
- [ ] Generar opciones de selectores dinámicamente
- [ ] No necesitar editar HTML manualmente

### v3.2 - Comparación:
- [ ] Vista lado a lado de 2 avatares
- [ ] Sincronización de animaciones
- [ ] Comparar diferentes señas

### v3.3 - Exportación:
- [ ] Exportar a video MP4
- [ ] Exportar a GIF animado
- [ ] Screenshots en alta resolución

### v3.4 - Controles Avanzados:
- [ ] Atajos de teclado
- [ ] Playlist de señas
- [ ] Slow motion frame-by-frame

---

## 📞 Comandos Útiles

```powershell
# Ver estado del sistema
python scripts\quick_status.py

# Ver animaciones disponibles
python scripts\check_animations.py

# Listar archivos procesados
Get-ChildItem output\*.fbx

# Procesar nueva combinación
blender --background --python scripts\apply_animation_to_avatars.py -- "[animation].fbx"

# Iniciar servidor
python -m http.server 8000

# Verificar puerto
netstat -an | findstr :8000
```

---

## 📚 Documentación Relacionada

- `GUIA_USO_OPTIMIZADO.md` - Workflow completo
- `docs/OPTIMIZACION_DEEPMOTION.md` - Ahorro de créditos
- `docs/SELECTOR_AVATARES.md` - Uso del selector
- `RESUMEN_CAMBIOS.md` - Historial de cambios
- `avatars/README.md` - Gestión de avatares

---

## 💡 Tips Rápidos

### Cambio Rápido de Avatar:
```
1. Clic en selector "👤 Avatar"
2. Seleccionar avatar diferente
3. Esperar carga automática (2-3 seg)
4. ▶️ Reproducir
```

### Comparar Avatares:
```
1. Seleccionar Remy → Observar letra B
2. Seleccionar JH → Observar letra B
3. Comparar visualmente las diferencias
```

### Exportar Frame:
```
Futuro: Botón de screenshot
Actual: Print Screen + recortar
```

---

## 🏆 Casos de Uso

### 1. Desarrollo de Contenido LSV
- Validar animaciones generadas
- Verificar calidad de retargeting
- Comparar diferentes avatares

### 2. Educación
- Enseñar alfabeto LSV
- Practicar señas
- Material visual para clases

### 3. Testing
- Validar pipeline de procesamiento
- Verificar compatibilidad de avatares
- Diagnosticar problemas de animación

### 4. Presentaciones
- Demo del sistema LSV
- Mostrar progreso del proyecto
- Exhibir capacidades técnicas

---

**Última actualización**: Octubre 22, 2025
**Versión**: 3.0
**Autor**: Sistema STT_LSV
**Licencia**: Proyecto académico USM
