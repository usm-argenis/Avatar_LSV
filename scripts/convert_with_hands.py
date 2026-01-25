"""
Script mejorado para convertir landmarks de MediaPipe a formato SignAvatar
con TODOS los puntos de las manos incluidos.

Estructura del JSON resultante:
- 16 huesos básicos del esqueleto (pose)
- 21 puntos de mano izquierda (índices 16-36)
- 21 puntos de mano derecha (índices 37-57)
Total: 58 puntos por frame
"""

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_COORDS = PROJECT_ROOT / 'data' / 'coordenates'
TEST_OUTPUT = PROJECT_ROOT / 'test' / 'output'

VIDEOS = ['b', 'c', 'd', 'e']

# MediaPipe Hand Landmarks (21 puntos por mano)
# 0: WRIST
# 1-4: THUMB (CMC, MCP, IP, TIP)
# 5-8: INDEX (MCP, PIP, DIP, TIP)
# 9-12: MIDDLE (MCP, PIP, DIP, TIP)
# 13-16: RING (MCP, PIP, DIP, TIP)
# 17-20: PINKY (MCP, PIP, DIP, TIP)

HAND_LANDMARK_NAMES = [
    'wrist',
    'thumb_cmc', 'thumb_mcp', 'thumb_ip', 'thumb_tip',
    'index_mcp', 'index_pip', 'index_dip', 'index_tip',
    'middle_mcp', 'middle_pip', 'middle_dip', 'middle_tip',
    'ring_mcp', 'ring_pip', 'ring_dip', 'ring_tip',
    'pinky_mcp', 'pinky_pip', 'pinky_dip', 'pinky_tip'
]

def create_bone_structure_with_hands():
    """
    Crea la estructura de huesos incluyendo esqueleto base + manos completas
    
    Retorna lista de 58 huesos:
    - 0-15: Esqueleto base (16 huesos)
    - 16-36: Mano izquierda (21 landmarks)
    - 37-57: Mano derecha (21 landmarks)
    """
    bones = [
        # Esqueleto base (16 huesos) - índices 0-15
        {"name": "hips", "parent": -1, "type": "skeleton"},
        {"name": "spine", "parent": 0, "type": "skeleton"},
        {"name": "neck", "parent": 1, "type": "skeleton"},
        {"name": "head", "parent": 2, "type": "skeleton"},
        {"name": "left_shoulder", "parent": 2, "type": "skeleton"},
        {"name": "left_elbow", "parent": 4, "type": "skeleton"},
        {"name": "left_wrist", "parent": 5, "type": "skeleton"},
        {"name": "right_shoulder", "parent": 2, "type": "skeleton"},
        {"name": "right_elbow", "parent": 7, "type": "skeleton"},
        {"name": "right_wrist", "parent": 8, "type": "skeleton"},
        {"name": "left_hip", "parent": 0, "type": "skeleton"},
        {"name": "left_knee", "parent": 10, "type": "skeleton"},
        {"name": "left_ankle", "parent": 11, "type": "skeleton"},
        {"name": "right_hip", "parent": 0, "type": "skeleton"},
        {"name": "right_knee", "parent": 13, "type": "skeleton"},
        {"name": "right_ankle", "parent": 14, "type": "skeleton"}
    ]
    
    # Mano izquierda (21 landmarks) - índices 16-36
    for i, landmark_name in enumerate(HAND_LANDMARK_NAMES):
        parent_idx = 6 if i == 0 else (16 + i - 1)  # wrist conecta a left_wrist, demás en cadena
        bones.append({
            "name": f"left_hand_{landmark_name}",
            "parent": parent_idx,
            "type": "hand_left",
            "hand_index": i
        })
    
    # Mano derecha (21 landmarks) - índices 37-57
    for i, landmark_name in enumerate(HAND_LANDMARK_NAMES):
        parent_idx = 9 if i == 0 else (37 + i - 1)  # wrist conecta a right_wrist, demás en cadena
        bones.append({
            "name": f"right_hand_{landmark_name}",
            "parent": parent_idx,
            "type": "hand_right",
            "hand_index": i
        })
    
    return bones

def convert_mediapipe_to_signavatar_with_hands(coords_file, output_file):
    """
    Convierte archivo de coordenadas MediaPipe a SignAvatar con manos completas
    """
    print(f"  📂 Leyendo: {coords_file.name}")
    
    with open(coords_file, 'r') as f:
        data = json.load(f)
    
    frames_data = data.get('frames', [])
    fps = data.get('fps', 30)
    
    if not frames_data:
        print(f"  ⚠️ No hay frames en {coords_file.name}")
        return False
    
    # Crear estructura de huesos (58 total)
    bones = create_bone_structure_with_hands()
    
    signavatar_frames = []
    scale = 2.0  # Escala para coordenadas
    
    for frame_idx, frame in enumerate(frames_data):
        pose = frame.get('pose', [])
        left_hand = frame.get('left_hand', [])
        right_hand = frame.get('right_hand', [])
        
        # Construir array de 58 posiciones
        positions = []
        
        # 1. Agregar 16 posiciones del esqueleto base (pose landmarks)
        # Mapeo de MediaPipe Pose a nuestro esqueleto:
        # 0:hips(pelvis), 1:spine(mid_shoulder), 2:neck, 3:head(nose)
        # 4:left_shoulder, 5:left_elbow, 6:left_wrist
        # 7:right_shoulder, 8:right_elbow, 9:right_wrist
        # 10:left_hip, 11:left_knee, 12:left_ankle
        # 13:right_hip, 14:right_knee, 15:right_ankle
        
        if len(pose) >= 33:  # MediaPipe Pose tiene 33 landmarks
            # Extraer landmarks relevantes del pose
            skeleton_indices = [
                23,  # hips (left_hip de MediaPipe)
                11,  # spine (left_shoulder aproximado)
                0,   # neck (nose como aproximación)
                0,   # head (nose)
                11,  # left_shoulder
                13,  # left_elbow
                15,  # left_wrist
                12,  # right_shoulder
                14,  # right_elbow
                16,  # right_wrist
                23,  # left_hip
                25,  # left_knee
                27,  # left_ankle
                24,  # right_hip
                26,  # right_knee
                28   # right_ankle
            ]
            
            for idx in skeleton_indices:
                if idx < len(pose):
                    pos = pose[idx]
                    # Escalar y ajustar coordenadas
                    positions.append([
                        float(pos[0]) * scale,
                        float(pos[1]) * scale + 1.0,
                        float(pos[2]) * scale
                    ])
                else:
                    positions.append([0.0, 1.0, 0.0])
        else:
            # Si no hay pose, rellenar con valores por defecto
            positions.extend([[0.0, 1.0, 0.0]] * 16)
        
        # 2. Agregar 21 puntos de mano izquierda
        if left_hand and len(left_hand) >= 21:
            for landmark in left_hand[:21]:
                positions.append([
                    float(landmark[0]) * scale,
                    float(landmark[1]) * scale + 1.0,
                    float(landmark[2]) * scale
                ])
        else:
            # Rellenar con posiciones por defecto si no hay detección
            if len(positions) >= 7:  # Usar posición de left_wrist como base
                base_pos = positions[6]
                positions.extend([base_pos.copy() for _ in range(21)])
            else:
                positions.extend([[0.0, 1.0, 0.0]] * 21)
        
        # 3. Agregar 21 puntos de mano derecha
        if right_hand and len(right_hand) >= 21:
            for landmark in right_hand[:21]:
                positions.append([
                    float(landmark[0]) * scale,
                    float(landmark[1]) * scale + 1.0,
                    float(landmark[2]) * scale
                ])
        else:
            # Rellenar con posiciones por defecto si no hay detección
            if len(positions) >= 10:  # Usar posición de right_wrist como base
                base_pos = positions[9]
                positions.extend([base_pos.copy() for _ in range(21)])
            else:
                positions.extend([[0.0, 1.0, 0.0]] * 21)
        
        # Verificar que tenemos exactamente 58 posiciones
        if len(positions) != 58:
            print(f"  ⚠️ Frame {frame_idx}: {len(positions)} posiciones (esperado: 58)")
            # Ajustar si es necesario
            while len(positions) < 58:
                positions.append([0.0, 1.0, 0.0])
            positions = positions[:58]
        
        # Calcular tiempo del frame
        time = frame_idx / fps
        
        signavatar_frames.append({
            'time': time,
            'positions': positions
        })
    
    # Crear estructura final SignAvatar
    signavatar_data = {
        'version': '2.0',
        'description': 'SignAvatar con esqueleto completo + landmarks de manos',
        'bones': bones,
        'fps': fps,
        'total_bones': len(bones),
        'bone_groups': {
            'skeleton': list(range(0, 16)),
            'left_hand': list(range(16, 37)),
            'right_hand': list(range(37, 58))
        },
        'frames': signavatar_frames
    }
    
    # Guardar
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w') as f:
        json.dump(signavatar_data, f, indent=2)
    
    print(f"  ✅ Generado: {output_file.name}")
    print(f"     - {len(signavatar_frames)} frames")
    print(f"     - {len(bones)} huesos (16 esqueleto + 21 mano izq + 21 mano der)")
    
    return True

def main():
    print("="*70)
    print("🦴 Conversión a SignAvatar con Manos Completas")
    print("="*70)
    print("\nEstructura del JSON resultante:")
    print("  - 16 huesos del esqueleto base")
    print("  - 21 landmarks de mano izquierda")
    print("  - 21 landmarks de mano derecha")
    print("  = 58 puntos totales por frame\n")
    
    TEST_OUTPUT.mkdir(parents=True, exist_ok=True)
    
    success_count = 0
    
    for video_name in VIDEOS:
        print(f"\n{'─'*70}")
        print(f"🎬 Procesando: {video_name.upper()}")
        print(f"{'─'*70}")
        
        coords_file = DATA_COORDS / f"{video_name}.json"
        output_file = TEST_OUTPUT / f"{video_name}_signavatar.json"
        
        if not coords_file.exists():
            print(f"  ❌ No existe: {coords_file}")
            continue
        
        try:
            if convert_mediapipe_to_signavatar_with_hands(coords_file, output_file):
                success_count += 1
        except Exception as e:
            print(f"  ❌ Error: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n{'='*70}")
    print(f"✅ Conversión completada: {success_count}/{len(VIDEOS)} videos procesados")
    print(f"{'='*70}")
    
    if success_count == len(VIDEOS):
        print("\n🎉 Todos los archivos SignAvatar ahora incluyen:")
        print("   - Esqueleto completo del cuerpo")
        print("   - Todos los dedos de la mano izquierda (21 puntos)")
        print("   - Todos los dedos de la mano derecha (21 puntos)")
        print(f"\n📁 Archivos generados en: {TEST_OUTPUT}")

if __name__ == "__main__":
    main()
