"""
Script para procesar video con FreeMoCap y exportar a Blender
"""
import os
from pathlib import Path

print("\n" + "="*70)
print("PROCESAMIENTO CON FREEMOCAP")
print("="*70)

# Verificar instalación
try:
    import freemocap
    print(f"\n✓ FreeMoCap instalado: v{freemocap.__version__}")
except Exception as e:
    print(f"\n❌ Error importando FreeMoCap: {e}")
    print("Instalando dependencias adicionales...")
    import subprocess
    subprocess.run(["pip", "install", "freemocap[all]"], check=True)
    import freemocap

# Rutas
base_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis")
video_path = base_path / "test" / "output" / "videos" / "yo.mp4"
output_folder = base_path / "freemocap_output"

if not video_path.exists():
    print(f"\n❌ No se encontró el video: {video_path}")
    exit(1)

print(f"\n📹 Video: {video_path.name}")
print(f"📁 Output: {output_folder}")

# Crear carpeta de salida
output_folder.mkdir(exist_ok=True)

print("\n" + "="*70)
print("PASOS PARA USAR FREEMOCAP CON TU VIDEO:")
print("="*70)

print("""
FreeMoCap está diseñado principalmente para su GUI interactiva.
Para usarlo con tu video único:

MÉTODO 1: GUI (Recomendado)
─────────────────────────────
1. Abre una terminal y ejecuta:
   
   freemocap

2. En la GUI que se abre:
   - Click en "Create New Session"
   - Selecciona "Single Video"
   - Navega a: test/output/videos/yo.mp4
   - Click "Process"
   - Espera el procesamiento (5-15 minutos)

3. Exportar a Blender:
   - En la GUI, click en "Export"
   - Selecciona formato: "Blender (FBX)" o "BVH"
   - Guarda el archivo

4. En Blender:
   - File > Import > Motion Capture (.bvh) o FBX
   - Selecciona el archivo exportado
   - Usa retargeting para aplicarlo a Nancy


MÉTODO 2: API Programática
───────────────────────────
Si prefieres hacerlo por código, aquí está el proceso:

from freemocap import FreeMoCapProject

# Crear proyecto
project = FreeMoCapProject.create_new_project(
    project_name="yo_mocap",
    base_folder_path=r"C:\\Users\\andre\\OneDrive\\Documentos\\tesis\\freemocap_output"
)

# Procesar video
project.process_single_video(
    video_path=r"C:\\Users\\andre\\OneDrive\\Documentos\\tesis\\test\\output\\videos\\yo.mp4"
)

# Exportar
project.export_to_blender()


MÉTODO 3: Usar la v12 mejorada
───────────────────────────────
Si FreeMoCap no funciona bien con un solo video, te recomiendo:

1. Usar los scripts que ya creamos (v9, v12) pero ajustar los parámetros
2. El problema principal es la conversión de coordenadas 2D→3D
3. Podemos calibrar mejor los valores de escala y offset


¿CUÁL MÉTODO PREFIERES?
────────────────────────
A) Abrir GUI de FreeMoCap ahora
B) Probar API programática
C) Ajustar y mejorar la v12 que ya tenemos (más rápido)

""")

print("="*70)
print("\nPara abrir la GUI de FreeMoCap, ejecuta en una terminal:")
print("  freemocap")
print("="*70)
