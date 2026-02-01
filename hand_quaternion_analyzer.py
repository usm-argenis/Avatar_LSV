"""
SISTEMA DE ANÁLISIS DE ORIENTACIÓN DE MANOS CON CUATERNIONES
==============================================================

Procesa video de manos usando MediaPipe Hands y calcula orientaciones
de la mano completa y cada dedo como cuaterniones (qx, qy, qz, qw).

MATEMÁTICA DE CUATERNIONES:
---------------------------
1. Sistema de referencia local de la mano:
   - Origen: Muñeca (landmark 0)
   - Eje Y: Vector muñeca → nudillo dedo medio (landmark 9)
   - Eje Z: Normal al plano de la palma (producto cruz)
   - Eje X: Perpendicular a Y y Z
   
2. Conversión de matriz de rotación R a cuaternión q = (qx, qy, qz, qw):
   - Se usa la fórmula de Shepperd para estabilidad numérica
   - scipy.spatial.transform.Rotation.from_matrix() implementa esto
   
3. Para cada dedo:
   - Se calcula la rotación relativa entre segmentos consecutivos
   - Cada articulación → siguiente articulación define un eje local

LANDMARKS DE MEDIAPIPE HANDS (21 puntos):
------------------------------------------
0:  WRIST (muñeca)
1-4:   THUMB (pulgar) - CMC, MCP, IP, TIP
5-8:   INDEX (índice) - MCP, PIP, DIP, TIP
9-12:  MIDDLE (medio) - MCP, PIP, DIP, TIP
13-16: RING (anular) - MCP, PIP, DIP, TIP
17-20: PINKY (meñique) - MCP, PIP, DIP, TIP
"""

import cv2
import mediapipe as mp
import numpy as np
from scipy.spatial.transform import Rotation
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from datetime import datetime

# Configuración de MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles


class HandQuaternionAnalyzer:
    """Analiza orientación de manos usando cuaterniones."""
    
    # Definición de dedos: cada lista contiene los índices de landmarks
    FINGER_INDICES = {
        'thumb':  [0, 1, 2, 3, 4],    # Muñeca → Pulgar
        'index':  [0, 5, 6, 7, 8],    # Muñeca → Índice
        'middle': [0, 9, 10, 11, 12], # Muñeca → Medio
        'ring':   [0, 13, 14, 15, 16],# Muñeca → Anular
        'pinky':  [0, 17, 18, 19, 20] # Muñeca → Meñique
    }
    
    def __init__(self, video_path: str):
        """
        Inicializa el analizador.
        
        Args:
            video_path: Ruta al archivo de video a procesar
        """
        self.video_path = Path(video_path)
        self.results_data = []
        
        # Configurar MediaPipe Hands
        self.hands = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
            model_complexity=1  # 0=lite, 1=full
        )
        
    def calculate_hand_basis(self, landmarks: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Calcula el sistema de coordenadas local de la mano.
        
        Args:
            landmarks: Array (21, 3) con posiciones 3D de los landmarks
            
        Returns:
            rotation_matrix: Matriz 3x3 de rotación de la mano
            origin: Punto de origen (muñeca)
            
        Matemática:
        -----------
        1. Origen O = muñeca (landmark 0)
        2. Eje Y primario: vector de muñeca a nudillo medio (landmark 9)
        3. Vector auxiliar: muñeca a nudillo índice (landmark 5)
        4. Eje Z: Y × auxiliar (normal a la palma)
        5. Eje X: Y × Z (perpendicular, completa sistema derecho)
        """
        # Origen: muñeca
        origin = landmarks[0]
        
        # Eje Y: dirección muñeca → nudillo medio (9)
        y_axis = landmarks[9] - landmarks[0]
        y_axis = y_axis / (np.linalg.norm(y_axis) + 1e-8)
        
        # Vector auxiliar: muñeca → nudillo índice (5)
        aux_vector = landmarks[5] - landmarks[0]
        aux_vector = aux_vector / (np.linalg.norm(aux_vector) + 1e-8)
        
        # Eje Z: producto cruz (normal a la palma)
        z_axis = np.cross(y_axis, aux_vector)
        z_axis = z_axis / (np.linalg.norm(z_axis) + 1e-8)
        
        # Eje X: completar sistema ortogonal derecho
        x_axis = np.cross(y_axis, z_axis)
        x_axis = x_axis / (np.linalg.norm(x_axis) + 1e-8)
        
        # Construir matriz de rotación: columnas son los ejes
        rotation_matrix = np.column_stack([x_axis, y_axis, z_axis])
        
        return rotation_matrix, origin
    
    def calculate_segment_rotation(self, 
                                   point1: np.ndarray, 
                                   point2: np.ndarray,
                                   up_reference: Optional[np.ndarray] = None) -> np.ndarray:
        """
        Calcula la matriz de rotación de un segmento (hueso) entre dos puntos.
        
        Args:
            point1: Punto inicial del segmento
            point2: Punto final del segmento
            up_reference: Vector de referencia "arriba" opcional
            
        Returns:
            rotation_matrix: Matriz 3x3 de rotación del segmento
            
        Matemática:
        -----------
        El segmento define un eje principal (Y), calculamos los otros dos ejes
        perpendiculares para formar una base ortonormal.
        """
        # Eje Y: dirección del segmento
        y_axis = point2 - point1
        length = np.linalg.norm(y_axis)
        
        if length < 1e-8:
            # Segmento degenerado, retornar identidad
            return np.eye(3)
        
        y_axis = y_axis / length
        
        # Si no hay referencia "up", usar un vector perpendicular arbitrario
        if up_reference is None:
            # Encontrar un vector perpendicular
            if abs(y_axis[0]) < 0.9:
                up_reference = np.array([1.0, 0.0, 0.0])
            else:
                up_reference = np.array([0.0, 1.0, 0.0])
        
        # Eje X: perpendicular a Y y up_reference
        x_axis = np.cross(y_axis, up_reference)
        x_axis_norm = np.linalg.norm(x_axis)
        
        if x_axis_norm < 1e-8:
            # Y y up_reference son paralelos, usar otro vector
            if abs(y_axis[2]) < 0.9:
                up_reference = np.array([0.0, 0.0, 1.0])
            else:
                up_reference = np.array([1.0, 0.0, 0.0])
            x_axis = np.cross(y_axis, up_reference)
            x_axis_norm = np.linalg.norm(x_axis)
        
        x_axis = x_axis / x_axis_norm
        
        # Eje Z: perpendicular a X e Y
        z_axis = np.cross(x_axis, y_axis)
        z_axis = z_axis / (np.linalg.norm(z_axis) + 1e-8)
        
        # Construir matriz de rotación
        rotation_matrix = np.column_stack([x_axis, y_axis, z_axis])
        
        return rotation_matrix
    
    def matrix_to_quaternion(self, rotation_matrix: np.ndarray) -> List[float]:
        """
        Convierte matriz de rotación a cuaternión.
        
        Args:
            rotation_matrix: Matriz 3x3 de rotación
            
        Returns:
            [qx, qy, qz, qw]: Cuaternión normalizado
            
        Matemática:
        -----------
        Usa scipy.spatial.transform.Rotation que implementa el algoritmo
        de Shepperd para conversión estable de matriz → cuaternión.
        
        Fórmula básica (simplificada):
        qw = sqrt(1 + m00 + m11 + m22) / 2
        qx = (m21 - m12) / (4*qw)
        qy = (m02 - m20) / (4*qw)
        qz = (m10 - m01) / (4*qw)
        
        Scipy maneja casos especiales y normalización automáticamente.
        """
        # Crear objeto Rotation desde matriz
        rot = Rotation.from_matrix(rotation_matrix)
        
        # Obtener cuaternión en formato (x, y, z, w)
        quat = rot.as_quat()  # Retorna [qx, qy, qz, qw]
        
        return quat.tolist()
    
    def analyze_hand(self, landmarks_3d: np.ndarray, handedness: str) -> Dict:
        """
        Analiza una mano y calcula todas las orientaciones.
        
        Args:
            landmarks_3d: Array (21, 3) con landmarks 3D
            handedness: "Left" o "Right"
            
        Returns:
            dict con orientaciones de mano y dedos en cuaterniones
        """
        # 1. Calcular orientación global de la mano
        hand_rotation, hand_origin = self.calculate_hand_basis(landmarks_3d)
        hand_quaternion = self.matrix_to_quaternion(hand_rotation)
        
        # 2. Calcular orientaciones de cada dedo
        finger_quaternions = {}
        
        for finger_name, indices in self.FINGER_INDICES.items():
            # Para cada dedo, calcular cuaterniones entre segmentos consecutivos
            segments = []
            
            for i in range(len(indices) - 1):
                idx1, idx2 = indices[i], indices[i + 1]
                point1 = landmarks_3d[idx1]
                point2 = landmarks_3d[idx2]
                
                # Calcular rotación del segmento
                segment_rotation = self.calculate_segment_rotation(point1, point2)
                segment_quaternion = self.matrix_to_quaternion(segment_rotation)
                
                segments.append(segment_quaternion)
            
            finger_quaternions[finger_name] = segments
        
        return {
            'handedness': handedness,
            'hand': {
                'quaternion': hand_quaternion,
                'origin': hand_origin.tolist()
            },
            'fingers': finger_quaternions
        }
    
    def process_video(self, 
                      output_json: Optional[str] = None,
                      output_csv: Optional[str] = None,
                      visualize: bool = True) -> List[Dict]:
        """
        Procesa el video completo y extrae cuaterniones.
        
        Args:
            output_json: Ruta para guardar JSON (opcional)
            output_csv: Ruta para guardar CSV (opcional)
            visualize: Si mostrar video con landmarks
            
        Returns:
            Lista de dictionaries con resultados por frame
        """
        if not self.video_path.exists():
            raise FileNotFoundError(f"Video no encontrado: {self.video_path}")
        
        # Abrir video
        cap = cv2.VideoCapture(str(self.video_path))
        
        if not cap.isOpened():
            raise ValueError(f"No se pudo abrir el video: {self.video_path}")
        
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        print(f"📹 Procesando: {self.video_path.name}")
        print(f"   FPS: {fps:.2f}")
        print(f"   Total frames: {total_frames}")
        print(f"   Duración: {total_frames/fps:.2f}s")
        print()
        
        frame_number = 0
        processed_frames = 0
        
        while cap.isOpened():
            success, frame = cap.read()
            
            if not success:
                break
            
            # Convertir BGR a RGB para MediaPipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Procesar con MediaPipe
            results = self.hands.process(rgb_frame)
            
            frame_data = {
                'frame': frame_number,
                'timestamp': frame_number / fps,
                'hands': []
            }
            
            # Si se detectaron manos
            if results.multi_hand_landmarks and results.multi_handedness:
                for hand_landmarks, handedness in zip(
                    results.multi_hand_landmarks,
                    results.multi_handedness
                ):
                    # Extraer landmarks 3D
                    landmarks_3d = np.array([
                        [lm.x, lm.y, lm.z] 
                        for lm in hand_landmarks.landmark
                    ])
                    
                    # Analizar mano
                    hand_label = handedness.classification[0].label
                    hand_analysis = self.analyze_hand(landmarks_3d, hand_label)
                    
                    frame_data['hands'].append(hand_analysis)
                    
                    # Dibujar landmarks si visualizar
                    if visualize:
                        mp_drawing.draw_landmarks(
                            frame,
                            hand_landmarks,
                            mp_hands.HAND_CONNECTIONS,
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style()
                        )
                
                processed_frames += 1
            
            # Agregar a resultados
            self.results_data.append(frame_data)
            
            # Mostrar video
            if visualize:
                # Agregar información en pantalla
                cv2.putText(frame, f"Frame: {frame_number}/{total_frames}", 
                           (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.putText(frame, f"Manos: {len(frame_data['hands'])}", 
                           (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
                cv2.imshow('Hand Quaternion Analysis', frame)
                
                # Presionar 'q' para salir
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("\n⚠️  Proceso interrumpido por usuario")
                    break
            
            frame_number += 1
            
            # Progreso cada 30 frames
            if frame_number % 30 == 0:
                progress = (frame_number / total_frames) * 100
                print(f"  📊 Progreso: {progress:.1f}% ({frame_number}/{total_frames} frames)")
        
        # Limpiar
        cap.release()
        if visualize:
            cv2.destroyAllWindows()
        self.hands.close()
        
        print(f"\n✅ Procesamiento completado!")
        print(f"   Frames totales: {frame_number}")
        print(f"   Frames con manos: {processed_frames}")
        print(f"   Tasa detección: {(processed_frames/frame_number)*100:.1f}%")
        
        # Guardar resultados
        if output_json:
            self.save_json(output_json)
        
        if output_csv:
            self.save_csv(output_csv)
        
        return self.results_data
    
    def save_json(self, output_path: str):
        """Guarda resultados en formato JSON."""
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                'metadata': {
                    'video': str(self.video_path),
                    'total_frames': len(self.results_data),
                    'processed_date': datetime.now().isoformat()
                },
                'frames': self.results_data
            }, f, indent=2)
        
        file_size = output_file.stat().st_size / 1024
        print(f"\n💾 JSON guardado: {output_file}")
        print(f"   Tamaño: {file_size:.1f} KB")
    
    def save_csv(self, output_path: str):
        """
        Guarda resultados en formato CSV plano.
        
        Formato: frame, timestamp, hand_index, handedness, 
                 hand_qx, hand_qy, hand_qz, hand_qw,
                 finger_name, segment_index, seg_qx, seg_qy, seg_qz, seg_qw
        """
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        import csv
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Encabezado
            writer.writerow([
                'frame', 'timestamp', 'hand_index', 'handedness',
                'hand_qx', 'hand_qy', 'hand_qz', 'hand_qw',
                'finger', 'segment', 'seg_qx', 'seg_qy', 'seg_qz', 'seg_qw'
            ])
            
            # Datos
            for frame_data in self.results_data:
                frame_num = frame_data['frame']
                timestamp = frame_data['timestamp']
                
                if not frame_data['hands']:
                    # Frame sin manos
                    writer.writerow([frame_num, timestamp, -1, 'None', 
                                    0, 0, 0, 1,  # Cuaternión identidad
                                    'None', -1, 0, 0, 0, 1])
                    continue
                
                for hand_idx, hand_data in enumerate(frame_data['hands']):
                    handedness = hand_data['handedness']
                    hand_quat = hand_data['hand']['quaternion']
                    
                    # Una fila por cada segmento de cada dedo
                    for finger_name, segments in hand_data['fingers'].items():
                        for seg_idx, seg_quat in enumerate(segments):
                            writer.writerow([
                                frame_num, timestamp, hand_idx, handedness,
                                hand_quat[0], hand_quat[1], hand_quat[2], hand_quat[3],
                                finger_name, seg_idx,
                                seg_quat[0], seg_quat[1], seg_quat[2], seg_quat[3]
                            ])
        
        file_size = output_file.stat().st_size / 1024
        print(f"💾 CSV guardado: {output_file}")
        print(f"   Tamaño: {file_size:.1f} KB")


def main():
    """Función principal de ejemplo."""
    
    # Configuración
    video_path = r"C:\Users\andre\OneDrive\Documentos\tesis\videos\miercoles.mp4"
    output_dir = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\output\hand_analysis")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Crear analizador
    analyzer = HandQuaternionAnalyzer(video_path)
    
    # Procesar video
    results = analyzer.process_video(
        output_json=str(output_dir / "miercoles_quaternions.json"),
        output_csv=str(output_dir / "miercoles_quaternions.csv"),
        visualize=True  # Cambiar a False para procesamiento más rápido
    )
    
    # Estadísticas
    total_hands = sum(len(frame['hands']) for frame in results)
    frames_with_hands = sum(1 for frame in results if frame['hands'])
    
    print(f"\n📊 ESTADÍSTICAS FINALES:")
    print(f"   Total manos detectadas: {total_hands}")
    print(f"   Frames con manos: {frames_with_hands}/{len(results)}")
    
    # Ejemplo: Mostrar primer frame con manos
    for frame_data in results:
        if frame_data['hands']:
            print(f"\n🖐️  EJEMPLO - Frame {frame_data['frame']}:")
            hand = frame_data['hands'][0]
            print(f"   Mano: {hand['handedness']}")
            print(f"   Cuaternión mano: {hand['hand']['quaternion']}")
            print(f"   Dedo índice segmentos: {len(hand['fingers']['index'])}")
            print(f"   Primer segmento índice: {hand['fingers']['index'][0]}")
            break


if __name__ == "__main__":
    main()
