"""
DEPURACIÓN: Verificar QUÉ se exportó realmente en el GLB
"""

import bpy
from pathlib import Path

glb_result = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_BRAZOS_FINAL.glb")

print("="*80)
print("DEPURACIÓN: Analizar GLB resultante")
print("="*80)

bpy.ops.wm.read_homefile(use_empty=True)

print(f"\n📦 Importando {glb_result.name}...")
bpy.ops.import_scene.gltf(filepath=str(glb_result))

# Encontrar armature
armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        armature = obj
        break

if not armature:
    print("❌ No se encontró armature")
    exit(1)

print(f"✓ Armature: {armature.name}")
print(f"✓ Huesos: {len(armature.data.bones)}")

# Verificar animación
if not armature.animation_data:
    print("❌ NO hay animation_data")
    exit(1)

if not armature.animation_data.action:
    print("❌ NO hay action")
    exit(1)

action = armature.animation_data.action
print(f"\n✓ Action: {action.name}")
print(f"✓ Frames: {action.frame_range[0]:.0f} - {action.frame_range[1]:.0f}")
print(f"✓ FCurves totales: {len(action.fcurves)}")

# Analizar FCurves de brazos
print(f"\n📊 Analizando FCurves de brazos:")

arm_bones = ['LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand',
             'RightShoulder', 'RightArm', 'RightForeArm', 'RightHand']

for bone_name in arm_bones:
    bone_path = f'pose.bones["{bone_name}"]'
    
    # Contar fcurves para este hueso
    fcurves_bone = [fc for fc in action.fcurves if fc.data_path.startswith(bone_path)]
    
    if not fcurves_bone:
        print(f"   ❌ {bone_name}: NO tiene FCurves")
    else:
        # Ver qué propiedades tienen keyframes
        properties = set()
        for fc in fcurves_bone:
            # Extraer propiedad (rotation_quaternion, location, etc.)
            prop = fc.data_path.split('.')[-1]
            properties.add(prop)
        
        total_keyframes = sum(len(fc.keyframe_points) for fc in fcurves_bone)
        print(f"   ✓ {bone_name}: {len(fcurves_bone)} fcurves, {total_keyframes} keyframes, propiedades: {properties}")

# Verificar un frame específico
print(f"\n🔍 Verificación Frame 30:")
bpy.context.scene.frame_set(30)
bpy.context.view_layer.update()

for bone_name in ['LeftShoulder', 'LeftArm']:
    if bone_name in armature.pose.bones:
        bone = armature.pose.bones[bone_name]
        rot = bone.rotation_quaternion
        loc = bone.location
        print(f"\n   {bone_name}:")
        print(f"      Rotation: w={rot.w:.3f}, x={rot.x:.3f}, y={rot.y:.3f}, z={rot.z:.3f}")
        print(f"      Location: x={loc.x:.3f}, y={loc.y:.3f}, z={loc.z:.3f}")
        
        # Ver si tiene constraint (no debería después del bake)
        if bone.constraints:
            print(f"      ⚠ TIENE CONSTRAINTS: {[c.type for c in bone.constraints]}")
        else:
            print(f"      ✓ Sin constraints (correcto)")

print(f"\n{'='*80}")
print(f"DEPURACIÓN COMPLETADA")
print(f"{'='*80}")
