import bpy
from pathlib import Path

BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_MODEL = BASE_DIR / "Nancy" / "Nancy.glb"
NINA_FILE = BASE_DIR / "Nina" / "cortesia" / "Nina_resultado_a la orden.glb"

print("="*80)
print("COMPARACIÓN DE NOMBRES DE HUESOS")
print("="*80)

# Cargar Nancy
print("\n📦 Cargando Nancy...")
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(NANCY_MODEL))

nancy_arm = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        nancy_arm = obj
        break

nancy_bones = set(nancy_arm.data.bones.keys())
print(f"   ✅ {len(nancy_bones)} huesos")

# Cargar Nina
print("\n📦 Cargando Nina...")
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(NINA_FILE))

nina_arm = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        nina_arm = obj
        break

nina_bones = set(nina_arm.data.bones.keys())
print(f"   ✅ {len(nina_bones)} huesos")

# Comparar
comunes = nancy_bones & nina_bones
solo_nancy = nancy_bones - nina_bones
solo_nina = nina_bones - nancy_bones

print(f"\n📊 Comparación:")
print(f"   Comunes: {len(comunes)}")
print(f"   Solo en Nancy: {len(solo_nancy)}")
print(f"   Solo en Nina: {len(solo_nina)}")

if solo_nancy:
    print(f"\n⚠️ Huesos solo en Nancy:")
    for bone in list(solo_nancy)[:10]:
        print(f"      - {bone}")

if solo_nina:
    print(f"\n⚠️ Huesos solo en Nina:")
    for bone in list(solo_nina)[:10]:
        print(f"      - {bone}")

# Verificar si LeftHand existe en ambos
print(f"\n🦴 Verificando 'LeftHand':")
print(f"   En Nancy: {'LeftHand' in nancy_bones}")
print(f"   En Nina: {'LeftHand' in nina_bones}")

# Mostrar algunos huesos de cada uno
print(f"\n📋 Primeros 10 huesos de Nancy:")
for bone in list(nancy_bones)[:10]:
    print(f"      - {bone}")

print(f"\n📋 Primeros 10 huesos de Nina:")
for bone in list(nina_bones)[:10]:
    print(f"      - {bone}")
