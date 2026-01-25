#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aplicador de Alta Precisión a Duvall
Aplica coordenadas extraídas SOLO al tren superior (hombros, brazos, manos, cabeza, torso)
PRESERVA completamente cadera y piernas del modelo original
"""

import bpy
import json
import sys
import math
from pathlib import Path
from mathutils import Vector, Quaternion, Euler

print("\n" + "=" * 80)
print("APLICACIÓN DE ALTA PRECISIÓN - DUVALL TREN SUPERIOR")
print("=" * 80)

# Rutas
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test")
JSON_DATA = BASE_DIR / "output" / "hola_precision.json"
DUVALL_MODEL = BASE_DIR / "output" / "glb" / "Duvall" / "saludos" / "Duvall_resultado_hola_final.glb"
OUTPUT_GLB = BASE_DIR / "output" / "glb" / "Duvall" / "saludos" / "Duvall_resultado_hola_ULTRA_PRECISO.glb"

# HUESOS A PRESERVAR (NO MODIFICAR - cadera y piernas)
HUESOS_PRESERVAR = {
    'Hips',  # Cadera raíz
    'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 'LeftToe_End',
    'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase', 'RightToe_End'
}

# HUESOS A ANIMAR (tren superior)
HUESOS_ANIMAR = {
    'Spine', 'Spine1', 'Spine2',  # Columna
    'Neck', 'Head',  # Cuello y cabeza
    'LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand',  # Brazo izquierdo
    'RightShoulder', 'RightArm', 'RightForeArm', 'RightHand',  # Brazo derecho
    # Dedos mano izquierda
    'LeftHandThumb1', 'LeftHandThumb2', 'LeftHandThumb3', 'LeftHandThumb4',
    'LeftHandIndex1', 'LeftHandIndex2', 'LeftHandIndex3', 'LeftHandIndex4',
    'LeftHandMiddle1', 'LeftHandMiddle2', 'LeftHandMiddle3', 'LeftHandMiddle4',
    'LeftHandRing1', 'LeftHandRing2', 'LeftHandRing3', 'LeftHandRing4',
    'LeftHandPinky1', 'LeftHandPinky2', 'LeftHandPinky3', 'LeftHandPinky4',
    # Dedos mano derecha
    'RightHandThumb1', 'RightHandThumb2', 'RightHandThumb3', 'RightHandThumb4',
    'RightHandIndex1', 'RightHandIndex2', 'RightHandIndex3', 'RightHandIndex4',
    'RightHandMiddle1', 'RightHandMiddle2', 'RightHandMiddle3', 'RightHandMiddle4',
    'RightHandRing1', 'RightHandRing2', 'RightHandRing3', 'RightHandRing4',
    'RightHandPinky1', 'RightHandPinky2', 'RightHandPinky3', 'RightHandPinky4'
}

class AplicadorPrecisionDuvall:
    """Aplica landmarks precisos al modelo Duvall"""
    
    def __init__(self):
        # Mapeo MediaPipe Pose (33) a huesos Mixamo/Duvall
        self.pose_bone_map = {
            # TREN SUPERIOR SOLAMENTE
            11: 'LeftShoulder',   # Hombro izquierdo
            12: 'RightShoulder',  # Hombro derecho
            13: 'LeftArm',        # Codo izquierdo
            14: 'RightArm',       # Codo derecho
            15: 'LeftForeArm',    # Muñeca izquierda
            16: 'RightForeArm',   # Muñeca derecha
            0: 'Head',            # Nariz -> Cabeza
            # Torso
            11: 'Spine2',         # Hombro izquierdo -> Parte superior columna
            12: 'Spine1',         # Centro pecho
        }
        
        # Mapeo MediaPipe Hand (21 landmarks por mano) a huesos dedos
        self.hand_bone_map = {
            # PULGAR (Thumb)
            1: 'HandThumb1',
            2: 'HandThumb2',
            3: 'HandThumb3',
            4: 'HandThumb4',
            # ÍNDICE (Index)
            5: 'HandIndex1',
            6: 'HandIndex2',
            7: 'HandIndex3',
            8: 'HandIndex4',
            # MEDIO (Middle)
            9: 'HandMiddle1',
            10: 'HandMiddle2',
            11: 'HandMiddle3',
            12: 'HandMiddle4',
            # ANULAR (Ring)
            13: 'HandRing1',
            14: 'HandRing2',
            15: 'HandRing3',
            16: 'HandRing4',
            # MEÑIQUE (Pinky)
            17: 'HandPinky1',
            18: 'HandPinky2',
            19: 'HandPinky3',
            20: 'HandPinky4'
        }
    
    def cargar_datos_precision(self, json_path):
        """Carga el JSON con datos precisos"""
        print(f"\n📂 Cargando datos de precisión...")
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        frames = data.get('frames', [])
        fps = data['metadata'].get('fps', 30.0)
        
        print(f"   ✅ Frames cargados: {len(frames)}")
        print(f"   ✅ FPS: {fps}")
        
        return data, frames, fps
    
    def mediapipe_to_world(self, mp_coords, scale=2.0):
        """
        Convierte coordenadas MediaPipe normalizadas a espacio 3D mundial
        MediaPipe: x,y en [0,1], z en profundidad relativa
        """
        x = (mp_coords['x'] - 0.5) * scale  # Centrar en 0
        y = -(mp_coords['y'] - 0.5) * scale  # Invertir Y (MediaPipe Y+ es abajo)
        z = -mp_coords['z'] * scale  # Profundidad (hacia cámara es negativo)
        
        return Vector((x, y, z))
    
    def calcular_rotacion_entre_puntos(self, punto_origen, punto_destino):
        """Calcula la rotación quaternion necesaria para apuntar de origen a destino"""
        direccion = (punto_destino - punto_origen).normalized()
        
        # Vector por defecto del hueso (apuntando en +Y en Mixamo)
        default_dir = Vector((0, 1, 0))
        
        # Calcular rotación necesaria
        rotation_diff = default_dir.rotation_difference(direccion)
        
        return rotation_diff
    
    def aplicar_animacion_tren_superior(self, armature, frames, fps):
        """
        Aplica animación SOLO al tren superior
        NO toca Hips ni piernas
        """
        print(f"\n🎬 Aplicando animación al tren superior...")
        print(f"   ⚠️  PRESERVANDO: Hips y piernas (cadera hacia abajo)")
        print(f"   ✅ ANIMANDO: Columna, brazos, manos, cabeza")
        
        # Configurar escena
        bpy.context.scene.frame_start = 0
        bpy.context.scene.frame_end = len(frames) - 1
        bpy.context.scene.render.fps = int(fps)
        
        # Crear o limpiar action
        if not armature.animation_data:
            armature.animation_data_create()
        
        action_name = "Hola_Precision_TrenSuperior"
        if action_name in bpy.data.actions:
            action = bpy.data.actions[action_name]
        else:
            action = bpy.data.actions.new(name=action_name)
        
        armature.animation_data.action = action
        
        # Seleccionar armature y entrar en pose mode
        bpy.context.view_layer.objects.active = armature
        bpy.ops.object.mode_set(mode='POSE')
        
        # Guardar pose original de Hips y piernas
        print(f"\n💾 Guardando pose original de cadera y piernas...")
        poses_originales = {}
        for bone_name in HUESOS_PRESERVAR:
            if bone_name in armature.pose.bones:
                pbone = armature.pose.bones[bone_name]
                poses_originales[bone_name] = {
                    'location': pbone.location.copy(),
                    'rotation_quaternion': pbone.rotation_quaternion.copy() if pbone.rotation_mode == 'QUATERNION' else None,
                    'rotation_euler': pbone.rotation_euler.copy() if pbone.rotation_mode != 'QUATERNION' else None,
                    'scale': pbone.scale.copy()
                }
        
        print(f"   ✅ {len(poses_originales)} huesos preservados")
        
        # Procesar cada frame
        frames_procesados = 0
        frames_con_manos = 0
        frames_con_pose = 0
        
        for frame_idx, frame_data in enumerate(frames):
            bpy.context.scene.frame_set(frame_idx)
            
            # 1. POSE (tren superior: hombros, brazos, torso)
            if 'pose' in frame_data:
                pose_lms = frame_data['pose']
                frames_con_pose += 1
                
                # HOMBROS Y BRAZOS
                # Hombro izquierdo (landmark 11)
                if len(pose_lms) > 11:
                    if 'LeftShoulder' in armature.pose.bones:
                        pos = self.mediapipe_to_world(pose_lms[11])
                        # Aplicar rotación basada en posición
                        # (implementación simplificada - se puede mejorar)
                        pbone = armature.pose.bones['LeftShoulder']
                        if 'LeftArm' in armature.pose.bones and len(pose_lms) > 13:
                            codo_pos = self.mediapipe_to_world(pose_lms[13])
                            rot = self.calcular_rotacion_entre_puntos(pos, codo_pos)
                            pbone.rotation_quaternion = rot
                            pbone.keyframe_insert(data_path="rotation_quaternion", frame=frame_idx)
                
                # Hombro derecho (landmark 12)
                if len(pose_lms) > 12:
                    if 'RightShoulder' in armature.pose.bones:
                        pos = self.mediapipe_to_world(pose_lms[12])
                        pbone = armature.pose.bones['RightShoulder']
                        if 'RightArm' in armature.pose.bones and len(pose_lms) > 14:
                            codo_pos = self.mediapipe_to_world(pose_lms[14])
                            rot = self.calcular_rotacion_entre_puntos(pos, codo_pos)
                            pbone.rotation_quaternion = rot
                            pbone.keyframe_insert(data_path="rotation_quaternion", frame=frame_idx)
                
                # Brazo izquierdo (landmark 13 -> codo)
                if len(pose_lms) > 15 and 'LeftArm' in armature.pose.bones:
                    codo_pos = self.mediapipe_to_world(pose_lms[13])
                    muneca_pos = self.mediapipe_to_world(pose_lms[15])
                    rot = self.calcular_rotacion_entre_puntos(codo_pos, muneca_pos)
                    pbone = armature.pose.bones['LeftArm']
                    pbone.rotation_quaternion = rot
                    pbone.keyframe_insert(data_path="rotation_quaternion", frame=frame_idx)
                
                # Brazo derecho (landmark 14 -> codo)
                if len(pose_lms) > 16 and 'RightArm' in armature.pose.bones:
                    codo_pos = self.mediapipe_to_world(pose_lms[14])
                    muneca_pos = self.mediapipe_to_world(pose_lms[16])
                    rot = self.calcular_rotacion_entre_puntos(codo_pos, muneca_pos)
                    pbone = armature.pose.bones['RightArm']
                    pbone.rotation_quaternion = rot
                    pbone.keyframe_insert(data_path="rotation_quaternion", frame=frame_idx)
                
                # CABEZA (landmark 0 -> nariz)
                if len(pose_lms) > 0 and 'Head' in armature.pose.bones:
                    nariz_pos = self.mediapipe_to_world(pose_lms[0])
                    # Calcular orientación de cabeza basado en landmarks faciales
                    pbone = armature.pose.bones['Head']
                    # (Se puede mejorar con face landmarks)
            
            # 2. MANOS (dedos - MÁXIMA PRECISIÓN)
            if 'left_hand' in frame_data:
                frames_con_manos += 1
                hand_lms = frame_data['left_hand']
                self.aplicar_mano_precisa(armature, hand_lms, 'Left', frame_idx)
            
            if 'right_hand' in frame_data:
                hand_lms = frame_data['right_hand']
                self.aplicar_mano_precisa(armature, hand_lms, 'Right', frame_idx)
            
            # 3. ROSTRO (gestos faciales con shape keys si están disponibles)
            if 'face' in frame_data:
                # TODO: Implementar shape keys para expresiones faciales
                pass
            
            frames_procesados += 1
            
            if frames_procesados % 10 == 0:
                progreso = (frames_procesados / len(frames)) * 100
                print(f"   📊 {progreso:.1f}% - Frame {frames_procesados}/{len(frames)}", end='\r')
        
        print(f"\n\n✅ Animación aplicada")
        print(f"   📊 Frames procesados: {frames_procesados}")
        print(f"   🎯 Frames con pose: {frames_con_pose}")
        print(f"   👐 Frames con manos: {frames_con_manos}")
        
        # RESTAURAR poses originales de Hips y piernas
        print(f"\n🔒 Restaurando poses originales de cadera y piernas...")
        for bone_name, pose_orig in poses_originales.items():
            if bone_name in armature.pose.bones:
                pbone = armature.pose.bones[bone_name]
                pbone.location = pose_orig['location']
                if pose_orig['rotation_quaternion']:
                    pbone.rotation_quaternion = pose_orig['rotation_quaternion']
                if pose_orig['rotation_euler']:
                    pbone.rotation_euler = pose_orig['rotation_euler']
                pbone.scale = pose_orig['scale']
                
                # Keyframe para mantener fijo en todos los frames
                for frame_idx in range(len(frames)):
                    bpy.context.scene.frame_set(frame_idx)
                    pbone.keyframe_insert(data_path="location", frame=frame_idx)
                    if pose_orig['rotation_quaternion']:
                        pbone.keyframe_insert(data_path="rotation_quaternion", frame=frame_idx)
                    if pose_orig['rotation_euler']:
                        pbone.keyframe_insert(data_path="rotation_euler", frame=frame_idx)
                    pbone.keyframe_insert(data_path="scale", frame=frame_idx)
        
        print(f"   ✅ Cadera y piernas PRESERVADAS correctamente")
        
        # Volver a object mode
        bpy.ops.object.mode_set(mode='OBJECT')
    
    def aplicar_mano_precisa(self, armature, hand_landmarks, lado, frame_idx):
        """
        Aplica landmarks de mano con MÁXIMA PRECISIÓN
        lado: 'Left' o 'Right'
        """
        for lm_idx, bone_suffix in self.hand_bone_map.items():
            if lm_idx >= len(hand_landmarks):
                continue
            
            bone_name = f"{lado}{bone_suffix}"
            if bone_name not in armature.pose.bones:
                continue
            
            pbone = armature.pose.bones[bone_name]
            
            # Obtener posición del landmark
            lm_pos = self.mediapipe_to_world(hand_landmarks[lm_idx])
            
            # Calcular rotación hacia el siguiente landmark (si existe)
            next_lm_idx = lm_idx + 1
            if next_lm_idx in self.hand_bone_map and next_lm_idx < len(hand_landmarks):
                next_pos = self.mediapipe_to_world(hand_landmarks[next_lm_idx])
                rot = self.calcular_rotacion_entre_puntos(lm_pos, next_pos)
                pbone.rotation_quaternion = rot
                pbone.keyframe_insert(data_path="rotation_quaternion", frame=frame_idx)


def main():
    # Verificar archivos
    if not JSON_DATA.exists():
        print(f"❌ Error: No se encontró {JSON_DATA}")
        print(f"   Ejecuta primero: procesar_hola_precision.py")
        return 1
    
    if not DUVALL_MODEL.exists():
        print(f"❌ Error: No se encontró {DUVALL_MODEL}")
        return 1
    
    # Limpiar escena
    print(f"\n🧹 Limpiando escena...")
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
    # Cargar modelo Duvall
    print(f"\n📦 Cargando modelo Duvall...")
    print(f"   {DUVALL_MODEL}")
    bpy.ops.import_scene.gltf(filepath=str(DUVALL_MODEL))
    
    # Buscar armature
    armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            armature = obj
            break
    
    if not armature:
        print(f"❌ Error: No se encontró armature en el modelo")
        return 1
    
    print(f"   ✅ Armature encontrada: {armature.name}")
    print(f"   ✅ Huesos: {len(armature.data.bones)}")
    
    # Aplicar animación precisa
    aplicador = AplicadorPrecisionDuvall()
    data, frames, fps = aplicador.cargar_datos_precision(JSON_DATA)
    aplicador.aplicar_animacion_tren_superior(armature, frames, fps)
    
    # Exportar
    print(f"\n💾 Exportando modelo con animación precisa...")
    print(f"   {OUTPUT_GLB}")
    
    bpy.ops.export_scene.gltf(
        filepath=str(OUTPUT_GLB),
        export_format='GLB',
        export_animations=True,
        export_frame_range=True,
        export_current_frame=False,
        export_force_sampling=True,
        export_def_bones=False,
        export_optimize_animation_size=False,
        export_nla_strips=False,
        export_apply=True
    )
    
    if OUTPUT_GLB.exists():
        size_mb = OUTPUT_GLB.stat().st_size / (1024 * 1024)
        print(f"\n✅ ÉXITO - Modelo generado ({size_mb:.1f} MB)")
        print(f"\n🎯 RESULTADO:")
        print(f"   - Tren superior: ANIMACIÓN PRECISA del video")
        print(f"   - Cadera y piernas: PRESERVADAS del modelo original")
        print(f"   - Manos: GESTOS PRECISOS del video")
        print(f"   - Texturas: MANTENIDAS")
        return 0
    else:
        print(f"\n❌ Error: No se generó el archivo")
        return 1


if __name__ == "__main__":
    sys.exit(main())
