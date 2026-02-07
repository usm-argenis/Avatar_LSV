#!/usr/bin/env python3
"""
Procesar Duvall_resultado_vestir.glb con Blender
"""
import bpy
import sys
from pathlib import Path

glb_input = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_vestir.glb")
glb_output = glb_input

if not glb_input.exists():
    print(f"❌ No existe: {glb_input}")
    sys.exit(1)

print(f"\n{'='*80}")
print(f"PROCESANDO: {glb_input.name}")
print(f"{'='*80}\n")

# Limpiar escena
bpy.ops.wm.read_factory_settings(use_empty=True)

# Importar GLB
print("Importando GLB...")
bpy.ops.import_scene.gltf(filepath=str(glb_input))

# Buscar Armature
armature_obj = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE' and obj.name == 'Armature':
        armature_obj = obj
        break

if armature_obj:
    print(f"✅ Armature encontrado")
    
    # Asegurarse de que está en modo object
    if bpy.context.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    
    # Seleccionar solo el Armature
    bpy.ops.object.select_all(action='DESELECT')
    armature_obj.select_set(True)
    bpy.context.view_layer.objects.active = armature_obj
    
    # Aplicar las transformaciones
    print("Aplicando transformaciones...")
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    print(f"✅ Transformaciones aplicadas")
else:
    print(f"⚠️ No se encontró Armature")

# Exportar a GLB
print("Exportando GLB...")
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

print(f"✅ Exportado: {glb_output.name}")
print(f"\n{'='*80}\n")
