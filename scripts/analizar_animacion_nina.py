import bpy
from pathlib import Path

NINA_FILE = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nina\cortesia\Nina_resultado_a la orden.glb")

print("="*80)
print("ANÁLISIS DE ANIMACIÓN DE NINA")
print("="*80)

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(NINA_FILE))

arm = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        arm = obj
        break

if not arm or not arm.animation_data or not arm.animation_data.action:
    print("❌ No hay animación")
    exit(1)

action = arm.animation_data.action

print(f"\n🎬 Action: {action.name}")
print(f"📊 Total FCurves: {len(action.fcurves)}")

# Analizar primeras 10 FCurves
print(f"\n📋 Primeras 10 FCurves:")
for i, fc in enumerate(action.fcurves[:10]):
    kf_count = len(fc.keyframe_points)
    print(f"  {i+1}. {fc.data_path}[{fc.array_index}] - {kf_count} keyframes")
    
    if kf_count > 0:
        first_kf = fc.keyframe_points[0]
        last_kf = fc.keyframe_points[-1]
        print(f"      Primera: frame {first_kf.co[0]:.0f}, valor {first_kf.co[1]:.4f}")
        print(f"      Última:  frame {last_kf.co[0]:.0f}, valor {last_kf.co[1]:.4f}")

# Buscar FCurves de LeftHand específicamente
print(f"\n🦴 FCurves de LeftHand:")
lefthand_fcurves = [fc for fc in action.fcurves if "LeftHand" in fc.data_path]
print(f"  Total: {len(lefthand_fcurves)}")

for fc in lefthand_fcurves[:5]:
    kf_count = len(fc.keyframe_points)
    print(f"  - {fc.data_path}[{fc.array_index}] - {kf_count} keyframes")

# Verificar si hay movimiento real
print(f"\n🎯 Verificando movimiento en diferentes frames:")
for frame in [0, 10, 20, 30, 40, 50, 60]:
    bpy.context.scene.frame_set(frame)
    if "LeftHand" in arm.pose.bones:
        bone = arm.pose.bones["LeftHand"]
        loc = bone.location
        rot = bone.rotation_quaternion
        print(f"  Frame {frame}: loc=({loc.x:.3f}, {loc.y:.3f}, {loc.z:.3f}), rot=({rot.w:.3f}, {rot.x:.3f}, {rot.y:.3f}, {rot.z:.3f})")
