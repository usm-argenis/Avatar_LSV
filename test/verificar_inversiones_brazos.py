"""
VERIFICACIÓN: Comparar rotaciones FBX vs GLB resultante para detectar inversiones
"""

import bpy
from pathlib import Path
import math

print("="*80)
print("VERIFICACIÓN: Detectar inversiones en rotaciones de brazos")
print("="*80)

fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")
glb_result = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_BRAZOS_FINAL.glb")

# Limpiar
bpy.ops.wm.read_homefile(use_empty=True)

# Importar FBX
print(f"\n📦 Importando FBX...")
bpy.ops.import_scene.fbx(filepath=str(fbx_path))
fbx_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        fbx_armature = obj
        fbx_armature.name = "FBX_Source"
        break

# Importar GLB
print(f"📦 Importando GLB resultante...")
bpy.ops.import_scene.gltf(filepath=str(glb_result))
glb_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE' and obj != fbx_armature:
        glb_armature = obj
        glb_armature.name = "GLB_Result"
        break

# Escalar FBX
SCALE_FACTOR = 0.0123
fbx_armature.scale = (SCALE_FACTOR, SCALE_FACTOR, SCALE_FACTOR)
bpy.context.view_layer.update()

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

# Verificar varios frames
test_frames = [1, 15, 30, 45, 60]

print(f"\n🔍 Analizando rotaciones en frames clave...")

for frame in test_frames:
    if frame > 73:
        continue
        
    bpy.context.scene.frame_set(frame)
    bpy.context.view_layer.update()
    
    print(f"\n{'='*80}")
    print(f"FRAME {frame}")
    print(f"{'='*80}")
    
    for fbx_bone, glb_bone in list(ARM_BONES.items())[:2]:  # Solo LeftShoulder y LeftArm
        if fbx_bone not in fbx_armature.pose.bones or glb_bone not in glb_armature.pose.bones:
            continue
            
        fbx_pb = fbx_armature.pose.bones[fbx_bone]
        glb_pb = glb_armature.pose.bones[glb_bone]
        
        # Obtener rotaciones en espacio local (bone space)
        fbx_rot_local = fbx_pb.rotation_quaternion.copy()
        glb_rot_local = glb_pb.rotation_quaternion.copy()
        
        # Obtener rotaciones en espacio world
        fbx_mat_world = fbx_armature.matrix_world @ fbx_pb.matrix
        glb_mat_world = glb_armature.matrix_world @ glb_pb.matrix
        
        fbx_rot_world = fbx_mat_world.to_quaternion()
        glb_rot_world = glb_mat_world.to_quaternion()
        
        print(f"\n{glb_bone}:")
        print(f"  FBX Local:  w={fbx_rot_local.w:7.3f}, x={fbx_rot_local.x:7.3f}, y={fbx_rot_local.y:7.3f}, z={fbx_rot_local.z:7.3f}")
        print(f"  GLB Local:  w={glb_rot_local.w:7.3f}, x={glb_rot_local.x:7.3f}, y={glb_rot_local.y:7.3f}, z={glb_rot_local.z:7.3f}")
        print(f"  FBX World:  w={fbx_rot_world.w:7.3f}, x={fbx_rot_world.x:7.3f}, y={fbx_rot_world.y:7.3f}, z={fbx_rot_world.z:7.3f}")
        print(f"  GLB World:  w={glb_rot_world.w:7.3f}, x={glb_rot_world.x:7.3f}, y={glb_rot_world.y:7.3f}, z={glb_rot_world.z:7.3f}")
        
        # Calcular diferencia angular en world space
        dot = abs(fbx_rot_world.w*glb_rot_world.w + fbx_rot_world.x*glb_rot_world.x + 
                  fbx_rot_world.y*glb_rot_world.y + fbx_rot_world.z*glb_rot_world.z)
        angle_diff = 2 * math.acos(min(dot, 1.0)) * (180/math.pi)
        
        print(f"  Diferencia angular (world): {angle_diff:.1f}°")
        
        # Verificar si hay inversión (componentes con signos opuestos)
        inversions = []
        for axis in ['w', 'x', 'y', 'z']:
            fbx_val = getattr(fbx_rot_world, axis)
            glb_val = getattr(glb_rot_world, axis)
            if abs(fbx_val) > 0.1 and abs(glb_val) > 0.1:
                if (fbx_val > 0 and glb_val < 0) or (fbx_val < 0 and glb_val > 0):
                    inversions.append(f"{axis}: {fbx_val:+.3f} → {glb_val:+.3f}")
        
        if inversions:
            print(f"  ⚠️ POSIBLES INVERSIONES: {', '.join(inversions)}")
        else:
            print(f"  ✓ Sin inversiones evidentes")

print(f"\n{'='*80}")
print(f"ANÁLISIS DE REST POSES")
print(f"{'='*80}")

# Verificar rest poses (frame 0 sin animación)
bpy.context.scene.frame_set(0)

for fbx_bone, glb_bone in list(ARM_BONES.items())[:4]:  # Brazo izquierdo completo
    if fbx_bone not in fbx_armature.data.bones or glb_bone not in glb_armature.data.bones:
        continue
        
    fbx_bone_obj = fbx_armature.data.bones[fbx_bone]
    glb_bone_obj = glb_armature.data.bones[glb_bone]
    
    # Obtener direcciones de los huesos en rest pose
    fbx_head = fbx_bone_obj.head_local
    fbx_tail = fbx_bone_obj.tail_local
    fbx_dir = (fbx_tail - fbx_head).normalized()
    
    glb_head = glb_bone_obj.head_local
    glb_tail = glb_bone_obj.tail_local
    glb_dir = (glb_tail - glb_head).normalized()
    
    print(f"\n{glb_bone} REST POSE:")
    print(f"  FBX dirección: ({fbx_dir.x:7.3f}, {fbx_dir.y:7.3f}, {fbx_dir.z:7.3f})")
    print(f"  GLB dirección: ({glb_dir.x:7.3f}, {glb_dir.y:7.3f}, {glb_dir.z:7.3f})")
    
    # Calcular ángulo entre direcciones
    dot_prod = fbx_dir.dot(glb_dir)
    angle = math.acos(max(-1, min(1, dot_prod))) * (180/math.pi)
    print(f"  Ángulo entre direcciones: {angle:.1f}°")
    
    if angle > 90:
        print(f"  ⚠️ ADVERTENCIA: Direcciones casi opuestas!")

print(f"\n{'='*80}")
print(f"VERIFICACIÓN COMPLETADA")
print(f"{'='*80}")
