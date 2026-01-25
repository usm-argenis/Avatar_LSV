import bpy
from pathlib import Path

print("="*80)
print("DIAGNÓSTICO: Verificación de huesos y animación")
print("="*80)

# Rutas
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_MODEL = BASE_DIR / "Nancy" / "Nancy.glb"
NINA_FILE = BASE_DIR / "Nina" / "cortesia" / "Nina_resultado_a la orden.glb"
NANCY_OUTPUT = BASE_DIR / "Nancy" / "cortesia" / "Nancy_resultado_a la orden.glb"

print("\n" + "="*80)
print("PASO 1: Verificar huesos de Nancy.glb")
print("="*80)

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(NANCY_MODEL))

nancy_arm = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        nancy_arm = obj
        break

if nancy_arm:
    print(f"\n✅ Armature Nancy: {nancy_arm.name}")
    print(f"Total huesos: {len(nancy_arm.data.bones)}")
    print("\nPrimeros 10 huesos de Nancy:")
    for i, bone in enumerate(list(nancy_arm.data.bones)[:10]):
        print(f"  {i+1}. {bone.name}")

print("\n" + "="*80)
print("PASO 2: Verificar huesos y animación de Nina")
print("="*80)

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(NINA_FILE))

nina_arm = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        nina_arm = obj
        break

if nina_arm:
    print(f"\n✅ Armature Nina: {nina_arm.name}")
    print(f"Total huesos: {len(nina_arm.data.bones)}")
    print("\nPrimeros 10 huesos de Nina:")
    for i, bone in enumerate(list(nina_arm.data.bones)[:10]):
        print(f"  {i+1}. {bone.name}")
    
    if nina_arm.animation_data and nina_arm.animation_data.action:
        nina_action = nina_arm.animation_data.action
        print(f"\n✅ Action: {nina_action.name}")
        print(f"FCurves: {len(nina_action.fcurves)}")
        
        # Analizar qué huesos están animados
        bones_animados = {}
        for fc in nina_action.fcurves:
            if "pose.bones[" in fc.data_path:
                # Extraer nombre del hueso
                start = fc.data_path.find('["') + 2
                end = fc.data_path.find('"]')
                bone_name = fc.data_path[start:end]
                
                if bone_name not in bones_animados:
                    bones_animados[bone_name] = []
                bones_animados[bone_name].append(fc.data_path)
        
        print(f"\n🦴 Huesos animados: {len(bones_animados)}")
        print("\nPrimeros 10 huesos con animación:")
        for i, (bone, paths) in enumerate(list(bones_animados.items())[:10]):
            print(f"  {i+1}. {bone} ({len(paths)} fcurves)")
        
        # Verificar algunos keyframes específicos
        print("\n📊 Verificación de keyframes:")
        sample_bone = list(bones_animados.keys())[0] if bones_animados else None
        if sample_bone:
            fcurves_bone = [fc for fc in nina_action.fcurves if f'["{sample_bone}"]' in fc.data_path]
            if fcurves_bone:
                fc = fcurves_bone[0]
                print(f"\nHueso ejemplo: {sample_bone}")
                print(f"Canal: {fc.data_path}")
                print(f"Keyframes: {len(fc.keyframe_points)}")
                print(f"Primeros 3 keyframes:")
                for i in range(min(3, len(fc.keyframe_points))):
                    kf = fc.keyframe_points[i]
                    print(f"  Frame {kf.co[0]:.1f}: {kf.co[1]:.6f}")

print("\n" + "="*80)
print("PASO 3: Verificar archivo exportado Nancy")
print("="*80)

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(NANCY_OUTPUT))

nancy_exp_arm = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        nancy_exp_arm = obj
        break

if nancy_exp_arm:
    print(f"\n✅ Armature: {nancy_exp_arm.name}")
    print(f"Total huesos: {len(nancy_exp_arm.data.bones)}")
    
    if nancy_exp_arm.animation_data and nancy_exp_arm.animation_data.action:
        nancy_action = nancy_exp_arm.animation_data.action
        print(f"\n✅ Action: {nancy_action.name}")
        print(f"FCurves: {len(nancy_action.fcurves)}")
        
        # Analizar qué huesos están animados en Nancy exportada
        bones_animados_nancy = {}
        for fc in nancy_action.fcurves:
            if "pose.bones[" in fc.data_path:
                start = fc.data_path.find('["') + 2
                end = fc.data_path.find('"]')
                bone_name = fc.data_path[start:end]
                
                if bone_name not in bones_animados_nancy:
                    bones_animados_nancy[bone_name] = []
                bones_animados_nancy[bone_name].append(fc.data_path)
        
        print(f"\n🦴 Huesos animados: {len(bones_animados_nancy)}")
        
        if bones_animados_nancy:
            sample_bone_nancy = list(bones_animados_nancy.keys())[0]
            fcurves_bone_nancy = [fc for fc in nancy_action.fcurves if f'["{sample_bone_nancy}"]' in fc.data_path]
            if fcurves_bone_nancy:
                fc = fcurves_bone_nancy[0]
                print(f"\nHueso ejemplo: {sample_bone_nancy}")
                print(f"Canal: {fc.data_path}")
                print(f"Keyframes: {len(fc.keyframe_points)}")
                print(f"Primeros 3 keyframes:")
                for i in range(min(3, len(fc.keyframe_points))):
                    kf = fc.keyframe_points[i]
                    print(f"  Frame {kf.co[0]:.1f}: {kf.co[1]:.6f}")
        else:
            print("\n❌ NO HAY HUESOS ANIMADOS EN NANCY EXPORTADA")
    else:
        print("\n❌ Nancy exportada NO TIENE ANIMACIÓN")

print("\n" + "="*80)
print("DIAGNÓSTICO COMPLETO")
print("="*80)
