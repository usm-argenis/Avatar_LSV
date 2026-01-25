"""
Análisis profundo del archivo .blend original
Verificar por qué la animación no tiene movimiento real
"""

import bpy
import sys
from pathlib import Path

BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output")
BLEND_DIR = BASE_DIR / "blend" / "cortesia"
TEST_BLEND = BLEND_DIR / "Nancy_a la orden.blend"

print("\n" + "="*80)
print("ANÁLISIS PROFUNDO DEL ARCHIVO .BLEND ORIGINAL")
print("="*80)

bpy.ops.wm.open_mainfile(filepath=str(TEST_BLEND))

armature = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE'][0]
print(f"\n✅ Armature: {armature.name}")

# Verificar TODAS las acciones disponibles
actions = list(bpy.data.actions)
print(f"\n📋 TODAS LAS ACCIONES ({len(actions)}):")

for i, action in enumerate(actions):
    frame_start, frame_end = action.frame_range
    print(f"\n{i+1}. {action.name}")
    print(f"   FCurves: {len(action.fcurves)}")
    print(f"   Frames: {frame_start:.0f} - {frame_end:.0f}")
    
    # Contar keyframes totales
    total_keyframes = 0
    for fcurve in action.fcurves:
        total_keyframes += len(fcurve.keyframe_points)
    print(f"   Total keyframes: {total_keyframes}")
    
    # Ver algunos paths
    unique_bones = set()
    for fcurve in action.fcurves:
        if 'pose.bones[' in fcurve.data_path:
            bone_name = fcurve.data_path.split('"')[1]
            unique_bones.add(bone_name)
    
    print(f"   Huesos animados: {len(unique_bones)}")
    if len(unique_bones) > 0:
        print(f"   Ejemplos: {', '.join(list(unique_bones)[:5])}")

# Probar cada acción para ver cuál tiene movimiento REAL
print(f"\n" + "="*80)
print("PROBANDO MOVIMIENTO REAL EN CADA ACCIÓN")
print("="*80)

for i, action in enumerate(actions):
    print(f"\n🔍 Probando acción {i+1}: {action.name}")
    
    # Asignar esta acción
    if not armature.animation_data:
        armature.animation_data_create()
    
    armature.animation_data.action = action
    armature.animation_data.use_nla = False
    
    frame_start, frame_end = action.frame_range
    
    # Verificar movimiento en varios huesos
    test_bones = ['Hips', 'Spine', 'Head', 'LeftArm', 'RightArm', 'LeftHand', 'RightHand']
    has_movement = False
    
    for bone_name in test_bones:
        if bone_name in armature.pose.bones:
            bone = armature.pose.bones[bone_name]
            
            bpy.context.scene.frame_set(int(frame_start))
            bpy.context.view_layer.update()
            pos_start = bone.matrix.translation.copy()
            rot_start = bone.matrix.to_quaternion().copy()
            
            bpy.context.scene.frame_set(int(frame_end))
            bpy.context.view_layer.update()
            pos_end = bone.matrix.translation.copy()
            rot_end = bone.matrix.to_quaternion().copy()
            
            pos_diff = (pos_start - pos_end).length
            rot_diff = abs(rot_start.w - rot_end.w) + abs(rot_start.x - rot_end.x) + \
                      abs(rot_start.y - rot_end.y) + abs(rot_start.z - rot_end.z)
            
            if pos_diff > 0.001 or rot_diff > 0.001:
                print(f"   ✅ {bone_name}: pos={pos_diff:.4f}, rot={rot_diff:.4f}")
                has_movement = True
            else:
                # Ver si tiene keyframes
                keyframe_count = 0
                for fcurve in action.fcurves:
                    if f'pose.bones["{bone_name}"]' in fcurve.data_path:
                        keyframe_count += len(fcurve.keyframe_points)
                
                if keyframe_count > 0:
                    print(f"   ⚠️ {bone_name}: {keyframe_count} keyframes pero SIN movimiento (pos={pos_diff:.6f}, rot={rot_diff:.6f})")
    
    if has_movement:
        print(f"\n   🎉 ESTA ACCIÓN TIENE MOVIMIENTO REAL")
    else:
        print(f"\n   ❌ Esta acción NO tiene movimiento real")

print("\n" + "="*80)
print("ANÁLISIS COMPLETADO")
print("="*80)
