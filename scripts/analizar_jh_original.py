import bpy
import sys

# Limpiar escena
bpy.ops.wm.read_factory_settings(use_empty=True)

# Importar JH original
fbx_path = r"c:\Users\andre\OneDrive\Documentos\tesis\avatars\JH.fbx"
print(f"\n{'='*70}")
print(f"ANALIZANDO: {fbx_path}")
print(f"{'='*70}\n")

bpy.ops.import_scene.fbx(filepath=fbx_path)

print("=== MESHES ===")
mesh_objects = [obj for obj in bpy.data.objects if obj.type == 'MESH']
print(f"Total meshes: {len(mesh_objects)}\n")

for obj in mesh_objects:
    print(f"📦 {obj.name}")
    print(f"   Data: {obj.data.name}")
    print(f"   Vertices: {len(obj.data.vertices)}")
    print(f"   Visible: {not obj.hide_viewport}")
    
    if obj.data.materials:
        print(f"   Materiales: {len(obj.data.materials)}")
        for mat in obj.data.materials:
            if mat:
                print(f"      - {mat.name}")
    print()

print("\n=== MATERIALES ===")
for mat in bpy.data.materials:
    print(f"🎨 {mat.name}")
    if mat.use_nodes:
        for node in mat.node_tree.nodes:
            if node.type == 'TEX_IMAGE' and node.image:
                print(f"   Textura: {node.image.name}")
    print()
