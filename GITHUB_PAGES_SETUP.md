# 🤟 Visualizador LSV - GitHub Pages

Esta es la página principal del Visualizador de Lengua de Señas Venezolana.

## ¿Cómo funciona?

1. La página principal (`index.html`) tiene una interfaz simple con:
   - **Selector de Avatar**: Remy o Carlos
   - **Campo de texto**: Para ingresar palabras a traducir
   - **Botón "Ver Animación"**: Abre el visualizador 3D

2. El visualizador (`test/prueba.html`) muestra las animaciones 3D.

## Configuración de GitHub Pages

1. Ve a Settings → Pages en tu repositorio de GitHub
2. En "Source", selecciona la rama `nuevo` (o tu rama principal)
3. En "Folder", selecciona `/ (root)`
4. Guarda los cambios

## URL de la página

Una vez configurado, tu página estará disponible en:
```
https://usm-argenis.github.io/STT_LSV/
```

## Archivos necesarios

- `index.html` - Página principal (ya creada ✅)
- `test/prueba.html` - Visualizador 3D (ya existe ✅)
- `test/output/glb/` - Modelos 3D (ya existen ✅)

## Pasos para publicar

```bash
# Agregar los archivos nuevos
git add index.html

# Hacer commit
git commit -m "Add GitHub Pages landing page"

# Subir a GitHub
git push origin nuevo
```

¡Listo! Tu visualizador estará en línea.
