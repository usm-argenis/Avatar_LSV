"""
Script de diagnóstico completo para entender el problema
"""
import bpy
from pathlib import Path

# Limpiar
bpy.ops.wm.read_homefile(use_empty=True)

print("\n" + "="*70)
print("PARTE 1: Verificar GLB ORIGINAL (antes de modificar)")
print("="*70)

# Importar GLB ORIGINAL sin modificar
original_glb = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\saludos\Duvall_hola.glb")
if original_glb.exists():
    bpy.ops.import_scene.gltf(filepath=str(original_glb))
    
    print("\nAcciones en GLB original:")
    for action in bpy.data.actions:
        print(f"  - {action.name}: {len(action.fcurves)} F-Curves")
    
    print("\nObjetos con animación:")
    for obj in bpy.data.objects:
        if obj.animation_data and obj.animation_data.action:
            print(f"  - {obj.name} ({obj.type}): {obj.animation_data.action.name}")
    
    # Verificar objeto con shape keys
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and 'Wolf3D_Head' in obj.name:
            print(f"\nObjeto: {obj.name}")
            if obj.data.shape_keys:
                print(f"  Shape keys: {len(obj.data.shape_keys.key_blocks)}")
            if obj.animation_data:
                print(f"  Tiene animation_data: Sí")
                if obj.animation_data.action:
                    print(f"  Action: {obj.animation_data.action.name}")
            else:
                print(f"  Tiene animation_data: No")
            break

# Limpiar para siguiente prueba
bpy.ops.wm.read_homefile(use_empty=True)

print("\n" + "="*70)
print("PARTE 2: Crear animación facial MANUALMENTE y exportar")
print("="*70)

# Importar GLB original de nuevo
bpy.ops.import_scene.gltf(filepath=str(original_glb))

# Encontrar Wolf3D_Head
head_obj = None
for obj in bpy.data.objects:
    if 'Wolf3D_Head' in obj.name and obj.type == 'MESH':
        head_obj = obj
        break

if head_obj and head_obj.data.shape_keys:
    print(f"\nObjeto encontrado: {head_obj.name}")
    print(f"Shape keys: {len(head_obj.data.shape_keys.key_blocks)}")
    
    # MÉTODO 1: Crear action en el MESH
    print("\n--- Probando MÉTODO 1: Action en el Mesh ---")
    if not head_obj.animation_data:
        head_obj.animation_data_create()
    
    action = bpy.data.actions.new(name="TestFacial_Mesh")
    head_obj.animation_data.action = action
    
    # Agregar F-Curve para mouthSmileLeft
    data_path = 'data.shape_keys.key_blocks["mouthSmileLeft"].value'
    fcurve = action.fcurves.new(data_path)
    fcurve.keyframe_points.insert(0, 0.0)
    fcurve.keyframe_points.insert(15, 0.5)
    fcurve.keyframe_points.insert(56, 0.5)
    fcurve.keyframe_points.insert(70, 0.0)
    
    print(f"F-Curve creado: {data_path}")
    print(f"Keyframes: {len(fcurve.keyframe_points)}")
    
    # Exportar para probar
    test_glb = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\test_facial_mesh.glb")
    bpy.ops.export_scene.gltf(
        filepath=str(test_glb),
        export_format='GLB',
        export_animations=True,
        export_morph=True,
        export_morph_normal=True,
        export_morph_tangent=True
    )
    print(f"\nExportado a: {test_glb}")
    
    # Limpiar y reimportar para verificar
    bpy.ops.wm.read_homefile(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(test_glb))
    
    print("\nVerificación después de reimportar:")
    for obj in bpy.data.objects:
        if 'Wolf3D_Head' in obj.name and obj.type == 'MESH':
            if obj.animation_data and obj.animation_data.action:
                print(f"  ✅ {obj.name} tiene action: {obj.animation_data.action.name}")
                print(f"     F-Curves: {len(obj.animation_data.action.fcurves)}")
            else:
                print(f"  ❌ {obj.name} NO tiene action")
            break

print("\n" + "="*70)
print("DIAGNÓSTICO COMPLETADO")
print("="*70)
