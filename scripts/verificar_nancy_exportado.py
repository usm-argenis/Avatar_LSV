import bpy
from pathlib import Path

print("="*80)
print("VERIFICACIÓN: Archivo Nancy exportado")
print("="*80)

NANCY_OUTPUT = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy\cortesia\Nancy_resultado_a la orden.glb")

bpy.ops.wm.read_factory_settings(use_empty=True)
print(f"\n📂 Cargando: {NANCY_OUTPUT.name}")
bpy.ops.import_scene.gltf(filepath=str(NANCY_OUTPUT))

arm = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        arm = obj
        break

if not arm:
    print("❌ No se encontró armature")
    exit(1)

print(f"\n✅ Armature: {arm.name}")

if not arm.animation_data:
    print("❌ No tiene animation_data")
    exit(1)

if not arm.animation_data.action:
    print("❌ No tiene action")
    exit(1)

action = arm.animation_data.action
print(f"\n🎬 Animación:")
print(f"   Nombre: {action.name}")
print(f"   Frames: {action.frame_range[1] - action.frame_range[0]:.0f}")
print(f"   FCurves: {len(action.fcurves)}")

# Analizar FCurves
print(f"\n📊 Analizando FCurves...")
bones_en_fcurves = set()
for fc in action.fcurves:
    if "pose.bones[" in fc.data_path:
        start = fc.data_path.find('["') + 2
        end = fc.data_path.find('"]')
        bone_name = fc.data_path[start:end]
        bones_en_fcurves.add(bone_name)

print(f"   Huesos con FCurves: {len(bones_en_fcurves)}")

# Verificar que los huesos existen en el armature
bones_armature = set([b.name for b in arm.data.bones])
print(f"   Huesos en armature: {len(bones_armature)}")

huesos_ok = bones_en_fcurves & bones_armature
huesos_faltantes = bones_en_fcurves - bones_armature

print(f"\n   ✅ Huesos que coinciden: {len(huesos_ok)}")
print(f"   ❌ Huesos en FCurves que NO existen en armature: {len(huesos_faltantes)}")

if huesos_faltantes:
    print(f"\n   ⚠️ PROBLEMA ENCONTRADO:")
    for bone in list(huesos_faltantes)[:10]:
        print(f"      - FCurve referencia '{bone}' pero no existe en armature")

# Probar animación en varios frames
print(f"\n🎥 Probando animación...")
bpy.context.scene.frame_start = int(action.frame_range[0])
bpy.context.scene.frame_end = int(action.frame_range[1])

test_bone_name = "LeftHand"
if test_bone_name in arm.pose.bones:
    bone = arm.pose.bones[test_bone_name]
    
    print(f"\n   Testeando hueso: {test_bone_name}")
    
    test_frames = [0, 10, 30, int(action.frame_range[1])]
    positions = []
    
    for frame in test_frames:
        bpy.context.scene.frame_set(frame)
        pos = bone.matrix.translation.copy()
        positions.append((frame, pos))
        print(f"      Frame {frame}: pos=({pos.x:.3f}, {pos.y:.3f}, {pos.z:.3f})")
    
    # Verificar si hay movimiento
    pos_inicial = positions[0][1]
    hay_movimiento = False
    
    for frame, pos in positions[1:]:
        distancia = (pos - pos_inicial).length
        if distancia > 0.001:  # Más de 1mm de movimiento
            hay_movimiento = True
            print(f"\n   ✅ Movimiento detectado en frame {frame}: {distancia:.4f} unidades")
            break
    
    if not hay_movimiento:
        print(f"\n   ❌ NO HAY MOVIMIENTO - El hueso permanece en pose A")
        print(f"   Esto indica que las FCurves NO se están aplicando")
        
        # Verificar si hay FCurves para este hueso
        fcurves_bone = [fc for fc in action.fcurves if test_bone_name in fc.data_path]
        print(f"\n   FCurves para {test_bone_name}: {len(fcurves_bone)}")
        if fcurves_bone:
            for fc in fcurves_bone[:3]:
                print(f"      - {fc.data_path}[{fc.array_index}]: {len(fc.keyframe_points)} keyframes")

print(f"\n{'='*80}")
print("CONCLUSIÓN:")
if huesos_faltantes:
    print("❌ Hay huesos en las FCurves que no existen en el armature")
elif not hay_movimiento:
    print("❌ Las FCurves existen pero NO se están aplicando al hueso")
else:
    print("✅ Todo funciona correctamente")
print(f"{'='*80}")
