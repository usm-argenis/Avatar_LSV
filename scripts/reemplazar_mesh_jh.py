import bpy
import sys
from pathlib import Path

print("\n" + "="*70)
print("REEMPLAZAR MESH DE JH CON AJUSTE DE ESCALA")
print("="*70)

# Limpiar escena
bpy.ops.wm.read_homefile(use_empty=True)

# Paso 1: Importar JH_resultado_b (tiene animación + armature escalado)
jh_animado_path = r"C:\Users\andre\OneDrive\Documentos\tesis\output\JH_resultado_b.fbx"
print(f"\n✅ Importando JH con animación: {Path(jh_animado_path).name}")
bpy.ops.import_scene.fbx(filepath=jh_animado_path)

# Obtener armature con animación
arm_animado = None
mesh_viejo = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        arm_animado = obj
    elif obj.type == 'MESH':
        mesh_viejo = obj

if not arm_animado:
    print("❌ ERROR: No se encontró armature con animación")
    sys.exit(1)

print(f"  Armature encontrado: {arm_animado.name}")
print(f"  Escala del armature: {arm_animado.scale}")
print(f"  Mesh viejo: {mesh_viejo.name if mesh_viejo else 'None'}")

# Guardar información del armature
escala_armature = arm_animado.scale.copy()
animacion = arm_animado.animation_data.action if arm_animado.animation_data else None

if animacion:
    print(f"  Animación: {animacion.name} ({len(animacion.fcurves)} FCurves)")

# Paso 2: Eliminar el mesh viejo
if mesh_viejo:
    print(f"\n🗑️ Eliminando mesh viejo: {mesh_viejo.name}")
    bpy.data.objects.remove(mesh_viejo, do_unlink=True)

# Paso 3: Importar JH.fbx original (tiene mesh con texturas)
jh_original_path = r"C:\Users\andre\OneDrive\Documentos\tesis\avatars\JH.fbx"
print(f"\n✅ Importando JH original: {Path(jh_original_path).name}")
bpy.ops.import_scene.fbx(filepath=jh_original_path)

# Obtener el nuevo mesh y armature original
arm_original = None
mesh_nuevo = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE' and obj != arm_animado:
        arm_original = obj
    elif obj.type == 'MESH' and obj not in [mesh_viejo]:
        mesh_nuevo = obj

if not mesh_nuevo:
    print("❌ ERROR: No se encontró mesh nuevo")
    sys.exit(1)

print(f"  Mesh nuevo: {mesh_nuevo.name}")
print(f"  Parent del mesh nuevo: {mesh_nuevo.parent.name if mesh_nuevo.parent else 'None'}")
print(f"  Armature original: {arm_original.name if arm_original else 'None'}")

# Paso 4: Reparentar el mesh nuevo al armature animado
print(f"\n🔗 Reparentando mesh nuevo al armature con animación...")

# Deseleccionar todo
bpy.ops.object.select_all(action='DESELECT')

# Primero, eliminar el parent actual
mesh_nuevo.parent = None
mesh_nuevo.matrix_parent_inverse.identity()

# Aplicar la misma escala del armature animado al mesh nuevo
# IMPORTANTE: El mesh debe tener la misma escala que el armature para que coincidan
mesh_nuevo.scale = escala_armature
print(f"  Escala aplicada al mesh: {mesh_nuevo.scale}")

# Ahora reparentar con Armature Deform
mesh_nuevo.parent = arm_animado
mesh_nuevo.parent_type = 'ARMATURE'

# Verificar que tenga el modifier de Armature
tiene_modifier = False
for mod in mesh_nuevo.modifiers:
    if mod.type == 'ARMATURE':
        mod.object = arm_animado
        tiene_modifier = True
        print(f"  ✅ Modifier Armature actualizado")
        break

if not tiene_modifier:
    # Agregar modifier de Armature
    mod = mesh_nuevo.modifiers.new(name="Armature", type='ARMATURE')
    mod.object = arm_animado
    print(f"  ✅ Modifier Armature creado")

# Paso 5: Eliminar el armature original de JH (ya no se necesita)
if arm_original:
    print(f"\n🗑️ Eliminando armature original: {arm_original.name}")
    bpy.data.objects.remove(arm_original, do_unlink=True)

# Paso 6: Limpiar datos huérfanos
print(f"\n🧹 Limpiando datos huérfanos...")

# Primero, asegurar que ningún objeto esté activo
bpy.context.view_layer.objects.active = None

# Limpiar armatures huérfanos
armatures_eliminados = []
for armature_data in list(bpy.data.armatures):
    if armature_data.users == 0:
        nombre = armature_data.name
        bpy.data.armatures.remove(armature_data)
        armatures_eliminados.append(nombre)

if armatures_eliminados:
    print(f"  Armatures eliminados: {', '.join(armatures_eliminados)}")

# Limpiar meshes huérfanos
meshes_eliminados = []
for mesh_data in list(bpy.data.meshes):
    if mesh_data.users == 0:
        nombre = mesh_data.name
        bpy.data.meshes.remove(mesh_data)
        meshes_eliminados.append(nombre)

if meshes_eliminados:
    print(f"  Meshes eliminados: {', '.join(meshes_eliminados)}")

# Paso 7: Verificar resultado
print(f"\n=== VERIFICACIÓN ===")
print(f"Objetos en escena:")
for obj in bpy.data.objects:
    print(f"  - {obj.type}: {obj.name}")
    if obj.type == 'MESH':
        print(f"    Parent: {obj.parent.name if obj.parent else 'None'}")
        print(f"    Escala: {obj.scale}")
        print(f"    Materiales: {len(obj.data.materials)}")
        for i, mat in enumerate(obj.data.materials):
            print(f"      [{i}] {mat.name if mat else 'None'}")

# Paso 8: Configurar frame range
if animacion:
    frame_start = int(animacion.frame_range[0])
    frame_end = int(animacion.frame_range[1])
    bpy.context.scene.frame_start = frame_start
    bpy.context.scene.frame_end = frame_end
    print(f"\nFrame range: {frame_start} - {frame_end}")

# Paso 9: Guardar .blend
blend_path = r"C:\Users\andre\OneDrive\Documentos\tesis\output\JH_resultado_c.blend"
bpy.ops.wm.save_as_mainfile(filepath=blend_path)
print(f"\n✅ Guardado .blend: {Path(blend_path).name}")

# Paso 10: Exportar a FBX
output_path_fbx = r"C:\Users\andre\OneDrive\Documentos\tesis\output\JH_resultado_c.fbx"
print(f"\n📦 Exportando a FBX: {Path(output_path_fbx).name}")

bpy.ops.object.select_all(action='DESELECT')
arm_animado.select_set(True)
mesh_nuevo.select_set(True)
bpy.context.view_layer.objects.active = arm_animado

bpy.ops.export_scene.fbx(
    filepath=output_path_fbx,
    use_selection=True,
    global_scale=1.0,
    apply_unit_scale=True,
    apply_scale_options='FBX_SCALE_NONE',
    use_space_transform=True,
    bake_space_transform=False,
    object_types={'ARMATURE', 'MESH'},
    use_mesh_modifiers=True,
    use_mesh_modifiers_render=True,
    mesh_smooth_type='FACE',
    use_armature_deform_only=False,
    armature_nodetype='NULL',
    add_leaf_bones=False,
    primary_bone_axis='Y',
    secondary_bone_axis='X',
    bake_anim=True,
    bake_anim_use_all_bones=True,
    bake_anim_use_nla_strips=False,
    bake_anim_use_all_actions=False,
    bake_anim_force_startend_keying=True,
    bake_anim_step=1.0,
    bake_anim_simplify_factor=0.0,
    path_mode='AUTO',
    embed_textures=True,
    axis_forward='-Z',
    axis_up='Y'
)

print("\n✅ Exportado exitosamente!")
print("="*70)
