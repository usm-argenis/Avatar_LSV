"""Test rápido de nancy_yo_real_v8.glb"""
import bpy
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
GLB_FILE = os.path.join(SCRIPT_DIR, 'nancy_yo_real_v8.glb')

print("\n" + "="*70)
print("TEST V8 - VERIFICACIÓN")
print("="*70)

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
bpy.ops.import_scene.gltf(filepath=GLB_FILE)

armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        armature = obj
        break

if not armature or not armature.animation_data or not armature.animation_data.action:
    print("❌ Sin animación")
    exit(1)

action = armature.animation_data.action
print(f"\n✓ Action: {action.name}")
print(f"✓ FCurves: {len(action.fcurves)}")

# Verificar valores EULER
bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode='POSE')

print(f"\n📊 TEST DE MOVIMIENTO (EULER):")
for bone_name in ['LeftArm', 'RightArm']:
    if bone_name not in armature.pose.bones:
        continue
    
    pose_bone = armature.pose.bones[bone_name]
    
    bpy.context.scene.frame_set(1)
    rot1 = pose_bone.rotation_euler.copy()
    
    bpy.context.scene.frame_set(30)
    rot2 = pose_bone.rotation_euler.copy()
    
    # Diferencia en radianes
    diff_x = abs(rot2.x - rot1.x)
    diff_z = abs(rot2.z - rot1.z)
    
    # Convertir a grados
    diff_deg = math.sqrt(diff_x**2 + diff_z**2) * 57.2958
    
    if diff_deg > 10.0:
        print(f"   ✓ {bone_name}: {diff_deg:.1f}° (EXCELENTE)")
    elif diff_deg > 5.0:
        print(f"   ⚠ {bone_name}: {diff_deg:.1f}° (BUENO)")
    elif diff_deg > 1.0:
        print(f"   ⚠ {bone_name}: {diff_deg:.1f}° (PEQUEÑO)")
    else:
        print(f"   ✗ {bone_name}: {diff_deg:.1f}° (MUY PEQUEÑO)")

bpy.ops.object.mode_set(mode='OBJECT')
print("="*70 + "\n")


print("\n" + "="*70)
print("TEST V6 - VERIFICACIÓN RÁPIDA")
print("="*70)

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
bpy.ops.import_scene.gltf(filepath=GLB_FILE)

armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        armature = obj
        break

if not armature or not armature.animation_data or not armature.animation_data.action:
    print("❌ Sin animación")
    exit(1)

action = armature.animation_data.action
print(f"\n✓ Action: {action.name}")
print(f"✓ FCurves: {len(action.fcurves)}")

# Verificar valores
bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode='POSE')

print(f"\n📊 TEST DE MOVIMIENTO:")
for bone_name in ['LeftArm', 'RightArm']:
    if bone_name not in armature.pose.bones:
        continue
    
    pose_bone = armature.pose.bones[bone_name]
    
    bpy.context.scene.frame_set(1)
    rot1 = pose_bone.rotation_quaternion.copy()
    
    bpy.context.scene.frame_set(30)
    rot2 = pose_bone.rotation_quaternion.copy()
    
    # Calcular diferencia angular
    diff_quat = rot1.rotation_difference(rot2)
    angle_diff = diff_quat.angle * 57.2958  # a grados
    
    if angle_diff > 5.0:
        print(f"   ✓ {bone_name}: {angle_diff:.1f}° cambio (BUENO)")
    elif angle_diff > 1.0:
        print(f"   ⚠ {bone_name}: {angle_diff:.1f}° cambio (PEQUEÑO)")
    else:
        print(f"   ✗ {bone_name}: {angle_diff:.1f}° cambio (MUY PEQUEÑO)")

bpy.ops.object.mode_set(mode='OBJECT')
print("="*70 + "\n")
