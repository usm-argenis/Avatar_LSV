#!/usr/bin/env blender --python
"""
Script de Blender para limpiar el archivo agarrar.glb
Elimina los objetos RootNode y Armature extras que causan el problema
"""
import bpy
import sys
from pathlib import Path

# Ruta del archivo
archivo_entrada = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.glb")

print(f"\n{'='*80}")
print("LIMPIEZA DE AGARRAR.GLB EN BLENDER")
print(f"{'='*80}\n")

# Crear backup antes de empezar
backup = archivo_entrada.with_suffix('.glb.backup_BLENDER')
import shutil
shutil.copy2(archivo_entrada, backup)
print(f"💾 Backup creado: {backup.name}\n")

# Limpiar escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Importar GLB
print(f"📂 Importando: {archivo_entrada.name}")
bpy.ops.import_scene.gltf(filepath=str(archivo_entrada))

print(f"\n🔍 Objetos en la escena:")
for obj in bpy.data.objects:
    obj_type = obj.type
    parent_info = f" (parent: {obj.parent.name})" if obj.parent else " (root)"
    print(f"  - {obj.name} [{obj_type}]{parent_info}")

# Buscar y eliminar objetos problemáticos
objetos_a_eliminar = []

for obj in bpy.data.objects:
    # Eliminar RootNode si existe
    if obj.name == "RootNode":
        print(f"\n🗑️  Marcando para eliminar: {obj.name}")
        objetos_a_eliminar.append(obj)
    
    # Eliminar Icosphere (objeto que no debería estar)
    if obj.name == "Icosphere":
        print(f"🗑️  Marcando para eliminar: {obj.name} (objeto extra)")
        objetos_a_eliminar.append(obj)
    
    # Eliminar EMPTYs duplicados (.001)
    if obj.type == 'EMPTY' and '.001' in obj.name:
        print(f"🗑️  Marcando para eliminar: {obj.name} (EMPTY duplicado)")
        objetos_a_eliminar.append(obj)

# Eliminar objetos marcados
if objetos_a_eliminar:
    print(f"\n🗑️  Eliminando {len(objetos_a_eliminar)} objeto(s)...")
    
    # Primero, reparentar los hijos al padre del objeto a eliminar (o a None)
    for obj in objetos_a_eliminar:
        if obj.children:
            print(f"    Reparentando {len(obj.children)} hijo(s) de {obj.name}")
            for child in obj.children:
                # Guardar la transformación mundial
                mat_world = child.matrix_world.copy()
                # Quitar el parent
                child.parent = obj.parent
                # Restaurar la transformación mundial
                child.matrix_world = mat_world
    
    # Ahora eliminar los objetos
    bpy.ops.object.select_all(action='DESELECT')
    for obj in objetos_a_eliminar:
        obj.select_set(True)
    bpy.ops.object.delete()
    print(f"✅ Objetos eliminados")
else:
    print(f"\n⚠️  No se encontraron objetos problemáticos para eliminar")

print(f"\n🔍 Objetos restantes:")
for obj in bpy.data.objects:
    obj_type = obj.type
    parent_info = f" (parent: {obj.parent.name})" if obj.parent else " (root)"
    print(f"  - {obj.name} [{obj_type}]{parent_info}")

# Guardar como .blend
archivo_blend = archivo_entrada.with_suffix('.blend')
print(f"\n💾 Guardando como: {archivo_blend.name}")
bpy.ops.wm.save_as_mainfile(filepath=str(archivo_blend))

print(f"\n✅ ARCHIVO LIMPIADO Y GUARDADO COMO .BLEND")
print(f"\n{'='*80}\n")

# Salir de Blender
sys.exit(0)
