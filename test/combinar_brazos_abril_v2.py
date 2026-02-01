"""
Script corregido para combinar animaciones de brazos
- Solo creará un archivo BLEND
- Verificación visual en Blender
"""

import bpy
import os
import sys

# Rutas
fbx_path = r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx"
glb_path = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_abril.glb"
output_blend = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_brazos_combinado_v2.blend"

print("="*80)
print("COMBINACIÓN DE ANIMACIONES - VERSIÓN 2")
print("="*80)

# Limpiar escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# 1. Importar GLB
print("\n1. Importando GLB base...")
bpy.ops.import_scene.gltf(filepath=glb_path)

glb_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        glb_armature = obj
        break

print(f"   ✓ Armature GLB: {glb_armature.name}")
original_action = glb_armature.animation_data.action if glb_armature.animation_data else None
print(f"   ✓ Animación original: {original_action.name if original_action else 'None'}")

# 2. Importar FBX
print("\n2. Importando FBX...")
bpy.ops.import_scene.fbx(filepath=fbx_path)

fbx_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE' and obj != glb_armature:
        fbx_armature = obj
        break

print(f"   ✓ Armature FBX: {fbx_armature.name}")
fbx_action = fbx_armature.animation_data.action if fbx_armature.animation_data else None
print(f"   ✓ Animación FBX: {fbx_action.name if fbx_action else 'None'}")

# 3. Mapeo de huesos
print("\n3. Mapeando huesos de brazos...")
bone_mapping = {
    'Bip001 L Clavicle': 'LeftShoulder',
    'Bip001 L UpperArm': 'LeftArm',
    'Bip001 L Forearm': 'LeftForeArm',
    'Bip001 L Hand': 'LeftHand',
    'Bip001 R Clavicle': 'RightShoulder',
    'Bip001 R UpperArm': 'RightArm',
    'Bip001 R Forearm': 'RightForeArm',
    'Bip001 R Hand': 'RightHand',
}

for fbx_bone, glb_bone in bone_mapping.items():
    print(f"   {fbx_bone} -> {glb_bone}")

# 4. Aplicar animación de brazos DIRECTAMENTE al armature GLB
print("\n4. Aplicando animación de brazos frame por frame...")

# Configurar rango de tiempo
start_frame = 1
end_frame = int(fbx_action.frame_range[1]) if fbx_action else 60
bpy.context.scene.frame_start = start_frame
bpy.context.scene.frame_end = end_frame

print(f"   Frames a procesar: {start_frame} - {end_frame}")

# Seleccionar el armature GLB
bpy.context.view_layer.objects.active = glb_armature
glb_armature.select_set(True)

# Entrar en modo pose
bpy.ops.object.mode_set(mode='POSE')

# Copiar transformaciones frame por frame
frames_procesados = 0
for frame in range(start_frame, end_frame + 1):
    bpy.context.scene.frame_set(frame)
    
    # Para cada mapeo de huesos
    for fbx_bone_name, glb_bone_name in bone_mapping.items():
        if fbx_bone_name in fbx_armature.pose.bones and glb_bone_name in glb_armature.pose.bones:
            fbx_bone = fbx_armature.pose.bones[fbx_bone_name]
            glb_bone = glb_armature.pose.bones[glb_bone_name]
            
            # Copiar transformaciones
            glb_bone.location = fbx_bone.location.copy()
            glb_bone.rotation_quaternion = fbx_bone.rotation_quaternion.copy()
            glb_bone.scale = fbx_bone.scale.copy()
            
            # Insertar keyframes
            glb_bone.keyframe_insert(data_path="location", frame=frame)
            glb_bone.keyframe_insert(data_path="rotation_quaternion", frame=frame)
            glb_bone.keyframe_insert(data_path="scale", frame=frame)
    
    frames_procesados += 1
    if frames_procesados % 10 == 0:
        print(f"   Procesados {frames_procesados}/{end_frame} frames...")

print(f"   ✓ {frames_procesados} frames procesados")

# Volver a modo objeto
bpy.ops.object.mode_set(mode='OBJECT')

# 5. Eliminar el armature del FBX y sus meshes
print("\n5. Limpiando escena...")
objects_to_delete = []
for obj in bpy.data.objects:
    if obj == fbx_armature or (obj.parent == fbx_armature if obj.parent else False):
        objects_to_delete.append(obj)

for obj in objects_to_delete:
    bpy.data.objects.remove(obj, do_unlink=True)
    
print(f"   ✓ Eliminados {len(objects_to_delete)} objetos del FBX")

# 6. Verificar resultado
print("\n6. Verificando resultado...")
print(f"   Objetos en escena: {len(bpy.data.objects)}")
print(f"   Armatures en escena: {len([o for o in bpy.data.objects if o.type == 'ARMATURE'])}")

# Contar keyframes de brazos
if glb_armature.animation_data and glb_armature.animation_data.action:
    action = glb_armature.animation_data.action
    arm_keyframes = 0
    for fcurve in action.fcurves:
        if 'pose.bones' in fcurve.data_path:
            bone_name = fcurve.data_path.split('"')[1]
            if bone_name in bone_mapping.values():
                arm_keyframes += len(fcurve.keyframe_points)
    
    print(f"   ✓ Animación: {action.name}")
    print(f"   ✓ Keyframes de brazos: {arm_keyframes}")

# 7. Guardar
print("\n7. Guardando archivo BLEND...")
os.makedirs(os.path.dirname(output_blend), exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=output_blend)

print("\n" + "="*80)
print("COMPLETADO")
print("="*80)
print(f"Archivo guardado: {output_blend}")
print("\nPara verificar:")
print("1. Abre el archivo .blend en Blender")
print("2. Selecciona el armature")
print("3. Reproduce la animación (barra espaciadora)")
print("4. Los brazos deben moverse diferente al resto del cuerpo")
print("="*80)
