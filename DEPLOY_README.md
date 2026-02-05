# 🤟 LSV - Sistema de Lengua de Señas Venezolana con Avatares 3D

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-success?style=for-the-badge&logo=github)](https://usm-argenis.github.io/Avatar_LSV/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
[![React Native](https://img.shields.io/badge/React%20Native-0.71-61DAFB?style=for-the-badge&logo=react)](https://reactnative.dev/)

## 🎯 Demos en Vivo

Visita la página de demos: **[https://usm-argenis.github.io/Avatar_LSV/](https://usm-argenis.github.io/Avatar_LSV/)**

### 📱 Demos Disponibles:

- **🎭 Animation Viewer**: Visualizador principal con 4 avatares (Luis, Nancy, Duvall, Carla)
- **📚 Lesson Mode**: Sistema educativo con controles interactivos
- **✍️ Smart Spelling**: Deletreo inteligente palabra por palabra con caché

## ✨ Características

- ✅ **4 Avatares 3D** animados con expresiones faciales
- ✅ **336+ palabras** del diccionario LSV
- ✅ **Alfabeto completo** (27 letras: A-Z, Ñ)
- ✅ **Números 0-99** con secuencias compuestas
- ✅ **Sistema de caché** inteligente para carga instantánea
- ✅ **Optimizado móvil** con hardware acceleration
- ✅ **API REST** para traducción (próximamente en Render/Railway)

## 🏗️ Estructura del Proyecto

```
Avatar_LSV/
├── mobile_app/                    # App móvil React Native + Expo
│   └── lengua-de-senas/
│       ├── screens/               # Pantallas del juego
│       ├── components/            # Componentes reutilizables
│       └── assets/                # Imágenes y recursos
├── test/                          # Demos HTML + Three.js
│   ├── output/glb/                # Archivos GLB de avatares
│   │   ├── Luis/
│   │   ├── Nancy/
│   │   ├── Duvall/
│   │   └── Carla/
│   ├── animation_mobile.html      # Visualizador principal
│   ├── lesson_simple.html         # Modo lección
│   └── avatar_spelling_optimized.html
├── backend/                       # API FastAPI (Python)
│   ├── main.py                    # Servidor principal
│   └── scripts/data.json          # Diccionario LSV
└── docs/                          # Documentación
```

## 🚀 Despliegue GitHub Pages

### Archivos Publicados:
- `index.html` - Página principal con selector de demos
- `animation_mobile.html` - Visualizador de avatares
- `lesson_simple.html` - Modo lección educativo
- `avatar_spelling_optimized.html` - Sistema de deletreo v2.4
- `.nojekyll` - Desactiva Jekyll para servir archivos estáticos

### Configuración Automática:
1. GitHub Pages está configurado desde la rama `main`
2. Los archivos se sirven desde la raíz del repositorio
3. Acceso público en: `https://usm-argenis.github.io/Avatar_LSV/`

## 🔧 API Backend (Próximamente)

### Opciones de Despliegue:

**Opción 1: Render.com (Recomendado)**
```bash
# 1. Crear cuenta en Render.com
# 2. Nuevo Web Service desde GitHub
# 3. Configurar:
Build Command: pip install -r backend/requirements.txt
Start Command: cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
```

**Opción 2: Railway.app**
```bash
# 1. Crear cuenta en Railway.app
# 2. Nuevo proyecto desde GitHub
# 3. Auto-detecta FastAPI y despliega
```

**Opción 3: Servidor Local**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 5000
```

### Endpoints de API:

```
POST /api/traducir
Body: { "texto": "hola mundo" }
Response: { "glosas": [...], "videos": [...] }

GET /api/stats
Response: { "total_words": 336, "categories": [...] }
```

## 💻 Desarrollo Local

### Requisitos:
- Node.js 18+
- Python 3.9+
- Expo CLI
- Git

### Instalación:

```bash
# Clonar repositorio
git clone https://github.com/usm-argenis/Avatar_LSV.git
cd Avatar_LSV

# Mobile App
cd mobile_app/lengua-de-senas
npm install
npx expo start

# Backend API
cd ../../backend
pip install -r requirements.txt
uvicorn main:app --reload --port 5000

# Servidor HTTP para demos
cd ../test
python -m http.server 8000
```

### Demos Locales:
- Navegador: `http://localhost:8000/animation_mobile.html`
- App Móvil: Escanear QR de Expo
- API: `http://localhost:5000/docs`

## 📊 Rendimiento

### Optimizaciones Implementadas:
- ✅ **WebView Cache**: LOAD_CACHE_ELSE_NETWORK para reuso
- ✅ **Hardware Acceleration**: androidLayerType="hardware"
- ✅ **Animation Cache**: Map con límite de 15 (móvil) / 30 (desktop)
- ✅ **Silent Loading**: Sin pantalla de carga entre animaciones
- ✅ **Dynamic Key**: Switching instantáneo de avatares
- ✅ **Intelligent Preloading**: LOOKAHEAD=4 letras

### Métricas:
- Carga inicial: ~2s
- Switching avatar: <500ms
- Animación desde caché: <100ms
- Animación desde servidor: ~800ms

## 🎓 Proyecto de Tesis

**Universidad Santa María**  
**Carrera**: Ingeniería de Sistemas  
**Autor**: Argenis Medina  
**Tema**: Sistema de Traducción de Lengua de Señas Venezolana con Avatares 3D Animados

## 📝 Licencia

MIT License - Ver [LICENSE](LICENSE) para más detalles

## 🔗 Enlaces

- 📦 [Repositorio](https://github.com/usm-argenis/Avatar_LSV)
- 🌐 [GitHub Pages](https://usm-argenis.github.io/Avatar_LSV/)
- 📖 [Documentación](docs/)
- 🐛 [Reportar Bug](https://github.com/usm-argenis/Avatar_LSV/issues)

---

⭐ Si te gusta este proyecto, dale una estrella en GitHub!
