"""
SOLUCIÓN CORRECTA: Invertir rotaciones SOLO del brazo IZQUIERDO
Basado en el diagnóstico: LeftShoulder tiene 170.8° de diferencia, RightShoulder solo 9.2°
"""

import bpy
from pathlib import Path
from mathutils import Quaternion
import math

print("="*80)
print("SOLUCIÓN: Invertir rotaciones solo del brazo IZQUIERDO")
print("="*80)

fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")
glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_abril.glb")
output_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_BRAZOS_CORREGIDO.glb")

# Limpiar escena
bpy.ops.wm.read_homefile(use_empty=True)

# Importar GLB target
print(f"📦 Importando GLB target...")
bpy.ops.import_scene.gltf(filepath=str(glb_path))
glb_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        glb_armature = obj
        glb_armature.name = "GLB_Target"
        break

# Importar FBX source
print(f"📦 Importando FBX source...")
bpy.ops.import_scene.fbx(filepath=str(fbx_path))
fbx_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE' and obj != glb_armature:
        fbx_armature = obj
        fbx_armature.name = "FBX_Source"
        break

# Escalar FBX
SCALE_FACTOR = 0.0123
print(f"📐 Escalando FBX a {SCALE_FACTOR}...")
fbx_armature.scale = (SCALE_FACTOR, SCALE_FACTOR, SCALE_FACTOR)
bpy.context.view_layer.update()

# Mapeo de huesos
ARM_BONES_MAPPING = {
    'Bip001 L Clavicle': 'LeftShoulder',
    'Bip001 L UpperArm': 'LeftArm',
    'Bip001 L Forearm': 'LeftForeArm',
    'Bip001 L Hand': 'LeftHand',
    'Bip001 R Clavicle': 'RightShoulder',
    'Bip001 R UpperArm': 'RightArm',
    'Bip001 R Forearm': 'RightForeArm',
    'Bip001 R Hand': 'RightHand',
}

# Huesos del brazo IZQUIERDO que necesitan inversión (170.8° de diferencia)
LEFT_ARM_BONES = ['LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand']

# Obtener rango de frames del FBX
fbx_action = fbx_armature.animation_data.action if fbx_armature.animation_data else None
if fbx_action:
    frame_start = int(fbx_action.frame_range[0])
    frame_end = int(fbx_action.frame_range[1])
else:
    frame_start = 1
    frame_end = 73

print(f"\n🎬 Copiando animación con corrección de orientación...")
print(f"  📊 Frames: {frame_start} - {frame_end}")
print(f"  🔄 Brazo IZQUIERDO: Invertir rotación (170.8° de diferencia)")
print(f"  ✓ Brazo DERECHO: Copiar directo (9.2° de diferencia)")

# Asegurar que GLB tiene animation_data
if not glb_armature.animation_data:
    glb_armature.animation_data_create()
if not glb_armature.animation_data.action:
    glb_armature.animation_data.action = bpy.data.actions.new(name="GLB_Animation")

# Procesar cada frame
for frame in range(frame_start, frame_end + 1):
    bpy.context.scene.frame_set(frame)
    bpy.context.view_layer.update()
    
    for fbx_bone_name, glb_bone_name in ARM_BONES_MAPPING.items():
        if fbx_bone_name not in fbx_armature.pose.bones or glb_bone_name not in glb_armature.pose.bones:
            continue
        
        fbx_pb = fbx_armature.pose.bones[fbx_bone_name]
        glb_pb = glb_armature.pose.bones[glb_bone_name]
        
        # Obtener rotación world del FBX
        fbx_mat_world = fbx_armature.matrix_world @ fbx_pb.matrix
        fbx_rot_world = fbx_mat_world.to_quaternion()
        
        # SI es brazo IZQUIERDO, invertir la rotación (rotar 180° en eje Y)
        if glb_bone_name in LEFT_ARM_BONES:
            # Inversión: Rotar 180° alrededor del eje Y (vertical)
            inversion = Quaternion((0, 1, 0), math.pi)
            fbx_rot_corrected = inversion @ fbx_rot_world
        else:
            # Brazo derecho: copiar directo
            fbx_rot_corrected = fbx_rot_world
        
        # Convertir a rotación local para GLB
        if glb_pb.parent:
            glb_parent_mat = glb_armature.matrix_world @ glb_pb.parent.matrix
            glb_rot_local = glb_parent_mat.inverted().to_quaternion() @ fbx_rot_corrected
        else:
            glb_rot_local = glb_armature.matrix_world.inverted().to_quaternion() @ fbx_rot_corrected
        
        # Aplicar al GLB
        glb_pb.rotation_quaternion = glb_rot_local
        
        # Insertar keyframe
        glb_pb.keyframe_insert(data_path="rotation_quaternion", frame=frame)
    
    if frame % 10 == 0:
        print(f"  📍 Frame {frame}/{frame_end}")

# Contar FCurves resultantes
fcurve_count = 0
if glb_armature.animation_data and glb_armature.animation_data.action:
    fcurve_count = len(glb_armature.animation_data.action.fcurves)

print(f"\n📊 Resultado: {fcurve_count} FCurves en GLB")

# ELIMINAR FBX y todos sus objetos asociados antes de exportar
print(f"\n🗑️ Eliminando FBX y objetos asociados...")

# Deseleccionar todo
bpy.ops.object.select_all(action='DESELECT')

# Seleccionar FBX armature y todos los objetos que empiecen con "Bip001"
objects_to_delete = []
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE' and obj.name == "FBX_Source":
        objects_to_delete.append(obj)
    elif obj.name.startswith("Bip001"):
        objects_to_delete.append(obj)
    elif obj.type == 'MESH' and obj.name in ['Eye', 'Gloves', 'Hair', 'Head', 'Icosphere', 'Jacket', 'Pants', 'Shoes', 'Socks']:
        objects_to_delete.append(obj)

for obj in objects_to_delete:
    obj.select_set(True)

# Eliminar objetos seleccionados
bpy.ops.object.delete()

print(f"  ✓ {len(objects_to_delete)} objetos del FBX eliminados")

# Verificar qué queda
armature_count = 0
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        armature_count += 1

if armature_count != 1:
    print(f"  ⚠️ ADVERTENCIA: Hay {armature_count} armatures (debería ser 1)")
else:
    print(f"  ✓ Solo 1 armature (correcto)")

# Exportar GLB
print(f"\n💾 Exportando resultado...")
output_path.parent.mkdir(exist_ok=True, parents=True)

bpy.ops.export_scene.gltf(
    filepath=str(output_path),
    export_format='GLB',
    use_selection=False,
    export_animations=True,
    export_frame_range=True,
    export_frame_step=1,
    export_nla_strips=False,
    export_def_bones=True,
    export_optimize_animation_size=False
)

file_size = output_path.stat().st_size / 1024

print(f"\n{'='*80}")
print(f"✅ PROCESO COMPLETADO")
print(f"{'='*80}")
print(f"📁 Archivo: {output_path.name}")
print(f"📊 Tamaño: {file_size:.1f} KB")
print(f"🎯 Total: {fcurve_count} fcurves")
print(f"🎬 Frames: {frame_start}-{frame_end}")
print(f"✨ Método: Inversión SOLO para brazo izquierdo (170.8° diff)")
print(f"✓ Brazo derecho copiado directo (9.2° diff)")
print(f"🗑️ FBX eliminado antes de exportar")
