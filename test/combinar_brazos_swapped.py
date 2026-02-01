"""
SOLUCIÓN: Intercambiar brazos izquierdo/derecho en el mapeo
"""

import bpy
from pathlib import Path

print("="*80)
print("SOLUCIÓN: Brazos con mapeo Left <-> Right intercambiado")
print("="*80)

fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")
glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_abril.glb")
output_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_BRAZOS_SWAPPED.glb")

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

# Mapeo de huesos INTERCAMBIADO (Left del FBX va a Right del GLB y viceversa)
ARM_BONES_MAPPING = {
    'Bip001 L Clavicle': 'RightShoulder',     # Intercambiado
    'Bip001 L UpperArm': 'RightArm',          # Intercambiado
    'Bip001 L Forearm': 'RightForeArm',       # Intercambiado
    'Bip001 L Hand': 'RightHand',             # Intercambiado
    'Bip001 R Clavicle': 'LeftShoulder',      # Intercambiado
    'Bip001 R UpperArm': 'LeftArm',           # Intercambiado
    'Bip001 R Forearm': 'LeftForeArm',        # Intercambiado
    'Bip001 R Hand': 'LeftHand',              # Intercambiado
}

print(f"\n🔗 Creando constraints COPY_ROTATION con mapeo INTERCAMBIADO...")

# Crear constraints
constraint_count = 0
for fbx_bone_name, glb_bone_name in ARM_BONES_MAPPING.items():
    if fbx_bone_name not in fbx_armature.pose.bones:
        print(f"  ⚠️ Hueso FBX no encontrado: {fbx_bone_name}")
        continue
    
    if glb_bone_name not in glb_armature.pose.bones:
        print(f"  ⚠️ Hueso GLB no encontrado: {glb_bone_name}")
        continue
    
    glb_bone = glb_armature.pose.bones[glb_bone_name]
    
    # Limpiar constraints existentes
    for c in glb_bone.constraints:
        glb_bone.constraints.remove(c)
    
    # Crear constraint COPY_ROTATION
    constraint = glb_bone.constraints.new('COPY_ROTATION')
    constraint.target = fbx_armature
    constraint.subtarget = fbx_bone_name
    constraint.target_space = 'WORLD'
    constraint.owner_space = 'WORLD'
    constraint.influence = 1.0
    constraint.mix_mode = 'REPLACE'
    
    constraint_count += 1
    print(f"  ✓ {fbx_bone_name} → {glb_bone_name}")

print(f"  ✓ {constraint_count} constraints creados")

# Obtener rango de frames del FBX
fbx_action = fbx_armature.animation_data.action if fbx_armature.animation_data else None
if fbx_action:
    frame_start = int(fbx_action.frame_range[0])
    frame_end = int(fbx_action.frame_range[1])
else:
    frame_start = 1
    frame_end = 73

print(f"\n🎬 Preparando para bake (frames {frame_start}-{frame_end})...")

# Configurar escena
bpy.context.scene.frame_start = frame_start
bpy.context.scene.frame_end = frame_end

# Seleccionar solo los huesos de brazos en GLB
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='DESELECT')
glb_armature.select_set(True)
bpy.context.view_layer.objects.active = glb_armature

bpy.ops.object.mode_set(mode='POSE')
bpy.ops.pose.select_all(action='DESELECT')

# Seleccionar solo los 8 huesos de brazos
selected_bones = []
for glb_bone_name in ARM_BONES_MAPPING.values():
    if glb_bone_name in glb_armature.pose.bones:
        bone = glb_armature.pose.bones[glb_bone_name]
        bone.bone.select = True
        selected_bones.append(glb_bone_name)

print(f"  📍 {len(selected_bones)} huesos seleccionados para bake")

# BAKE con visual keying
print(f"\n🔥 Baking animación...")
bpy.ops.nla.bake(
    frame_start=frame_start,
    frame_end=frame_end,
    only_selected=True,
    visual_keying=True,
    clear_constraints=True,
    clear_parents=False,
    use_current_action=True,
    bake_types={'POSE'}
)

print(f"  ✓ Bake completado")

# Volver a object mode
bpy.ops.object.mode_set(mode='OBJECT')

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
print(f"✨ Método: COPY_ROTATION con mapeo Left↔Right INTERCAMBIADO")
print(f"🗑️ FBX eliminado antes de exportar")
