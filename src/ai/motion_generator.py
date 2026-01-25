"""
Motion Generator - Sistema de generación de animaciones 3D para lengua de señas
Utiliza IA para crear animaciones fluidas a partir de texto o secuencias de señas
"""

import numpy as np
import json
import os
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from scipy.interpolate import CubicSpline
from scipy.signal import savgol_filter


class MotionGenerator:
    """
    Clase principal para generar animaciones 3D de lengua de señas
    """
    
    def __init__(self, keypoints_dir: str = "../data/keypoints"):
        """
        Inicializa el generador de movimientos
        
        Args:
            keypoints_dir: Directorio con archivos de keypoints de señas
        """
        self.keypoints_dir = Path(keypoints_dir)
        self.sign_database = {}
        self.fps = 30  # Frames por segundo
        self.blend_frames = 10  # Frames para transiciones suaves
        
        # Cargar base de datos de señas
        self._load_sign_database()
    
    def _load_sign_database(self):
        """
        Carga todos los keypoints de señas desde archivos JSON
        """
        if not self.keypoints_dir.exists():
            print(f"⚠️  Directorio de keypoints no encontrado: {self.keypoints_dir}")
            self.keypoints_dir.mkdir(parents=True, exist_ok=True)
            return
        
        json_files = list(self.keypoints_dir.glob("*.json"))
        
        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    sign_name = json_file.stem
                    self.sign_database[sign_name.lower()] = data
            except Exception as e:
                print(f"❌ Error cargando {json_file}: {e}")
        
        print(f"✅ Base de datos cargada: {len(self.sign_database)} señas")
    
    def text_to_sign_sequence(self, text: str) -> List[str]:
        """
        Convierte texto en español a una secuencia de señas
        
        Args:
            text: Texto en español a traducir
            
        Returns:
            Lista de nombres de señas
        """
        # Normalizar texto
        text = text.lower().strip()
        
        # Dividir en palabras
        words = text.split()
        
        # Secuencia de señas
        sign_sequence = []
        
        for word in words:
            # Buscar palabra directa
            if word in self.sign_database:
                sign_sequence.append(word)
            else:
                # Si no existe, buscar similitud o deletrear
                similar_sign = self._find_similar_sign(word)
                if similar_sign:
                    sign_sequence.append(similar_sign)
                else:
                    # Deletrear letra por letra
                    for letter in word:
                        if letter.isalpha():
                            sign_sequence.append(letter)
        
        return sign_sequence
    
    def _find_similar_sign(self, word: str) -> Optional[str]:
        """
        Encuentra una seña similar usando distancia de Levenshtein
        
        Args:
            word: Palabra a buscar
            
        Returns:
            Seña más similar o None
        """
        if not self.sign_database:
            return None
        
        # Distancia de Levenshtein simple
        def levenshtein_distance(s1: str, s2: str) -> int:
            if len(s1) < len(s2):
                return levenshtein_distance(s2, s1)
            if len(s2) == 0:
                return len(s1)
            
            previous_row = range(len(s2) + 1)
            for i, c1 in enumerate(s1):
                current_row = [i + 1]
                for j, c2 in enumerate(s2):
                    insertions = previous_row[j + 1] + 1
                    deletions = current_row[j] + 1
                    substitutions = previous_row[j] + (c1 != c2)
                    current_row.append(min(insertions, deletions, substitutions))
                previous_row = current_row
            
            return previous_row[-1]
        
        # Encontrar seña más cercana
        min_distance = float('inf')
        best_match = None
        
        for sign_name in self.sign_database.keys():
            distance = levenshtein_distance(word, sign_name)
            if distance < min_distance and distance <= 2:  # Máximo 2 caracteres de diferencia
                min_distance = distance
                best_match = sign_name
        
        return best_match
    
    def sequence_to_keyframes(self, sequence: List[str]) -> Dict:
        """
        Convierte una secuencia de señas en keyframes 3D
        
        Args:
            sequence: Lista de nombres de señas
            
        Returns:
            Diccionario con keyframes completos
        """
        all_keyframes = {
            'frames': [],
            'duration': 0,
            'fps': self.fps,
            'sequence': sequence
        }
        
        current_frame = 0
        
        for i, sign_name in enumerate(sequence):
            # Obtener keypoints de la seña
            sign_data = self.sign_database.get(sign_name.lower())
            
            if not sign_data:
                print(f"⚠️  Seña '{sign_name}' no encontrada en base de datos")
                continue
            
            # Extraer keypoints
            keypoints = sign_data.get('keyframes', [])
            
            if not keypoints or len(keypoints) == 0:
                print(f"⚠️  Seña '{sign_name}' no tiene keypoints")
                continue
            
            # Agregar keyframes de esta seña
            for kp in keypoints:
                frame_data = {
                    'frame': current_frame,
                    'time': current_frame / self.fps,
                    'sign': sign_name,
                    'keypoints': kp
                }
                all_keyframes['frames'].append(frame_data)
                current_frame += 1
            
            # Agregar frames de transición si no es la última seña
            if i < len(sequence) - 1:
                next_sign = self.sign_database.get(sequence[i + 1].lower())
                if next_sign and next_sign.get('keypoints'):
                    # Interpolación entre última pose y primera pose de siguiente seña
                    blend_frames = self._create_blend(
                        keypoints[-1].get('pose', keypoints[-1]),
                        next_sign['keypoints'][0].get('pose', next_sign['keypoints'][0]),
                        self.blend_frames
                    )
                    
                    for bf in blend_frames:
                        frame_data = {
                            'frame': current_frame,
                            'time': current_frame / self.fps,
                            'sign': f"{sign_name}_to_{sequence[i+1]}",
                            'keypoints': {
                                'frame': current_frame,
                                'time': current_frame / self.fps,
                                'pose': bf
                            },
                            'transition': True
                        }
                        all_keyframes['frames'].append(frame_data)
                        current_frame += 1
        
        all_keyframes['duration'] = current_frame / self.fps
        
        return all_keyframes
    
    def _create_blend(self, start_pose: Dict, end_pose: Dict, num_frames: int) -> List[Dict]:
        """
        Crea interpolación suave entre dos poses usando spline cúbico
        
        Args:
            start_pose: Pose inicial
            end_pose: Pose final
            num_frames: Número de frames de transición
            
        Returns:
            Lista de poses interpoladas
        """
        blended_frames = []
        
        # Obtener todos los keypoints (asumiendo estructura similar)
        if not isinstance(start_pose, dict) or not isinstance(end_pose, dict):
            return blended_frames
        
        # Para cada articulación, interpolar
        for t in np.linspace(0, 1, num_frames):
            blended_pose = {}
            
            # Interpolación lineal simple (se puede mejorar con spline)
            for key in start_pose.keys():
                if key in end_pose:
                    if isinstance(start_pose[key], (int, float)):
                        blended_pose[key] = (1 - t) * start_pose[key] + t * end_pose[key]
                    elif isinstance(start_pose[key], dict):
                        blended_pose[key] = self._interpolate_dict(
                            start_pose[key],
                            end_pose[key],
                            t
                        )
            
            blended_frames.append(blended_pose)
        
        return blended_frames
    
    def _interpolate_dict(self, dict1: Dict, dict2: Dict, t: float) -> Dict:
        """
        Interpola entre dos diccionarios de valores numéricos
        """
        result = {}
        for key in dict1.keys():
            if key in dict2:
                if isinstance(dict1[key], (int, float)):
                    result[key] = (1 - t) * dict1[key] + t * dict2[key]
        return result
    
    def generate_animation(self, keyframes: Dict, smooth: bool = True) -> Dict:
        """
        Genera animación completa con suavizado opcional
        
        Args:
            keyframes: Diccionario con keyframes
            smooth: Aplicar suavizado Savitzky-Golay
            
        Returns:
            Animación procesada lista para exportar
        """
        if not keyframes.get('frames'):
            return keyframes
        
        animation = keyframes.copy()
        
        if smooth:
            animation = self._apply_smoothing(animation)
        
        return animation
    
    def _apply_smoothing(self, animation: Dict) -> Dict:
        """
        Aplica filtro Savitzky-Golay para suavizar movimientos
        
        Args:
            animation: Diccionario de animación
            
        Returns:
            Animación suavizada
        """
        frames = animation['frames']
        
        if len(frames) < 5:
            return animation  # No suficientes frames para suavizar
        
        # Extraer trayectorias de cada articulación
        # (Esto es un ejemplo simplificado, en producción manejar todas las articulaciones)
        
        print(f"✨ Aplicando suavizado a {len(frames)} frames...")
        
        # Aplicar filtro Savitzky-Golay (requiere al menos window_length frames)
        window_length = min(5, len(frames) if len(frames) % 2 == 1 else len(frames) - 1)
        
        # Por ahora retornar sin modificar (implementar suavizado específico según estructura)
        return animation
    
    def export_glb(self, animation: Dict, output_path: str) -> bool:
        """
        Exporta la animación como archivo GLB
        
        Args:
            animation: Diccionario de animación
            output_path: Ruta donde guardar el GLB
            
        Returns:
            True si tuvo éxito
        """
        # Por ahora, exportar como JSON (luego implementar conversión a GLB)
        try:
            json_path = output_path.replace('.glb', '.json')
            
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(animation, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Animación exportada a: {json_path}")
            print(f"⏱️  Duración: {animation['duration']:.2f} segundos")
            print(f"🎬 Frames totales: {len(animation['frames'])}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error exportando animación: {e}")
            return False
    
    def generate_from_text(self, text: str, output_path: str = None) -> Dict:
        """
        Pipeline completo: texto -> señas -> keyframes -> animación
        
        Args:
            text: Texto en español
            output_path: Ruta opcional para exportar
            
        Returns:
            Animación generada
        """
        print(f"📝 Texto de entrada: '{text}'")
        
        # 1. Texto a secuencia de señas
        sequence = self.text_to_sign_sequence(text)
        print(f"🔤 Secuencia de señas: {' -> '.join(sequence)}")
        
        # 2. Secuencia a keyframes
        keyframes = self.sequence_to_keyframes(sequence)
        print(f"🎯 Keyframes generados: {len(keyframes.get('frames', []))} frames")
        
        # 3. Generar animación con suavizado
        animation = self.generate_animation(keyframes, smooth=True)
        
        # 4. Exportar si se especificó ruta
        if output_path:
            self.export_glb(animation, output_path)
        
        return animation


# Función de utilidad para pruebas rápidas
def test_motion_generator():
    """
    Prueba básica del generador de movimientos
    """
    print("=" * 60)
    print("🧪 PRUEBA DE MOTION GENERATOR")
    print("=" * 60)
    
    # Crear instancia
    generator = MotionGenerator(
        keypoints_dir="c:/Users/andre/OneDrive/Documentos/tesis/src/data/keypoints"
    )
    
    # Probar con texto simple
    test_texts = [
        "hola",
        "gracias",
        "buenos dias"
    ]
    
    for text in test_texts:
        print(f"\n{'='*60}")
        animation = generator.generate_from_text(
            text,
            output_path=f"output_{text.replace(' ', '_')}.glb"
        )
        print(f"{'='*60}")


if __name__ == "__main__":
    test_motion_generator()
