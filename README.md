# Avatar LSV - Traductor de Lengua de Señas Venezolana

Sistema de traducción automática de Lengua de Señas Venezolana (LSV) con avatares 3D animados.

## 🌐 Demo en Vivo

**GitHub Pages:** [https://usm-argenis.github.io/Avatar_LSV/](https://usm-argenis.github.io/Avatar_LSV/)

## 🚀 Características

- ✅ Avatares 3D animados en tiempo real
- ✅ Traducción de texto a señas venezolanas
- ✅ Interfaz móvil optimizada
- ✅ Animaciones suaves con transiciones naturales
- ✅ Soporte para múltiples avatares (Duvall, Luis, Nancy, Carla)
- ✅ Integración con API de traducción LSV

## 📱 Uso

1. Abre la aplicación en tu navegador
2. Ingresa el texto que deseas traducir
3. Presiona "Traducir"
4. El avatar animará las señas correspondientes

## 🛠️ Tecnologías

- **Frontend:** Three.js, JavaScript
- **Backend:** FastAPI (Python)
- **3D Models:** Blender, GLB/FBX
- **Animación:** Deepmotion, MediaPipe
- **Deployment:** GitHub Pages

## 📦 Estructura del Proyecto

```
├── index.html              # Página principal (GitHub Pages)
├── backend/                # API FastAPI
├── mobile_app/             # Aplicación móvil Expo
├── test/output/glb/        # Modelos 3D y animaciones
└── scripts/                # Scripts de procesamiento
```

## 🔧 Desarrollo Local

### Servidor de Prueba
```bash
python run_local_server.py
```

O en Windows:
```cmd
run_local_server.bat
```

### Backend API
```bash
cd backend
uvicorn main:app --reload --port 5000
```

## 📚 Documentación

- [Configuración GitHub Pages](GITHUB_PAGES_SETUP.md)
- [Sistema LSV Completo](SISTEMA_LSV_COMPLETO.md)

## 👥 Autor

Universidad Santa María - Proyecto de Tesis

## 📄 Licencia

Proyecto académico - USM 2026
