"""
Script para PROBAR la animación directamente en Blender
Abre Blender con el GLB y reproduce la animación
"""
import bpy
import sys
from pathlib import Path

GLB_FILE = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\nancy_yo_real_v3.glb")

print("\n" + "="*70)
print("  PRUEBA DE ANIMACIÓN EN BLENDER")
print("="*70 + "\n")

# Limpiar escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Importar GLB
print(f"Importando: {GLB_FILE}")
bpy.ops.import_scene.gltf(filepath=str(GLB_FILE))

# Encontrar armature
armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        armature = obj
        break

if not armature:
    print("❌ No se encontró armature")
    sys.exit(1)

print(f"✓ Armature: {armature.name}")

# Verificar animation data
if not armature.animation_data:
    print("❌ No tiene animation_data")
    sys.exit(1)

print(f"✓ Tiene animation_data")

# Verificar actions
if not armature.animation_data.action:
    print("⚠️ No hay action activa, buscando actions disponibles...")
    
    if len(bpy.data.actions) == 0:
        print("❌ No hay actions en el archivo")
        sys.exit(1)
    
    print(f"\nActions disponibles: {len(bpy.data.actions)}")
    for action in bpy.data.actions:
        print(f"  - {action.name}: {len(action.fcurves)} FCurves")
    
    # Usar la acción con más FCurves
    best_action = max(bpy.data.actions, key=lambda a: len(a.fcurves))
    armature.animation_data.action = best_action
    print(f"\n✓ Acción activada: {best_action.name}")
else:
    best_action = armature.animation_data.action
    print(f"✓ Action activa: {best_action.name}")

print(f"  FCurves: {len(best_action.fcurves)}")
print(f"  Frame range: {best_action.frame_range[0]:.0f} - {best_action.frame_range[1]:.0f}")

# Analizar FCurves
print("\n" + "="*70)
print("ANÁLISIS DETALLADO DE FCURVES")
print("="*70 + "\n")

bone_animations = {}
for fc in best_action.fcurves:
    if 'pose.bones[' in fc.data_path:
        bone_name = fc.data_path.split('"')[1]
        prop = fc.data_path.split('.')[-1]
        
        if bone_name not in bone_animations:
            bone_animations[bone_name] = {'location': 0, 'rotation_euler': 0, 'rotation_quaternion': 0, 'scale': 0}
        
        bone_animations[bone_name][prop] += 1

# Categorizar
categories = {
    'Brazos Izq': ['LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand'],
    'Brazos Der': ['RightShoulder', 'RightArm', 'RightForeArm', 'RightHand'],
    'Piernas Izq': ['LeftUpLeg', 'LeftLeg', 'LeftFoot'],
    'Piernas Der': ['RightUpLeg', 'RightLeg', 'RightFoot'],
    'Torso': ['Hips', 'Spine', 'Spine1', 'Spine2', 'Neck', 'Head']
}

print("Huesos principales animados:\n")

for cat_name, bones in categories.items():
    print(f"{cat_name}:")
    for bone_name in bones:
        if bone_name in bone_animations:
            anims = bone_animations[bone_name]
            parts = []
            if anims['location'] > 0:
                parts.append(f"loc({anims['location']})")
            if anims['rotation_euler'] > 0:
                parts.append(f"rot_e({anims['rotation_euler']})")
            if anims['rotation_quaternion'] > 0:
                parts.append(f"rot_q({anims['rotation_quaternion']})")
            if anims['scale'] > 0:
                parts.append(f"scale({anims['scale']})")
            
            status = "✅" if any(anims.values()) else "❌"
            print(f"  {status} {bone_name:20s} {' '.join(parts)}")
        else:
            print(f"  ❌ {bone_name:20s} SIN ANIMACIÓN")
    print()

# Configurar timeline
bpy.context.scene.frame_start = int(best_action.frame_range[0])
bpy.context.scene.frame_end = int(best_action.frame_range[1])

# Seleccionar armature
bpy.context.view_layer.objects.active = armature
armature.select_set(True)

# Entrar en modo pose
bpy.ops.object.mode_set(mode='POSE')

# Mover a diferentes frames y verificar pose
print("="*70)
print("VERIFICACIÓN DE POSES EN DIFERENTES FRAMES")
print("="*70 + "\n")

test_frames = [1, 10, 20, 30, 40]
test_bones = ['LeftArm', 'RightArm', 'LeftUpLeg', 'RightUpLeg']

for frame in test_frames:
    if frame <= bpy.context.scene.frame_end:
        bpy.context.scene.frame_set(frame)
        print(f"Frame {frame}:")
        
        for bone_name in test_bones:
            if bone_name in armature.pose.bones:
                bone = armature.pose.bones[bone_name]
                loc = bone.location
                rot = bone.rotation_euler if bone.rotation_mode == 'XYZ' else bone.rotation_quaternion
                
                # Verificar si hay movimiento (no es (0,0,0))
                has_location = abs(loc.x) > 0.001 or abs(loc.y) > 0.001 or abs(loc.z) > 0.001
                has_rotation = (abs(rot[0]) > 0.001 or abs(rot[1]) > 0.001 or abs(rot[2]) > 0.001) if len(rot) >= 3 else False
                
                status = "✅" if (has_location or has_rotation) else "⚠️"
                print(f"  {status} {bone_name:15s} loc:{loc.x:.3f},{loc.y:.3f},{loc.z:.3f}  rot:{rot[0]:.3f},{rot[1]:.3f},{rot[2]:.3f}")
        print()

# Volver a modo objeto
bpy.ops.object.mode_set(mode='OBJECT')

print("="*70)
print("CONCLUSIÓN")
print("="*70 + "\n")

critical_bones_animated = sum(1 for bone in ['LeftArm', 'RightArm', 'LeftForeArm', 'RightForeArm', 'LeftUpLeg', 'RightUpLeg'] if bone in bone_animations)

if critical_bones_animated >= 6:
    print("✅ ANIMACIÓN COMPLETA")
    print(f"   Huesos críticos animados: {critical_bones_animated}/6")
    print(f"   Total huesos animados: {len(bone_animations)}")
    print(f"   Total FCurves: {len(best_action.fcurves)}")
    print("\n🎉 El GLB tiene animación completa de brazos y piernas!")
elif critical_bones_animated >= 3:
    print("⚠️ ANIMACIÓN PARCIAL")
    print(f"   Huesos críticos animados: {critical_bones_animated}/6")
    print("   Faltan algunos huesos importantes")
else:
    print("❌ ANIMACIÓN INCOMPLETA")
    print(f"   Huesos críticos animados: {critical_bones_animated}/6")
    print("   La mayoría de extremidades no están animadas")

print("\n" + "="*70 + "\n")
