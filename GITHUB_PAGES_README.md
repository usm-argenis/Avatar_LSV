# LSV Mobile - GitHub Pages Setup

## Descripción
Esta es una aplicación web interactiva para visualizar animaciones de la Lengua de Señas Venezolana (LSV) con múltiples avatares 3D. Funciona completamente en el navegador con integración de API backend (opcional).

## Características

✅ **Interfaz responsiva** - Funciona en desktop, tablet y móvil
✅ **Múltiples avatares** - Nancy, Duvall, Carla, Remy
✅ **Traducción en tiempo real** - Procesa texto a secuencias de animaciones
✅ **API integrada** - Conecta con backend para traducciones avanzadas
✅ **Fallback local** - Funciona sin backend si es necesario
✅ **Controles intuitivos** - Pausar, reanudar, repetir, resetear cámara
✅ **Caché optimizado** - Precarga inteligente de animaciones

## Instalación en GitHub Pages

### Paso 1: Clona el repositorio
```bash
git clone https://github.com/usm-argenis/Avatar_LSV.git
cd Avatar_LSV
```

### Paso 2: Configura las URLs de API (opcional)

Si quieres usar el backend para traducciones avanzadas, edita el archivo `index.html`:

```javascript
// Línea 450-460 aproximadamente
const API_CONFIG = {
    useBackend: true,
    backendUrl: (() => {
        const isDev = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
        // Cambiar a tu URL de API remota
        return isDev ? 'http://localhost:3000' : 'https://tu-api-lsv.com';
    })(),
    baseUrl: (() => {
        const isGithubPages = window.location.hostname.includes('github.io');
        return isGithubPages 
            ? 'https://usm-argenis.github.io/Avatar_LSV/'
            : '';
    })()
};
```

### Paso 3: Habilita GitHub Pages

1. Ve a **Settings** del repositorio
2. Busca **Pages** en el menú izquierdo
3. En **Source**, selecciona **Deploy from a branch**
4. Selecciona **main** como rama
5. Haz clic en **Save**

### Paso 4: Accede a tu página

Tu aplicación estará disponible en:
```
https://usm-argenis.github.io/Avatar_LSV/
```

## Uso Local

### Con Python (simple)
```bash
cd c:\ruta\a\Avatar_LSV
python -m http.server 8000
```
Luego abre `http://localhost:8000` en tu navegador.

### Con Node.js
```bash
npx http-server
```

### Con Fast API (si tienes el backend)
```bash
cd backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 3000
```

## Configuración del Backend

### Variables de entorno necesarias:

**Backend (FastAPI)**:
```env
PORT=3000
CORS_ORIGINS=http://localhost:8000,https://usm-argenis.github.io
```

**Frontend (index.html)**:
```javascript
// Para desarrollo local:
backendUrl: 'http://localhost:3000'

// Para GitHub Pages:
backendUrl: 'https://tu-servidor.com'
```

## Estructura de directorios

```
Avatar_LSV/
├── index.html                 # Página principal (GitHub Pages)
├── test/
│   ├── animation_mobile.html # Versión móvil original
│   ├── output/
│   │   └── glb/              # Modelos 3D de avatares
│   │       ├── Nancy/
│   │       ├── Duvall/
│   │       ├── Carla/
│   │       └── Remy/
│   └── ...
├── backend/                   # API FastAPI (opcional)
│   ├── main.py
│   ├── requirements.txt
│   └── ...
└── README.md
```

## API Endpoints (Opcional)

Si tienes el backend corriendo, los endpoints disponibles son:

### GET `/api/diccionario`
Obtiene el diccionario completo de palabras y sus animaciones.

```bash
curl http://localhost:3000/api/diccionario
```

### POST `/api/translate`
Traduce texto a secuencia de animaciones.

```bash
curl -X POST http://localhost:3000/api/translate \
  -H "Content-Type: application/json" \
  -d '{
    "texto": "hola buenos dias",
    "avatar": "Nancy",
    "deletrear_desconocidas": true,
    "corregir_ortografia": true,
    "velocidad_deletreo": 1.2
  }'
```

**Respuesta:**
```json
{
  "animaciones": [
    { "nombre": "hola" },
    { "nombre": "buenos dias" }
  ],
  "total_animaciones": 2,
  "texto_corregido": "hola buenos días",
  "correcciones": []
}
```

## Troubleshooting

### ❌ "No se puede cargar el avatar"
- Verifica que la URL base sea correcta en `API_CONFIG.baseUrl`
- Asegúrate de que los archivos GLB existan en la ruta correcta
- Revisa la consola del navegador (F12) para más detalles

### ❌ "API no responde"
- Si estás en desarrollo local, asegúrate de que el backend esté corriendo en `localhost:3000`
- Si estás en GitHub Pages, configura la URL correcta del backend remoto
- La aplicación funciona sin backend (modo fallback local)

### ❌ "Palabras no se traducen"
- Verifica que la palabra exista en el diccionario
- Prueba con palabras conocidas como: "hola", "gracias", "bien"
- Si tienes backend, revisa que devuelva el diccionario correctamente

### ⚠️ "Animaciones lentas en móvil"
- Es normal en dispositivos con menos recursos
- La caché se ajusta automáticamente (menos animaciones en caché en móvil)
- Las primeras animaciones pueden ser más lentas mientras se precargan

## Desarrollo Futuro

- [ ] Soporte para texto con puntuación
- [ ] Historial de búsquedas
- [ ] Exportar animaciones a video
- [ ] Aplicación nativa React Native mejorada
- [ ] Reconocimiento de voz (speech-to-text)
- [ ] Más avatares personalizables

## Créditos

**Proyecto de Tesis**: Sistema LSV - Lengua de Señas Venezolana
**Autor**: Argenis
**Instituto**: Universidad Simón Bolívar (USB)

## Licencia

Este proyecto es parte de una tesis académica. Úsalo con fines educativos.

## Soporte

Para reportar bugs o sugerir mejoras, abre un **Issue** en GitHub.

---

**Última actualización**: Febrero 2026
