"""
Script de validación de la animación de manos corregida
"""
import json
import math

def validate_hand_animation():
    """Valida que la animación de manos tenga movimientos coherentes"""
    
    # Cargar los landmarks originales
    with open('temp_hands_data.json', 'r') as f:
        data = json.load(f)
    
    landmarks = data['frames']
    total_frames = len(landmarks)
    
    print("\n" + "="*70)
    print("📊 VALIDACIÓN DE ANIMACIÓN DE MANOS")
    print("="*70)
    print(f"Total de frames: {total_frames}\n")
    
    # Analizar movimiento de cada dedo
    fingers = {
        'thumb': [1, 2, 3, 4],
        'index': [5, 6, 7, 8],
        'middle': [9, 10, 11, 12],
        'ring': [13, 14, 15, 16],
        'pinky': [17, 18, 19, 20]
    }
    
    for hand in ['left_hand', 'right_hand']:
        print(f"\n🤚 {hand.upper()}:")
        print("-" * 70)
        
        for finger_name, indices in fingers.items():
            movements = []
            
            # Calcular movimiento total de cada articulación
            for idx in indices:
                total_movement = 0
                prev_pos = None
                
                for frame in landmarks:
                    if frame[hand]:
                        current_pos = frame[hand][idx]
                        if prev_pos:
                            # Distancia euclidiana entre frames
                            dist = math.sqrt(
                                (current_pos['x'] - prev_pos['x'])**2 +
                                (current_pos['y'] - prev_pos['y'])**2 +
                                (current_pos['z'] - prev_pos['z'])**2
                            )
                            total_movement += dist
                        prev_pos = current_pos
                
                movements.append(total_movement)
            
            # Calcular promedio y varianza
            if movements:
                avg_movement = sum(movements) / len(movements)
                max_movement = max(movements)
                min_movement = min(movements)
                
                print(f"  {finger_name:8s}: Promedio={avg_movement:.4f}, "
                      f"Max={max_movement:.4f}, Min={min_movement:.4f}")
                
                # Validar que no haya movimientos excesivos
                if max_movement > 1.0:
                    print(f"    ⚠️  ADVERTENCIA: Movimiento excesivo detectado")
                elif avg_movement < 0.001:
                    print(f"    ⚠️  ADVERTENCIA: Movimiento muy bajo, posible congelamiento")
                else:
                    print(f"    ✅ Movimiento dentro de rangos normales")
    
    print("\n" + "="*70)
    print("✅ VALIDACIÓN COMPLETADA")
    print("="*70)

if __name__ == "__main__":
    validate_hand_animation()
