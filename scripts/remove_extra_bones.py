import bpy
from pathlib import Path

# Archivo a procesar
archivo = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy\tiempo\Nancy_resultado_ayer.glb")

print(f"\n{'='*80}")
print(f"ELIMINANDO HUESOS EXTRAS")
print(f"{'='*80}")
print(f"📂 Archivo: {archivo.name}\n")

# Limpiar escena
bpy.ops.wm.read_homefile(use_empty=True)

# Importar GLB
print("📦 Importando archivo...")
bpy.ops.import_scene.gltf(filepath=str(archivo))

# Lista de objetos mesh a eliminar (duplicados con .004, etc.)
objetos_a_eliminar = [
    "EyeLeft.004",
    "EyeRight.004",
    "Wolf3D_Head.004",
    "Wolf3D_Teeth.004",
    "Icosphere"
]

print(f"\n🗑️ Eliminando objetos mesh duplicados y extras...")
eliminados = 0

for obj_name in objetos_a_eliminar:
    if obj_name in bpy.data.objects:
        obj = bpy.data.objects[obj_name]
        print(f"   ❌ Eliminando: {obj_name}")
        bpy.data.objects.remove(obj, do_unlink=True)
        eliminados += 1

print(f"✅ Total eliminados: {eliminados} objetos")

# Listar objetos restantes
meshes_restantes = [obj.name for obj in bpy.data.objects if obj.type == 'MESH']
print(f"✅ Objetos mesh restantes: {len(meshes_restantes)}")
for mesh_name in sorted(meshes_restantes):
    print(f"   - {mesh_name}")

# Exportar
print(f"\n💾 Exportando archivo...")
bpy.ops.export_scene.gltf(
    filepath=str(archivo),
    export_format='GLB',
    export_animations=True,
    export_frame_range=True,
    export_force_sampling=True,
    export_def_bones=False,
    export_optimize_animation_size=False
)

file_size = archivo.stat().st_size / (1024*1024)
print(f"✅ Guardado: {archivo.name} ({file_size:.1f} MB)")

print(f"\n{'='*80}")
print(f"✅ COMPLETADO - {eliminados} objetos eliminados")
print(f"{'='*80}\n")
