"""
Abre nancy_yo.glb en Blender con UI para inspeccionar la animación
"""
import bpy

# Limpiar escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Importar nancy_yo.glb
glb_path = r"C:\Users\andre\OneDrive\Documentos\tesis\nancy_yo.glb"
bpy.ops.import_scene.gltf(filepath=glb_path)

# Encontrar armature y seleccionarlo
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)
        
        # Verificar animación
        if obj.animation_data and obj.animation_data.action:
            action = obj.animation_data.action
            print(f"\n✅ ANIMACIÓN ENCONTRADA:")
            print(f"   Action: {action.name}")
            print(f"   FCurves: {len(action.fcurves)}")
            print(f"   Keyframes: {sum(len(fc.keyframe_points) for fc in action.fcurves)}")
            print(f"   Frame range: {action.frame_range[0]:.0f} - {action.frame_range[1]:.0f}")
            
            # Configurar timeline
            bpy.context.scene.frame_start = int(action.frame_range[0])
            bpy.context.scene.frame_end = int(action.frame_range[1])
            bpy.context.scene.frame_current = 1
            
            print(f"\n📺 INSTRUCCIONES:")
            print(f"   1. Presiona ESPACIO para reproducir")
            print(f"   2. Deberías ver a Nancy moviéndose")
            print(f"   3. Si se mueve, la exportación fue exitosa!")
        else:
            print("\n❌ NO HAY ANIMACIÓN")
        break

# Cambiar a workspace de animación
for workspace in bpy.data.workspaces:
    if 'Animation' in workspace.name:
        bpy.context.window.workspace = workspace
        break
