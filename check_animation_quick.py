import bpy

filepath = r'c:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\deepmotion\verbo_default_1.glb'

bpy.ops.import_scene.gltf(filepath=filepath)

arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]
has_anim = arm.animation_data and arm.animation_data.action

print(f'\nAnimación: {"SI" if has_anim else "NO"}')
if has_anim:
    print(f'Action: {arm.animation_data.action.name}')
    print(f'Frames: {int(arm.animation_data.action.frame_range[0])}-{int(arm.animation_data.action.frame_range[1])}')
else:
    print('Action: NINGUNA')
    print('Frames: Sin frames')
