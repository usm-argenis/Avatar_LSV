import bpy
from pathlib import Path

# Ruta del FBX
FBX_PATH = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\Duvall_TPose.fbx")

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

print("="*60)
print("VERIFICACIÓN DE MATERIALES Y TEXTURAS EN FBX")
print("="*60)

clear_scene()
bpy.ops.import_scene.fbx(filepath=str(FBX_PATH))

print(f"\n📦 Archivo: {FBX_PATH.name}")
print("\n" + "="*60)
print("MATERIALES Y TEXTURAS")
print("="*60)

total_materials = 0
total_textures = 0
materials_with_textures = 0

for obj in bpy.data.objects:
    if obj.type == 'MESH':
        print(f"\n🔷 Mesh: {obj.name}")
        print(f"   Materiales: {len(obj.data.materials)}")
        
        for mat_slot in obj.data.materials:
            if mat_slot:
                total_materials += 1
                print(f"\n   📝 Material: {mat_slot.name}")
                
                # Verificar si tiene nodos (Principled BSDF)
                if mat_slot.use_nodes:
                    has_texture = False
                    for node in mat_slot.node_tree.nodes:
                        if node.type == 'TEX_IMAGE':
                            total_textures += 1
                            has_texture = True
                            if node.image:
                                print(f"      ✅ Textura: {node.image.name}")
                                print(f"         Ruta: {node.image.filepath}")
                                print(f"         Tamaño: {node.image.size[0]}x{node.image.size[1]}")
                            else:
                                print(f"      ⚠️ Nodo de textura sin imagen")
                        elif node.type == 'BSDF_PRINCIPLED':
                            # Verificar si tiene color base
                            base_color = node.inputs['Base Color'].default_value
                            print(f"      🎨 Color Base: RGB({base_color[0]:.2f}, {base_color[1]:.2f}, {base_color[2]:.2f})")
                    
                    if has_texture:
                        materials_with_textures += 1
                else:
                    print(f"      ⚠️ Material sin nodos (no usa Shader Editor)")

print("\n" + "="*60)
print("RESUMEN")
print("="*60)
print(f"Total de materiales: {total_materials}")
print(f"Materiales con texturas: {materials_with_textures}")
print(f"Total de texturas: {total_textures}")

if total_textures > 0:
    print("\n✅ FBX tiene texturas correctamente")
else:
    print("\n⚠️ FBX no tiene texturas embebidas")
    print("\nPosible solución:")
    print("1. Exportar con path_mode='COPY' y embed_textures=True")
    print("2. O exportar con path_mode='AUTO' para referencias externas")
