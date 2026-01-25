import bpy
from pathlib import Path

print("="*80)
print("COMPARACIÓN VISUAL: Nancy original vs Nancy con animación")
print("="*80)

BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_ORIGINAL = BASE_DIR / "Nancy" / "Nancy.glb"
NANCY_ANIMADA = BASE_DIR / "Nancy" / "saludos" / "Nancy_resultado_hola_FINAL.glb"

print(f"\n📂 Comparando:")
print(f"   Original: {NANCY_ORIGINAL}")
print(f"   Animada:  {NANCY_ANIMADA}")

# Analizar Nancy original
print(f"\n{'='*80}")
print("NANCY ORIGINAL:")
print(f"{'='*80}")
bpy.ops.wm.read_homefile(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(NANCY_ORIGINAL))

original_materials = {}
for obj in bpy.data.objects:
    if obj.type == 'MESH' and obj.data.materials:
        for mat in obj.data.materials:
            if mat and mat.name not in original_materials:
                original_materials[mat.name] = {
                    'nodes': [],
                    'images': []
                }
                
                if mat.use_nodes:
                    for node in mat.node_tree.nodes:
                        original_materials[mat.name]['nodes'].append(node.type)
                        
                        if node.type == 'TEX_IMAGE' and node.image:
                            original_materials[mat.name]['images'].append({
                                'name': node.image.name,
                                'size': node.image.size[:],
                                'pixels': len(node.image.pixels)
                            })

print(f"\n📦 Materiales: {len(original_materials)}")
for mat_name, data in original_materials.items():
    print(f"\n   🎨 {mat_name}:")
    print(f"      Nodos: {len(data['nodes'])}")
    print(f"      Imágenes: {len(data['images'])}")
    for img in data['images']:
        print(f"         📷 {img['name']}: {img['size'][0]}x{img['size'][1]} ({img['pixels']} pixels)")

# Analizar Nancy animada
print(f"\n{'='*80}")
print("NANCY ANIMADA (FINAL):")
print(f"{'='*80}")
bpy.ops.wm.read_homefile(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(NANCY_ANIMADA))

animada_materials = {}
for obj in bpy.data.objects:
    if obj.type == 'MESH' and obj.data.materials:
        for mat in obj.data.materials:
            if mat and mat.name not in animada_materials:
                animada_materials[mat.name] = {
                    'nodes': [],
                    'images': []
                }
                
                if mat.use_nodes:
                    for node in mat.node_tree.nodes:
                        animada_materials[mat.name]['nodes'].append(node.type)
                        
                        if node.type == 'TEX_IMAGE' and node.image:
                            animada_materials[mat.name]['images'].append({
                                'name': node.image.name,
                                'size': node.image.size[:],
                                'pixels': len(node.image.pixels)
                            })

print(f"\n📦 Materiales: {len(animada_materials)}")
for mat_name, data in animada_materials.items():
    print(f"\n   🎨 {mat_name}:")
    print(f"      Nodos: {len(data['nodes'])}")
    print(f"      Imágenes: {len(data['images'])}")
    for img in data['images']:
        print(f"         📷 {img['name']}: {img['size'][0]}x{img['size'][1]} ({img['pixels']} pixels)")

# Comparación
print(f"\n{'='*80}")
print("COMPARACIÓN:")
print(f"{'='*80}")

print(f"\nMateriales originales: {len(original_materials)}")
print(f"Materiales animados:   {len(animada_materials)}")

# Verificar qué materiales faltan o son diferentes
materiales_faltantes = set(original_materials.keys()) - set(animada_materials.keys())
materiales_nuevos = set(animada_materials.keys()) - set(original_materials.keys())

if materiales_faltantes:
    print(f"\n❌ Materiales FALTANTES en animada:")
    for mat in materiales_faltantes:
        print(f"   - {mat}")

if materiales_nuevos:
    print(f"\n⚠️ Materiales NUEVOS en animada (no estaban en original):")
    for mat in materiales_nuevos:
        print(f"   - {mat}")

# Verificar diferencias en materiales comunes
materiales_comunes = set(original_materials.keys()) & set(animada_materials.keys())
print(f"\n📊 Materiales comunes: {len(materiales_comunes)}")

for mat_name in materiales_comunes:
    orig = original_materials[mat_name]
    anim = animada_materials[mat_name]
    
    if len(orig['images']) != len(anim['images']):
        print(f"\n⚠️ {mat_name}:")
        print(f"   Original: {len(orig['images'])} imágenes")
        print(f"   Animada:  {len(anim['images'])} imágenes")

print(f"\n{'='*80}")
print("DIAGNÓSTICO:")
print(f"{'='*80}")

total_imgs_original = sum(len(m['images']) for m in original_materials.values())
total_imgs_animada = sum(len(m['images']) for m in animada_materials.values())

print(f"\nTotal imágenes original: {total_imgs_original}")
print(f"Total imágenes animada:  {total_imgs_animada}")

if total_imgs_original == total_imgs_animada and len(original_materials) == len(animada_materials):
    print(f"\n✅ Los materiales parecen completos")
    print(f"⚠️ PERO puede haber diferencias en los datos de imagen (colores, etc.)")
else:
    print(f"\n❌ HAY DIFERENCIAS en materiales/texturas")
    print(f"   Esto explica por qué no se ve igual")
