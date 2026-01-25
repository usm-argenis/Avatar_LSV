import bpy
import sys

# Limpiar escena
bpy.ops.wm.read_factory_settings(use_empty=True)

# Importar FBX de Leonard
fbx_path = r"C:\Users\andre\OneDrive\Documentos\tesis\output\Leonard_resultado_b.fbx"
print(f"📂 Importando: {fbx_path}")
bpy.ops.import_scene.fbx(filepath=fbx_path)

print("\n" + "="*60)
print("🎨 MATERIALES DE LEONARD")
print("="*60)

for mat in bpy.data.materials:
    print(f"\n📌 Material: {mat.name}")
    print(f"   Use nodes: {mat.use_nodes}")
    
    # Diffuse color (legacy)
    if hasattr(mat, 'diffuse_color'):
        r, g, b, a = mat.diffuse_color
        brightness = (r + g + b) / 3
        print(f"   Diffuse: RGB({r:.3f}, {g:.3f}, {b:.3f}) Alpha:{a:.3f}")
        print(f"   Brightness: {brightness:.3f} {'⚠️ OSCURO' if brightness < 0.3 else '✅'}")
    
    # Node-based materials
    if mat.use_nodes and mat.node_tree:
        for node in mat.node_tree.nodes:
            if node.type == 'BSDF_PRINCIPLED':
                base_color = node.inputs['Base Color'].default_value
                r, g, b, a = base_color
                brightness = (r + g + b) / 3
                print(f"   Base Color: RGB({r:.3f}, {g:.3f}, {b:.3f}) Alpha:{a:.3f}")
                print(f"   Brightness: {brightness:.3f} {'⚠️ OSCURO' if brightness < 0.3 else '✅'}")
                
                # Otros parámetros
                metallic = node.inputs['Metallic'].default_value
                roughness = node.inputs['Roughness'].default_value
                print(f"   Metallic: {metallic:.3f}, Roughness: {roughness:.3f}")

print("\n" + "="*60)
print("🧍 MESHES Y SUS MATERIALES")
print("="*60)

for obj in bpy.data.objects:
    if obj.type == 'MESH':
        print(f"\n📦 Mesh: {obj.name}")
        if obj.data.materials:
            for slot in obj.material_slots:
                if slot.material:
                    mat = slot.material
                    print(f"   └─ Material: {mat.name}")
                    
                    # Determinar si es piel/cuerpo
                    name_lower = obj.name.lower()
                    is_body = any(word in name_lower for word in 
                                 ['body', 'skin', 'face', 'head', 'arm', 'hand', 'neck'])
                    tipo = "🧑 PIEL/CUERPO" if is_body else "👔 ROPA/OTROS"
                    print(f"      Tipo: {tipo}")
        else:
            print(f"   └─ ⚠️ Sin materiales")

print("\n" + "="*60)
print("✅ Análisis completado")
print("="*60)
