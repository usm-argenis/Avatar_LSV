import bpy
from pathlib import Path

# Archivos a comparar
FILE1 = Path(r"C:\Users\andre\Downloads\verbo_default (1).glb")
FILE2 = Path(r"C:\Users\andre\Downloads\verbo_default.glb")

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def analyze_file(filepath):
    """Analiza un archivo GLB de Deepmotion"""
    clear_scene()
    bpy.ops.import_scene.gltf(filepath=str(filepath))
    
    info = {
        'meshes': [],
        'armature': None,
        'bones': [],
        'animations': [],
        'duration': 0
    }
    
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            info['meshes'].append(obj.name)
        elif obj.type == 'ARMATURE':
            info['armature'] = obj.name
            info['bones'] = [bone.name for bone in obj.data.bones]
    
    # Verificar animaciones
    for action in bpy.data.actions:
        info['animations'].append(action.name)
        if action.frame_range[1] > info['duration']:
            info['duration'] = action.frame_range[1]
    
    return info

print("="*70)
print("ANÁLISIS DE ARCHIVOS DEEPMOTION")
print("="*70)

# Analizar archivo 1
print(f"\n📦 ARCHIVO 1: {FILE1.name}")
info1 = analyze_file(FILE1)
print(f"   Armature: {info1['armature']}")
print(f"   Huesos: {len(info1['bones'])}")
print(f"   Meshes: {len(info1['meshes'])}")
print(f"   Animaciones: {len(info1['animations'])}")
print(f"   Duración: {info1['duration']} frames")

if info1['bones']:
    print(f"\n   🦴 Huesos principales:")
    for bone in sorted(info1['bones'])[:20]:
        print(f"      - {bone}")

# Analizar archivo 2
print(f"\n📦 ARCHIVO 2: {FILE2.name}")
info2 = analyze_file(FILE2)
print(f"   Armature: {info2['armature']}")
print(f"   Huesos: {len(info2['bones'])}")
print(f"   Meshes: {len(info2['meshes'])}")
print(f"   Animaciones: {len(info2['animations'])}")
print(f"   Duración: {info2['duration']} frames")

if info2['bones']:
    print(f"\n   🦴 Huesos principales:")
    for bone in sorted(info2['bones'])[:20]:
        print(f"      - {bone}")

# Comparación
print("\n" + "="*70)
print("COMPARACIÓN")
print("="*70)

if info1['bones'] == info2['bones']:
    print("✅ Mismo esqueleto (huesos idénticos)")
else:
    print("⚠️ Esqueletos diferentes")
    bones1_only = set(info1['bones']) - set(info2['bones'])
    bones2_only = set(info2['bones']) - set(info1['bones'])
    if bones1_only:
        print(f"   Huesos solo en archivo 1: {bones1_only}")
    if bones2_only:
        print(f"   Huesos solo en archivo 2: {bones2_only}")

if info1['duration'] == info2['duration']:
    print(f"✅ Misma duración ({info1['duration']} frames)")
else:
    print(f"⚠️ Duración diferente: {info1['duration']} vs {info2['duration']} frames")

# Verificar compatibilidad con Duvall
print("\n" + "="*70)
print("VERIFICACIÓN DE COMPATIBILIDAD CON DUVALL")
print("="*70)

# Cargar Duvall para comparar
DUVALL = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\Duvall.glb")
clear_scene()
bpy.ops.import_scene.gltf(filepath=str(DUVALL))

duvall_armature = None
duvall_bones = []
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        duvall_armature = obj
        duvall_bones = [bone.name for bone in obj.data.bones]
        break

print(f"Duvall tiene {len(duvall_bones)} huesos")
print(f"Deepmotion tiene {len(info1['bones'])} huesos")

# Buscar huesos comunes críticos
critical_bones = ['Hips', 'Spine', 'Spine1', 'Spine2', 'Neck', 'Head',
                  'LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand',
                  'RightShoulder', 'RightArm', 'RightForeArm', 'RightHand',
                  'LeftUpLeg', 'LeftLeg', 'LeftFoot',
                  'RightUpLeg', 'RightLeg', 'RightFoot']

print("\n🔍 Huesos críticos:")
deepmotion_bones_lower = [b.lower() for b in info1['bones']]
duvall_bones_lower = [b.lower() for b in duvall_bones]

for bone in critical_bones:
    in_deepmotion = any(bone.lower() in db for db in deepmotion_bones_lower)
    in_duvall = any(bone.lower() in db for db in duvall_bones_lower)
    
    if in_deepmotion and in_duvall:
        print(f"   ✅ {bone}")
    elif in_deepmotion:
        print(f"   ⚠️ {bone} (solo en Deepmotion)")
    elif in_duvall:
        print(f"   ⚠️ {bone} (solo en Duvall)")
    else:
        print(f"   ❌ {bone} (no encontrado)")

print("\n" + "="*70)
print("CONCLUSIÓN")
print("="*70)

if len(info1['bones']) > 0 and len(duvall_bones) > 0:
    print("✅ Retargeting es posible")
    print(f"   Método: Mapeo de huesos Deepmotion → Duvall")
else:
    print("❌ Retargeting NO es posible")
