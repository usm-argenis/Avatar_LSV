"""
Script para verificar la animación en nancy_yo_real.glb
Analiza qué huesos tienen animación
"""
import bpy
from pathlib import Path
import sys

GLB_FILE = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\nancy_yo_real_v3.glb")

print("\n" + "="*70)
print("VERIFICACIÓN DE ANIMACIÓN EN nancy_yo_real_v3.glb")
print("="*70 + "\n")

# Limpiar escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Importar GLB
print(f"Importando: {GLB_FILE}")
bpy.ops.import_scene.gltf(filepath=str(GLB_FILE))

# Encontrar armature
armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        armature = obj
        break

if not armature:
    print("❌ No se encontró armature")
    sys.exit(1)

print(f"✓ Armature encontrado: {armature.name}")

# Verificar animation data
if not armature.animation_data:
    print("❌ No tiene animation_data")
    sys.exit(1)

print(f"✓ Tiene animation_data")

# Verificar action
action = armature.animation_data.action
if not action:
    print("❌ No tiene action")
    sys.exit(1)

print(f"✓ Action: {action.name}")
print(f"  Frame range: {action.frame_range[0]:.0f} - {action.frame_range[1]:.0f}")
print(f"  Total FCurves: {len(action.fcurves)}")

# Analizar FCurves por hueso
print("\n" + "="*70)
print("ANÁLISIS DE ANIMACIÓN POR HUESO")
print("="*70)

bone_fcurves = {}
for fc in action.fcurves:
    # El data_path tiene formato: pose.bones["BoneName"].location
    if 'pose.bones[' in fc.data_path:
        bone_name = fc.data_path.split('"')[1]
        prop_type = fc.data_path.split('.')[-1]
        
        if bone_name not in bone_fcurves:
            bone_fcurves[bone_name] = {
                'location': [],
                'rotation_euler': [],
                'rotation_quaternion': [],
                'scale': []
            }
        
        bone_fcurves[bone_name][prop_type].append(fc)

# Categorizar huesos
categories = {
    'Cuerpo': ['Hips', 'Spine', 'Spine1', 'Spine2', 'Neck', 'Head'],
    'Brazos Izq': ['LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand'],
    'Brazos Der': ['RightShoulder', 'RightArm', 'RightForeArm', 'RightHand'],
    'Piernas Izq': ['LeftUpLeg', 'LeftLeg', 'LeftFoot'],
    'Piernas Der': ['RightUpLeg', 'RightLeg', 'RightFoot'],
}

for category, bones in categories.items():
    print(f"\n{category}:")
    for bone_name in bones:
        if bone_name in bone_fcurves:
            data = bone_fcurves[bone_name]
            total = sum(len(data[k]) for k in data.keys())
            keyframes = sum(len(fc.keyframe_points) for fcurves in data.values() for fc in fcurves)
            
            details = []
            if data['location']:
                details.append(f"loc({len(data['location'])})")
            if data['rotation_euler']:
                details.append(f"rot({len(data['rotation_euler'])})")
            if data['rotation_quaternion']:
                details.append(f"quat({len(data['rotation_quaternion'])})")
            
            status = "✓" if total > 0 else "✗"
            print(f"  {status} {bone_name:20s} - {keyframes:4d} keyframes {' '.join(details)}")
        else:
            print(f"  ✗ {bone_name:20s} - SIN ANIMACIÓN")

# Resumen
print("\n" + "="*70)
print("RESUMEN")
print("="*70)

total_bones_animated = len(bone_fcurves)
total_keyframes = sum(len(fc.keyframe_points) for fc in action.fcurves)

print(f"Total huesos animados: {total_bones_animated}")
print(f"Total keyframes: {total_keyframes}")

# Verificar huesos clave
critical_bones = ['LeftArm', 'RightArm', 'LeftForeArm', 'RightForeArm', 'LeftUpLeg', 'RightUpLeg']
animated_critical = [b for b in critical_bones if b in bone_fcurves]

print(f"\nHuesos críticos (extremidades) animados: {len(animated_critical)}/{len(critical_bones)}")

if len(animated_critical) >= 4:
    print("✅ ANIMACIÓN COMPLETA - Brazos y piernas tienen movimiento")
elif len(animated_critical) >= 2:
    print("⚠️  ANIMACIÓN PARCIAL - Solo algunos miembros animados")
else:
    print("❌ ANIMACIÓN INCOMPLETA - Extremidades sin movimiento")

print("\n" + "="*70)
