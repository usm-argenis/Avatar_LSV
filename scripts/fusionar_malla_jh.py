import bpy
import sys
from pathlib import Path

print("\n" + "="*70)
print("FUSION: ESQUELETO CON ANIMACION + MALLA CON TEXTURAS")
print("="*70)

# Limpiar escena
bpy.ops.wm.read_homefile(use_empty=True)

# ========== PASO 1: Importar esqueleto con animación ==========
esqueleto_path = r"C:\Users\andre\OneDrive\Documentos\tesis\output\JH_resultado_b.fbx"
print(f"\n✅ PASO 1: Importando esqueleto con animación")
print(f"   Archivo: {Path(esqueleto_path).name}")
bpy.ops.import_scene.fbx(filepath=esqueleto_path)

# Identificar armature y mesh del esqueleto
arm_animado = None
mesh_viejo = None

for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        arm_animado = obj
        print(f"   ✓ Armature encontrado: {obj.name}")
        print(f"     Escala: {obj.scale}")
    elif obj.type == 'MESH':
        mesh_viejo = obj
        print(f"   ✓ Mesh antiguo: {obj.name}")

if not arm_animado:
    print("❌ ERROR: No se encontró armature con animación")
    sys.exit(1)

# Verificar animación
if arm_animado.animation_data and arm_animado.animation_data.action:
    accion = arm_animado.animation_data.action
    print(f"   ✓ Animación: {accion.name}")
    print(f"     FCurves: {len(accion.fcurves)}")
    print(f"     Frames: {int(accion.frame_range[0])} - {int(accion.frame_range[1])}")
    frame_start = int(accion.frame_range[0])
    frame_end = int(accion.frame_range[1])
else:
    print("❌ ERROR: No hay animación en el armature")
    sys.exit(1)

# Guardar escala del armature
escala_armature = arm_animado.scale.copy()

# ========== PASO 2: Eliminar mesh antiguo ==========
if mesh_viejo:
    print(f"\n✅ PASO 2: Eliminando mesh antiguo")
    print(f"   🗑️ {mesh_viejo.name}")
    bpy.data.objects.remove(mesh_viejo, do_unlink=True)
else:
    print(f"\n⚠️ PASO 2: No hay mesh antiguo para eliminar")

# ========== PASO 3: Importar malla con texturas ==========
malla_path = r"C:\Users\andre\OneDrive\Documentos\tesis\deploy-viewer-temp\output\JH_malla1.fbx"
print(f"\n✅ PASO 3: Importando malla con texturas")
print(f"   Archivo: {Path(malla_path).name}")
bpy.ops.import_scene.fbx(filepath=malla_path)

# Identificar la nueva malla y su armature
arm_malla = None
mesh_nuevo = None

for obj in bpy.data.objects:
    if obj.type == 'ARMATURE' and obj != arm_animado:
        arm_malla = obj
        print(f"   ✓ Armature de la malla: {obj.name}")
        print(f"     Escala: {obj.scale}")
    elif obj.type == 'MESH' and obj != mesh_viejo:
        mesh_nuevo = obj
        print(f"   ✓ Mesh nuevo: {obj.name}")
        if obj.data.materials:
            print(f"     Materiales: {len(obj.data.materials)}")
            for i, mat in enumerate(obj.data.materials):
                if mat:
                    print(f"       [{i}] {mat.name}")

if not mesh_nuevo:
    print("❌ ERROR: No se encontró la malla nueva")
    sys.exit(1)

# ========== PASO 4: Ajustar posición y escala del mesh ==========
print(f"\n✅ PASO 4: Ajustando posición y escala del mesh")

# Remover parent actual
mesh_nuevo.parent = None
mesh_nuevo.matrix_parent_inverse.identity()

# Mostrar valores originales
print(f"   📊 Estado original del mesh:")
print(f"      Posición: {mesh_nuevo.location}")
print(f"      Escala: {mesh_nuevo.scale}")
print(f"   📊 Estado del armature:")
print(f"      Posición: {arm_animado.location}")
print(f"      Escala: {escala_armature}")

# AJUSTAR POSICIÓN: El mesh debe estar en la misma posición que el armature
mesh_nuevo.location = arm_animado.location.copy()
print(f"   ✅ Posición del mesh ajustada a: {mesh_nuevo.location}")

# AJUSTAR ESCALA: El mesh debe tener la misma escala que el armature
mesh_nuevo.scale = escala_armature.copy()
print(f"   ✅ Escala del mesh ajustada a: {mesh_nuevo.scale}")

# Reparentar al armature con animación
mesh_nuevo.parent = arm_animado
mesh_nuevo.parent_type = 'ARMATURE'
print(f"   ✓ Mesh reparentado a: {arm_animado.name}")

# Actualizar/crear modifier de Armature
modifier_encontrado = False
for mod in mesh_nuevo.modifiers:
    if mod.type == 'ARMATURE':
        mod.object = arm_animado
        modifier_encontrado = True
        print(f"   ✓ Modifier Armature actualizado")
        break

if not modifier_encontrado:
    mod = mesh_nuevo.modifiers.new(name="Armature", type='ARMATURE')
    mod.object = arm_animado
    print(f"   ✓ Modifier Armature creado")

# ========== PASO 5: Eliminar armature de la malla ==========
if arm_malla:
    print(f"\n✅ PASO 5: Eliminando armature de la malla")
    print(f"   🗑️ {arm_malla.name}")
    bpy.data.objects.remove(arm_malla, do_unlink=True)

# ========== PASO 6: Limpiar datos huérfanos ==========
print(f"\n✅ PASO 6: Limpiando datos huérfanos")

bpy.context.view_layer.objects.active = None

# Limpiar armatures
armatures_eliminados = []
for armature_data in list(bpy.data.armatures):
    if armature_data.users == 0:
        nombre = armature_data.name
        bpy.data.armatures.remove(armature_data)
        armatures_eliminados.append(nombre)

if armatures_eliminados:
    print(f"   🗑️ Armatures: {', '.join(armatures_eliminados)}")

# Limpiar meshes
meshes_eliminados = []
for mesh_data in list(bpy.data.meshes):
    if mesh_data.users == 0:
        nombre = mesh_data.name
        bpy.data.meshes.remove(mesh_data)
        meshes_eliminados.append(nombre)

if meshes_eliminados:
    print(f"   🗑️ Meshes: {', '.join(meshes_eliminados)}")

# ========== PASO 7: Verificación ==========
print(f"\n{'='*70}")
print("VERIFICACIÓN FINAL")
print(f"{'='*70}")

print(f"\n📦 Objetos en la escena:")
for obj in bpy.data.objects:
    print(f"  • {obj.type}: {obj.name}")
    if obj.type == 'MESH':
        print(f"    └─ Parent: {obj.parent.name if obj.parent else 'None'}")
        print(f"    └─ Escala: {obj.scale}")
        print(f"    └─ Materiales: {len(obj.data.materials)}")
        for mat in obj.data.materials:
            if mat:
                print(f"       └─ {mat.name}")
    elif obj.type == 'ARMATURE':
        print(f"    └─ Escala: {obj.scale}")
        if obj.animation_data and obj.animation_data.action:
            print(f"    └─ Animación: {obj.animation_data.action.name}")

# ========== PASO 8: Configurar frame range ==========
print(f"\n✅ PASO 8: Configurando frame range")
bpy.context.scene.frame_start = frame_start
bpy.context.scene.frame_end = frame_end
bpy.context.scene.frame_set(frame_start)
print(f"   Frames: {frame_start} - {frame_end}")

# ========== PASO 9: Guardar .blend ==========
blend_path = r"C:\Users\andre\OneDrive\Documentos\tesis\output\JH_final.blend"
bpy.ops.wm.save_as_mainfile(filepath=blend_path)
print(f"\n✅ PASO 9: Guardado .blend")
print(f"   📁 {Path(blend_path).name}")

# ========== PASO 10: Exportar a FBX ==========
output_path_fbx = r"C:\Users\andre\OneDrive\Documentos\tesis\output\JH_final.fbx"
print(f"\n✅ PASO 10: Exportando a FBX")
print(f"   📁 {Path(output_path_fbx).name}")

# Seleccionar armature y mesh
bpy.ops.object.select_all(action='DESELECT')
arm_animado.select_set(True)
mesh_nuevo.select_set(True)
bpy.context.view_layer.objects.active = arm_animado

# Exportar
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

print(f"\n{'='*70}")
print("✅ PROCESO COMPLETADO EXITOSAMENTE")
print(f"{'='*70}")
print(f"\n📊 Resultado:")
print(f"  • Esqueleto: Con animación de {frame_end - frame_start + 1} frames")
print(f"  • Malla: Con texturas y materiales originales")
print(f"  • Escala: {escala_armature} (consistente en armature y mesh)")
print(f"  • Archivo: JH_final.fbx")
print(f"\n🎯 Listo para usar en el visualizador!")
