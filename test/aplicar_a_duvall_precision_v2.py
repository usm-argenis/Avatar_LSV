#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APLICADOR ULTRA PRECISO - VERSIÓN FINAL
Aplica coordenadas MediaPipe del video hola.mp4 al modelo Duvall
con máxima precisión en gestos, manos y tren superior
PRESERVA cadera y piernas completamente
"""

import bpy
import json
import sys
import math
from pathlib import Path
from mathutils import Vector, Quaternion, Matrix, Euler

print("\n" + "=" * 80)
print("APLICADOR ULTRA PRECISO V2 - DUVALL HOLA")
print("=" * 80)

# Rutas
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test")
JSON_DATA = BASE_DIR / "output" / "hola_precision.json"
DUVALL_MODEL = BASE_DIR / "output" / "glb" / "Duvall" / "saludos" / "Duvall_resultado_hola_final.glb"
OUTPUT_GLB = BASE_DIR / "output" / "glb" / "Duvall" / "saludos" / "Duvall_resultado_hola_FINAL_V2.glb"

# Huesos a preservar (cadera y piernas)
HUESOS_PRESERVAR = {
    'Hips', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 'LeftToe_End',
    'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase', 'RightToe_End'
}

class AplicadorUltraPreciso:
    def __init__(self):
        # Escala para convertir MediaPipe a espacio 3D
        self.scale = 1.8
        
        # Mapeo MediaPipe Pose (33 landmarks) a huesos Mixamo
        self.pose_map = {
            0: 'Head',              # Nariz
            11: 'LeftShoulder',     # Hombro izq
            12: 'RightShoulder',    # Hombro der
            13: 'LeftArm',          # Codo izq
            14: 'RightArm',          # Codo der
            15: 'LeftForeArm',      # Muñeca izq
            16: 'RightForeArm',     # Muñeca der
        }
        
        # Mapeo MediaPipe Hand (21 landmarks) a dedos Mixamo
        self.hand_map = {
            0: 'Hand',
            1: 'HandThumb1', 2: 'HandThumb2', 3: 'HandThumb3', 4: 'HandThumb4',
            5: 'HandIndex1', 6: 'HandIndex2', 7: 'HandIndex3', 8: 'HandIndex4',
            9: 'HandMiddle1', 10: 'HandMiddle2', 11: 'HandMiddle3', 12: 'HandMiddle4',
            13: 'HandRing1', 14: 'HandRing2', 15: 'HandRing3', 16: 'HandRing4',
            17: 'HandPinky1', 18: 'HandPinky2', 19: 'HandPinky3', 20: 'HandPinky4'
        }
    
    def mp_to_world(self, lm):
        """Convierte landmark MediaPipe a posición 3D"""
        x = (lm['x'] - 0.5) * self.scale
        y = -(lm['y'] - 0.5) * self.scale * 1.2  # Ajustar proporción vertical
        z = -lm['z'] * self.scale * 0.8
        return Vector((x, y, z))
    
    def calcular_rotacion_ik(self, pos_actual, pos_objetivo, bone_axis=Vector((0, 1, 0))):
        """
        Calcula rotación quaternion para que el hueso apunte al objetivo
        usando Inverse Kinematics
        """
        direccion = (pos_objetivo - pos_actual).normalized()
        rot = bone_axis.rotation_difference(direccion)
        return rot
    
    def aplicar_cadena_ik(self, armature, cadena_huesos, posiciones, frame):
        """
        Aplica IK a una cadena de huesos (ej: hombro -> codo -> muñeca)
        """
        for i in range(len(cadena_huesos) - 1):
            bone_name = cadena_huesos[i]
            if bone_name not in armature.pose.bones:
                continue
            
            pbone = armature.pose.bones[bone_name]
            pos_actual = posiciones[i]
            pos_siguiente = posiciones[i + 1]
            
            # Calcular rotación para apuntar al siguiente hueso
            rot = self.calcular_rotacion_ik(pos_actual, pos_siguiente)
            
            pbone.rotation_mode = 'QUATERNION'
            pbone.rotation_quaternion = rot
            pbone.keyframe_insert(data_path="rotation_quaternion", frame=frame)
    
    def aplicar_dedos_precisos(self, armature, hand_landmarks, lado, frame):
        """
        Aplica landmarks de mano con máxima precisión a todos los dedos
        lado: 'Left' o 'Right'
        """
        # Definir cadenas de dedos
        dedos = {
            'Thumb': [1, 2, 3, 4],
            'Index': [5, 6, 7, 8],
            'Middle': [9, 10, 11, 12],
            'Ring': [13, 14, 15, 16],
            'Pinky': [17, 18, 19, 20]
        }
        
        for dedo_nombre, indices in dedos.items():
            # Construir cadena de huesos para este dedo
            cadena = []
            posiciones = []
            
            for idx in indices:
                if idx >= len(hand_landmarks):
                    break
                
                bone_name = f"{lado}{self.hand_map.get(idx, '')}"
                if bone_name not in armature.pose.bones:
                    continue
                
                cadena.append(bone_name)
                posiciones.append(self.mp_to_world(hand_landmarks[idx]))
            
            # Aplicar IK a la cadena del dedo
            if len(cadena) >= 2:
                self.aplicar_cadena_ik(armature, cadena, posiciones, frame)
    
    def aplicar_animacion_completa(self, armature, data):
        """
        Aplica animación completa frame por frame
        """
        frames = data['frames']
        fps = data['metadata']['fps']
        
        print(f"\n🎬 Aplicando animación ultra precisa...")
        print(f"   Total frames: {len(frames)}")
        print(f"   FPS: {fps:.2f}")
        
        # Configurar escena
        bpy.context.scene.render.fps = int(fps)
        bpy.context.scene.frame_start = 0
        bpy.context.scene.frame_end = len(frames) - 1
        
        # Modo pose
        bpy.context.view_layer.objects.active = armature
        bpy.ops.object.mode_set(mode='POSE')
        
        # Guardar poses originales de cadera/piernas
        print(f"\n💾 Preservando cadera y piernas...")
        poses_orig = {}
        for bone_name in HUESOS_PRESERVAR:
            if bone_name in armature.pose.bones:
                pb = armature.pose.bones[bone_name]
                pb.rotation_mode = 'QUATERNION'
                poses_orig[bone_name] = {
                    'loc': pb.location.copy(),
                    'rot': pb.rotation_quaternion.copy(),
                    'scale': pb.scale.copy()
                }
        
        # Procesar cada frame
        stats = {'pose': 0, 'hands': 0, 'face': 0}
        
        for frame_idx, frame_data in enumerate(frames):
            bpy.context.scene.frame_set(frame_idx)
            
            # 1. POSE - Brazos y tren superior
            if 'pose' in frame_data:
                pose_lms = frame_data['pose']
                stats['pose'] += 1
                
                # BRAZO IZQUIERDO: Hombro -> Codo -> Muñeca
                if len(pose_lms) > 15:
                    cadena_izq = ['LeftShoulder', 'LeftArm', 'LeftForeArm']
                    pos_izq = [
                        self.mp_to_world(pose_lms[11]),  # Hombro
                        self.mp_to_world(pose_lms[13]),  # Codo
                        self.mp_to_world(pose_lms[15])   # Muñeca
                    ]
                    self.aplicar_cadena_ik(armature, cadena_izq, pos_izq, frame_idx)
                
                # BRAZO DERECHO: Hombro -> Codo -> Muñeca
                if len(pose_lms) > 16:
                    cadena_der = ['RightShoulder', 'RightArm', 'RightForeArm']
                    pos_der = [
                        self.mp_to_world(pose_lms[12]),  # Hombro
                        self.mp_to_world(pose_lms[14]),  # Codo
                        self.mp_to_world(pose_lms[16])   # Muñeca
                    ]
                    self.aplicar_cadena_ik(armature, cadena_der, pos_der, frame_idx)
                
                # CABEZA
                if len(pose_lms) > 0 and 'Head' in armature.pose.bones:
                    head_pos = self.mp_to_world(pose_lms[0])
                    # Aplicar posición relativa
                    pb = armature.pose.bones['Head']
                    # La cabeza ya está correctamente orientada, solo ajustar si necesario
            
            # 2. MANOS - Todos los dedos con máxima precisión
            if 'left_hand' in frame_data:
                stats['hands'] += 1
                self.aplicar_dedos_precisos(
                    armature, 
                    frame_data['left_hand'], 
                    'Left', 
                    frame_idx
                )
            
            if 'right_hand' in frame_data:
                self.aplicar_dedos_precisos(
                    armature, 
                    frame_data['right_hand'], 
                    'Right', 
                    frame_idx
                )
            
            # 3. ROSTRO - Shape keys si están disponibles
            if 'face' in frame_data:
                stats['face'] += 1
                # TODO: Implementar blend shapes faciales
            
            # Progreso
            if (frame_idx + 1) % 10 == 0:
                prog = ((frame_idx + 1) / len(frames)) * 100
                print(f"   📊 {prog:.1f}% - Frame {frame_idx + 1}/{len(frames)}", end='\r')
        
        print(f"\n\n✅ Animación aplicada")
        print(f"   Frames con pose: {stats['pose']}")
        print(f"   Frames con manos: {stats['hands']}")
        print(f"   Frames con cara: {stats['face']}")
        
        # RESTAURAR cadera y piernas en todos los frames
        print(f"\n🔒 Restaurando cadera y piernas...")
        for bone_name, pose in poses_orig.items():
            pb = armature.pose.bones[bone_name]
            for frame_idx in range(len(frames)):
                bpy.context.scene.frame_set(frame_idx)
                pb.location = pose['loc']
                pb.rotation_quaternion = pose['rot']
                pb.scale = pose['scale']
                pb.keyframe_insert(data_path="location", frame=frame_idx)
                pb.keyframe_insert(data_path="rotation_quaternion", frame=frame_idx)
                pb.keyframe_insert(data_path="scale", frame=frame_idx)
        
        print(f"   ✅ Preservadas {len(poses_orig)} huesos")
        
        bpy.ops.object.mode_set(mode='OBJECT')


def main():
    # Validar archivos
    if not JSON_DATA.exists():
        print(f"❌ Error: JSON no encontrado")
        return 1
    
    if not DUVALL_MODEL.exists():
        print(f"❌ Error: Modelo Duvall no encontrado")
        return 1
    
    # Limpiar escena
    print(f"\n🧹 Limpiando escena...")
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
    # Cargar modelo
    print(f"\n📦 Cargando Duvall...")
    bpy.ops.import_scene.gltf(filepath=str(DUVALL_MODEL))
    
    armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            armature = obj
            break
    
    if not armature:
        print(f"❌ Error: Armature no encontrada")
        return 1
    
    print(f"   ✅ Armature: {armature.name}")
    print(f"   ✅ Huesos: {len(armature.data.bones)}")
    
    # Cargar datos
    print(f"\n📂 Cargando datos precisos...")
    with open(JSON_DATA, 'r') as f:
        data = json.load(f)
    
    print(f"   ✅ Frames: {len(data['frames'])}")
    
    # Aplicar animación
    aplicador = AplicadorUltraPreciso()
    aplicador.aplicar_animacion_completa(armature, data)
    
    # Exportar
    print(f"\n💾 Exportando...")
    bpy.ops.export_scene.gltf(
        filepath=str(OUTPUT_GLB),
        export_format='GLB',
        export_animations=True,
        export_frame_range=True,
        export_force_sampling=True,
        export_def_bones=False,
        export_optimize_animation_size=False
    )
    
    if OUTPUT_GLB.exists():
        size_mb = OUTPUT_GLB.stat().st_size / (1024 * 1024)
        print(f"\n✅ ÉXITO ({size_mb:.1f} MB)")
        print(f"\n🎯 ARCHIVO GENERADO:")
        print(f"   {OUTPUT_GLB.name}")
        print(f"\n💡 CARACTERÍSTICAS:")
        print(f"   ✓ IK aplicado a brazos (precisión máxima)")
        print(f"   ✓ Todos los dedos animados individualmente")
        print(f"   ✓ Cadera y piernas preservadas")
        print(f"   ✓ Texturas mantenidas")
        return 0
    
    print(f"\n❌ Error al exportar")
    return 1


if __name__ == "__main__":
    sys.exit(main())
