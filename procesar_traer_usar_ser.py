#!/usr/bin/env python3
"""
Procesar traer, usar y ser con Blender
"""
import bpy
import sys
from pathlib import Path

# Leer lista de archivos
lista_file = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\archivos_procesar_blender.txt")
with open(lista_file, 'r') as f:
    archivos = [line.strip() for line in f if line.strip()]

base_dir = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos")

print(f"\n{'='*80}")
print(f"PROCESANDO {len(archivos)} ARCHIVOS DUVALL")
print(f"{'='*80}\n")

procesados = 0
errores = 0

for nombre in archivos:
    glb_input = base_dir / f"Duvall_resultado_{nombre}.glb"
    glb_output = glb_input
    
    if not glb_input.exists():
        print(f"⚠️  No existe: {glb_input.name}")
        errores += 1
        continue
    
    try:
        # Limpiar escena
        bpy.ops.wm.read_factory_settings(use_empty=True)
        
        # Importar GLB
        bpy.ops.import_scene.gltf(filepath=str(glb_input))
        
        # Buscar Armature
        armature_obj = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE' and obj.name == 'Armature':
                armature_obj = obj
                break
        
        if armature_obj:
            # Asegurarse de que está en modo object
            if bpy.context.mode != 'OBJECT':
                bpy.ops.object.mode_set(mode='OBJECT')
            
            # Seleccionar solo el Armature
            bpy.ops.object.select_all(action='DESELECT')
            armature_obj.select_set(True)
            bpy.context.view_layer.objects.active = armature_obj
            
            # Aplicar las transformaciones
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            
            print(f"✅ Transformaciones aplicadas: {glb_input.name}")
        else:
            print(f"⚠️  No se encontró Armature en: {glb_input.name}")
        
        # Exportar a GLB
        bpy.ops.export_scene.gltf(
            filepath=str(glb_output),
            export_format='GLB',
            use_selection=False,
            export_animations=True,
            export_frame_range=True,
            export_force_sampling=True,
            export_def_bones=False,
            export_optimize_animation_size=False
        )
        
        print(f"   ➜ Exportado: {glb_output.name}")
        procesados += 1
        
    except Exception as e:
        print(f"❌ Error en {glb_input.name}: {str(e)}")
        errores += 1

print(f"\n{'='*80}")
print(f"✅ Procesados: {procesados}")
print(f"❌ Errores: {errores}")
print(f"{'='*80}\n")
