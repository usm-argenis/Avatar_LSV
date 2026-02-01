"""
VERIFICACIÓN FINAL: Comparar posiciones de brazos entre FBX y GLB resultante
"""

import bpy
from pathlib import Path
import math

print("="*80)
print("VERIFICACIÓN: Posiciones de brazos FBX vs GLB Rokoko")
print("="*80)

# === ARCHIVOS ===
fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")
glb_result = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_BRAZOS_ROKOKO.glb")

# Mapeo de huesos
ARM_BONES = {
    'Bip001 L Clavicle': 'LeftShoulder',
    'Bip001 L UpperArm': 'LeftArm',
    'Bip001 L Forearm': 'LeftForeArm',
    'Bip001 L Hand': 'LeftHand',
    'Bip001 R Clavicle': 'RightShoulder',
    'Bip001 R UpperArm': 'RightArm',
    'Bip001 R Forearm': 'RightForeArm',
    'Bip001 R Hand': 'RightHand',
}

# === LIMPIAR ===
print("\n🧹 Limpiando escena...")
bpy.ops.wm.read_homefile(use_empty=True)

# === IMPORTAR FBX ===
print(f"\n📦 Importando FBX...")
bpy.ops.import_scene.fbx(filepath=str(fbx_path))
fbx_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        fbx_armature = obj
        fbx_armature.name = "FBX_Source"
        break

if not fbx_armature:
    raise Exception("❌ No se encontró armature en FBX")

print(f"✓ FBX armature: {fbx_armature.name}")

# === IMPORTAR GLB RESULTADO ===
print(f"\n📦 Importando GLB resultado...")
bpy.ops.import_scene.gltf(filepath=str(glb_result))
glb_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE' and obj != fbx_armature:
        glb_armature = obj
        glb_armature.name = "GLB_Result"
        break

if not glb_armature:
    raise Exception("❌ No se encontró armature en GLB")

print(f"✓ GLB armature: {glb_armature.name}")

# === OBTENER ANIMACIONES ===
fbx_action = fbx_armature.animation_data.action if fbx_armature.animation_data else None
glb_action = glb_armature.animation_data.action if glb_armature.animation_data else None

if not fbx_action:
    raise Exception("❌ FBX sin animación")
if not glb_action:
    raise Exception("❌ GLB sin animación")

fbx_frames = (int(fbx_action.frame_range[0]), int(fbx_action.frame_range[1]))
glb_frames = (int(glb_action.frame_range[0]), int(glb_action.frame_range[1]))

print(f"\n✓ FBX frames: {fbx_frames[0]} - {fbx_frames[1]}")
print(f"✓ GLB frames: {glb_frames[0]} - {glb_frames[1]}")

# === ESCALAR FBX ===
print(f"\n📏 Escalando FBX...")
SCALE_FACTOR = 0.0123
fbx_armature.scale = (SCALE_FACTOR, SCALE_FACTOR, SCALE_FACTOR)
bpy.context.view_layer.update()

# === VERIFICAR FRAMES CLAVE ===
test_frames = [1, 20, 40, 60, 73]
print(f"\n🔍 Verificando frames clave: {test_frames}")
print(f"\n{'='*80}")

total_diff = 0
max_diff = 0
max_diff_info = ""
comparisons = 0

for frame in test_frames:
    if frame > fbx_frames[1] or frame > glb_frames[1]:
        continue
        
    bpy.context.scene.frame_set(frame)
    bpy.context.view_layer.update()
    
    print(f"\n📍 FRAME {frame}:")
    print(f"{'  Hueso':<20} {'Distancia':<12} {'Estado':<10}")
    print(f"  {'-'*42}")
    
    frame_total_diff = 0
    
    for fbx_bone, glb_bone in ARM_BONES.items():
        if fbx_bone not in fbx_armature.pose.bones:
            continue
        if glb_bone not in glb_armature.pose.bones:
            continue
            
        # Posiciones en mundo
        fbx_pos = fbx_armature.matrix_world @ fbx_armature.pose.bones[fbx_bone].matrix @ fbx_armature.pose.bones[fbx_bone].bone.matrix_local.inverted() @ fbx_armature.pose.bones[fbx_bone].bone.head_local
        glb_pos = glb_armature.matrix_world @ glb_armature.pose.bones[glb_bone].matrix @ glb_armature.pose.bones[glb_bone].bone.matrix_local.inverted() @ glb_armature.pose.bones[glb_bone].bone.head_local
        
        diff = (fbx_pos - glb_pos).length
        
        frame_total_diff += diff
        total_diff += diff
        comparisons += 1
        
        if diff > max_diff:
            max_diff = diff
            max_diff_info = f"Frame {frame}, {glb_bone}: {diff:.4f}"
        
        status = "✓ Perfecto" if diff < 0.01 else "✓ Muy bien" if diff < 0.05 else "✓ Bien" if diff < 0.1 else "⚠ Regular" if diff < 0.2 else "✗ Mal"
        
        print(f"  {glb_bone:<20} {diff:>10.4f}m  {status}")
    
    avg_frame = frame_total_diff / len(ARM_BONES)
    print(f"  {'─'*42}")
    print(f"  Promedio frame {frame}: {avg_frame:.4f}m")

# === RESUMEN FINAL ===
print(f"\n{'='*80}")
print(f"RESUMEN FINAL")
print(f"{'='*80}")

avg_total = total_diff / comparisons if comparisons > 0 else 0

print(f"\n📊 Estadísticas:")
print(f"   • Comparaciones realizadas: {comparisons}")
print(f"   • Diferencia promedio total: {avg_total:.4f}m ({avg_total*100:.2f}cm)")
print(f"   • Diferencia máxima: {max_diff:.4f}m ({max_diff*100:.2f}cm)")
print(f"   • Ubicación máxima: {max_diff_info}")

print(f"\n🎯 Evaluación:")
if avg_total < 0.05:
    print(f"   ✅ EXCELENTE - Las posiciones de brazos coinciden casi perfectamente")
    print(f"   El retargeting de Rokoko funcionó correctamente")
elif avg_total < 0.1:
    print(f"   ✓ MUY BIEN - Diferencias mínimas, resultado aceptable")
    print(f"   El retargeting es funcional y visualmente correcto")
elif avg_total < 0.2:
    print(f"   ✓ BIEN - Hay algunas diferencias pero el resultado es usable")
    print(f"   Puede necesitar ajustes menores")
else:
    print(f"   ⚠ REGULAR - Las diferencias son significativas")
    print(f"   Revisar el proceso de retargeting")

print(f"\n{'='*80}")
print(f"VERIFICACIÓN COMPLETADA")
print(f"{'='*80}")

# Análisis de rotaciones
print(f"\n📐 Análisis de rotaciones (muestra):")
bpy.context.scene.frame_set(30)
bpy.context.view_layer.update()

for fbx_bone, glb_bone in list(ARM_BONES.items())[:2]:  # Solo LeftShoulder y LeftArm
    if fbx_bone in fbx_armature.pose.bones and glb_bone in glb_armature.pose.bones:
        fbx_rot = fbx_armature.pose.bones[fbx_bone].rotation_quaternion
        glb_rot = glb_armature.pose.bones[glb_bone].rotation_quaternion
        
        # Calcular diferencia angular
        dot = fbx_rot.w*glb_rot.w + fbx_rot.x*glb_rot.x + fbx_rot.y*glb_rot.y + fbx_rot.z*glb_rot.z
        angle_diff = 2 * math.acos(min(abs(dot), 1.0)) * (180/math.pi)
        
        print(f"\n   {glb_bone}:")
        print(f"      FBX: w={fbx_rot.w:.3f}, x={fbx_rot.x:.3f}, y={fbx_rot.y:.3f}, z={fbx_rot.z:.3f}")
        print(f"      GLB: w={glb_rot.w:.3f}, x={glb_rot.x:.3f}, y={glb_rot.y:.3f}, z={glb_rot.z:.3f}")
        print(f"      Diferencia angular: {angle_diff:.1f}°")
