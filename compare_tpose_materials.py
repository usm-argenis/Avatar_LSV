import bpy
from pathlib import Path

# Rutas
ORIGINAL_GLB = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\Duvall.glb")
TPOSE_GLB = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\Duvall_TPose.glb")

def count_textures(materials):
    """Cuenta texturas en materiales"""
    total = 0
    for mat in materials:
        if mat.use_nodes:
            for node in mat.node_tree.nodes:
                if node.type == 'TEX_IMAGE' and node.image:
                    total += 1
    return total

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

print("="*60)
print("COMPARACIÓN: ORIGINAL vs T-POSE")
print("="*60)

# Cargar ORIGINAL
clear_scene()
bpy.ops.import_scene.gltf(filepath=str(ORIGINAL_GLB))

original_materials = len(bpy.data.materials)
original_textures = count_textures(bpy.data.materials)
original_meshes = len([obj for obj in bpy.data.objects if obj.type == 'MESH'])

print(f"\n📦 ORIGINAL (A-pose):")
print(f"   Meshes: {original_meshes}")
print(f"   Materiales: {original_materials}")
print(f"   Texturas: {original_textures}")

# Mostrar texturas
print("\n   🎨 Texturas originales:")
for mat in bpy.data.materials:
    if mat.use_nodes:
        for node in mat.node_tree.nodes:
            if node.type == 'TEX_IMAGE' and node.image:
                print(f"      - {node.image.name} ({node.image.size[0]}x{node.image.size[1]})")

# Cargar T-POSE
clear_scene()
bpy.ops.import_scene.gltf(filepath=str(TPOSE_GLB))

tpose_materials = len(bpy.data.materials)
tpose_textures = count_textures(bpy.data.materials)
tpose_meshes = len([obj for obj in bpy.data.objects if obj.type == 'MESH'])

print(f"\n📦 T-POSE:")
print(f"   Meshes: {tpose_meshes}")
print(f"   Materiales: {tpose_materials}")
print(f"   Texturas: {tpose_textures}")

# Mostrar texturas
print("\n   🎨 Texturas en T-pose:")
for mat in bpy.data.materials:
    if mat.use_nodes:
        for node in mat.node_tree.nodes:
            if node.type == 'TEX_IMAGE' and node.image:
                print(f"      - {node.image.name} ({node.image.size[0]}x{node.image.size[1]})")

# Verificar pose
armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        armature = obj
        break

if armature:
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='EDIT')
    
    left_arm = armature.data.edit_bones.get('LeftArm')
    if left_arm:
        direction = (left_arm.tail - left_arm.head).normalized()
        print(f"\n   🦴 Pose verificada:")
        print(f"      LeftArm: ({direction.x:.3f}, {direction.y:.3f}, {direction.z:.3f})")
        if abs(direction.x) > 0.9:
            print(f"      ✅ T-pose confirmada")
        else:
            print(f"      ❌ No es T-pose")

print("\n" + "="*60)
print("RESUMEN")
print("="*60)

if tpose_textures == original_textures:
    print(f"✅ TODAS LAS TEXTURAS PRESERVADAS ({tpose_textures}/{original_textures})")
else:
    print(f"⚠️ Texturas diferentes: {tpose_textures} vs {original_textures}")

if tpose_materials == original_materials:
    print(f"✅ TODOS LOS MATERIALES PRESERVADOS ({tpose_materials}/{original_materials})")
else:
    print(f"⚠️ Materiales diferentes: {tpose_materials} vs {original_materials}")
