#!/usr/bin/env python3
"""
Procesar archivos .glb de Duvall/verbos y aplicar transformaciones de Armature
"""
import bpy
import sys
from pathlib import Path

# Archivos a procesar en Duvall/verbos
archivos = [
    "agarrar", "amar", "ayudar", "cansar", "comer", "conocer",
    "decir", "deletrear", "dormir", "estar", "estudiar", "invitar",
    "preguntar", "presentar", "querer", "responder", "saludar",
    "sentir", "trabajar", "ver", "vivir"
]

base_glb = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos")

procesados = 0
errores = 0

print(f"\n{'='*80}")
print("PROCESANDO GLB DUVALL/VERBOS → APLICAR TRANSFORMACIONES → EXPORTAR")
print(f"{'='*80}\n")

for nombre in archivos:
    glb_input = base_glb / f"Duvall_resultado_{nombre}.glb"
    glb_output = base_glb / f"Duvall_resultado_{nombre}.glb"
    
    if not glb_input.exists():
        print(f"⚠️  No existe GLB: {glb_input.name}")
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
            
            # Aplicar las transformaciones (esto convierte los valores actuales en la "identidad")
            # Location, Rotation, Scale
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
