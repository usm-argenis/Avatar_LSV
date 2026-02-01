"""
Script para abrir el GLB en Blender y verificar que tiene las animaciones faciales
"""
import bpy
from pathlib import Path

# Limpiar escena
bpy.ops.wm.read_homefile(use_empty=True)

# Ruta al archivo GLB procesado
glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\saludos\Duvall_resultado_hola.glb")

# Importar GLB
print(f"Importando: {glb_path}")
bpy.ops.import_scene.gltf(filepath=str(glb_path))

# Buscar objeto con shape keys
for obj in bpy.data.objects:
    if obj.type == 'MESH' and 'Wolf3D_Head' in obj.name:
        print(f"\n✅ Objeto encontrado: {obj.name}")
        
        if obj.data.shape_keys:
            print(f"  Shape keys: {len(obj.data.shape_keys.key_blocks)}")
            
            # Verificar si tiene animación
            if obj.animation_data and obj.animation_data.action:
                action = obj.animation_data.action
                print(f"\n  ✅ Acción encontrada: {action.name}")
                print(f"  F-Curves: {len(action.fcurves)}")
                
                # Listar F-Curves
                for fcurve in action.fcurves:
                    data_path = fcurve.data_path
                    keyframes = len(fcurve.keyframe_points)
                    # Obtener valores min y max
                    if keyframes > 0:
                        values = [kf.co[1] for kf in fcurve.keyframe_points]
                        min_val = min(values)
                        max_val = max(values)
                        print(f"    - {data_path}: {keyframes} keyframes (min: {min_val:.3f}, max: {max_val:.3f})")
            else:
                print("  ❌ NO tiene animation_data o action")
        else:
            print("  ❌ NO tiene shape keys")
        break

print("\n✅ Verificación completada")
