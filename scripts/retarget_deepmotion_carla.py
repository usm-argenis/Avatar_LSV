import bpy
import sys
import os
from pathlib import Path
from mathutils import Vector, Quaternion

# ====================================================================
# RETARGET DEEPMOTION -> CARLA
# Convierte animaciones de Deepmotion a armadura de Carla
# ====================================================================

# Rutas base
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis")
DOWNLOADS_DIR = Path(r"C:\Users\andre\Downloads")

# Avatar destino
CARLA_GLB = BASE_DIR / "test" / "output" / "glb" / "Carla" / "Carla.glb"

# Mapeo de huesos Deepmotion -> Carla (mismo que Duvall)
BONE_MAPPING = {
    # Torso
    'hips_JNT': 'Hips',
    'spine_JNT': 'Spine',
    'spine1_JNT': 'Spine1',
    'spine2_JNT': 'Spine2',
    'neck_JNT': 'Neck',
    'head_JNT': 'Head',
    
    # Brazo izquierdo
    'l_shoulder_JNT': 'LeftShoulder',
    'l_arm_JNT': 'LeftArm',
    'l_forearm_JNT': 'LeftForeArm',
    'l_hand_JNT': 'LeftHand',
    
    # Dedos izquierdos
    'l_handThumb1_JNT': 'LeftHandThumb1',
    'l_handThumb2_JNT': 'LeftHandThumb2',
    'l_handThumb3_JNT': 'LeftHandThumb3',
    'l_handIndex1_JNT': 'LeftHandIndex1',
    'l_handIndex2_JNT': 'LeftHandIndex2',
    'l_handIndex3_JNT': 'LeftHandIndex3',
    'l_handMiddle1_JNT': 'LeftHandMiddle1',
    'l_handMiddle2_JNT': 'LeftHandMiddle2',
    'l_handMiddle3_JNT': 'LeftHandMiddle3',
    'l_handRing1_JNT': 'LeftHandRing1',
    'l_handRing2_JNT': 'LeftHandRing2',
    'l_handRing3_JNT': 'LeftHandRing3',
    'l_handPinky1_JNT': 'LeftHandPinky1',
    'l_handPinky2_JNT': 'LeftHandPinky2',
    'l_handPinky3_JNT': 'LeftHandPinky3',
    
    # Brazo derecho
    'r_shoulder_JNT': 'RightShoulder',
    'r_arm_JNT': 'RightArm',
    'r_forearm_JNT': 'RightForeArm',
    'r_hand_JNT': 'RightHand',
    
    # Dedos derechos
    'r_handThumb1_JNT': 'RightHandThumb1',
    'r_handThumb2_JNT': 'RightHandThumb2',
    'r_handThumb3_JNT': 'RightHandThumb3',
    'r_handIndex1_JNT': 'RightHandIndex1',
    'r_handIndex2_JNT': 'RightHandIndex2',
    'r_handIndex3_JNT': 'RightHandIndex3',
    'r_handMiddle1_JNT': 'RightHandMiddle1',
    'r_handMiddle2_JNT': 'RightHandMiddle2',
    'r_handMiddle3_JNT': 'RightHandMiddle3',
    'r_handRing1_JNT': 'RightHandRing1',
    'r_handRing2_JNT': 'RightHandRing2',
    'r_handRing3_JNT': 'RightHandRing3',
    'r_handPinky1_JNT': 'RightHandPinky1',
    'r_handPinky2_JNT': 'RightHandPinky2',
    'r_handPinky3_JNT': 'RightHandPinky3',
    
    # Piernas izquierdas
    'l_upleg_JNT': 'LeftUpLeg',
    'l_leg_JNT': 'LeftLeg',
    'l_foot_JNT': 'LeftFoot',
    'l_toebase_JNT': 'LeftToeBase',
    
    # Piernas derechas
    'r_upleg_JNT': 'RightUpLeg',
    'r_leg_JNT': 'RightLeg',
    'r_foot_JNT': 'RightFoot',
    'r_toebase_JNT': 'RightToeBase',
}

def clear_scene():
    """Limpia la escena"""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    for action in bpy.data.actions:
        bpy.data.actions.remove(action)

def retarget_animation(source_glb, output_path, palabra):
    """
    Retargeta animación de Deepmotion a Carla
    
    Args:
        source_glb: Archivo GLB de Deepmotion
        output_path: Ruta de salida
        palabra: Nombre de la palabra/seña
    """
    print(f"\n{'='*70}")
    print(f"RETARGETING: {source_glb.name} -> Carla")
    print(f"Palabra: {palabra}")
    print(f"{'='*70}")
    
    # Limpiar escena
    clear_scene()
    
    # 1. Importar Deepmotion
    print(f"\n📥 Cargando animación Deepmotion...")
    bpy.ops.import_scene.gltf(filepath=str(source_glb))
    
    source_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            source_armature = obj
            break
    
    if not source_armature:
        print("❌ No se encontró armature en Deepmotion")
        return False
    
    print(f"   ✅ Armature: {source_armature.name}")
    
    # Obtener animación
    source_action = None
    if source_armature.animation_data and source_armature.animation_data.action:
        source_action = source_armature.animation_data.action
    elif len(bpy.data.actions) > 0:
        source_action = bpy.data.actions[0]
    
    if not source_action:
        print("❌ No se encontró animación")
        return False
    
    frame_start = int(source_action.frame_range[0])
    frame_end = int(source_action.frame_range[1])
    total_frames = frame_end - frame_start + 1
    
    print(f"   ✅ Animación: {source_action.name}")
    print(f"   📊 Frames: {frame_start} - {frame_end} ({total_frames} frames)")
    
    # 2. Importar Carla
    print(f"\n📥 Cargando Carla...")
    bpy.ops.import_scene.gltf(filepath=str(CARLA_GLB))
    
    target_armature = None
    target_meshes = []
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE' and obj != source_armature:
            target_armature = obj
        elif obj.type == 'MESH' and obj.parent != source_armature:
            target_meshes.append(obj)
    
    if not target_armature:
        print("❌ No se encontró armature de Carla")
        return False
    
    print(f"   ✅ Carla armature: {target_armature.name}")
    print(f"   ✅ Meshes: {len(target_meshes)}")
    
    # 3. Crear nueva acción para Carla
    print(f"\n🎬 Creando animación retargeteada...")
    new_action = bpy.data.actions.new(name=f"{palabra}_retargeted")
    target_armature.animation_data_create()
    target_armature.animation_data.action = new_action
    
    # 4. Retargetear cada frame
    bpy.context.scene.frame_start = frame_start
    bpy.context.scene.frame_end = frame_end
    
    bones_retargeted = 0
    bones_skipped = 0
    
    # Cambiar a modo pose para Deepmotion
    bpy.context.view_layer.objects.active = source_armature
    bpy.ops.object.mode_set(mode='POSE')
    
    for frame in range(frame_start, frame_end + 1):
        bpy.context.scene.frame_set(frame)
        
        # Cambiar a Carla
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.view_layer.objects.active = target_armature
        bpy.ops.object.mode_set(mode='POSE')
        
        for source_bone_name, target_bone_name in BONE_MAPPING.items():
            if source_bone_name in source_armature.pose.bones and target_bone_name in target_armature.pose.bones:
                source_bone = source_armature.pose.bones[source_bone_name]
                target_bone = target_armature.pose.bones[target_bone_name]
                
                # Copiar rotación
                target_bone.rotation_quaternion = source_bone.rotation_quaternion.copy()
                target_bone.keyframe_insert(data_path="rotation_quaternion", frame=frame)
                
                if frame == frame_start:
                    bones_retargeted += 1
            elif frame == frame_start:
                bones_skipped += 1
        
        if frame % 10 == 0 or frame == frame_end:
            progress = ((frame - frame_start + 1) / total_frames) * 100
            print(f"   Progreso: {progress:.1f}% (frame {frame}/{frame_end})", end='\r')
    
    print(f"\n   ✅ Huesos retargeteados: {bones_retargeted}")
    if bones_skipped > 0:
        print(f"   ⚠️ Huesos omitidos: {bones_skipped}")
    
    # 5. Congelar piernas (LeftUpLeg, LeftLeg, RightUpLeg, RightLeg)
    print(f"\n🧊 Congelando piernas...")
    bpy.ops.object.mode_set(mode='POSE')
    
    freeze_bones = ['LeftUpLeg', 'LeftLeg', 'RightUpLeg', 'RightLeg']
    for bone_name in freeze_bones:
        if bone_name in target_armature.pose.bones:
            bone = target_armature.pose.bones[bone_name]
            
            # Resetear a identidad
            bone.rotation_quaternion = Quaternion()
            bone.location = Vector()
            
            # Keyframe en todos los frames
            for frame in range(frame_start, frame_end + 1):
                bpy.context.scene.frame_set(frame)
                bone.keyframe_insert(data_path="rotation_quaternion", frame=frame)
                bone.keyframe_insert(data_path="location", frame=frame)
            
            print(f"   ✅ {bone_name} congelado")
    
    # 6. Exportar
    print(f"\n💾 Exportando...")
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Seleccionar solo Carla (armature + meshes)
    bpy.ops.object.select_all(action='DESELECT')
    target_armature.select_set(True)
    for mesh in target_meshes:
        mesh.select_set(True)
    bpy.context.view_layer.objects.active = target_armature
    
    # Crear directorio de salida
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Exportar GLB con animación
    bpy.ops.export_scene.gltf(
        filepath=str(output_path),
        export_format='GLB',
        use_selection=True,
        export_animations=True,
        export_frame_range=True,
        export_frame_step=1,
        export_def_bones=True,
        export_image_format='AUTO',
        export_materials='EXPORT',
        export_bake_animation=True
    )
    
    print(f"   ✅ Exportado: {output_path.name}")
    print(f"\n{'='*70}")
    print(f"✅ RETARGETING COMPLETADO")
    print(f"{'='*70}\n")
    
    return True

def main():
    """Función principal"""
    # Obtener archivo source desde argumentos
    argv = sys.argv
    argv = argv[argv.index("--") + 1:] if "--" in argv else []
    
    if len(argv) < 1:
        print("❌ ERROR: Debes especificar el archivo fuente")
        print("Uso: blender --background --python retarget_deepmotion_carla.py -- <archivo> [palabra]")
        sys.exit(1)
    
    source_file = argv[0]
    palabra = argv[1] if len(argv) > 1 else Path(source_file).stem
    
    # Verificar archivo fuente
    source_path = Path(source_file)
    if not source_path.exists():
        # Intentar en Downloads
        source_path = DOWNLOADS_DIR / source_file
        if not source_path.exists():
            print(f"❌ ERROR: No se encuentra {source_file}")
            sys.exit(1)
    
    # Crear ruta de salida
    output_dir = BASE_DIR / "test" / "output" / "glb" / "Carla" / "deepmotion"
    output_path = output_dir / f"{palabra}.glb"
    
    # Ejecutar retargeting
    success = retarget_animation(source_path, output_path, palabra)
    
    if not success:
        print("❌ ERROR en retargeting")
        sys.exit(1)

if __name__ == "__main__":
    main()
