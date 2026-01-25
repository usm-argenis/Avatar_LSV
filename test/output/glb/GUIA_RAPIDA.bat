@echo off
chcp 65001 > nul
echo ============================================================
echo  GUÍA RÁPIDA: Setup de Emociones Faciales en Blender
echo ============================================================
echo.
echo 📁 Ubicación: test/output/glb/
echo.
echo ARCHIVOS DISPONIBLES:
echo   1. setup_facial_emotions_arkit.py    (Script principal)
echo   2. inspect_arkit_shapekeys.py        (Inspector)
echo   3. README_FACIAL_SETUP.md            (Documentación)
echo.
echo ============================================================
echo  INSTRUCCIONES PASO A PASO
echo ============================================================
echo.
echo PASO 1: Abrir Blender 4.5+
echo.
echo PASO 2: Importar modelo GLB
echo   • File ^> Import ^> glTF 2.0 (.glb/.gltf)
echo   • Seleccionar archivo de esta carpeta (ej: Remy_resultado_b.glb)
echo   • Import
echo.
echo PASO 3: Abrir Scripting workspace
echo   • Clic en pestaña "Scripting" (arriba en Blender)
echo.
echo PASO 4: Cargar script
echo   • Text ^> Open
echo   • Seleccionar: setup_facial_emotions_arkit.py
echo.
echo PASO 5: Ejecutar
echo   • Alt+P o botón "Run Script"
echo.
echo PASO 6: Usar controles
echo   • Seleccionar Armature en Outliner
echo   • Object Properties ^> Custom Properties
echo   • Ajustar los 6 sliders de emociones
echo.
echo ============================================================
echo  MODELOS GLB DISPONIBLES
echo ============================================================
echo.
dir /b *.glb 2>nul
echo.
echo ============================================================
echo  SCRIPTS DE PYTHON
echo ============================================================
echo.
dir /b *.py 2>nul
echo.
echo ============================================================
echo.
echo 💡 TIP: Lee README_FACIAL_SETUP.md para más detalles
echo.
echo Para inspeccionar blendshapes primero:
echo   ^> Usa inspect_arkit_shapekeys.py en Blender
echo.
echo ============================================================
pause
