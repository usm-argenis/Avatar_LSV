"""
Script de verificación: Abre Blender con UI para inspeccionar nancy_yo.glb
"""
import bpy
import sys

GLB_PATH = r"C:\Users\andre\OneDrive\Documentos\tesis\nancy_yo.glb"

# Limpiar escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Importar GLB
bpy.ops.import_scene.gltf(filepath=GLB_PATH)

print("\n" + "="*60)
print("VERIFICACIÓN DE ANIMACIÓN")
print("="*60)

# Buscar armature
armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        armature = obj
        break

if not armature:
    print("❌ NO HAY ARMATURE")
    sys.exit(1)

print(f"\n✓ Armature encontrado: {armature.name}")

# Verificar animation_data
if not armature.animation_data:
    print("❌ NO HAY ANIMATION DATA")
    sys.exit(1)

print(f"✓ Animation data existe")

# Verificar action
if not armature.animation_data.action:
    print("❌ NO HAY ACTION ASIGNADA")
    sys.exit(1)

action = armature.animation_data.action
print(f"✓ Action: {action.name}")
print(f"  Frame range: {action.frame_range[0]:.0f} - {action.frame_range[1]:.0f}")
print(f"  FCurves: {len(action.fcurves)}")

if len(action.fcurves) == 0:
    print("\n❌ PROBLEMA CRÍTICO: NO HAY FCURVES EN LA ACTION")
    print("   Esto significa que los keyframes NO se guardaron")
else:
    print(f"\n✓ La action tiene {len(action.fcurves)} FCurves")
    for fc in action.fcurves[:5]:  # Mostrar primeras 5
        print(f"  - {fc.data_path} [{fc.array_index}]: {len(fc.keyframe_points)} keyframes")

# Configurar timeline
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 120
bpy.context.scene.frame_current = 1

print("\n✓ Timeline configurado: frames 1-120")
print("\n" + "="*60)
print("INSTRUCCIONES:")
print("1. Ve a la pestaña 'Animation'")
print("2. Selecciona el Armature")
print("3. Presiona ESPACIO para reproducir")
print("4. Si NO se mueve, el problema está en el script de creación")
print("="*60)
