"""
SOLUCIÓN DEFINITIVA: Método manual con constraints correcto
Copiar SOLO las animaciones de brazos del FBX al GLB
"""

import bpy
from pathlib import Path

print("="*80)
print("COMBINACIÓN BRAZOS: Método Manual Definitivo")
print("="*80)

# === ARCHIVOS ===
glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_abril.glb")
fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")
output_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_BRAZOS_FINAL.glb")

# Mapeo de huesos - SOLO BRAZOS
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

print(f"\n📂 Archivos:")
print(f"   GLB: {glb_path.name}")
print(f"   FBX: {fbx_path.name}")

# === PASO 1: LIMPIAR ===
print(f"\n🧹 [1/7] Limpiando...")
bpy.ops.wm.read_homefile(use_empty=True)

# === PASO 2: IMPORTAR GLB ===
print(f"\n📦 [2/7] Importando GLB...")
bpy.ops.import_scene.gltf(filepath=str(glb_path))

glb_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        glb_armature = obj
        glb_armature.name = "DeepMotion_Target"
        break

if not glb_armature:
    raise Exception("❌ No se encontró armature en GLB")

print(f"✓ Target: {glb_armature.name}, {len(glb_armature.data.bones)} huesos")

# Guardar la acción original del GLB
original_glb_action = None
if glb_armature.animation_data and glb_armature.animation_data.action:
    original_glb_action = glb_armature.animation_data.action
    print(f"✓ Animación original: {original_glb_action.name}")

# === PASO 3: IMPORTAR FBX ===
print(f"\n📦 [3/7] Importando FBX...")
bpy.ops.import_scene.fbx(filepath=str(fbx_path))

fbx_armature = None
fbx_meshes = []
for obj in bpy.context.selected_objects:
    if obj.type == 'ARMATURE' and obj != glb_armature:
        fbx_armature = obj
        fbx_armature.name = "QuickMagic_Source"
    elif obj.type == 'MESH':
        fbx_meshes.append(obj)

if not fbx_armature:
    raise Exception("❌ No se encontró armature en FBX")

print(f"✓ Source: {fbx_armature.name}, {len(fbx_armature.data.bones)} huesos")

# Verificar animación FBX
if not fbx_armature.animation_data or not fbx_armature.animation_data.action:
    raise Exception("❌ FBX sin animación")

fbx_action = fbx_armature.animation_data.action
frame_start = int(fbx_action.frame_range[0])
frame_end = int(fbx_action.frame_range[1])
print(f"✓ Animación FBX: frames {frame_start}-{frame_end}")

# === PASO 4: ESCALAR FBX ===
print(f"\n📏 [4/7] Escalando FBX...")
SCALE_FACTOR = 0.0123
fbx_armature.scale = (SCALE_FACTOR, SCALE_FACTOR, SCALE_FACTOR)
for mesh in fbx_meshes:
    mesh.scale = (SCALE_FACTOR, SCALE_FACTOR, SCALE_FACTOR)

bpy.context.view_layer.update()
print(f"✓ FBX escalado por {SCALE_FACTOR}")

# === PASO 5: CREAR CONSTRAINTS ===
print(f"\n⚙️ [5/7] Creando constraints para brazos...")

# Seleccionar GLB
bpy.ops.object.select_all(action='DESELECT')
glb_armature.select_set(True)
bpy.context.view_layer.objects.active = glb_armature

# Crear constraints SOLO para brazos
bpy.ops.object.mode_set(mode='POSE')

constraints_count = 0
for fbx_bone_name, glb_bone_name in ARM_BONES_MAPPING.items():
    if glb_bone_name not in glb_armature.pose.bones:
        print(f"   ⚠ {glb_bone_name} no existe en GLB")
        continue
    
    if fbx_bone_name not in fbx_armature.pose.bones:
        print(f"   ⚠ {fbx_bone_name} no existe en FBX")
        continue
    
    glb_bone = glb_armature.pose.bones[glb_bone_name]
    
    # IMPORTANTE: Limpiar constraints existentes
    for constraint in list(glb_bone.constraints):
        glb_bone.constraints.remove(constraint)
    
    # Crear COPY_ROTATION constraint (SOLO rotación, NO location)
    # Esto evita que los brazos se agachen siguiendo la posición del FBX
    constraint = glb_bone.constraints.new('COPY_ROTATION')
    constraint.target = fbx_armature
    constraint.subtarget = fbx_bone_name
    constraint.target_space = 'WORLD'
    constraint.owner_space = 'WORLD'
    constraint.influence = 1.0
    constraint.mix_mode = 'REPLACE'
    
    constraints_count += 1
    print(f"   ✓ {glb_bone_name} ← {fbx_bone_name}")

bpy.ops.object.mode_set(mode='OBJECT')

print(f"✓ Total constraints: {constraints_count}/8")

if constraints_count != 8:
    raise Exception(f"❌ Se esperaban 8 constraints, se crearon {constraints_count}")

# === PASO 6: BAKE ===
print(f"\n🔥 [6/7] Baking animación...")

# Configurar frame range
bpy.context.scene.frame_start = frame_start
bpy.context.scene.frame_end = frame_end

# Seleccionar GLB
bpy.ops.object.select_all(action='DESELECT')
glb_armature.select_set(True)
bpy.context.view_layer.objects.active = glb_armature

# Ir a modo pose
bpy.ops.object.mode_set(mode='POSE')

# Seleccionar SOLO los 8 huesos de brazos
bpy.ops.pose.select_all(action='DESELECT')
for bone_name in ARM_BONES_MAPPING.values():
    if bone_name in glb_armature.data.bones:
        glb_armature.data.bones[bone_name].select = True
        print(f"   ✓ Seleccionado: {bone_name}")

# BAKE con only_selected=True
print(f"   🔥 Baking frames {frame_start}-{frame_end}...")

bpy.ops.nla.bake(
    frame_start=frame_start,
    frame_end=frame_end,
    step=1,
    only_selected=True,           # CRÍTICO: Solo los brazos
    visual_keying=True,            # Usar transformaciones visuales
    clear_constraints=True,        # Eliminar constraints después
    clear_parents=False,           # Mantener jerarquía
    use_current_action=True,       # Usar acción actual
    clean_curves=False,            # No limpiar curvas
    bake_types={'POSE'}
)

bpy.ops.object.mode_set(mode='OBJECT')

print(f"✓ Bake completado")

# Verificar resultado
if not glb_armature.animation_data or not glb_armature.animation_data.action:
    raise Exception("❌ El target no tiene animación después del bake")

final_action = glb_armature.animation_data.action
print(f"✓ Acción final: {final_action.name}")
print(f"✓ FCurves: {len(final_action.fcurves)}")

# === PASO 7: LIMPIAR Y EXPORTAR ===
print(f"\n🧹 [7/7] Limpiando y exportando...")

# Eliminar FBX
bpy.ops.object.select_all(action='DESELECT')
fbx_armature.select_set(True)
for mesh in fbx_meshes:
    mesh.select_set(True)
bpy.ops.object.delete()

print(f"✓ FBX eliminado")

# Exportar GLB
output_path.parent.mkdir(parents=True, exist_ok=True)
bpy.ops.export_scene.gltf(
    filepath=str(output_path),
    export_format='GLB',
    export_animations=True,
    export_frame_range=True,
    export_frame_step=1,
    export_force_sampling=True
)

print(f"\n{'='*80}")
print(f"✅ PROCESO COMPLETADO")
print(f"{'='*80}")
print(f"\n📁 Archivo: {output_path}")
print(f"📊 Tamaño: {output_path.stat().st_size / 1024:.1f} KB")
print(f"\n🎯 El GLB contiene:")
print(f"   • Animación del cuerpo completo del GLB original")
print(f"   • Animación de BRAZOS del FBX (8 huesos retargeteados)")
print(f"   • Total: {len(final_action.fcurves)} fcurves")
