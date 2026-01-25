import bpy
from pathlib import Path

# Test aleatorio de un archivo del batch anterior
TEST_FILE = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy\saludos\Nancy_resultado_hola.glb")

print(f"🔍 Verificando archivo del batch anterior: {TEST_FILE.name}")

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(TEST_FILE))

test_arm = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        test_arm = obj
        break

if test_arm and test_arm.animation_data and test_arm.animation_data.action:
    test_action = test_arm.animation_data.action
    
    print(f"Action: {test_action.name}")
    print(f"FCurves totales: {len(test_action.fcurves)}")
    
    # Test de movimiento
    bpy.context.scene.frame_set(0)
    pos_inicial = test_arm.pose.bones["Hips"].matrix.translation.copy()
    bpy.context.scene.frame_set(30)
    pos_final = test_arm.pose.bones["Hips"].matrix.translation.copy()
    distancia = (pos_final - pos_inicial).length
    
    print(f"Movimiento Hips frame 0→30: {distancia:.6f}")
    
    if distancia > 0.001:
        print("✅ Animación funciona")
    else:
        print("❌ Sin movimiento")
else:
    print("❌ Sin action")
