import bpy
from pathlib import Path

print("="*80)
print("TEST: Verificar animación completa en Nancy exportada")
print("="*80)

NANCY_OUTPUT = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy\cortesia\Nancy_resultado_a la orden.glb")

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(NANCY_OUTPUT))

arm = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        arm = obj
        break

if not arm:
    print("❌ No hay armature")
    exit(1)

if not arm.animation_data or not arm.animation_data.action:
    print("❌ No hay animación")
    exit(1)

action = arm.animation_data.action
print(f"\n✅ Action: {action.name}")
print(f"FCurves: {len(action.fcurves)}")
print(f"Frames: {action.frame_range[1] - action.frame_range[0]:.0f}")

# Contar tipos de canales
tipos_canales = {}
for fc in action.fcurves:
    # Obtener tipo (location, rotation, scale)
    if "location" in fc.data_path:
        tipo = "location"
    elif "rotation" in fc.data_path:
        tipo = "rotation"
    elif "scale" in fc.data_path:
        tipo = "scale"
    else:
        tipo = "otro"
    
    tipos_canales[tipo] = tipos_canales.get(tipo, 0) + 1

print(f"\nTipos de canales:")
for tipo, count in tipos_canales.items():
    print(f"  {tipo}: {count}")

# Buscar un hueso que debería moverse (RightArm por ejemplo)
print(f"\n🦴 Verificando hueso RightArm:")
rightarm_fcs = [fc for fc in action.fcurves if "RightArm" in fc.data_path and "rotation" in fc.data_path]

if rightarm_fcs:
    print(f"  FCurves rotation: {len(rightarm_fcs)}")
    fc = rightarm_fcs[0]
    print(f"  Canal: {fc.data_path}")
    print(f"  Keyframes: {len(fc.keyframe_points)}")
    
    # Verificar que los valores cambien
    valores = [kf.co[1] for kf in fc.keyframe_points[:10]]
    valores_unicos = len(set([round(v, 4) for v in valores]))
    
    if valores_unicos > 1:
        print(f"  ✅ Los valores CAMBIAN (hay movimiento)")
        print(f"  Rango: {min(valores):.4f} a {max(valores):.4f}")
    else:
        print(f"  ❌ Los valores NO CAMBIAN (sin movimiento)")
        print(f"  Valor constante: {valores[0]:.4f}")
else:
    print(f"  ❌ No hay FCurves de rotation para RightArm")

# Probar animación frame por frame
print(f"\n🎬 Probando animación frame por frame:")
bpy.context.scene.frame_set(0)
initial_loc = arm.pose.bones["Hips"].matrix.translation.copy()

bpy.context.scene.frame_set(30)
mid_loc = arm.pose.bones["Hips"].matrix.translation.copy()

diff = (mid_loc - initial_loc).length

if diff > 0.001:
    print(f"  ✅ Los huesos SE MUEVEN")
    print(f"  Distancia Hips frame 0→30: {diff:.4f}")
else:
    print(f"  ❌ Los huesos NO SE MUEVEN")
    print(f"  Distancia: {diff:.6f}")

print("\n" + "="*80)
