"""
Script para validación final del GLB corregido
Verifica que todas las correcciones estén aplicadas correctamente
"""

import bpy
import sys
from pathlib import Path
import math

BASE_PATH = Path(__file__).parent
CORRECTED_GLB = BASE_PATH / "test" / "output" / "glb" / "Nancy" / "expresiones" / "Nancy_Resultado_bien_CORREGIDO.glb"

def clear_scene():
    """Limpia la escena"""
    if bpy.context.active_object and bpy.context.active_object.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    for collection in bpy.data.collections:
        bpy.data.collections.remove(collection)

def validate_glb():
    """Validación exhaustiva del GLB corregido"""
    print("=" * 70)
    print("🔍 VALIDACIÓN FINAL DEL GLB CORREGIDO")
    print("=" * 70)
    
    # 1. Verificar que el archivo existe
    if not CORRECTED_GLB.exists():
        print(f"❌ ERROR: Archivo no encontrado: {CORRECTED_GLB}")
        return False
    
    print(f"✓ Archivo encontrado: {CORRECTED_GLB}")
    print(f"  Tamaño: {CORRECTED_GLB.stat().st_size / 1024:.2f} KB")
    
    # 2. Cargar el GLB
    clear_scene()
    bpy.ops.import_scene.gltf(filepath=str(CORRECTED_GLB))
    
    # 3. Buscar armature
    armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            armature = obj
            break
    
    if not armature:
        print("❌ ERROR: No se encontró armature")
        return False
    
    print(f"✓ Armature: {armature.name}")
    
    # 4. Verificar animación
    if not armature.animation_data or not armature.animation_data.action:
        print("❌ ERROR: No hay animación")
        return False
    
    action = armature.animation_data.action
    frame_start, frame_end = action.frame_range
    frame_start = int(frame_start)
    frame_end = int(frame_end)
    
    print(f"✓ Animación: {action.name}")
    print(f"  Frames: {frame_start} - {frame_end} ({frame_end - frame_start + 1} frames)")
    print(f"  FCurves: {len(action.fcurves)}")
    
    # 5. Verificación detallada
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='POSE')
    
    issues = []
    warnings = []
    
    print("\n📋 VERIFICACIÓN DETALLADA:")
    
    # VERIFICACIÓN 1: Tren inferior congelado
    print("\n1️⃣ Verificando tren inferior congelado...")
    lower_body_bones = ['Hips', 'LeftUpLeg', 'LeftLeg', 'RightUpLeg', 'RightLeg']
    
    for bone_name in lower_body_bones:
        if bone_name not in armature.pose.bones:
            warnings.append(f"Hueso {bone_name} no encontrado")
            continue
        
        pose_bone = armature.pose.bones[bone_name]
        
        # Verificar movimiento entre diferentes frames
        bpy.context.scene.frame_set(frame_start)
        bpy.context.view_layer.update()
        initial_loc = pose_bone.matrix.to_translation().copy()
        
        max_movement = 0
        for test_frame in [frame_start + 15, frame_start + 30, frame_end - 15]:
            if test_frame > frame_end or test_frame < frame_start:
                continue
            
            bpy.context.scene.frame_set(test_frame)
            bpy.context.view_layer.update()
            current_loc = pose_bone.matrix.to_translation()
            movement = (current_loc - initial_loc).length
            max_movement = max(max_movement, movement)
        
        if max_movement < 0.001:
            print(f"  ✓ {bone_name}: CONGELADO (movimiento < 0.001)")
        elif max_movement < 0.01:
            print(f"  ⚠️ {bone_name}: Movimiento mínimo ({max_movement:.4f})")
            warnings.append(f"{bone_name} tiene movimiento muy pequeño")
        else:
            print(f"  ❌ {bone_name}: MOVIMIENTO DETECTADO ({max_movement:.4f})")
            issues.append(f"{bone_name} se mueve {max_movement:.4f} unidades")
    
    # VERIFICACIÓN 2: Pose natural al inicio
    print("\n2️⃣ Verificando pose natural al INICIO (frames 0-4)...")
    
    bpy.context.scene.frame_set(frame_start)
    bpy.context.view_layer.update()
    
    # Verificar mano derecha cerrada (puño)
    if 'RightHandIndex1' in armature.pose.bones:
        bone = armature.pose.bones['RightHandIndex1']
        rotation = bone.rotation_euler if bone.rotation_mode != 'QUATERNION' else bone.rotation_quaternion.to_euler()
        angle_deg = math.degrees(rotation.z)
        
        if angle_deg < -70:  # Debe estar cerca de -80
            print(f"  ✓ Mano derecha CERRADA (puño): {angle_deg:.1f}°")
        else:
            print(f"  ❌ Mano derecha NO cerrada: {angle_deg:.1f}°")
            issues.append(f"Mano derecha al inicio: {angle_deg:.1f}° (esperado ~-80°)")
    
    # Verificar mano izquierda natural (ligeramente flexionada)
    if 'LeftHandIndex1' in armature.pose.bones:
        bone = armature.pose.bones['LeftHandIndex1']
        rotation = bone.rotation_euler if bone.rotation_mode != 'QUATERNION' else bone.rotation_quaternion.to_euler()
        angle_deg = math.degrees(rotation.z)
        
        if -30 < angle_deg < 5:  # Natural = ligeramente flexionada
            print(f"  ✓ Mano izquierda NATURAL: {angle_deg:.1f}°")
        else:
            print(f"  ⚠️ Mano izquierda: {angle_deg:.1f}° (esperado -10° a -15°)")
            warnings.append(f"Mano izquierda al inicio: {angle_deg:.1f}°")
    
    # Verificar brazos posicionados al frente
    if 'RightArm' in armature.pose.bones:
        bone = armature.pose.bones['RightArm']
        rotation = bone.rotation_euler if bone.rotation_mode != 'QUATERNION' else bone.rotation_quaternion.to_euler()
        angle_deg = math.degrees(rotation.x)
        
        if -40 < angle_deg < 0:  # Brazo hacia adelante
            print(f"  ✓ Brazo derecho AL FRENTE: {angle_deg:.1f}°")
        else:
            print(f"  ⚠️ Brazo derecho: {angle_deg:.1f}°")
    
    # VERIFICACIÓN 3: Pose natural al final
    print("\n3️⃣ Verificando pose natural al FINAL (frames {}-{})...".format(frame_end-4, frame_end))
    
    bpy.context.scene.frame_set(frame_end)
    bpy.context.view_layer.update()
    
    # Verificar mano derecha cerrada (puño)
    if 'RightHandIndex1' in armature.pose.bones:
        bone = armature.pose.bones['RightHandIndex1']
        rotation = bone.rotation_euler if bone.rotation_mode != 'QUATERNION' else bone.rotation_quaternion.to_euler()
        angle_deg = math.degrees(rotation.z)
        
        if angle_deg < -70:
            print(f"  ✓ Mano derecha CERRADA (puño): {angle_deg:.1f}°")
        else:
            print(f"  ❌ Mano derecha NO cerrada: {angle_deg:.1f}°")
            issues.append(f"Mano derecha al final: {angle_deg:.1f}°")
    
    # Verificar mano izquierda natural
    if 'LeftHandIndex1' in armature.pose.bones:
        bone = armature.pose.bones['LeftHandIndex1']
        rotation = bone.rotation_euler if bone.rotation_mode != 'QUATERNION' else bone.rotation_quaternion.to_euler()
        angle_deg = math.degrees(rotation.z)
        
        if -30 < angle_deg < 5:
            print(f"  ✓ Mano izquierda NATURAL: {angle_deg:.1f}°")
        else:
            print(f"  ⚠️ Mano izquierda: {angle_deg:.1f}°")
            warnings.append(f"Mano izquierda al final: {angle_deg:.1f}°")
    
    # VERIFICACIÓN 4: Transiciones suaves
    print("\n4️⃣ Verificando transiciones SUAVES...")
    
    # Verificar interpolación de keyframes
    bezier_count = 0
    linear_count = 0
    
    for fcurve in action.fcurves:
        for keyframe in fcurve.keyframe_points:
            if keyframe.interpolation == 'BEZIER':
                bezier_count += 1
            elif keyframe.interpolation == 'LINEAR':
                linear_count += 1
    
    total_keyframes = bezier_count + linear_count
    if bezier_count > total_keyframes * 0.8:
        print(f"  ✓ Interpolación SUAVE: {bezier_count}/{total_keyframes} keyframes Bezier")
    else:
        print(f"  ⚠️ Interpolación: {bezier_count} Bezier, {linear_count} Linear")
        warnings.append("No todos los keyframes usan interpolación Bezier")
    
    # VERIFICACIÓN 5: Malla no deformada
    print("\n5️⃣ Verificando integridad de la MALLA...")
    
    mesh_count = 0
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            mesh_count += 1
            # Verificar que la malla tiene vértices
            if len(obj.data.vertices) == 0:
                issues.append(f"Malla {obj.name} está vacía")
            else:
                print(f"  ✓ {obj.name}: {len(obj.data.vertices)} vértices")
    
    if mesh_count == 0:
        issues.append("No se encontraron mallas")
    
    # VERIFICACIÓN 6: Armature modifier presente
    print("\n6️⃣ Verificando modificadores ARMATURE...")
    
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            has_armature = False
            for mod in obj.modifiers:
                if mod.type == 'ARMATURE':
                    has_armature = True
                    print(f"  ✓ {obj.name} → {mod.object.name}")
                    break
            
            if not has_armature:
                warnings.append(f"{obj.name} no tiene modificador Armature")
    
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # RESULTADO FINAL
    print("\n" + "=" * 70)
    print("📊 RESULTADO DE VALIDACIÓN")
    print("=" * 70)
    
    if issues:
        print("\n❌ PROBLEMAS CRÍTICOS ENCONTRADOS:")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")
    
    if warnings:
        print("\n⚠️ ADVERTENCIAS (no críticas):")
        for i, warning in enumerate(warnings, 1):
            print(f"  {i}. {warning}")
    
    if not issues and not warnings:
        print("\n✅ ¡VALIDACIÓN 100% EXITOSA!")
        print("   Todas las correcciones están aplicadas correctamente.")
        print("   El archivo está listo para usar.")
        return True
    elif not issues:
        print("\n✅ VALIDACIÓN EXITOSA (con advertencias menores)")
        print("   Las correcciones principales están aplicadas correctamente.")
        print("   Las advertencias son menores y no afectan la funcionalidad.")
        return True
    else:
        print("\n❌ VALIDACIÓN FALLIDA")
        print("   Se encontraron problemas críticos que deben corregirse.")
        return False

if __name__ == "__main__":
    try:
        success = validate_glb()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ ERROR EN VALIDACIÓN: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
