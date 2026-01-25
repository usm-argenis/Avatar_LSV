"""
ESCANER DE TODOS LOS GLB - Busca cuales tienen shape keys
Ejecutar en Blender
"""

import bpy
import os
from pathlib import Path

DIRECTORIO = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb"

print("\n" + "="*70)
print("ESCANEANDO TODOS LOS GLB EN BUSCA DE SHAPE KEYS")
print("="*70)
print(f"\nDirectorio: {DIRECTORIO}\n")

# Buscar todos los GLB recursivamente (incluyendo subcarpetas)
archivos_glb = list(Path(DIRECTORIO).glob("**/*.glb"))

if not archivos_glb:
    print("ERROR: No se encontraron archivos GLB")
else:
    print(f"Encontrados {len(archivos_glb)} archivos GLB\n")
    
    archivos_con_shapes = []
    archivos_sin_shapes = []
    
    for idx, archivo in enumerate(archivos_glb, 1):
        nombre = archivo.name
        print(f"[{idx}/{len(archivos_glb)}] Analizando: {nombre}...")
        
        # Limpiar escena
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        
        try:
            # Importar
            bpy.ops.import_scene.gltf(filepath=str(archivo), loglevel=50)
            
            # Buscar meshes con shape keys
            meshes_con_shapes = []
            total_shape_keys = 0
            
            for obj in bpy.data.objects:
                if obj.type == 'MESH' and obj.data.shape_keys:
                    num_shapes = len(obj.data.shape_keys.key_blocks)
                    meshes_con_shapes.append((obj.name, num_shapes))
                    total_shape_keys += num_shapes
            
            if meshes_con_shapes:
                print(f"   OK - Tiene {total_shape_keys} shape keys")
                for mesh_name, num in meshes_con_shapes:
                    print(f"      - {mesh_name}: {num} shape keys")
                archivos_con_shapes.append((nombre, total_shape_keys, meshes_con_shapes))
            else:
                print("   SIN shape keys")
                archivos_sin_shapes.append(nombre)
                
        except Exception as e:
            print(f"   ERROR: {e}")
            archivos_sin_shapes.append(nombre)
        
        print()
    
    # RESUMEN FINAL
    print("="*70)
    print("RESUMEN")
    print("="*70)
    
    if archivos_con_shapes:
        print(f"\nARCHIVOS CON SHAPE KEYS ({len(archivos_con_shapes)}):")
        print("-" * 70)
        for nombre, total, meshes in archivos_con_shapes:
            print(f"\n  {nombre}")
            print(f"     Total: {total} shape keys")
            for mesh_name, num in meshes:
                print(f"        {mesh_name}: {num}")
    else:
        print("\nNINGUN ARCHIVO TIENE SHAPE KEYS")
    
    if archivos_sin_shapes:
        print(f"\n\nARCHIVOS SIN SHAPE KEYS ({len(archivos_sin_shapes)}):")
        print("-" * 70)
        for nombre in archivos_sin_shapes:
            print(f"  - {nombre}")
    
    print("\n" + "="*70)
    
    if archivos_con_shapes:
        print("\nUSA UNO DE LOS ARCHIVOS CON SHAPE KEYS")
        print("Edita generar_todas_emociones.py y cambia RUTA_GLB_ORIGINAL")
    else:
        print("\nNINGUN GLB TIENE SHAPE KEYS")
        print("Necesitas exportar desde DeepMotion con Face Animation habilitado")
    
    print("="*70 + "\n")
