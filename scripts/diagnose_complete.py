import bpy
from pathlib import Path
import tempfile
import os

# Limpiar
bpy.ops.wm.read_factory_settings(use_empty=True)

print("\n" + "="*80)
print("FASE 1: IMPORTAR NANCY BASE (CON TEXTURAS)")
print("="*80)

NANCY_BASE = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy\Nancy.glb")
bpy.ops.import_scene.gltf(filepath=str(NANCY_BASE))

nancy_arm = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        nancy_arm = obj
        break

print(f"Armature: {nancy_arm.name}")
print(f"Tiene animation_data: {nancy_arm.animation_data is not None}")
if nancy_arm.animation_data:
    print(f"  Action: {nancy_arm.animation_data.action}")
    print(f"  NLA tracks: {len(nancy_arm.animation_data.nla_tracks)}")
print(f"Imágenes: {len([img for img in bpy.data.images if img.packed_file])}")
print(f"Acciones en bpy.data.actions: {len(bpy.data.actions)}")

print("\n" + "="*80)
print("FASE 2: IMPORTAR ARCHIVO ANIMADO (NINA)")
print("="*80)

NINA_FILE = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nina\cortesia\Nina_resultado_cortesia.glb")
bpy.ops.import_scene.gltf(filepath=str(NINA_FILE))

nina_arm = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE' and obj != nancy_arm:
        nina_arm = obj
        break

print(f"Armature Nina: {nina_arm.name}")
print(f"Tiene animation_data: {nina_arm.animation_data is not None}")
if nina_arm.animation_data and nina_arm.animation_data.action:
    action_original = nina_arm.animation_data.action
    print(f"  Action: {action_original.name}")
    print(f"  FCurves: {len(action_original.fcurves)}")
    frame_start = min([min([kf.co[0] for kf in fc.keyframe_points]) for fc in action_original.fcurves])
    frame_end = max([max([kf.co[0] for kf in fc.keyframe_points]) for fc in action_original.fcurves])
    print(f"  Frame range: {frame_start} - {frame_end}")
    print(f"  NLA tracks: {len(nina_arm.animation_data.nla_tracks)}")

print(f"Imágenes totales: {len([img for img in bpy.data.images if img.packed_file])}")
print(f"Acciones en bpy.data.actions: {len(bpy.data.actions)}")
for act in bpy.data.actions:
    print(f"  - {act.name} ({len(act.fcurves)} FCurves, users={act.users})")

print("\n" + "="*80)
print("FASE 3: COPIAR ANIMACIÓN Y ASIGNAR A NANCY")
print("="*80)

# Copiar action
action = action_original.copy()
action.name = "AnimacionLimpia"
print(f"Action copiada: {action.name}")

# Eliminar FCurves de piernas
huesos_piernas = ["Hips", "LeftUpLeg", "LeftLeg", "LeftFoot", "LeftToeBase", "LeftToe_End",
                  "RightUpLeg", "RightLeg", "RightFoot", "RightToeBase", "RightToe_End"]
fcurves_eliminar = [fc for fc in action.fcurves if any(f'pose.bones["{h}"]' in fc.data_path for h in huesos_piernas)]
for fc in fcurves_eliminar:
    action.fcurves.remove(fc)
print(f"FCurves eliminadas: {len(fcurves_eliminar)}")
print(f"FCurves restantes: {len(action.fcurves)}")

# Eliminar objetos de Nina
objetos_nancy = [obj for obj in bpy.data.objects if obj == nancy_arm or obj.parent == nancy_arm]
objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_nancy]
for obj in objetos_eliminar:
    bpy.data.objects.remove(obj, do_unlink=True)
print(f"Objetos eliminados: {len(objetos_eliminar)}")

# Asignar action a Nancy
if not nancy_arm.animation_data:
    nancy_arm.animation_data_create()
    
nancy_arm.animation_data.action = action
print(f"Action asignada a Nancy: {nancy_arm.animation_data.action.name}")
print(f"NLA tracks en Nancy: {len(nancy_arm.animation_data.nla_tracks)}")

# Marcar action con fake_user para que no se elimine
action.use_fake_user = True
print(f"Action tiene fake_user: {action.use_fake_user}")

print(f"\nAcciones en bpy.data.actions: {len(bpy.data.actions)}")
for act in bpy.data.actions:
    print(f"  - {act.name} (FCurves={len(act.fcurves)}, users={act.users}, fake_user={act.use_fake_user})")

print("\n" + "="*80)
print("FASE 4: EXPORTAR CON DIFERENTES CONFIGURACIONES")
print("="*80)

temp_dir = Path(tempfile.gettempdir())

# Configuración 1: Default (lo que estábamos usando)
archivo1 = temp_dir / "test_config1_default.glb"
bpy.ops.export_scene.gltf(
    filepath=str(archivo1),
    export_format='GLB',
    export_animations=True,
    export_force_sampling=False,
    export_image_format='AUTO'
)
print(f"✓ Config 1 (default): {archivo1.stat().st_size / (1024*1024):.1f}MB")

# Configuración 2: Con force_sampling
archivo2 = temp_dir / "test_config2_sampling.glb"
bpy.ops.export_scene.gltf(
    filepath=str(archivo2),
    export_format='GLB',
    export_animations=True,
    export_force_sampling=True,
    export_image_format='AUTO'
)
print(f"✓ Config 2 (force_sampling): {archivo2.stat().st_size / (1024*1024):.1f}MB")

# Configuración 3: Sin NLA strips
archivo3 = temp_dir / "test_config3_no_nla.glb"
bpy.ops.export_scene.gltf(
    filepath=str(archivo3),
    export_format='GLB',
    export_animations=True,
    export_nla_strips=False,
    export_force_sampling=False,
    export_image_format='AUTO'
)
print(f"✓ Config 3 (no NLA): {archivo3.stat().st_size / (1024*1024):.1f}MB")

print("\n" + "="*80)
print("FASE 5: VERIFICAR CADA ARCHIVO EXPORTADO")
print("="*80)

for i, archivo in enumerate([archivo1, archivo2, archivo3], 1):
    print(f"\n--- Config {i}: {archivo.name} ---")
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(archivo))
    
    arm = next((obj for obj in bpy.data.objects if obj.type == 'ARMATURE'), None)
    if arm:
        print(f"Armature: {arm.name}")
        if arm.animation_data:
            print(f"  ✓ Tiene animation_data")
            print(f"  Action: {arm.animation_data.action.name if arm.animation_data.action else 'None'}")
            if arm.animation_data.action:
                print(f"    FCurves: {len(arm.animation_data.action.fcurves)}")
            print(f"  NLA tracks: {len(arm.animation_data.nla_tracks)}")
            for track in arm.animation_data.nla_tracks:
                print(f"    Track: {track.name}")
                for strip in track.strips:
                    print(f"      Strip: {strip.name} | Action: {strip.action.name if strip.action else 'None'}")
        else:
            print(f"  ✗ NO tiene animation_data")
            
        print(f"  Imágenes: {len([img for img in bpy.data.images if img.packed_file])}")
    else:
        print("  ✗ NO se encontró armature")

print("\n" + "="*80)
print("CONCLUSIÓN: ¿Cuál configuración mantiene animación + texturas?")
print("="*80)
