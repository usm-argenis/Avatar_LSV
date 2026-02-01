"""
Script para verificar visualmente la animación combinada en Blender
Abre el archivo Blend y reproduce la animación
"""

import bpy
import sys

blend_file = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_brazos_combinado.blend"

print("="*80)
print("VERIFICACIÓN VISUAL DE ANIMACIÓN COMBINADA")
print("="*80)

# Abrir el archivo
print(f"\nAbriendo archivo: {blend_file}")
bpy.ops.wm.open_mainfile(filepath=blend_file)

# Obtener el armature
armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        armature = obj
        break

if not armature:
    print("ERROR: No se encontró armature")
    sys.exit(1)

print(f"✓ Armature encontrado: {armature.name}")

# Verificar animación
if armature.animation_data and armature.animation_data.action:
    action = armature.animation_data.action
    print(f"✓ Animación: {action.name}")
    print(f"✓ Frames: {int(action.frame_range[0])} - {int(action.frame_range[1])}")
    print(f"✓ Total FCurves: {len(action.fcurves)}")
    
    # Huesos de brazos
    arm_bones = ['LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand',
                 'RightShoulder', 'RightArm', 'RightForeArm', 'RightHand']
    
    print("\n🎯 Verificación de huesos de brazos:")
    for bone_name in arm_bones:
        fcurves = [f for f in action.fcurves if f'pose.bones["{bone_name}"]' in f.data_path]
        if fcurves:
            print(f"  ✓ {bone_name}: {len(fcurves)} canales con keyframes")
        else:
            print(f"  ✗ {bone_name}: SIN KEYFRAMES")
    
    # Configurar para reproducción
    bpy.context.scene.frame_start = int(action.frame_range[0])
    bpy.context.scene.frame_end = int(action.frame_range[1])
    bpy.context.scene.frame_current = int(action.frame_range[0])
    
    print("\n" + "="*80)
    print("✅ VERIFICACIÓN COMPLETADA")
    print("="*80)
    print("El archivo Blender se abrió correctamente.")
    print("Puedes reproducir la animación con la barra espaciadora.")
    print("Los brazos deben moverse según la animación del FBX.")
    print("El resto del cuerpo debe mantener la animación original del GLB.")
    
else:
    print("ERROR: No se encontró animación")
    sys.exit(1)
