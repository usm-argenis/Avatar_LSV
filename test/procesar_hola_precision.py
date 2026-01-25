#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Procesador de Alta Precisión para Video Hola
Extrae coordenadas exactas y las aplica solo al tren superior de Duvall
NO modifica cadera ni piernas (preserva correcciones existentes)
"""

import cv2
import mediapipe as mp
import json
import numpy as np
from pathlib import Path
import sys

class ProcesadorHolaPrecision:
    """Procesa video con máxima precisión para tren superior"""
    
    def __init__(self):
        # Configurar MediaPipe con MÁXIMA PRECISIÓN
        self.mp_holistic = mp.solutions.holistic
        
        # CONFIGURACIÓN DE ALTA PRECISIÓN (no optimizada, sino precisa)
        self.holistic = self.mp_holistic.Holistic(
            static_image_mode=False,
            model_complexity=2,  # Modelo COMPLETO (máxima precisión)
            smooth_landmarks=True,  # Suavizado para mejor tracking
            enable_segmentation=False,
            refine_face_landmarks=True,  # REFINAR landmarks faciales
            min_detection_confidence=0.7,  # Alta confianza
            min_tracking_confidence=0.7
        )
        
        print("✅ MediaPipe configurado para MÁXIMA PRECISIÓN")
        print("   - Modelo complexity: 2 (completo)")
        print("   - Face refinement: ACTIVADO")
        print("   - Smooth landmarks: ACTIVADO")
        print("   - Confidence: 0.7+")
    
    def extraer_coordenadas_video(self, video_path, output_json):
        """
        Extrae coordenadas con máxima precisión del video
        
        Returns:
            dict: Datos completos con landmarks precisos
        """
        print(f"\n📹 Procesando video: {video_path}")
        
        cap = cv2.VideoCapture(str(video_path))
        if not cap.isOpened():
            print("❌ Error: No se pudo abrir el video")
            return None
        
        # Info del video
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        print(f"   📊 Resolución: {width}x{height}")
        print(f"   🎞️  FPS: {fps:.2f}")
        print(f"   🎬 Total frames: {total_frames}")
        
        data = {
            "metadata": {
                "video": str(video_path),
                "fps": fps,
                "total_frames": total_frames,
                "width": width,
                "height": height,
                "precision": "HIGH"
            },
            "frames": []
        }
        
        frame_count = 0
        processed = 0
        
        print(f"\n🔍 Extrayendo coordenadas con MÁXIMA PRECISIÓN...")
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            # NO REDUCIR RESOLUCIÓN - usar tamaño completo para máxima precisión
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Procesar con MediaPipe Holistic (TODO junto)
            results = self.holistic.process(frame_rgb)
            
            frame_data = {
                "frame": frame_count,
                "timestamp": frame_count / fps
            }
            
            # Extraer TODOS los landmarks con precisión
            
            # 1. POSE (33 landmarks) - TREN SUPERIOR Y BRAZOS
            if results.pose_landmarks:
                pose_landmarks = []
                for lm in results.pose_landmarks.landmark:
                    pose_landmarks.append({
                        "x": float(lm.x),
                        "y": float(lm.y),
                        "z": float(lm.z),
                        "visibility": float(lm.visibility)
                    })
                frame_data["pose"] = pose_landmarks
            
            # 2. MANOS (21 landmarks cada una) - PRECISIÓN CRÍTICA
            if results.left_hand_landmarks:
                left_hand = []
                for lm in results.left_hand_landmarks.landmark:
                    left_hand.append({
                        "x": float(lm.x),
                        "y": float(lm.y),
                        "z": float(lm.z)
                    })
                frame_data["left_hand"] = left_hand
            
            if results.right_hand_landmarks:
                right_hand = []
                for lm in results.right_hand_landmarks.landmark:
                    right_hand.append({
                        "x": float(lm.x),
                        "y": float(lm.y),
                        "z": float(lm.z)
                    })
                frame_data["right_hand"] = right_hand
            
            # 3. CARA (468 landmarks refinados) - GESTOS FACIALES
            if results.face_landmarks:
                face_landmarks = []
                for lm in results.face_landmarks.landmark:
                    face_landmarks.append({
                        "x": float(lm.x),
                        "y": float(lm.y),
                        "z": float(lm.z)
                    })
                frame_data["face"] = face_landmarks
            
            data["frames"].append(frame_data)
            processed += 1
            
            # Progreso
            if processed % 10 == 0:
                progreso = (processed / total_frames) * 100
                print(f"   📊 {progreso:.1f}% - Frame {processed}/{total_frames}", end='\r')
            
            frame_count += 1
        
        cap.release()
        
        print(f"\n\n✅ Extracción completada")
        print(f"   📊 Frames procesados: {processed}")
        
        # Guardar JSON
        print(f"\n💾 Guardando datos...")
        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        
        print(f"   ✅ Guardado en: {output_json}")
        
        return data
    
    def analizar_precision_datos(self, data):
        """Analiza la calidad y precisión de los datos extraídos"""
        print(f"\n📊 ANÁLISIS DE PRECISIÓN")
        print("=" * 80)
        
        frames_con_pose = 0
        frames_con_manos = 0
        frames_con_cara = 0
        frames_con_ambas_manos = 0
        
        for frame in data["frames"]:
            if "pose" in frame:
                frames_con_pose += 1
            if "face" in frame:
                frames_con_cara += 1
            if "left_hand" in frame or "right_hand" in frame:
                frames_con_manos += 1
            if "left_hand" in frame and "right_hand" in frame:
                frames_con_ambas_manos += 1
        
        total = len(data["frames"])
        
        print(f"Total frames: {total}")
        print(f"")
        print(f"Pose detectada:       {frames_con_pose:3d} frames ({frames_con_pose/total*100:.1f}%)")
        print(f"Cara detectada:       {frames_con_cara:3d} frames ({frames_con_cara/total*100:.1f}%)")
        print(f"Manos detectadas:     {frames_con_manos:3d} frames ({frames_con_manos/total*100:.1f}%)")
        print(f"Ambas manos:          {frames_con_ambas_manos:3d} frames ({frames_con_ambas_manos/total*100:.1f}%)")
        
        # Validar que tenemos datos suficientes
        if frames_con_pose < total * 0.9:
            print(f"\n⚠️  ADVERTENCIA: Detección de pose baja ({frames_con_pose/total*100:.1f}%)")
        if frames_con_manos < total * 0.8:
            print(f"\n⚠️  ADVERTENCIA: Detección de manos baja ({frames_con_manos/total*100:.1f}%)")
        
        if frames_con_pose > total * 0.9 and frames_con_manos > total * 0.8:
            print(f"\n✅ PRECISIÓN ALTA - Datos suficientes para aplicar al modelo")
            return True
        else:
            print(f"\n❌ PRECISIÓN INSUFICIENTE - Revisar video o iluminación")
            return False


def main():
    print("\n" + "=" * 80)
    print("EXTRACCIÓN DE ALTA PRECISIÓN - VIDEO HOLA")
    print("=" * 80)
    
    # Rutas
    BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test")
    VIDEO_PATH = BASE_DIR / "output" / "videos" / "hola.mp4"
    OUTPUT_JSON = BASE_DIR / "output" / "hola_precision.json"
    
    if not VIDEO_PATH.exists():
        print(f"❌ Error: Video no encontrado en {VIDEO_PATH}")
        return 1
    
    # Procesar
    procesador = ProcesadorHolaPrecision()
    data = procesador.extraer_coordenadas_video(VIDEO_PATH, OUTPUT_JSON)
    
    if data is None:
        return 1
    
    # Analizar precisión
    es_preciso = procesador.analizar_precision_datos(data)
    
    if es_preciso:
        print(f"\n🎯 SIGUIENTE PASO:")
        print(f"   Ejecutar: aplicar_a_duvall_precision.py")
        print(f"   Este script aplicará las coordenadas al tren superior de Duvall")
        print(f"   preservando cadera y piernas.")
        return 0
    else:
        print(f"\n⚠️  RECOMENDACIÓN:")
        print(f"   Revisar video o ajustar configuración de detección")
        return 1


if __name__ == "__main__":
    sys.exit(main())
