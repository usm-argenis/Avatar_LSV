"""
DIAGNÓSTICO PROFUNDO: Analizar exactamente por qué los brazos no se copian correctamente
"""

import bpy
from pathlib import Path
from mathutils import Vector, Matrix
import math

print("="*80)
print("DIAGNÓSTICO PROFUNDO DEL PROBLEMA")
print("="*80)

fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")
glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_abril.glb")

# Limpiar
bpy.ops.wm.read_homefile(use_empty=True)

# Importar FBX
print(f"\n📦 Importando FBX...")
bpy.ops.import_scene.fbx(filepath=str(fbx_path))
fbx_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        fbx_armature = obj
        break

# Importar GLB
print(f"📦 Importando GLB...")
bpy.ops.import_scene.gltf(filepath=str(glb_path))
glb_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE' and obj != fbx_armature:
        glb_armature = obj
        break

# Escalar FBX
SCALE_FACTOR = 0.0123
fbx_armature.scale = (SCALE_FACTOR, SCALE_FACTOR, SCALE_FACTOR)
bpy.context.view_layer.update()

print(f"\n{'='*80}")
print(f"ANÁLISIS 1: REST POSE - Dirección de huesos")
print(f"{'='*80}")

# Analizar rest pose de ambos esqueletos
bones_to_analyze = [
    ('Bip001 L Clavicle', 'LeftShoulder'),
    ('Bip001 L UpperArm', 'LeftArm'),
    ('Bip001 R Clavicle', 'RightShoulder'),
    ('Bip001 R UpperArm', 'RightArm'),
]

for fbx_bone, glb_bone in bones_to_analyze:
    if fbx_bone not in fbx_armature.data.bones or glb_bone not in glb_armature.data.bones:
        continue
    
    fbx_b = fbx_armature.data.bones[fbx_bone]
    glb_b = glb_armature.data.bones[glb_bone]
    
    # Dirección del hueso en rest pose (local)
    fbx_dir = (fbx_b.tail_local - fbx_b.head_local).normalized()
    glb_dir = (glb_b.tail_local - glb_b.head_local).normalized()
    
    # Matriz de rest pose
    fbx_rest = fbx_b.matrix_local
    glb_rest = glb_b.matrix_local
    
    # Eje X, Y, Z del hueso en rest pose
    fbx_x = fbx_rest.to_3x3() @ Vector((1,0,0))
    fbx_y = fbx_rest.to_3x3() @ Vector((0,1,0))
    fbx_z = fbx_rest.to_3x3() @ Vector((0,0,1))
    
    glb_x = glb_rest.to_3x3() @ Vector((1,0,0))
    glb_y = glb_rest.to_3x3() @ Vector((0,1,0))
    glb_z = glb_rest.to_3x3() @ Vector((0,0,1))
    
    print(f"\n{glb_bone} ({fbx_bone}):")
    print(f"  FBX dirección: ({fbx_dir.x:7.3f}, {fbx_dir.y:7.3f}, {fbx_dir.z:7.3f})")
    print(f"  GLB dirección: ({glb_dir.x:7.3f}, {glb_dir.y:7.3f}, {glb_dir.z:7.3f})")
    print(f"  FBX ejes - X:({fbx_x.x:5.2f},{fbx_x.y:5.2f},{fbx_x.z:5.2f}) Y:({fbx_y.x:5.2f},{fbx_y.y:5.2f},{fbx_y.z:5.2f}) Z:({fbx_z.x:5.2f},{fbx_z.y:5.2f},{fbx_z.z:5.2f})")
    print(f"  GLB ejes - X:({glb_x.x:5.2f},{glb_x.y:5.2f},{glb_x.z:5.2f}) Y:({glb_y.x:5.2f},{glb_y.y:5.2f},{glb_y.z:5.2f}) Z:({glb_z.x:5.2f},{glb_z.y:5.2f},{glb_z.z:5.2f})")
    
    # Ángulo entre direcciones
    dot = fbx_dir.dot(glb_dir)
    angle = math.acos(max(-1, min(1, dot))) * (180/math.pi)
    print(f"  Ángulo entre direcciones: {angle:.1f}°")

print(f"\n{'='*80}")
print(f"ANÁLISIS 2: ANIMACIÓN - Frame 30 en POSE MODE")
print(f"{'='*80}")

bpy.context.scene.frame_set(30)
bpy.context.view_layer.update()

for fbx_bone, glb_bone in bones_to_analyze[:2]:  # Solo brazo izquierdo
    if fbx_bone not in fbx_armature.pose.bones or glb_bone not in glb_armature.pose.bones:
        continue
    
    fbx_pb = fbx_armature.pose.bones[fbx_bone]
    glb_pb = glb_armature.pose.bones[glb_bone]
    
    # Rotación en bone space (local)
    fbx_rot_local = fbx_pb.rotation_quaternion
    
    # Matriz world
    fbx_mat_world = fbx_armature.matrix_world @ fbx_pb.matrix
    glb_mat_world = glb_armature.matrix_world @ glb_pb.matrix
    
    # Rotación world
    fbx_rot_world = fbx_mat_world.to_quaternion()
    glb_rot_world = glb_mat_world.to_quaternion()
    
    # Dirección actual del hueso (animado)
    fbx_bone_axis = fbx_mat_world.to_3x3() @ Vector((0,1,0))  # Y es el eje del hueso
    glb_bone_axis = glb_mat_world.to_3x3() @ Vector((0,1,0))
    
    print(f"\n{glb_bone} en frame 30:")
    print(f"  FBX local rot: w={fbx_rot_local.w:7.3f}, x={fbx_rot_local.x:7.3f}, y={fbx_rot_local.y:7.3f}, z={fbx_rot_local.z:7.3f}")
    print(f"  FBX world rot:  w={fbx_rot_world.w:7.3f}, x={fbx_rot_world.x:7.3f}, y={fbx_rot_world.y:7.3f}, z={fbx_rot_world.z:7.3f}")
    print(f"  GLB world rot:  w={glb_rot_world.w:7.3f}, x={glb_rot_world.x:7.3f}, y={glb_rot_world.y:7.3f}, z={glb_rot_world.z:7.3f}")
    print(f"  FBX dirección animada: ({fbx_bone_axis.x:7.3f}, {fbx_bone_axis.y:7.3f}, {fbx_bone_axis.z:7.3f})")
    print(f"  GLB dirección animada: ({glb_bone_axis.x:7.3f}, {glb_bone_axis.y:7.3f}, {glb_bone_axis.z:7.3f})")

print(f"\n{'='*80}")
print(f"ANÁLISIS 3: ROLL DE HUESOS (orientación alrededor del eje)")
print(f"{'='*80}")

for fbx_bone, glb_bone in bones_to_analyze:
    if fbx_bone not in fbx_armature.data.bones or glb_bone not in glb_armature.data.bones:
        continue
    
    fbx_b = fbx_armature.data.bones[fbx_bone]
    glb_b = glb_armature.data.bones[glb_bone]
    
    print(f"\n{glb_bone}:")
    print(f"  FBX roll: {math.degrees(fbx_b.roll):.1f}°")
    print(f"  GLB roll: {math.degrees(glb_b.roll):.1f}°")
    print(f"  Diferencia: {math.degrees(glb_b.roll - fbx_b.roll):.1f}°")

print(f"\n{'='*80}")
print(f"ANÁLISIS 4: POSICIÓN WORLD DE HUESOS")
print(f"{'='*80}")

bpy.context.scene.frame_set(1)
bpy.context.view_layer.update()

for fbx_bone, glb_bone in bones_to_analyze[:2]:
    if fbx_bone not in fbx_armature.pose.bones or glb_bone not in glb_armature.pose.bones:
        continue
    
    fbx_pb = fbx_armature.pose.bones[fbx_bone]
    glb_pb = glb_armature.pose.bones[glb_bone]
    
    fbx_head = fbx_armature.matrix_world @ fbx_pb.head
    glb_head = glb_armature.matrix_world @ glb_pb.head
    
    print(f"\n{glb_bone} en frame 1:")
    print(f"  FBX head world: ({fbx_head.x:7.3f}, {fbx_head.y:7.3f}, {fbx_head.z:7.3f})")
    print(f"  GLB head world: ({glb_head.x:7.3f}, {glb_head.y:7.3f}, {glb_head.z:7.3f})")

print(f"\n{'='*80}")
print(f"ANÁLISIS 5: ORIENTACIÓN DE ARMATURES")
print(f"{'='*80}")

print(f"\nFBX Armature:")
print(f"  Location: ({fbx_armature.location.x:.3f}, {fbx_armature.location.y:.3f}, {fbx_armature.location.z:.3f})")
print(f"  Rotation: ({math.degrees(fbx_armature.rotation_euler.x):.1f}°, {math.degrees(fbx_armature.rotation_euler.y):.1f}°, {math.degrees(fbx_armature.rotation_euler.z):.1f}°)")
print(f"  Scale: ({fbx_armature.scale.x:.4f}, {fbx_armature.scale.y:.4f}, {fbx_armature.scale.z:.4f})")

print(f"\nGLB Armature:")
print(f"  Location: ({glb_armature.location.x:.3f}, {glb_armature.location.y:.3f}, {glb_armature.location.z:.3f})")
print(f"  Rotation: ({math.degrees(glb_armature.rotation_euler.x):.1f}°, {math.degrees(glb_armature.rotation_euler.y):.1f}°, {math.degrees(glb_armature.rotation_euler.z):.1f}°)")
print(f"  Scale: ({glb_armature.scale.x:.4f}, {glb_armature.scale.y:.4f}, {glb_armature.scale.z:.4f})")

print(f"\n{'='*80}")
print(f"DIAGNÓSTICO COMPLETADO")
print(f"{'='*80}")
