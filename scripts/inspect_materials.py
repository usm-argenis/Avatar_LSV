import bpy
from pathlib import Path

# Archivo a inspeccionar
archivo = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy\cortesia\Nancy_resultado_cortesia.glb")

print(f"\n{'='*80}")
print(f"INSPECCIONANDO MATERIALES Y TEXTURAS")
print(f"{'='*80}")
print(f"📂 Archivo: {archivo.name}\n")

# Limpiar escena
bpy.ops.wm.read_homefile(use_empty=True)

# Importar GLB
print("📦 Importando archivo...")
bpy.ops.import_scene.gltf(filepath=str(archivo))

# Listar objetos mesh
meshes = [obj for obj in bpy.data.objects if obj.type == 'MESH']
print(f"\n🎨 Objetos Mesh: {len(meshes)}")

for mesh_obj in meshes:
    print(f"\n📦 {mesh_obj.name}")
    
    # Verificar materiales
    if mesh_obj.data.materials:
        print(f"   ✅ Materiales: {len(mesh_obj.data.materials)}")
        for i, mat in enumerate(mesh_obj.data.materials):
            if mat:
                print(f"      [{i}] {mat.name}")
                
                # Verificar nodos del material
                if mat.use_nodes:
                    print(f"         ✅ Usa nodos")
                    nodes = mat.node_tree.nodes
                    print(f"         Nodos: {len(nodes)}")
                    
                    for node in nodes:
                        print(f"            - {node.type}: {node.name}")
                        
                        # Si es un nodo de textura de imagen, verificar la imagen
                        if node.type == 'TEX_IMAGE':
                            if node.image:
                                print(f"              ✅ Imagen: {node.image.name}")
                                print(f"              Tamaño: {node.image.size[0]}x{node.image.size[1]}")
                                print(f"              Packed: {node.image.packed_file is not None}")
                            else:
                                print(f"              ❌ Sin imagen asignada")
                else:
                    print(f"         ❌ No usa nodos")
            else:
                print(f"      [{i}] ❌ Material vacío")
    else:
        print(f"   ❌ Sin materiales")
    
    # Verificar UV maps
    if mesh_obj.data.uv_layers:
        print(f"   ✅ UV Layers: {len(mesh_obj.data.uv_layers)}")
        for uv in mesh_obj.data.uv_layers:
            print(f"      - {uv.name}")
    else:
        print(f"   ❌ Sin UV Layers")

# Listar todas las imágenes en el archivo
print(f"\n🖼️ Imágenes en el archivo: {len(bpy.data.images)}")
for img in bpy.data.images:
    packed = "✅ Packed" if img.packed_file else "❌ No packed"
    print(f"   - {img.name} | {img.size[0]}x{img.size[1]} | {packed}")

print(f"\n{'='*80}\n")
