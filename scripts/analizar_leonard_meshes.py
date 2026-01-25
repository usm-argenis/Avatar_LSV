import bpy
import sys

# Limpiar escena
bpy.ops.wm.read_factory_settings(use_empty=True)

# Importar FBX
fbx_path = r"c:\Users\andre\OneDrive\Documentos\tesis\output\Leonard_resultado_b.fbx"
bpy.ops.import_scene.fbx(filepath=fbx_path)

print("\n" + "="*60)
print("ANÁLISIS EXHAUSTIVO DE LEONARD_RESULTADO_B.FBX")
print("="*60)

print("\n=== OBJETOS MESH ===")
mesh_objects = [obj for obj in bpy.data.objects if obj.type == 'MESH']
for obj in mesh_objects:
    print(f"\n📦 Objeto: {obj.name}")
    print(f"   - Data name: {obj.data.name}")
    print(f"   - Visible: {not obj.hide_viewport}")
    
    # Materiales del objeto
    if obj.data.materials:
        print(f"   - Materiales ({len(obj.data.materials)}):")
        for i, mat in enumerate(obj.data.materials):
            if mat:
                print(f"      [{i}] {mat.name}")
            else:
                print(f"      [{i}] None")
    else:
        print(f"   - Sin materiales")

print("\n=== TODOS LOS MATERIALES EN EL ARCHIVO ===")
for mat in bpy.data.materials:
    print(f"\n🎨 Material: {mat.name}")
    if mat.use_nodes:
        print(f"   - Usa nodos: Sí")
        for node in mat.node_tree.nodes:
            print(f"      - Nodo: {node.type} ({node.name})")
    else:
        print(f"   - Usa nodos: No")
        print(f"   - Color difuso: {mat.diffuse_color[:3]}")

print("\n=== ARMATURE ===")
armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
for arm in armatures:
    print(f"🦴 Armature: {arm.name}")
    print(f"   - Escala: {arm.scale}")
    print(f"   - Huesos: {len(arm.data.bones)}")

print("\n" + "="*60)
print("ANÁLISIS COMPLETADO")
print("="*60)
