import bpy
from pathlib import Path

LUIS_BASE = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Luis\Luis.glb")

print(f"Verificando: {LUIS_BASE}")
print(f"Existe: {LUIS_BASE.exists()}")
print(f"Tamaño: {LUIS_BASE.stat().st_size if LUIS_BASE.exists() else 0}")

try:
    print("Intentando importar...")
    bpy.ops.import_scene.gltf(filepath=str(LUIS_BASE))
    print(f"✅ Importado correctamente")
    print(f"Objetos en escena: {len(bpy.data.objects)}")
    for obj in bpy.data.objects:
        print(f"  - {obj.name} ({obj.type})")
except Exception as e:
    print(f"❌ Error: {e}")
