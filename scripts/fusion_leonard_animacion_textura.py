"""
Script para fusionar:
- Animación de Leonard_resultado_b.fbx (con animación transferida)
- Texturas y materiales de Leonard.fbx (original)

El resultado tendrá:
- La animación completa (92 frames)
- Los materiales originales con referencias a texturas
- Mismo tamaño que Remy
"""

import bpy
import os
from pathlib import Path

# Rutas
base_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis")
leonard_animado = base_path / "output" / "Leonard_resultado_b.fbx"
leonard_original = base_path / "avatars" / "Leonard.fbx"
output_dir = base_path / "deploy-viewer-temp" / "output"
output_fbx = output_dir / "Leonard_resultado_b_con_texturas.fbx"
output_blend = output_dir / "Leonard_resultado_b_con_texturas.blend"

# Crear directorio de salida si no existe
output_dir.mkdir(parents=True, exist_ok=True)

print("\n" + "="*70)
print("🎨 FUSIÓN: Animación + Texturas de Leonard")
print("="*70)

# 1. Limpiar escena
print("\n1️⃣ Limpiando escena...")
bpy.ops.wm.read_factory_settings(use_empty=True)

# 2. Importar Leonard CON ANIMACIÓN
print(f"\n2️⃣ Importando Leonard animado: {leonard_animado.name}")
bpy.ops.import_scene.fbx(filepath=str(leonard_animado))

# Obtener el armature y meshes importados
armature_animado = None
meshes_animados = []

for obj in bpy.context.scene.objects:
    if obj.type == 'ARMATURE':
        armature_animado = obj
        print(f"   ✅ Armature encontrado: {obj.name}")
    elif obj.type == 'MESH':
        meshes_animados.append(obj)
        print(f"   📦 Mesh: {obj.name}")

if not armature_animado:
    print("❌ ERROR: No se encontró armature en Leonard animado")
    raise SystemExit(1)

# Verificar animación
if armature_animado.animation_data and armature_animado.animation_data.action:
    action = armature_animado.animation_data.action
    print(f"   🎬 Animación encontrada: {action.name}")
    print(f"   📊 FCurves: {len(action.fcurves)}")
    print(f"   ⏱️ Frame range: {action.frame_range[0]:.1f} - {action.frame_range[1]:.1f}")
else:
    print("   ⚠️ WARNING: No se encontró animación")

# 3. Guardar referencia a los materiales originales (antes de importar el segundo)
print(f"\n3️⃣ Materiales actuales (del animado):")
materiales_animado = {}
for obj in meshes_animados:
    for slot in obj.material_slots:
        if slot.material:
            mat = slot.material
            print(f"   📌 {obj.name} → {mat.name}")
            print(f"      Color: {mat.diffuse_color[:3]}")
            materiales_animado[mat.name] = mat

# 4. Importar Leonard ORIGINAL (solo para copiar materiales)
print(f"\n4️⃣ Importando Leonard original (para texturas): {leonard_original.name}")

# Marcar objetos actuales
objetos_antes = set(bpy.data.objects)
materiales_antes = set(bpy.data.materials)

bpy.ops.import_scene.fbx(filepath=str(leonard_original))

# Identificar nuevos objetos importados
objetos_nuevos = set(bpy.data.objects) - objetos_antes
materiales_nuevos = set(bpy.data.materials) - materiales_antes

print(f"   ✅ Importados {len(objetos_nuevos)} objetos nuevos")
print(f"   ✅ Importados {len(materiales_nuevos)} materiales nuevos")

# 5. Copiar materiales del original a los meshes animados
print(f"\n5️⃣ Copiando materiales con texturas...")

# Mapeo de materiales: animado → original
mapeo_materiales = {
    'Ch31_body': None,
    'Ch31_hair': None
}

# Encontrar materiales del original
for mat in materiales_nuevos:
    if 'Ch31_body' in mat.name:
        mapeo_materiales['Ch31_body'] = mat
        print(f"   📌 Material body original: {mat.name}")
    elif 'Ch31_hair' in mat.name:
        mapeo_materiales['Ch31_hair'] = mat
        print(f"   📌 Material hair original: {mat.name}")

# Asignar materiales originales a meshes animados
for obj in meshes_animados:
    print(f"\n   🔄 Procesando: {obj.name}")
    for slot in obj.material_slots:
        if slot.material:
            mat_name = slot.material.name
            # Determinar qué material original usar
            if 'body' in mat_name.lower():
                if mapeo_materiales['Ch31_body']:
                    slot.material = mapeo_materiales['Ch31_body']
                    print(f"      ✅ Material asignado: Ch31_body (con texturas)")
            elif 'hair' in mat_name.lower():
                if mapeo_materiales['Ch31_hair']:
                    slot.material = mapeo_materiales['Ch31_hair']
                    print(f"      ✅ Material asignado: Ch31_hair (con texturas)")

# 6. Eliminar objetos del Leonard original (solo necesitamos los materiales)
print(f"\n6️⃣ Limpiando objetos del original (solo conservamos materiales)...")
for obj in objetos_nuevos:
    if obj.type in ['MESH', 'ARMATURE']:
        print(f"   🗑️ Eliminando: {obj.name}")
        bpy.data.objects.remove(obj, do_unlink=True)

# 7. Verificar resultado
print(f"\n7️⃣ Verificación final:")
print(f"   Armature: {armature_animado.name}")
print(f"   Meshes: {len(meshes_animados)}")
for obj in meshes_animados:
    for slot in obj.material_slots:
        if slot.material:
            print(f"   📦 {obj.name} → {slot.material.name}")

# 8. Guardar resultado
print(f"\n8️⃣ Guardando archivos...")

# Guardar .blend
print(f"   💾 Guardando Blender: {output_blend.name}")
bpy.ops.wm.save_as_mainfile(filepath=str(output_blend))

# Exportar FBX
print(f"   📤 Exportando FBX: {output_fbx.name}")
bpy.ops.export_scene.fbx(
    filepath=str(output_fbx),
    use_selection=False,
    use_active_collection=False,
    global_scale=1.0,
    apply_unit_scale=True,
    apply_scale_options='FBX_SCALE_NONE',
    bake_space_transform=False,
    object_types={'ARMATURE', 'MESH'},
    use_mesh_modifiers=True,
    use_mesh_modifiers_render=True,
    mesh_smooth_type='OFF',
    use_subsurf=False,
    use_mesh_edges=False,
    use_tspace=False,
    use_custom_props=False,
    add_leaf_bones=False,
    primary_bone_axis='Y',
    secondary_bone_axis='X',
    armature_nodetype='NULL',
    bake_anim=True,
    bake_anim_use_all_bones=True,
    bake_anim_use_nla_strips=False,
    bake_anim_use_all_actions=False,
    bake_anim_force_startend_keying=True,
    bake_anim_step=1.0,
    bake_anim_simplify_factor=0.0,
    path_mode='COPY',  # IMPORTANTE: Copiar texturas
    embed_textures=True,  # Intentar embeber
    batch_mode='OFF',
    use_batch_own_dir=False,
    use_metadata=True,
    # CRÍTICO: NO usar use_armature_deform_only
    use_armature_deform_only=False
)

print("\n" + "="*70)
print("✅ FUSIÓN COMPLETADA")
print("="*70)
print(f"📁 Archivos generados:")
print(f"   • {output_fbx}")
print(f"   • {output_blend}")
print(f"\n💡 Nota: Las texturas PNG deben estar en la misma carpeta que el FBX")
print(f"   Texturas necesarias:")
print(f"   • Ch31_1001_Diffuse.png")
print(f"   • Ch31_1001_Specular.png")
print(f"   • Ch31_1001_Normal.png")
print(f"   • Ch31_1001_Glossiness.png")
print(f"   • Ch31_1002_Diffuse.png")
print("="*70)
