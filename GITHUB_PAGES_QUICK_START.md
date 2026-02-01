# 🚀 GitHub Pages - Guía Rápida

## ¿Qué se hizo?

Se creó una versión completa de `animation_mobile.html` optimizada para **GitHub Pages** con:

✅ **API integrada** - Conecta automáticamente con tu backend
✅ **Fallback automático** - Si el API falla, funciona localmente
✅ **URLs flexibles** - Cambia fácilmente entre desarrollo y producción
✅ **Avatares múltiples** - Nancy, Duvall, Carla, Remy
✅ **Interfaz mejorada** - Selector de avatares, controles intuitivos
✅ **Optimizado para móvil** - Funciona perfectamente en smartphones

---

## 📍 ¿Dónde está?

Tu página está en: **`/index.html`** (raíz del repositorio)

Cuando hagas push a GitHub, estará disponible en:
```
https://usm-argenis.github.io/Avatar_LSV/
```

---

## ⚙️ Configuración de la API

### Opción 1: Solo modificar URLs en index.html

Abre `index.html` y busca (línea ~450):

```javascript
const API_CONFIG = {
    useBackend: true,
    backendUrl: (() => {
        const isDev = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
        return isDev ? 'http://localhost:3000' : 'https://api-lsv.tu-dominio.com';  // ← CAMBIAR AQUÍ
    })(),
    baseUrl: (() => {
        const isGithubPages = window.location.hostname.includes('github.io');
        return isGithubPages 
            ? 'https://usm-argenis.github.io/Avatar_LSV/'  // ← Y AQUÍ
            : '';
    })()
};
```

### Opción 2: Usar el archivo config.json

Edita `config.json` y actualiza:

```json
{
  "api": {
    "production": {
      "backendUrl": "https://tu-api-real.com",  // ← TU API AQUÍ
      "baseUrl": "https://usm-argenis.github.io/Avatar_LSV/"
    }
  }
}
```

---

## 🧪 Probar Localmente

### Opción A: Python (más simple)
```bash
cd c:\Users\andre\OneDrive\Documentos\tesis
python -m http.server 8000
```
Luego abre: `http://localhost:8000`

### Opción B: Node.js
```bash
npx http-server
```

### Opción C: Live Server (VS Code)
Haz clic derecho en `index.html` → "Open with Live Server"

---

## 📤 Publicar en GitHub Pages

### 1. Asegúrate de que GitHub Pages esté habilitado

Ve a: **Settings → Pages**
- Source: `Deploy from a branch`
- Branch: `main`
- Folder: `/ (root)`

### 2. Si ya hiciste cambios locales
```bash
git add index.html config.json
git commit -m "🔧 Configurar URLs de API para GitHub Pages"
git push
```

### 3. Accede a tu página

Abre: `https://usm-argenis.github.io/Avatar_LSV/`

---

## 🎯 Cómo Funciona

1. **Usuario abre la página**
   ↓
2. **Carga Three.js (3D)**
   ↓
3. **Intenta cargar diccionario desde API**
   ├─ Si funciona: usa API para traducciones inteligentes ✅
   └─ Si falla: usa diccionario local (fallback) ⚠️
   ↓
4. **Carga el avatar (Nancy/Duvall/Carla/Remy)**
   ↓
5. **Usuario ingresa texto y presiona ANIMAR**
   ├─ Envía a API si está disponible
   └─ O procesa localmente
   ↓
6. **Carga las animaciones GLB y las reproduce**

---

## 🔌 APIs Esperadas (Backend)

Si tienes el backend corriendo, debe responder:

### GET `/api/diccionario`
```json
{
  "hola": { "categoria": "frases", "archivo": "hola" },
  "buenos dias": { "categoria": "frases", "archivo": "buenos dias" },
  ...
}
```

### POST `/api/translate`
```json
{
  "texto": "hola buenos dias",
  "avatar": "Nancy",
  "deletrear_desconocidas": true,
  "corregir_ortografia": true,
  "velocidad_deletreo": 1.2
}
```

Respuesta esperada:
```json
{
  "animaciones": [
    { "nombre": "hola" },
    { "nombre": "buenos dias" }
  ],
  "total_animaciones": 2,
  "texto_corregido": "hola buenos días"
}
```

---

## 📁 Archivos Creados

```
index.html                    ← Tu página de GitHub Pages 🎯
config.json                   ← Configuración centralizada
setup_github_pages.sh         ← Script para configurar automáticamente
GITHUB_PAGES_README.md        ← Documentación completa
GITHUB_PAGES_QUICK_START.md   ← Esta guía rápida
```

---

## ✨ Características

| Feature | Local | GitHub Pages | Con API |
|---------|-------|--------------|---------|
| Avatares múltiples | ✅ | ✅ | ✅ |
| Controles (pausa, repetir) | ✅ | ✅ | ✅ |
| Diccionario local | ✅ | ✅ | ✅ |
| Traducción inteligente | ❌ | ❌ | ✅ |
| Corrección ortográfica | ❌ | ❌ | ✅ |
| Deletreo automático | ❌ | ❌ | ✅ |

---

## 🐛 Debugging

### Abrir consola del navegador
Presiona: **F12** o **Ctrl+Shift+I**

### Ver logs
- Busca mensajes con emojis (✅, ❌, ⚠️, 🌐)
- Si ves "API no disponible" → el backend no está corriendo
- Si ves "Diccionario cargado" → está usando API o fallback

### Verificar URLs
En la consola, escribe:
```javascript
console.log(API_CONFIG);  // Ver configuración actual
```

---

## 📞 Soporte Rápido

| Problema | Solución |
|----------|----------|
| "No se carga el avatar" | Verifica que los GLB existan en `test/output/glb/` |
| "API no responde" | Asegúrate de que backend esté corriendo en puerto 3000 |
| "Palabras no se encuentran" | Usa el diccionario local (fallback automático) |
| "Lento en móvil" | Es normal, la caché se ajusta automáticamente |
| "Error CORS" | Configura CORS en tu backend: `CORS_ORIGINS` |

---

## 🎉 ¡Listo!

Tu página está lista para:
- ✅ Usarla localmente
- ✅ Publicarla en GitHub Pages
- ✅ Conectarla con tu API backend
- ✅ Compartirla con otros usuarios

---

**¿Necesitas más ayuda?**
Revisa `GITHUB_PAGES_README.md` para documentación completa.

**Última actualización:** Febrero 2026
