"""
Script para generar animaciones faciales automáticamente para todos los GLB de Duvall
Usa Blender para leer los frames de cada GLB y genera JSON con expresiones faciales
"""

import bpy
import os
import json
from pathlib import Path

# Mapeo de palabras a expresiones faciales
WORD_TO_EXPRESSION = {
    # Emociones positivas
    'amar': 'happy',
    'feliz': 'happy',
    'alegre': 'happy',
    'contento': 'happy',
    'bienvenido': 'happy',
    'hola': 'friendly',
    'buenos dias': 'friendly',
    'buenas tardes': 'friendly',
    'buenas noches': 'friendly',
    'saludar': 'friendly',
    
    # Emociones negativas
    'triste': 'sad',
    'mal': 'sad',
    'llorar': 'sad',
    'adios': 'sad',
    'chao': 'sad',
    'cansar': 'tired',
    
    # Preguntas
    'pregunta': 'lsv_question',
    'preguntar': 'lsv_question',
    'como estas': 'lsv_question',
    'cual es tu nombre': 'lsv_question',
    'cual es tu sena': 'lsv_question',
    'que tal': 'lsv_question',
    
    # Negación
    'no': 'lsv_negation',
    'nada': 'lsv_negation',
    'nadie': 'lsv_negation',
    'ningun': 'lsv_negation',
    
    # Sorpresa/Interés
    'sorpresa': 'surprised',
    'wow': 'surprised',
    
    # Enojo
    'enojado': 'angry',
    'molesto': 'angry',
    'furioso': 'angry',
    
    # Neutral - palabras que no requieren expresión fuerte
    'el': 'neutral',
    'ella': 'neutral',
    'ellos': 'neutral',
    'ellas': 'neutral',
    'yo': 'neutral',
    'tu': 'neutral',
    'nosotros': 'neutral',
    'ustedes': 'neutral',
    'mio': 'neutral',
    'tuyo': 'neutral',
    'suyo': 'neutral',
    'nuestro': 'neutral',
}

# Presets de expresiones faciales (valores de shape keys ARKit)
EXPRESSION_PRESETS = {
    'neutral': {},  # Sin cambios
    
    'happy': {
        'mouthSmileLeft': 0.8,
        'mouthSmileRight': 0.8,
        'eyeSquintLeft': 0.3,
        'eyeSquintRight': 0.3,
        'cheekSquintLeft': 0.4,
        'cheekSquintRight': 0.4,
    },
    
    'sad': {
        'mouthFrownLeft': 0.7,
        'mouthFrownRight': 0.7,
        'browInnerUp': 0.6,
        'eyeBlinkLeft': 0.2,
        'eyeBlinkRight': 0.2,
    },
    
    'angry': {
        'browDownLeft': 0.8,
        'browDownRight': 0.8,
        'mouthPressLeft': 0.6,
        'mouthPressRight': 0.6,
        'jawForward': 0.4,
        'noseSneerLeft': 0.3,
        'noseSneerRight': 0.3,
    },
    
    'surprised': {
        'eyeWideLeft': 1.0,
        'eyeWideRight': 1.0,
        'browInnerUp': 0.8,
        'mouthOpen': 0.6,
        'jawOpen': 0.7,
    },
    
    'friendly': {
        'mouthSmileLeft': 0.5,
        'mouthSmileRight': 0.5,
        'eyeSquintLeft': 0.2,
        'eyeSquintRight': 0.2,
    },
    
    'tired': {
        'eyeBlinkLeft': 0.4,
        'eyeBlinkRight': 0.4,
        'mouthFrownLeft': 0.3,
        'mouthFrownRight': 0.3,
        'browDownLeft': 0.3,
        'browDownRight': 0.3,
    },
    
    # Expresiones específicas para LSV
    'lsv_question': {
        'browInnerUp': 0.8,
        'eyeWideLeft': 0.5,
        'eyeWideRight': 0.5,
        'mouthOpen': 0.3,
    },
    
    'lsv_negation': {
        'browDownLeft': 0.5,
        'browDownRight': 0.5,
        'mouthFrownLeft': 0.4,
        'mouthFrownRight': 0.4,
        'headShake': True,  # Nota: esto requeriría animación de cabeza
    },
    
    'lsv_affirmation': {
        'mouthSmileLeft': 0.6,
        'mouthSmileRight': 0.6,
        'headNod': True,  # Nota: esto requeriría animación de cabeza
    },
}

def get_glb_frame_count(glb_path):
    """Obtiene el número total de frames de un archivo GLB"""
    try:
        # Limpiar la escena
        bpy.ops.wm.read_homefile(use_empty=True)
        
        # Importar el GLB
        bpy.ops.import_scene.gltf(filepath=glb_path)
        
        # Buscar el objeto con animación
        frame_count = 0
        for obj in bpy.data.objects:
            if obj.animation_data and obj.animation_data.action:
                action = obj.animation_data.action
                frame_start, frame_end = action.frame_range
                frame_count = int(frame_end)
                break
        
        return frame_count if frame_count > 0 else None
        
    except Exception as e:
        print(f"Error leyendo GLB {glb_path}: {e}")
        return None

def generate_facial_animation(word_name, total_frames, expression_name='neutral'):
    """
    Genera una animación facial con interpolación suave
    
    Args:
        word_name: Nombre de la palabra/seña
        total_frames: Número total de frames de la animación
        expression_name: Nombre de la expresión facial a usar
    
    Returns:
        dict: Datos de animación en formato JSON
    """
    
    # Obtener el preset de expresión
    expression_values = EXPRESSION_PRESETS.get(expression_name, {})
    
    # Margen de 15 frames al inicio y al final
    margin = 15
    
    # Calcular rangos
    ramp_up_start = 0
    ramp_up_end = margin  # Frame 15
    
    hold_start = margin + 1  # Frame 16
    hold_end = total_frames - margin - 1  # total - 16
    
    ramp_down_start = total_frames - margin  # total - 15
    ramp_down_end = total_frames - 1
    
    # Todas las shape keys ARKit disponibles
    shape_keys = [
        'eyeBlinkLeft', 'eyeLookDownLeft', 'eyeLookInLeft', 'eyeLookOutLeft',
        'eyeLookUpLeft', 'eyeSquintLeft', 'eyeWideLeft', 'eyeBlinkRight',
        'eyeLookDownRight', 'eyeLookInRight', 'eyeLookOutRight', 'eyeLookUpRight',
        'eyeSquintRight', 'eyeWideRight', 'jawForward', 'jawLeft', 'jawRight',
        'jawOpen', 'mouthClose', 'mouthFunnel', 'mouthPucker', 'mouthLeft',
        'mouthRight', 'mouthSmileLeft', 'mouthSmileRight', 'mouthFrownLeft',
        'mouthFrownRight', 'mouthDimpleLeft', 'mouthDimpleRight', 'mouthStretchLeft',
        'mouthStretchRight', 'mouthRollLower', 'mouthRollUpper', 'mouthShrugLower',
        'mouthShrugUpper', 'mouthPressLeft', 'mouthPressRight', 'mouthLowerDownLeft',
        'mouthLowerDownRight', 'mouthUpperUpLeft', 'mouthUpperUpRight', 'browDownLeft',
        'browDownRight', 'browInnerUp', 'browOuterUpLeft', 'browOuterUpRight',
        'cheekPuff', 'cheekSquintLeft', 'cheekSquintRight', 'noseSneerLeft',
        'noseSneerRight', 'tongueOut', 'mouthOpen'
    ]
    
    # Inicializar datos de animación
    animation_data = {
        'word': word_name,
        'expression': expression_name,
        'totalFrames': total_frames,
        'fps': 30,
        'duration': total_frames / 30,
        'shapeKeys': {}
    }
    
    # Generar valores para cada shape key
    for shape_key in shape_keys:
        target_value = expression_values.get(shape_key, 0.0)
        
        # Solo añadir si el valor no es 0
        if target_value > 0:
            frames = []
            
            # Generar interpolación
            for frame in range(total_frames):
                if frame <= ramp_up_end:
                    # Rampa de subida (0 a 1)
                    progress = frame / ramp_up_end if ramp_up_end > 0 else 0
                    value = target_value * progress
                elif frame <= hold_end:
                    # Mantener valor
                    value = target_value
                else:
                    # Rampa de bajada (1 a 0)
                    progress = (ramp_down_end - frame) / (ramp_down_end - ramp_down_start) if (ramp_down_end - ramp_down_start) > 0 else 0
                    value = target_value * progress
                
                frames.append({
                    'frame': frame,
                    'value': round(value, 3)
                })
            
            animation_data['shapeKeys'][shape_key] = frames
    
    return animation_data

def process_duvall_folder():
    """Procesa todos los archivos GLB en la carpeta Duvall"""
    
    # Rutas base
    base_dir = Path(__file__).parent
    duvall_dir = base_dir / 'output' / 'glb' / 'Duvall'
    output_dir = base_dir / 'output' / 'glb' / 'Rostro'
    
    # Crear directorio de salida si no existe
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Buscar todos los GLB en Duvall (excluyendo alfabeto)
    glb_files = []
    for glb_file in duvall_dir.rglob('*.glb'):
        # Excluir alfabeto
        if 'alfabeto' in str(glb_file).lower() or 'abecedario' in str(glb_file).lower():
            continue
        glb_files.append(glb_file)
    
    print(f"Encontrados {len(glb_files)} archivos GLB")
    print("=" * 70)
    
    processed = 0
    skipped = 0
    
    for i, glb_path in enumerate(glb_files, 1):
        # Obtener nombre de la palabra desde el archivo
        filename = glb_path.stem
        # Remover prefijo "Duvall_resultado_"
        word_name = filename.replace('Duvall_resultado_', '')
        
        print(f"[{i}/{len(glb_files)}] {word_name}")
        
        # Obtener número de frames
        frame_count = get_glb_frame_count(str(glb_path))
        
        if frame_count is None or frame_count < 31:
            print(f"  ⚠️  Saltando: {frame_count} frames (mínimo 31)")
            skipped += 1
            continue
        
        # Seleccionar expresión basada en el nombre
        expression = 'neutral'  # Por defecto
        for word_key, expr in WORD_TO_EXPRESSION.items():
            if word_key in word_name.lower():
                expression = expr
                break
        
        print(f"  📊 Frames: {frame_count} | Expresión: {expression}")
        
        # Generar animación facial
        animation_data = generate_facial_animation(word_name, frame_count, expression)
        
        # Guardar JSON
        output_file = output_dir / f"{word_name}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(animation_data, f, indent=2, ensure_ascii=False)
        
        print(f"  ✅ Guardado: {output_file.name}")
        processed += 1
    
    print("=" * 70)
    print(f"✅ Procesados: {processed}")
    print(f"⚠️  Saltados: {skipped}")
    print(f"📂 Ubicación: {output_dir}")
    print("=" * 70)

if __name__ == "__main__":
    process_duvall_folder()
