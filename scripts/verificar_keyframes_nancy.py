import bpy
from pathlib import Path

NANCY_HOLA = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy\saludos\Nancy_resultado_hola.glb")
NINA_HOLA = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nina\saludos\Nina_resultado_hola.glb")

print("="*80)
print("VERIFICACIÓN DETALLADA: Comparando keyframes de Nina vs Nancy")
print("="*80)

# Cargar Nancy
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(NANCY_HOLA))

nancy_arm = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        nancy_arm = obj
        break

if not nancy_arm or not nancy_arm.animation_data or not nancy_arm.animation_data.action:
    print("❌ Nancy no tiene animación")
    exit(1)

nancy_action = nancy_arm.animation_data.action

# Cargar Nina
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(NINA_HOLA))

nina_arm = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        nina_arm = obj
        break

if not nina_arm or not nina_arm.animation_data or not nina_arm.animation_data.action:
    print("❌ Nina no tiene animación")
    exit(1)

nina_action = nina_arm.animation_data.action

# Comparar un hueso específico (LeftHand por ejemplo)
print("\n🦴 Comparando hueso: LeftHand")
print("-" * 80)

nina_fcurves_lefthand = [fc for fc in nina_action.fcurves if "LeftHand" in fc.data_path and "location" in fc.data_path]
nancy_fcurves_lefthand = [fc for fc in nancy_action.fcurves if "LeftHand" in fc.data_path and "location" in fc.data_path]

print(f"Nina FCurves LeftHand location: {len(nina_fcurves_lefthand)}")
print(f"Nancy FCurves LeftHand location: {len(nancy_fcurves_lefthand)}")

if nina_fcurves_lefthand and nancy_fcurves_lefthand:
    nina_fc = nina_fcurves_lefthand[0]
    nancy_fc = nancy_fcurves_lefthand[0]
    
    print(f"\nNina keyframes en {nina_fc.data_path}[{nina_fc.array_index}]: {len(nina_fc.keyframe_points)}")
    print(f"Nancy keyframes en {nancy_fc.data_path}[{nancy_fc.array_index}]: {len(nancy_fc.keyframe_points)}")
    
    # Comparar primeros 5 keyframes
    print("\nComparando primeros 5 keyframes:")
    for i in range(min(5, len(nina_fc.keyframe_points), len(nancy_fc.keyframe_points))):
        nina_kf = nina_fc.keyframe_points[i]
        nancy_kf = nancy_fc.keyframe_points[i]
        
        print(f"  Frame {nina_kf.co[0]:.0f}:")
        print(f"    Nina:  {nina_kf.co[1]:.6f}")
        print(f"    Nancy: {nancy_kf.co[1]:.6f}")
        
        if abs(nina_kf.co[0] - nancy_kf.co[0]) < 0.01 and abs(nina_kf.co[1] - nancy_kf.co[1]) < 0.0001:
            print(f"    ✅ COINCIDE")
        else:
            print(f"    ❌ DIFERENTE")

print("\n" + "="*80)
print("CONCLUSIÓN:")
if len(nina_fcurves_lefthand) == len(nancy_fcurves_lefthand) and len(nina_fcurves_lefthand) > 0:
    print("✅ Nancy tiene la animación de Nina copiada correctamente")
else:
    print("⚠️ Hay diferencias en las FCurves")
print("="*80)
