"""
Sistema de Comparación Video Original vs Animación GLB
Para refinar precisión de dedos en señas LSV

Flujo:
1. Analizar video original con MediaPipe Hands
2. Extraer keypoints y ángulos de dedos
3. Cargar animación GLB y extraer rotaciones de dedos
4. Comparar frame por frame
5. Generar reporte de diferencias
6. Crear correcciones para Blender

Autor: Sistema LSV
Fecha: 2025
"""

import cv2
import mediapipe as mp
import numpy as np
import json
import os
from pathlib import Path
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
from dataclasses import dataclass, asdict
from pygltflib import GLTF2


@dataclass
class HandAngles:
    """Ángulos de articulaciones de la mano"""
    # Pulgar (Thumb)
    thumb_cmc: float  # Carpometacarpal
    thumb_mcp: float  # Metacarpofalángica
    thumb_ip: float   # Interfalángica
    
    # Índice (Index)
    index_mcp: float
    index_pip: float  # Proximal interphalangeal
    index_dip: float  # Distal interphalangeal
    
    # Medio (Middle)
    middle_mcp: float
    middle_pip: float
    middle_dip: float
    
    # Anular (Ring)
    ring_mcp: float
    ring_pip: float
    ring_dip: float
    
    # Meñique (Pinky)
    pinky_mcp: float
    pinky_pip: float
    pinky_dip: float
    
    # Orientación de la palma
    palm_normal: Tuple[float, float, float]
    palm_direction: Tuple[float, float, float]


@dataclass
class FrameComparison:
    """Comparación de un frame específico"""
    frame_number: int
    timestamp: float
    video_angles: HandAngles
    glb_angles: HandAngles
    differences: Dict[str, float]
    max_difference: float
    needs_correction: bool


class MediaPipeHandAnalyzer:
    """Analiza videos con MediaPipe Hands para extraer keypoints precisos"""
    
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
    
    def calculate_angle(self, p1: np.ndarray, p2: np.ndarray, p3: np.ndarray) -> float:
        """Calcula ángulo entre tres puntos (p2 es el vértice)"""
        v1 = p1 - p2
        v2 = p3 - p2
        
        cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-6)
        angle = np.arccos(np.clip(cos_angle, -1.0, 1.0))
        return np.degrees(angle)
    
    def extract_hand_angles(self, landmarks) -> HandAngles:
        """Extrae ángulos de todas las articulaciones de la mano"""
        # Convertir landmarks a numpy array
        points = np.array([[lm.x, lm.y, lm.z] for lm in landmarks.landmark])
        
        # Índices de MediaPipe Hands
        WRIST = 0
        THUMB_CMC = 1
        THUMB_MCP = 2
        THUMB_IP = 3
        THUMB_TIP = 4
        INDEX_MCP = 5
        INDEX_PIP = 6
        INDEX_DIP = 7
        INDEX_TIP = 8
        MIDDLE_MCP = 9
        MIDDLE_PIP = 10
        MIDDLE_DIP = 11
        MIDDLE_TIP = 12
        RING_MCP = 13
        RING_PIP = 14
        RING_DIP = 15
        RING_TIP = 16
        PINKY_MCP = 17
        PINKY_PIP = 18
        PINKY_DIP = 19
        PINKY_TIP = 20
        
        # Calcular ángulos de cada articulación
        angles = HandAngles(
            # Pulgar
            thumb_cmc=self.calculate_angle(points[WRIST], points[THUMB_CMC], points[THUMB_MCP]),
            thumb_mcp=self.calculate_angle(points[THUMB_CMC], points[THUMB_MCP], points[THUMB_IP]),
            thumb_ip=self.calculate_angle(points[THUMB_MCP], points[THUMB_IP], points[THUMB_TIP]),
            
            # Índice
            index_mcp=self.calculate_angle(points[WRIST], points[INDEX_MCP], points[INDEX_PIP]),
            index_pip=self.calculate_angle(points[INDEX_MCP], points[INDEX_PIP], points[INDEX_DIP]),
            index_dip=self.calculate_angle(points[INDEX_PIP], points[INDEX_DIP], points[INDEX_TIP]),
            
            # Medio
            middle_mcp=self.calculate_angle(points[WRIST], points[MIDDLE_MCP], points[MIDDLE_PIP]),
            middle_pip=self.calculate_angle(points[MIDDLE_MCP], points[MIDDLE_PIP], points[MIDDLE_DIP]),
            middle_dip=self.calculate_angle(points[MIDDLE_PIP], points[MIDDLE_DIP], points[MIDDLE_TIP]),
            
            # Anular
            ring_mcp=self.calculate_angle(points[WRIST], points[RING_MCP], points[RING_PIP]),
            ring_pip=self.calculate_angle(points[RING_MCP], points[RING_PIP], points[RING_DIP]),
            ring_dip=self.calculate_angle(points[RING_PIP], points[RING_DIP], points[RING_TIP]),
            
            # Meñique
            pinky_mcp=self.calculate_angle(points[WRIST], points[PINKY_MCP], points[PINKY_PIP]),
            pinky_pip=self.calculate_angle(points[PINKY_MCP], points[PINKY_PIP], points[PINKY_DIP]),
            pinky_dip=self.calculate_angle(points[PINKY_PIP], points[PINKY_DIP], points[PINKY_TIP]),
            
            # Orientación de la palma
            palm_normal=self.calculate_palm_normal(points),
            palm_direction=self.calculate_palm_direction(points)
        )
        
        return angles
    
    def calculate_palm_normal(self, points: np.ndarray) -> Tuple[float, float, float]:
        """Calcula el vector normal de la palma"""
        # Usar muñeca, índice MCP y meñique MCP para definir el plano
        wrist = points[0]
        index_mcp = points[5]
        pinky_mcp = points[17]
        
        v1 = index_mcp - wrist
        v2 = pinky_mcp - wrist
        
        normal = np.cross(v1, v2)
        normal = normal / (np.linalg.norm(normal) + 1e-6)
        
        return tuple(normal)
    
    def calculate_palm_direction(self, points: np.ndarray) -> Tuple[float, float, float]:
        """Calcula la dirección hacia donde apunta la palma"""
        wrist = points[0]
        middle_mcp = points[9]
        
        direction = middle_mcp - wrist
        direction = direction / (np.linalg.norm(direction) + 1e-6)
        
        return tuple(direction)
    
    def analyze_video(self, video_path: str, output_dir: str = None) -> List[HandAngles]:
        """Analiza un video completo frame por frame"""
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        print(f"📹 Analizando: {Path(video_path).name}")
        print(f"   FPS: {fps}, Frames: {frame_count}")
        
        all_angles = []
        frame_idx = 0
        
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(
                os.path.join(output_dir, 'analyzed_' + Path(video_path).name),
                fourcc, fps, 
                (int(cap.get(3)), int(cap.get(4)))
            )
        
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break
            
            # Convertir a RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(frame_rgb)
            
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Extraer ángulos
                    angles = self.extract_hand_angles(hand_landmarks)
                    all_angles.append(angles)
                    
                    # Dibujar landmarks en el frame
                    if output_dir:
                        self.mp_drawing.draw_landmarks(
                            frame, 
                            hand_landmarks, 
                            self.mp_hands.HAND_CONNECTIONS
                        )
            
            if output_dir:
                out.write(frame)
            
            frame_idx += 1
            if frame_idx % 30 == 0:
                print(f"   Procesados {frame_idx}/{frame_count} frames...")
        
        cap.release()
        if output_dir:
            out.release()
        
        print(f"✅ Análisis completado: {len(all_angles)} frames con manos detectadas")
        return all_angles
    
    def save_angles_to_json(self, angles_list: List[HandAngles], output_path: str):
        """Guarda los ángulos en formato JSON"""
        data = {
            'frames': [asdict(angles) for angles in angles_list],
            'total_frames': len(angles_list)
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        
        print(f"💾 Guardado: {output_path}")


class GLBAnimationAnalyzer:
    """Analiza animaciones GLB para extraer rotaciones de dedos"""
    
    def __init__(self, glb_path: str):
        self.glb_path = glb_path
        self.gltf = GLTF2().load(glb_path)
        self.finger_bones = self._identify_finger_bones()
    
    def _identify_finger_bones(self) -> Dict[str, int]:
        """Identifica los índices de los huesos de los dedos en el GLB"""
        finger_mapping = {}
        
        # Nombres comunes de huesos de dedos en rigs
        finger_patterns = {
            'thumb': ['thumb', 'pulgar'],
            'index': ['index', 'indice'],
            'middle': ['middle', 'medio'],
            'ring': ['ring', 'anular'],
            'pinky': ['pinky', 'meñique', 'little']
        }
        
        for node_idx, node in enumerate(self.gltf.nodes):
            if node.name:
                name_lower = node.name.lower()
                for finger, patterns in finger_patterns.items():
                    if any(p in name_lower for p in patterns):
                        # Identificar si es MCP, PIP o DIP
                        if 'mcp' in name_lower or '1' in name_lower:
                            finger_mapping[f'{finger}_mcp'] = node_idx
                        elif 'pip' in name_lower or '2' in name_lower:
                            finger_mapping[f'{finger}_pip'] = node_idx
                        elif 'dip' in name_lower or '3' in name_lower:
                            finger_mapping[f'{finger}_dip'] = node_idx
        
        return finger_mapping
    
    def extract_rotation_angles(self, frame: int) -> HandAngles:
        """Extrae ángulos de rotación de los dedos en un frame específico"""
        # TODO: Implementar extracción de rotaciones del GLB
        # Por ahora retorna ángulos dummy
        return HandAngles(
            thumb_cmc=0, thumb_mcp=0, thumb_ip=0,
            index_mcp=0, index_pip=0, index_dip=0,
            middle_mcp=0, middle_pip=0, middle_dip=0,
            ring_mcp=0, ring_pip=0, ring_dip=0,
            pinky_mcp=0, pinky_pip=0, pinky_dip=0,
            palm_normal=(0, 0, 1),
            palm_direction=(0, 1, 0)
        )


class VideoGLBComparator:
    """Compara video original con animación GLB"""
    
    def __init__(self, video_path: str, glb_path: str):
        self.video_path = video_path
        self.glb_path = glb_path
        self.video_analyzer = MediaPipeHandAnalyzer()
        self.glb_analyzer = GLBAnimationAnalyzer(glb_path)
        
    def compare(self, threshold: float = 15.0) -> List[FrameComparison]:
        """Compara video vs GLB frame por frame"""
        print("\n" + "="*60)
        print("🔍 INICIANDO COMPARACIÓN VIDEO vs GLB")
        print("="*60)
        
        # 1. Analizar video
        print("\n[1/3] Analizando video original...")
        video_angles = self.video_analyzer.analyze_video(self.video_path)
        
        # 2. Analizar GLB
        print("\n[2/3] Analizando animación GLB...")
        glb_angles = []
        for frame_idx in range(len(video_angles)):
            angles = self.glb_analyzer.extract_rotation_angles(frame_idx)
            glb_angles.append(angles)
        
        # 3. Comparar frame por frame
        print("\n[3/3] Comparando frames...")
        comparisons = []
        
        for frame_idx, (v_angles, g_angles) in enumerate(zip(video_angles, glb_angles)):
            differences = self._calculate_differences(v_angles, g_angles)
            max_diff = max(differences.values())
            
            comparison = FrameComparison(
                frame_number=frame_idx,
                timestamp=frame_idx / 30.0,  # Asumiendo 30 FPS
                video_angles=v_angles,
                glb_angles=g_angles,
                differences=differences,
                max_difference=max_diff,
                needs_correction=max_diff > threshold
            )
            
            comparisons.append(comparison)
        
        # Estadísticas
        needs_correction = sum(1 for c in comparisons if c.needs_correction)
        print(f"\n📊 RESULTADOS:")
        print(f"   Total frames: {len(comparisons)}")
        print(f"   Requieren corrección: {needs_correction} ({needs_correction/len(comparisons)*100:.1f}%)")
        print(f"   Umbral de diferencia: {threshold}°")
        
        return comparisons
    
    def _calculate_differences(self, video_angles: HandAngles, glb_angles: HandAngles) -> Dict[str, float]:
        """Calcula diferencias angulares entre video y GLB"""
        differences = {}
        
        # Comparar cada articulación
        for field in HandAngles.__dataclass_fields__:
            if field.startswith('palm'):
                continue  # Skipeamos vectores por ahora
            
            v_angle = getattr(video_angles, field)
            g_angle = getattr(glb_angles, field)
            differences[field] = abs(v_angle - g_angle)
        
        return differences
    
    def generate_report(self, comparisons: List[FrameComparison], output_path: str):
        """Genera reporte detallado de diferencias"""
        report = {
            'video': self.video_path,
            'glb': self.glb_path,
            'total_frames': len(comparisons),
            'frames_needing_correction': sum(1 for c in comparisons if c.needs_correction),
            'average_max_difference': np.mean([c.max_difference for c in comparisons]),
            'frames': []
        }
        
        for comp in comparisons:
            if comp.needs_correction:
                report['frames'].append({
                    'frame': comp.frame_number,
                    'timestamp': comp.timestamp,
                    'max_difference': comp.max_difference,
                    'differences': comp.differences
                })
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        print(f"📄 Reporte guardado: {output_path}")
    
    def visualize_differences(self, comparisons: List[FrameComparison], output_path: str):
        """Genera gráficos de visualización de diferencias"""
        fig, axes = plt.subplots(3, 1, figsize=(12, 10))
        
        frames = [c.frame_number for c in comparisons]
        max_diffs = [c.max_difference for c in comparisons]
        
        # Gráfico 1: Diferencia máxima por frame
        axes[0].plot(frames, max_diffs, linewidth=2)
        axes[0].axhline(y=15, color='r', linestyle='--', label='Umbral')
        axes[0].set_title('Diferencia Máxima por Frame')
        axes[0].set_xlabel('Frame')
        axes[0].set_ylabel('Diferencia Angular (°)')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # Gráfico 2: Heatmap de dedos más problemáticos
        finger_errors = {
            'Pulgar': [],
            'Índice': [],
            'Medio': [],
            'Anular': [],
            'Meñique': []
        }
        
        for comp in comparisons:
            finger_errors['Pulgar'].append(np.mean([
                comp.differences.get('thumb_cmc', 0),
                comp.differences.get('thumb_mcp', 0),
                comp.differences.get('thumb_ip', 0)
            ]))
            finger_errors['Índice'].append(np.mean([
                comp.differences.get('index_mcp', 0),
                comp.differences.get('index_pip', 0),
                comp.differences.get('index_dip', 0)
            ]))
            finger_errors['Medio'].append(np.mean([
                comp.differences.get('middle_mcp', 0),
                comp.differences.get('middle_pip', 0),
                comp.differences.get('middle_dip', 0)
            ]))
            finger_errors['Anular'].append(np.mean([
                comp.differences.get('ring_mcp', 0),
                comp.differences.get('ring_pip', 0),
                comp.differences.get('ring_dip', 0)
            ]))
            finger_errors['Meñique'].append(np.mean([
                comp.differences.get('pinky_mcp', 0),
                comp.differences.get('pinky_pip', 0),
                comp.differences.get('pinky_dip', 0)
            ]))
        
        for finger, errors in finger_errors.items():
            axes[1].plot(frames, errors, label=finger, linewidth=2)
        
        axes[1].set_title('Error Promedio por Dedo')
        axes[1].set_xlabel('Frame')
        axes[1].set_ylabel('Error Angular Promedio (°)')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
        
        # Gráfico 3: Barras de error promedio total por dedo
        avg_errors = {k: np.mean(v) for k, v in finger_errors.items()}
        axes[2].bar(avg_errors.keys(), avg_errors.values(), color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8'])
        axes[2].set_title('Error Promedio Total por Dedo')
        axes[2].set_ylabel('Error Angular Promedio (°)')
        axes[2].grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        plt.savefig(output_path, dpi=300)
        print(f"📊 Visualización guardada: {output_path}")


def main():
    """Función principal para ejecutar el comparador"""
    # Configuración
    BASE_DIR = Path(__file__).parent.parent
    VIDEO_DIR = BASE_DIR / "test" / "output" / "videos"
    GLB_DIR = BASE_DIR / "test" / "output" / "glb" / "Nancy" / "cortesia"
    OUTPUT_DIR = BASE_DIR / "test" / "output" / "comparisons"
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    # Ejemplo: Comparar "gracias"
    video_path = VIDEO_DIR / "gracias.mp4"
    glb_path = GLB_DIR / "Nancy_resultado_gracias.glb"
    
    if not video_path.exists():
        print(f"❌ Video no encontrado: {video_path}")
        return
    
    if not glb_path.exists():
        print(f"❌ GLB no encontrado: {glb_path}")
        return
    
    # Crear comparador
    comparator = VideoGLBComparator(str(video_path), str(glb_path))
    
    # Ejecutar comparación
    comparisons = comparator.compare(threshold=15.0)
    
    # Generar reporte
    report_path = OUTPUT_DIR / "gracias_comparison_report.json"
    comparator.generate_report(comparisons, str(report_path))
    
    # Generar visualización
    viz_path = OUTPUT_DIR / "gracias_comparison_viz.png"
    comparator.visualize_differences(comparisons, str(viz_path))
    
    print("\n✅ Análisis completado!")
    print(f"📁 Resultados en: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
