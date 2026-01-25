import bpy
import sys
from pathlib import Path

print("\n" + "="*70)
print("FUSION DE MATERIALES: JH_resultado_b + JH.fbx")
print("="*70)

# Limpiar escena
bpy.ops.wm.read_homefile(use_empty=True)

# PASO 1: Importar JH_resultado_b (tiene animación pero materiales/piel incorrectos)
jh_animado_path = r"C:\Users\andre\OneDrive\Documentos\tesis\output\JH_resultado_b.fbx"
print(f"\n📥 Importando JH con animación: {Path(jh_animado_path).name}")
bpy.ops.import_scene.fbx(filepath=jh_animado_path)

# Encontrar el armature con animación
arm_animado = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        arm_animado = obj
        break

if not arm_animado or not arm_animado.animation_data:
    print("❌ ERROR: No se encontró armature con animación")
    sys.exit(1)

print(f"  ✅ Armature encontrado: {arm_animado.name}")
print(f"  ✅ Animación: {arm_animado.animation_data.action.name}")
print(f"  ✅ Frames: {int(arm_animado.animation_data.action.frame_range[0])} - {int(arm_animado.animation_data.action.frame_range[1])}")
print(f"  ✅ Escala actual: {arm_animado.scale.z:.6f}")

# Guardar datos de animación
accion_original = arm_animado.animation_data.action
frame_start = int(accion_original.frame_range[0])
frame_end = int(accion_original.frame_range[1])

# Guardar escala del armature con animación
escala_animado = arm_animado.scale.z

# PASO 2: Recolectar meshes actuales (para eliminar después)
meshes_viejos = [obj for obj in bpy.data.objects if obj.type == 'MESH' and obj.parent == arm_animado]
print(f"\n📦 Meshes con materiales incorrectos a eliminar: {len(meshes_viejos)}")
for mesh in meshes_viejos:
    print(f"  - {mesh.name}")

# PASO 3: Importar JH.fbx original (tiene los materiales/texturas correctos)
jh_original_path = r"C:\Users\andre\OneDrive\Documentos\tesis\avatars\JH.fbx"
print(f"\n📥 Importando JH original (con materiales correctos): {Path(jh_original_path).name}")
bpy.ops.import_scene.fbx(filepath=jh_original_path)

# Encontrar armature del JH original
arm_original = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE' and obj != arm_animado:
        arm_original = obj
        break

if not arm_original:
    print("❌ ERROR: No se encontró JH original")
    sys.exit(1)

print(f"  ✅ Armature original: {arm_original.name}")
print(f"  ✅ Escala original: {arm_original.scale.z:.6f}")

# PASO 4: Recolectar meshes del JH original (tienen los materiales correctos)
meshes_nuevos = [obj for obj in bpy.data.objects if obj.type == 'MESH' and obj.parent == arm_original]
print(f"\n📦 Meshes con materiales correctos del original: {len(meshes_nuevos)}")
for mesh in meshes_nuevos:
    print(f"  - {mesh.name}")
    if mesh.data.materials:
        print(f"    Materiales: {[mat.name for mat in mesh.data.materials if mat]}")

# PASO 5: Calcular escala necesaria para los meshes nuevos
# Los meshes del original están a escala 1.0, pero necesitamos que estén a la escala del animado
escala_necesaria = escala_animado / arm_original.scale.z if arm_original.scale.z != 0 else escala_animado

print(f"\n📏 Ajustando escala de meshes nuevos:")
print(f"  Escala del armature animado: {escala_animado:.6f}")
print(f"  Escala del armature original: {arm_original.scale.z:.6f}")
print(f"  Escala a aplicar a meshes nuevos: {escala_necesaria:.6f}")

# PASO 6: Reparentar meshes del original al armature con animación
print(f"\n🔗 Reparentando meshes nuevos al armature con animación...")
for mesh in meshes_nuevos:
    # Desvincular del armature original
    mesh.parent = None
    mesh.matrix_parent_inverse.identity()
    
    # Aplicar la escala necesaria al mesh
    mesh.scale = (escala_necesaria, escala_necesaria, escala_necesaria)
    
    # Parentear al armature con animación
    mesh.parent = arm_animado
    mesh.parent_type = 'ARMATURE'
    
    # Agregar modificador Armature si no existe
    tiene_armature_mod = False
    for mod in mesh.modifiers:
        if mod.type == 'ARMATURE':
            mod.object = arm_animado
            tiene_armature_mod = True
            print(f"  ✅ {mesh.name} - Modificador Armature actualizado")
            break
    
    if not tiene_armature_mod:
        mod = mesh.modifiers.new(name="Armature", type='ARMATURE')
        mod.object = arm_animado
        print(f"  ✅ {mesh.name} - Modificador Armature agregado")

# PASO 7: Eliminar meshes viejos (con materiales incorrectos)
print(f"\n🗑️ Eliminando meshes viejos con materiales incorrectos...")
for mesh in meshes_viejos:
    print(f"  - Eliminando: {mesh.name}")
    bpy.data.objects.remove(mesh, do_unlink=True)

# PASO 8: Eliminar armature original (ya no lo necesitamos)
print(f"\n🗑️ Eliminando armature original...")
print(f"  - Eliminando: {arm_original.name}")
bpy.data.objects.remove(arm_original, do_unlink=True)

# PASO 9: Limpiar datos huérfanos
print(f"\n🧹 Limpiando datos huérfanos...")
for armature_data in list(bpy.data.armatures):
    if armature_data.users == 0:
        print(f"  - Limpiando armature data: {armature_data.name}")
        bpy.data.armatures.remove(armature_data)

for mesh_data in list(bpy.data.meshes):
    if mesh_data.users == 0:
        print(f"  - Limpiando mesh data: {mesh_data.name}")
        bpy.data.meshes.remove(mesh_data)

# PASO 10: Verificar resultado
print(f"\n=== VERIFICACIÓN ===")
meshes_finales = [obj for obj in bpy.data.objects if obj.type == 'MESH' and obj.parent == arm_animado]
print(f"Meshes finales vinculados al armature: {len(meshes_finales)}")
for mesh in meshes_finales:
    print(f"  📦 {mesh.name}")
    print(f"     Escala: {mesh.scale.z:.6f}")
    if mesh.data.materials:
        print(f"     Materiales: {[mat.name for mat in mesh.data.materials if mat]}")

print(f"\nAnimación preservada:")
print(f"  Action: {arm_animado.animation_data.action.name}")
print(f"  Frames: {frame_start} - {frame_end}")
print(f"  FCurves: {len(arm_animado.animation_data.action.fcurves)}")

# PASO 11: Guardar .blend
blend_path = r"C:\Users\andre\OneDrive\Documentos\tesis\output\JH_resultado_b_con_materiales.blend"
bpy.ops.wm.save_as_mainfile(filepath=blend_path)
print(f"\n✅ Guardado .blend: {Path(blend_path).name}")

# PASO 12: Configurar frame range
bpy.context.scene.frame_start = frame_start
bpy.context.scene.frame_end = frame_end
bpy.context.scene.frame_set(frame_start)

# PASO 13: Exportar FBX
output_path = r"C:\Users\andre\OneDrive\Documentos\tesis\output\JH_resultado_b_con_materiales.fbx"
print(f"\n📦 Exportando FBX: {Path(output_path).name}")

# Seleccionar todo
bpy.ops.object.select_all(action='DESELECT')
arm_animado.select_set(True)
bpy.context.view_layer.objects.active = arm_animado

for mesh in meshes_finales:
    mesh.select_set(True)

bpy.ops.export_scene.fbx(
    filepath=output_path,
    use_selection=False,
    use_visible=False,
    use_active_collection=False,
    
    # Escala y transformación
    global_scale=1.0,
    apply_unit_scale=True,
    apply_scale_options='FBX_SCALE_NONE',
    use_space_transform=True,
    bake_space_transform=False,
    
    # Tipos de objetos
    object_types={'ARMATURE', 'MESH'},
    use_mesh_modifiers=True,
    use_mesh_modifiers_render=True,
    mesh_smooth_type='FACE',
    
    # Armature
    use_armature_deform_only=False,
    armature_nodetype='NULL',
    add_leaf_bones=False,
    primary_bone_axis='Y',
    secondary_bone_axis='X',
    
    # Animación
    bake_anim=True,
    bake_anim_use_all_bones=True,
    bake_anim_use_nla_strips=False,
    bake_anim_use_all_actions=False,
    bake_anim_force_startend_keying=True,
    bake_anim_step=1.0,
    bake_anim_simplify_factor=0.0,
    
    # Texturas - INTENTAR EMBEBER
    path_mode='COPY',
    embed_textures=True,
    
    axis_forward='-Z',
    axis_up='Y'
)

print("\n✅ EXPORTADO EXITOSAMENTE!")
print("="*70)
print("\n📋 RESUMEN:")
print(f"  - Animación: ✅ Preservada ({frame_start}-{frame_end} frames)")
print(f"  - Materiales: ✅ Del JH original")
print(f"  - Texturas: ✅ Intentadas embeber")
print(f"  - Escala: ✅ Ajustada ({escala_necesaria:.6f})")
print(f"  - Archivo: {Path(output_path).name}")
print("="*70)
