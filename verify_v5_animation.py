"""Verificar animación en nancy_yo_real_v5.glb"""
import bpy
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
GLB_FILE = os.path.join(SCRIPT_DIR, 'nancy_yo_real_v5.glb')

print("\n" + "="*70)
print("VERIFICACIÓN ANIMACIÓN V5")
print("="*70)

# Limpiar escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Importar GLB
bpy.ops.import_scene.gltf(filepath=GLB_FILE)
print(f"\n✓ GLB importado: nancy_yo_real_v5.glb")

# Encontrar armature
armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        armature = obj
        break

if not armature:
    print("❌ No armature encontrada")
    exit(1)

print(f"\n📦 Armature: {armature.name}")

# Verificar animation data
if not armature.animation_data:
    print("❌ NO HAY ANIMATION_DATA")
    exit(1)

if not armature.animation_data.action:
    print("❌ NO HAY ACTION")
    exit(1)

action = armature.animation_data.action
print(f"✓ Action: {action.name}")
print(f"✓ FCurves: {len(action.fcurves)}")

# Analizar FCurves
print(f"\n📊 ANÁLISIS DE FCURVES:")
bones_animated = {}
for fc in action.fcurves:
    # Extraer nombre del hueso
    path = fc.data_path
    if 'pose.bones[' in path:
        bone_name = path.split('"')[1]
        if bone_name not in bones_animated:
            bones_animated[bone_name] = []
        bones_animated[bone_name].append(fc.array_index)

for bone_name, channels in sorted(bones_animated.items()):
    print(f"   {bone_name}: canales {channels}")

# Verificar keyframes en frame específicos
print(f"\n🔍 VALORES EN FRAMES ESPECÍFICOS:")
bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode='POSE')

test_bones = ['LeftArm', 'RightArm', 'LeftForeArm', 'RightForeArm']
test_frames = [1, 10, 30, 54]

for bone_name in test_bones:
    if bone_name not in armature.pose.bones:
        continue
    print(f"\n{bone_name}:")
    pose_bone = armature.pose.bones[bone_name]
    
    for frame in test_frames:
        bpy.context.scene.frame_set(frame)
        rot = pose_bone.rotation_euler
        print(f"  Frame {frame:2d}: ({rot.x:.4f}, {rot.y:.4f}, {rot.z:.4f})")

bpy.ops.object.mode_set(mode='OBJECT')

print("\n" + "="*70)
print("DIAGNÓSTICO:")

# Verificar si hay cambio entre frames
has_movement = False
for bone_name in test_bones:
    if bone_name not in armature.pose.bones:
        continue
    pose_bone = armature.pose.bones[bone_name]
    
    bpy.context.scene.frame_set(1)
    rot1 = pose_bone.rotation_euler.copy()
    
    bpy.context.scene.frame_set(30)
    rot2 = pose_bone.rotation_euler.copy()
    
    diff = (rot2 - rot1).length
    if diff > 0.01:
        has_movement = True
        print(f"✓ {bone_name}: SÍ hay movimiento (diff={diff:.4f})")
    else:
        print(f"✗ {bone_name}: NO hay movimiento (diff={diff:.4f})")

print("\n" + "="*70)
if has_movement:
    print("✓ ANIMACIÓN PRESENTE")
else:
    print("❌ ANIMACIÓN AUSENTE O VALORES DEMASIADO PEQUEÑOS")
print("="*70 + "\n")
