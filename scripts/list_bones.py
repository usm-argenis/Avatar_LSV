import bpy
from pathlib import Path

# Archivo a inspeccionar
archivo = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy\tiempo\Nancy_resultado_ayer.glb")

print(f"\n{'='*80}")
print(f"LISTANDO HUESOS DEL ARCHIVO")
print(f"{'='*80}")
print(f"📂 Archivo: {archivo.name}\n")

# Limpiar escena
bpy.ops.wm.read_homefile(use_empty=True)

# Importar GLB
print("📦 Importando archivo...")
bpy.ops.import_scene.gltf(filepath=str(archivo))

# Buscar armatures
armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
print(f"✅ Armatures encontrados: {len(armatures)}\n")

for armature in armatures:
    print(f"🦴 Armature: {armature.name}")
    print(f"   Total de huesos: {len(armature.data.bones)}\n")
    
    print("   Lista de huesos:")
    for bone in sorted(armature.data.bones, key=lambda b: b.name):
        print(f"   - {bone.name}")
    print()

# Listar también los objetos mesh
meshes = [obj for obj in bpy.data.objects if obj.type == 'MESH']
print(f"\n📦 Objetos Mesh encontrados: {len(meshes)}")
for mesh in meshes:
    print(f"   - {mesh.name}")

print(f"\n{'='*80}\n")
