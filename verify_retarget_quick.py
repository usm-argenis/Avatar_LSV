import bpy

GLB_PATH = r"c:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\deepmotion\test_verbo1.glb"

bpy.ops.import_scene.gltf(filepath=GLB_PATH)

arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]
action = arm.animation_data.action if arm.animation_data else None
meshes = [o for o in bpy.data.objects if o.type == 'MESH']

print(f'\n✅ Animación: {action.name if action else "NINGUNA"}')
if action:
    print(f'✅ Frames: {int(action.frame_range[0])}-{int(action.frame_range[1])} ({int(action.frame_range[1] - action.frame_range[0] + 1)} frames)')
else:
    print('❌ No hay acción')
print(f'✅ Meshes: {len(meshes)}')
print(f'✅ Huesos: {len(arm.data.bones)}')
