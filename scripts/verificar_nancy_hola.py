import bpy
from pathlib import Path

# Ruta al archivo a verificar
NANCY_HOLA = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy\saludos\Nancy_resultado_hola.glb")
NINA_HOLA = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nina\saludos\Nina_resultado_hola.glb")

print("="*80)
print("VERIFICACIÓN: Nancy_resultado_hola.glb")
print("="*80)

# Limpiar escena
bpy.ops.wm.read_factory_settings(use_empty=True)

# Cargar Nancy
print("\n1. Cargando Nancy_resultado_hola.glb...")
bpy.ops.import_scene.gltf(filepath=str(NANCY_HOLA))

# Buscar armature
nancy_arm = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        nancy_arm = obj
        break

if not nancy_arm:
    print("❌ No se encontró armature")
    exit(1)

print(f"✅ Armature encontrado: {nancy_arm.name}")

# Verificar animación
if not nancy_arm.animation_data:
    print("❌ No tiene animation_data")
    exit(1)

if not nancy_arm.animation_data.action:
    print("❌ No tiene action")
    exit(1)

action = nancy_arm.animation_data.action
print(f"✅ Action: {action.name}")

# Contar fcurves y frames
num_fcurves = len(action.fcurves)
frame_start, frame_end = action.frame_range
num_frames = frame_end - frame_start

print(f"✅ FCurves: {num_fcurves}")
print(f"✅ Frames: {num_frames:.0f} (de {frame_start:.0f} a {frame_end:.0f})")

# Contar keyframes totales
total_keyframes = sum(len(fc.keyframe_points) for fc in action.fcurves)
print(f"✅ Keyframes totales: {total_keyframes}")

# Verificar mallas
print("\n2. Verificando mallas de Nancy...")
meshes = [obj for obj in bpy.data.objects if obj.type == 'MESH']
print(f"✅ Mallas encontradas: {len(meshes)}")
for mesh in meshes:
    print(f"   - {mesh.name}")

# Comparar con Nina
print("\n3. Comparando con Nina_resultado_hola.glb...")
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(NINA_HOLA))

nina_arm = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        nina_arm = obj
        break

if nina_arm and nina_arm.animation_data and nina_arm.animation_data.action:
    nina_action = nina_arm.animation_data.action
    nina_frames = nina_action.frame_range[1] - nina_action.frame_range[0]
    nina_keyframes = sum(len(fc.keyframe_points) for fc in nina_action.fcurves)
    
    print(f"Nina frames: {nina_frames:.0f}")
    print(f"Nina keyframes: {nina_keyframes}")
    
    if abs(nina_frames - num_frames) < 1:
        print("✅ FRAMES COINCIDEN")
    else:
        print(f"⚠️ Diferencia en frames: {abs(nina_frames - num_frames):.0f}")
    
    if abs(nina_keyframes - total_keyframes) < 100:
        print("✅ KEYFRAMES SIMILARES")
    else:
        print(f"⚠️ Diferencia en keyframes: {abs(nina_keyframes - total_keyframes)}")

print("\n" + "="*80)
print("VERIFICACIÓN COMPLETADA")
print("="*80)
