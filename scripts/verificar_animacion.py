"""
Script para verificar la animación en un FBX
Abre Blender y muestra información detallada sobre la animación
"""

import bpy
import sys

# Limpiar escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Obtener archivo del argumento
if len(sys.argv) > 4:
    fbx_path = sys.argv[4]  # Blender pasa args después de --
else:
    fbx_path = r"C:\Users\andre\OneDrive\Documentos\tesis\output\Leonard_con_animacion_b.fbx"

print("="*70)
print(f"VERIFICANDO: {fbx_path}")
print("="*70)

# Importar FBX
print("\n📥 Importando FBX...")
bpy.ops.import_scene.fbx(filepath=fbx_path)

# Encontrar armature
armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']

if not armatures:
    print("❌ No se encontró armature")
    sys.exit(1)

armature = armatures[0]
print(f"✅ Armature encontrado: {armature.name}")
print(f"   Huesos: {len(armature.data.bones)}")

# Verificar animación
if not armature.animation_data:
    print("\n❌ NO HAY ANIMACIÓN")
    sys.exit(1)

if not armature.animation_data.action:
    print("\n❌ NO HAY ACTION")
    sys.exit(1)

action = armature.animation_data.action
print(f"\n✅ Animación encontrada: {action.name}")
print(f"   Frames: {int(action.frame_range[0])} - {int(action.frame_range[1])}")
print(f"   Total frames: {int(action.frame_range[1] - action.frame_range[0]) + 1}")

# Contar FCurves
print(f"   FCurves: {len(action.fcurves)}")

# Analizar huesos animados
huesos_animados = set()
for fcurve in action.fcurves:
    if "pose.bones" in fcurve.data_path:
        inicio = fcurve.data_path.find('["') + 2
        fin = fcurve.data_path.find('"]')
        if inicio >= 2 and fin > 0:
            hueso = fcurve.data_path[inicio:fin]
            huesos_animados.add(hueso)

print(f"   Huesos animados: {len(huesos_animados)}")

if huesos_animados:
    print("\n🦴 Primeros 10 huesos animados:")
    for i, hueso in enumerate(list(huesos_animados)[:10]):
        print(f"   {i+1}. {hueso}")

# Verificar keyframes
total_keyframes = sum(len(fc.keyframe_points) for fc in action.fcurves)
print(f"\n⏱️  Total keyframes: {total_keyframes}")

# Verificar meshes
meshes = [obj for obj in bpy.data.objects if obj.type == 'MESH' and obj.parent == armature]
print(f"\n🎨 Meshes: {len(meshes)}")
for mesh in meshes[:5]:
    print(f"   - {mesh.name}")
    if mesh.data.materials:
        for mat in mesh.data.materials[:2]:
            if mat:
                print(f"     Material: {mat.name}")

# Configurar escena para reproducir
bpy.context.scene.frame_start = int(action.frame_range[0])
bpy.context.scene.frame_end = int(action.frame_range[1])

print("\n" + "="*70)
if total_keyframes > 100:
    print("✅ ANIMACIÓN VÁLIDA - Tiene suficientes keyframes")
else:
    print("⚠️  ANIMACIÓN SOSPECHOSA - Pocos keyframes")
print("="*70)

# Guardar blend file para inspección manual
blend_path = fbx_path.replace('.fbx', '_verificacion.blend')
bpy.ops.wm.save_as_mainfile(filepath=blend_path)
print(f"\n💾 Archivo .blend guardado: {blend_path}")
print("   Ábrelo en Blender y presiona ESPACIO para ver la animación")
