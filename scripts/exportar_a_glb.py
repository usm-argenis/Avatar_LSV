import bpy
import sys

print("\n" + "="*70)
print("EXPORTANDO A GLB (formato que funciona mejor con Three.js)")
print("="*70)

# Abrir el archivo .blend
blend_path = r"C:\Users\andre\OneDrive\Documentos\tesis\output\Leonard_con_animacion_b.blend"
bpy.ops.wm.open_mainfile(filepath=blend_path)

print(f"\nArchivo abierto: {blend_path}")

# Verificar que hay animación
arm = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        arm = obj
        break

if arm and arm.animation_data and arm.animation_data.action:
    action = arm.animation_data.action
    print(f"\n✓ Animación encontrada: {action.name}")
    print(f"  Frames: {int(action.frame_range[0])} - {int(action.frame_range[1])}")
    print(f"  FCurves: {len(action.fcurves)}")
else:
    print("\n❌ ERROR: No hay animación")
    sys.exit(1)

# Configurar frame range
bpy.context.scene.frame_start = int(action.frame_range[0])
bpy.context.scene.frame_end = int(action.frame_range[1])

# Exportar a GLB
glb_path = r"C:\Users\andre\OneDrive\Documentos\tesis\output\Leonard_con_animacion_b.glb"

print(f"\n📦 Exportando a GLB...")
print(f"   {glb_path}")

bpy.ops.export_scene.gltf(
    filepath=glb_path,
    export_format='GLB',
    export_animations=True,
    export_apply=True,
    export_current_frame=False,
    export_frame_range=True,
    export_frame_step=1,
    export_force_sampling=True,
    export_lights=False,
    export_cameras=False
)

print("\n✓ GLB exportado exitosamente!")
print("\nPara usar en Three.js:")
print("""
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';

const loader = new GLTFLoader();
loader.load('Leonard_con_animacion_b.glb', (gltf) => {
    const model = gltf.scene;
    const animations = gltf.animations;
    
    scene.add(model);
    
    const mixer = new THREE.AnimationMixer(model);
    const action = mixer.clipAction(animations[0]);
    action.play();
});
""")

print("="*70)
