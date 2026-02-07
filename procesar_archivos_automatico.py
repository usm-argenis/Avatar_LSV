#!/usr/bin/env blender --python
"""
Procesar automáticamente todos los archivos GLB con problemas
"""
import bpy
import sys
from pathlib import Path
import shutil
import time

print(f"\n{'='*80}")
print("PROCESAMIENTO AUTOMÁTICO DE ARCHIVOS CON PROBLEMAS")
print(f"{'='*80}\n")

# Leer lista de archivos
lista_file = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\archivos_con_problema_detectados.txt")
if not lista_file.exists():
    print("❌ No existe archivo de lista. Ejecuta primero detectar_archivos_problema.py")
    sys.exit(1)

archivos = []
with open(lista_file, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            archivos.append(Path(line))

if not archivos:
    print("❌ No hay archivos en la lista")
    sys.exit(1)

print(f"📋 {len(archivos)} archivo(s) a procesar\n")

def procesar_archivo(archivo_glb):
    """Procesar un archivo GLB completo"""
    
    print(f"\n{'='*80}")
    print(f"📝 {archivo_glb.name}")
    print(f"{'='*80}")
    
    inicio = time.time()
    
    try:
        # === PASO 1: CREAR BACKUPS ===
        # Buscar backup FINAL
        backup_final = archivo_glb.with_suffix('.glb.backup_FINAL')
        if backup_final.exists():
            print(f"💾 Restaurando desde: {backup_final.name}")
            shutil.copy2(backup_final, archivo_glb)
        else:
            print(f"⚠️  No existe backup_FINAL, usando archivo actual")
        
        # === PASO 2: LIMPIAR ESCENA ===
        print(f"🧹 [1/5] Limpiando escena...")
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()
        
        # === PASO 3: IMPORTAR GLB ===
        print(f"📂 [2/5] Importando GLB...")
        bpy.ops.import_scene.gltf(filepath=str(archivo_glb))
        
        objetos_importados = list(bpy.data.objects)
        print(f"   ✅ {len(objetos_importados)} objetos importados")
        
        # === PASO 4: ELIMINAR OBJETOS PROBLEMÁTICOS ===
        print(f"🗑️  [3/5] Eliminando objetos problemáticos...")
        
        objetos_a_eliminar = []
        
        for obj in bpy.data.objects:
            # Eliminar RootNode
            if obj.name == "RootNode":
                print(f"   - RootNode")
                objetos_a_eliminar.append(obj)
            
            # Eliminar Icosphere
            elif obj.name == "Icosphere":
                print(f"   - Icosphere")
                objetos_a_eliminar.append(obj)
            
            # Eliminar EMPTYs duplicados
            elif obj.type == 'EMPTY' and '.001' in obj.name:
                print(f"   - {obj.name} (EMPTY duplicado)")
                objetos_a_eliminar.append(obj)
        
        # Reparentar hijos antes de eliminar
        for obj in objetos_a_eliminar:
            if obj.children:
                for child in obj.children:
                    mat_world = child.matrix_world.copy()
                    child.parent = obj.parent
                    child.matrix_world = mat_world
        
        # Eliminar
        bpy.ops.object.select_all(action='DESELECT')
        for obj in objetos_a_eliminar:
            bpy.data.objects.remove(obj, do_unlink=True)
        
        print(f"   ✅ {len(objetos_a_eliminar)} objetos eliminados")
        
        # === PASO 5: CORREGIR ARMATURE ===
        print(f"🔧 [4/5] Corrigiendo transformaciones Armature...")
        
        armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                armature = obj
                break
        
        if armature:
            print(f"   Armature: {armature.name}")
            print(f"   ANTES: Rot={armature.rotation_quaternion[:]} Scale={armature.scale[:]}")
            
            # Aplicar transformaciones
            bpy.context.view_layer.objects.active = armature
            armature.select_set(True)
            bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
            
            print(f"   DESPUÉS: Rot={armature.rotation_quaternion[:]} Scale={armature.scale[:]}")
        else:
            print(f"   ⚠️  No se encontró Armature")
        
        # === PASO 6: EXPORTAR GLB ===
        print(f"📤 [5/5] Exportando GLB...")
        
        # Crear backup del GLB antes de sobrescribir
        backup_pre = archivo_glb.with_suffix('.glb.backup_PRE_AUTO')
        if not backup_pre.exists():  # Solo si no existe ya
            shutil.copy2(archivo_glb, backup_pre)
        
        bpy.ops.export_scene.gltf(
            filepath=str(archivo_glb),
            export_format='GLB',
            export_image_format='AUTO',
            export_texcoords=True,
            export_normals=True,
            export_draco_mesh_compression_enable=False,
            export_materials='EXPORT',
            export_cameras=False,
            use_selection=False,
            use_visible=True,
            use_renderable=True,
            use_active_collection=False,
            export_yup=True,
            export_apply=False,
            export_animations=True,
            export_frame_range=True,
            export_frame_step=1,
            export_force_sampling=True,
            export_nla_strips=False,
            export_def_bones=True,
            export_skins=True,
            export_morph=True,
            export_lights=False
        )
        
        # === PASO 7: ELIMINAR .BLEND SI EXISTE ===
        archivo_blend = archivo_glb.with_suffix('.blend')
        if archivo_blend.exists():
            archivo_blend.unlink()
            print(f"   🗑️  Eliminado: {archivo_blend.name}")
        
        tamaño_kb = archivo_glb.stat().st_size / 1024
        tiempo = time.time() - inicio
        
        print(f"\n   ✅ COMPLETADO: {tamaño_kb:.2f} KB en {tiempo:.1f}s")
        return True
        
    except Exception as e:
        print(f"\n   ❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

# === PROCESAR TODOS ===
inicio_total = time.time()
resultados = {"exitosos": [], "fallidos": []}

for i, archivo in enumerate(archivos, 1):
    print(f"\n[{i}/{len(archivos)}]")
    exito = procesar_archivo(archivo)
    
    if exito:
        resultados["exitosos"].append(archivo.name)
    else:
        resultados["fallidos"].append(archivo.name)

tiempo_total = time.time() - inicio_total

# === RESUMEN ===
print(f"\n{'='*80}")
print(f"📊 RESUMEN FINAL")
print(f"{'='*80}")
print(f"⏱️  Tiempo total: {tiempo_total:.1f}s")
print(f"✅ Exitosos: {len(resultados['exitosos'])}/{len(archivos)}")
print(f"❌ Fallidos: {len(resultados['fallidos'])}/{len(archivos)}")

if resultados["fallidos"]:
    print(f"\n❌ Archivos fallidos:")
    for item in resultados["fallidos"]:
        print(f"   - {item}")

if resultados["exitosos"]:
    print(f"\n✅ Archivos procesados:")
    for item in resultados["exitosos"]:
        print(f"   - {item}")

print(f"\n🎉 PROCESO COMPLETADO")
print(f"{'='*80}\n")

sys.exit(0)
