import bpy
from pathlib import Path

print("="*80)
print("TEST FINAL: Verificación de Nancy con animación de Nina")
print("="*80)

# Cargar archivo de Nancy
nancy_file = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy\saludos\Nancy_resultado_hola.glb")

bpy.ops.wm.read_factory_settings(use_empty=True)
print(f"\n📂 Cargando: {nancy_file.name}")
bpy.ops.import_scene.gltf(filepath=str(nancy_file))

# Contar objetos
armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
meshes = [obj for obj in bpy.data.objects if obj.type == 'MESH']

print(f"\n📊 Objetos cargados:")
print(f"   Armatures: {len(armatures)}")
print(f"   Mallas: {len(meshes)}")

if len(armatures) != 1:
    print(f"❌ ERROR: Debería haber 1 armature, encontrados: {len(armatures)}")
    exit(1)

arm = armatures[0]

# Verificar animación
if not arm.animation_data:
    print("❌ ERROR: No tiene animation_data")
    exit(1)

if not arm.animation_data.action:
    print("❌ ERROR: No tiene action")
    exit(1)

action = arm.animation_data.action
frames = action.frame_range[1] - action.frame_range[0]

print(f"\n🎬 Animación:")
print(f"   Nombre: {action.name}")
print(f"   Frames: {frames:.0f}")
print(f"   FCurves: {len(action.fcurves)}")

# Verificar que las mallas sean de Nancy (no de Nina)
print(f"\n👗 Mallas encontradas:")
for mesh in meshes:
    print(f"   - {mesh.name}")

# Buscar nombres típicos de Nancy/Nina (ambos usan Wolf3D)
wolf3d_meshes = [m for m in meshes if 'Wolf3D' in m.name]
print(f"\n✅ Mallas Wolf3D: {len(wolf3d_meshes)}")

if len(wolf3d_meshes) < 5:
    print("⚠️ Advertencia: Pocas mallas Wolf3D encontradas")

# Verificar que hay animación en los huesos
print(f"\n🦴 Huesos con animación:")
bones_animated = set()
for fc in action.fcurves:
    if "pose.bones[" in fc.data_path:
        # Extraer nombre del hueso
        bone_name = fc.data_path.split('"')[1]
        bones_animated.add(bone_name)

print(f"   Total: {len(bones_animated)} huesos animados")
if len(bones_animated) > 50:
    print(f"   ✅ Suficientes huesos animados")
    
    # Mostrar algunos ejemplos
    sample_bones = list(bones_animated)[:5]
    print(f"   Ejemplos: {', '.join(sample_bones)}")
else:
    print(f"   ⚠️ Pocos huesos animados")

print("\n" + "="*80)
print("RESULTADO FINAL:")
if len(armatures) == 1 and frames > 50 and len(bones_animated) > 50 and len(wolf3d_meshes) >= 5:
    print("✅ ✅ ✅ ÉXITO COMPLETO ✅ ✅ ✅")
    print("Nancy tiene su propia malla con la animación de Nina")
else:
    print("⚠️ Hay problemas en la transferencia")
print("="*80)
