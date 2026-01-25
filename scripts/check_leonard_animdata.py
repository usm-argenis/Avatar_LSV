import bpy

# Limpiar
bpy.ops.wm.read_factory_settings(use_empty=True)

# Importar Leonard ORIGINAL
leonard_original = r"C:\Users\andre\OneDrive\Documentos\tesis\avatars\leonard.fbx"
print(f"\n📂 Importando Leonard ORIGINAL: {leonard_original}")
bpy.ops.import_scene.fbx(filepath=leonard_original)

print("\n" + "="*60)
print("🎨 MATERIALES ORIGINALES DE LEONARD")
print("="*60)

for mat in bpy.data.materials:
    print(f"\n📌 Material: {mat.name}")
    if hasattr(mat, 'diffuse_color'):
        r, g, b, a = mat.diffuse_color
        print(f"   Diffuse: RGB({r:.3f}, {g:.3f}, {b:.3f})")
    
    if mat.use_nodes and mat.node_tree:
        for node in mat.node_tree.nodes:
            if node.type == 'BSDF_PRINCIPLED':
                base_color = node.inputs['Base Color'].default_value
                r, g, b, a = base_color
                print(f"   Base Color: RGB({r:.3f}, {g:.3f}, {b:.3f})")
                print(f"   Hex: 0x{int(r*255):02X}{int(g*255):02X}{int(b*255):02X}")

print("\n" + "="*60)
print("🧍 MESHES Y MATERIALES")
print("="*60)

for obj in bpy.data.objects:
    if obj.type == 'MESH':
        print(f"\n📦 {obj.name}")
        for slot in obj.material_slots:
            if slot.material:
                print(f"   └─ {slot.material.name}")
