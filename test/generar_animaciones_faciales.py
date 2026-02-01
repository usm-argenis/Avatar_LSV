"""
Generador automático de animaciones faciales para palabras de Lengua de Señas
Excluye alfabeto y genera JSONs con gestos apropiados
"""
import json
import os
from pathlib import Path
from pygltflib import GLTF2

# Mapeo de palabras a expresiones (basado en presets del HTML)
WORD_TO_EXPRESSION = {
    # Emociones positivas
    'amar': 'happy',
    'alegre': 'smile_big',
    'feliz': 'happy',
    'gustar': 'smile_light',
    'contento': 'content',
    'reir': 'laugh',
    
    # Emociones negativas
    'mal': 'surprised',  # Ya existe
    'triste': 'sad',
    'llorar': 'sad_crying',
    'enojado': 'angry',
    'furioso': 'angry_shouting',
    'preocupado': 'worried',
    'miedo': 'fearful',
    'nervioso': 'nervous',
    'decepcionado': 'disappointed',
    
    # Preguntas y comunicación LSV
    'pregunta': 'lsv_question',
    'por que': 'lsv_question',
    'porque': 'lsv_question',
    'como': 'lsv_question',
    'donde': 'lsv_question',
    'cuando': 'lsv_question',
    'quien': 'lsv_question',
    'cual': 'lsv_question',
    'que': 'lsv_question',
    
    # Negación
    'no': 'lsv_negation',
    'nunca': 'lsv_negation',
    'nada': 'lsv_negation',
    
    # Afirmación
    'si': 'lsv_affirmation',
    'bueno': 'lsv_affirmation',
    'ok': 'lsv_affirmation',
    'bien': 'lsv_affirmation',
    
    # Énfasis
    'muy': 'lsv_emphasis',
    'mucho': 'lsv_emphasis',
    'importante': 'lsv_emphasis',
    
    # Acciones
    'comer': 'mouth_open',
    'hablar': 'mouth_wide',
    'gritar': 'angry_shouting',
    'cantar': 'mouth_o',
    'beso': 'kiss',
    'soplar': 'blow',
    
    # Estados
    'cansado': 'tired',
    'aburrido': 'bored',
    'sorprendido': 'surprised',
    'confundido': 'confused',
    'pensando': 'thinking',
    'duda': 'lsv_doubt',
    
    # Default para palabras sin emoción específica
    'default': 'neutral'
}

# Presets de expresiones (del HTML)
EXPRESSION_PRESETS = {
    'neutral': {},
    'happy': {
        'mouthSmileLeft': 0.90,
        'mouthSmileRight': 0.90,
        'cheekSquintLeft': 0.60,
        'cheekSquintRight': 0.60,
        'eyeSquintLeft': 0.30,
        'eyeSquintRight': 0.30,
        'browInnerUp': 0.20
    },
    'sad': {
        'browInnerUp': 0.70,
        'mouthFrownLeft': 0.50,
        'mouthFrownRight': 0.50,
        'eyeSquintLeft': 0.30,
        'eyeSquintRight': 0.30,
        'mouthLowerDownLeft': 0.25,
        'mouthLowerDownRight': 0.25
    },
    'angry': {
        'browDownLeft': 0.80,
        'browDownRight': 0.80,
        'eyeSquintLeft': 0.60,
        'eyeSquintRight': 0.60,
        'mouthFrownLeft': 0.60,
        'mouthFrownRight': 0.60,
        'noseSneerLeft': 0.40,
        'noseSneerRight': 0.40,
        'jawOpen': 0.15
    },
    'surprised': {
        'eyeWideLeft': 1.00,
        'eyeWideRight': 1.00,
        'browInnerUp': 0.80,
        'browOuterUpLeft': 0.80,
        'browOuterUpRight': 0.80,
        'mouthOpen': 0.60,
        'jawOpen': 0.70
    },
    'smile_light': {
        'mouthSmileLeft': 0.40,
        'mouthSmileRight': 0.40,
        'cheekSquintLeft': 0.20,
        'cheekSquintRight': 0.20
    },
    'smile_big': {
        'mouthSmileLeft': 1.00,
        'mouthSmileRight': 1.00,
        'cheekSquintLeft': 0.80,
        'cheekSquintRight': 0.80,
        'eyeSquintLeft': 0.50,
        'eyeSquintRight': 0.50,
        'browInnerUp': 0.30,
        'mouthOpen': 0.20
    },
    'laugh': {
        'mouthSmileLeft': 1.00,
        'mouthSmileRight': 1.00,
        'cheekSquintLeft': 0.90,
        'cheekSquintRight': 0.90,
        'eyeSquintLeft': 0.70,
        'eyeSquintRight': 0.70,
        'jawOpen': 0.50,
        'browInnerUp': 0.40
    },
    'sad_crying': {
        'browInnerUp': 0.90,
        'mouthFrownLeft': 0.80,
        'mouthFrownRight': 0.80,
        'eyeSquintLeft': 0.60,
        'eyeSquintRight': 0.60,
        'mouthLowerDownLeft': 0.50,
        'mouthLowerDownRight': 0.50,
        'jawOpen': 0.30
    },
    'angry_shouting': {
        'browDownLeft': 1.00,
        'browDownRight': 1.00,
        'eyeSquintLeft': 0.80,
        'eyeSquintRight': 0.80,
        'mouthOpen': 0.80,
        'jawOpen': 0.90,
        'noseSneerLeft': 0.60,
        'noseSneerRight': 0.60,
        'mouthUpperUpLeft': 0.50,
        'mouthUpperUpRight': 0.50
    },
    'lsv_question': {
        'browInnerUp': 0.80,
        'browOuterUpLeft': 0.70,
        'browOuterUpRight': 0.70,
        'eyeWideLeft': 0.50,
        'eyeWideRight': 0.50,
        'mouthFunnel': 0.40,
        'jawOpen': 0.30
    },
    'lsv_negation': {
        'browDownLeft': 0.60,
        'browDownRight': 0.60,
        'mouthFrownLeft': 0.50,
        'mouthFrownRight': 0.50,
        'eyeSquintLeft': 0.40,
        'eyeSquintRight': 0.40,
        'noseSneerLeft': 0.30,
        'noseSneerRight': 0.30
    },
    'lsv_affirmation': {
        'mouthSmileLeft': 0.60,
        'mouthSmileRight': 0.60,
        'cheekSquintLeft': 0.30,
        'cheekSquintRight': 0.30,
        'browInnerUp': 0.30
    },
    'lsv_emphasis': {
        'eyeWideLeft': 0.60,
        'eyeWideRight': 0.60,
        'browInnerUp': 0.70,
        'mouthOpen': 0.40,
        'noseSneerLeft': 0.30,
        'noseSneerRight': 0.30
    },
    'lsv_doubt': {
        'browInnerUp': 0.50,
        'browDownLeft': 0.30,
        'eyeSquintRight': 0.40,
        'mouthPucker': 0.30,
        'mouthFrownLeft': 0.40,
        'mouthFrownRight': 0.40
    },
    'worried': {
        'browInnerUp': 0.80,
        'eyeSquintLeft': 0.30,
        'eyeSquintRight': 0.30,
        'mouthFrownLeft': 0.40,
        'mouthFrownRight': 0.40
    },
    'fearful': {
        'eyeWideLeft': 0.90,
        'eyeWideRight': 0.90,
        'browInnerUp': 0.90,
        'browOuterUpLeft': 0.70,
        'browOuterUpRight': 0.70,
        'mouthOpen': 0.60,
        'jawOpen': 0.40
    },
    'nervous': {
        'browInnerUp': 0.50,
        'eyeSquintLeft': 0.20,
        'eyeSquintRight': 0.20,
        'mouthPucker': 0.25,
        'jawOpen': 0.15
    },
    'disappointed': {
        'browInnerUp': 0.40,
        'mouthFrownLeft': 0.60,
        'mouthFrownRight': 0.60,
        'eyeSquintLeft': 0.20,
        'eyeSquintRight': 0.20
    },
    'confused': {
        'browInnerUp': 0.60,
        'browDownRight': 0.40,
        'eyeSquintLeft': 0.25,
        'eyeSquintRight': 0.25
    },
    'thinking': {
        'browInnerUp': 0.40,
        'browDownLeft': 0.30,
        'eyeSquintRight': 0.30,
        'mouthPucker': 0.30
    },
    'mouth_open': {
        'jawOpen': 0.60,
        'mouthOpen': 0.70
    },
    'mouth_wide': {
        'mouthSmileLeft': 0.40,
        'mouthSmileRight': 0.40,
        'jawOpen': 0.50
    },
    'mouth_o': {
        'mouthFunnel': 0.70,
        'jawOpen': 0.50
    },
    'kiss': {
        'mouthPucker': 0.80,
        'mouthFunnel': 0.50,
        'browInnerUp': 0.20
    },
    'blow': {
        'cheekPuff': 0.80,
        'mouthPucker': 0.60
    },
    'content': {
        'mouthSmileLeft': 0.20,
        'mouthSmileRight': 0.20,
        'cheekSquintLeft': 0.15,
        'cheekSquintRight': 0.15
    },
    'tired': {
        'eyeBlinkLeft': 0.50,
        'eyeBlinkRight': 0.50,
        'browInnerUp': 0.30,
        'mouthFrownLeft': 0.20,
        'mouthFrownRight': 0.20
    },
    'bored': {
        'eyeBlinkLeft': 0.40,
        'eyeBlinkRight': 0.40,
        'mouthFrownLeft': 0.30,
        'mouthFrownRight': 0.30
    }
}

def get_glb_frame_count(glb_path):
    """Obtener número total de frames de un archivo GLB"""
    try:
        gltf = GLTF2().load(str(glb_path))
        
        if gltf.animations and len(gltf.animations) > 0:
            anim = gltf.animations[0]
            max_time = 0
            
            for sampler_idx in range(len(anim.samplers)):
                sampler = anim.samplers[sampler_idx]
                accessor = gltf.accessors[sampler.input]
                buffer_view = gltf.bufferViews[accessor.bufferView]
                
                # Leer tiempos
                import struct
                buffer_data = gltf.buffers[buffer_view.buffer].data
                start = buffer_view.byteOffset if buffer_view.byteOffset else 0
                
                times = []
                for i in range(accessor.count):
                    offset = start + (i * 4)  # float32 = 4 bytes
                    time_val = struct.unpack('<f', buffer_data[offset:offset+4])[0]
                    times.append(time_val)
                
                if times:
                    max_time = max(max_time, max(times))
            
            # Convertir tiempo a frames (asumiendo 30 FPS)
            total_frames = int(max_time * 30) + 1
            return total_frames
    except Exception as e:
        print(f"Error leyendo GLB {glb_path}: {e}")
        return None
    
    return None

def get_expression_for_word(word_name):
    """Obtener expresión apropiada para una palabra"""
    word_lower = word_name.lower()
    
    # Buscar coincidencia exacta
    if word_lower in WORD_TO_EXPRESSION:
        return WORD_TO_EXPRESSION[word_lower]
    
    # Buscar coincidencia parcial
    for key in WORD_TO_EXPRESSION.keys():
        if key in word_lower or word_lower in key:
            return WORD_TO_EXPRESSION[key]
    
    # Default
    return 'neutral'

def interpolate_value(start, end, progress):
    """Interpolación lineal"""
    return start + (end - start) * progress

def generate_facial_animation(word_name, total_frames, fps=30):
    """Generar animación facial para una palabra"""
    
    # Calcular rangos (15 frames al inicio y 15 al final)
    margin = 15
    ramp_start = 0
    ramp_end = margin
    hold_start = margin + 1
    hold_end = total_frames - margin - 1
    down_start = total_frames - margin
    down_end = total_frames - 1
    
    # Obtener expresión
    expression_name = get_expression_for_word(word_name)
    peak_values = EXPRESSION_PRESETS.get(expression_name, {})
    
    print(f"  📝 {word_name} → {expression_name}")
    print(f"  📊 Ramp Up: 0-{ramp_end}, Hold: {hold_start}-{hold_end}, Ramp Down: {down_start}-{down_end}")
    
    # Generar frames
    frames = []
    
    for frame in range(total_frames):
        shape_keys = {}
        
        for key, peak_value in peak_values.items():
            if frame <= ramp_end:
                # Ramp Up
                progress = frame / ramp_end if ramp_end > 0 else 0
                value = interpolate_value(0, peak_value, progress)
            elif frame >= hold_start and frame <= hold_end:
                # Hold
                value = peak_value
            elif frame >= down_start:
                # Ramp Down
                progress = (frame - down_start) / (down_end - down_start + 1) if (down_end - down_start) > 0 else 0
                value = interpolate_value(peak_value, 0, progress)
            else:
                value = peak_value
            
            shape_keys[key] = round(value, 2)
        
        frames.append({
            "frame": frame,
            "time": round(frame / fps, 2),
            "shape_keys": shape_keys
        })
    
    # Crear objeto de animación
    animation = {
        "name": word_name,
        "fps": fps,
        "duration": round((total_frames - 1) / fps, 2),
        "frames": frames
    }
    
    return animation

def process_duvall_folder():
    """Procesar todos los GLB de Duvall (excepto alfabeto)"""
    
    base_path = Path(r"C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Duvall")
    output_path = Path(r"C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Rostro")
    output_path.mkdir(exist_ok=True)
    
    # Buscar todos los GLB excepto alfabeto
    glb_files = []
    for glb_file in base_path.rglob("*.glb"):
        if 'alfabeto' not in str(glb_file):
            glb_files.append(glb_file)
    
    print(f"\n{'='*80}")
    print(f"📁 Encontrados {len(glb_files)} archivos GLB en Duvall (sin alfabeto)")
    print(f"{'='*80}\n")
    
    processed = 0
    skipped = 0
    
    for glb_file in glb_files:
        word_name = glb_file.stem.replace('Duvall_resultado_', '')
        
        print(f"\n[{processed + skipped + 1}/{len(glb_files)}] {word_name}")
        
        # Obtener frames
        total_frames = get_glb_frame_count(glb_file)
        
        if not total_frames or total_frames < 31:  # Mínimo 31 frames (15+1+15)
            print(f"  ⚠️  Saltando: {total_frames} frames (mínimo 31)")
            skipped += 1
            continue
        
        print(f"  🎬 Total frames: {total_frames}")
        
        # Generar animación
        animation = generate_facial_animation(word_name, total_frames)
        
        # Guardar JSON
        output_file = output_path / f"{word_name}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(animation, f, indent=2, ensure_ascii=False)
        
        print(f"  ✅ Guardado: {output_file.name}")
        processed += 1
    
    print(f"\n{'='*80}")
    print(f"✅ Procesados: {processed}")
    print(f"⚠️  Saltados: {skipped}")
    print(f"📂 Ubicación: {output_path}")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    process_duvall_folder()
