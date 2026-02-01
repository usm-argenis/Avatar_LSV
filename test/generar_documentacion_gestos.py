"""
Script para generar documentación JSON de qué gestos faciales hace cada palabra
"""

import json
from pathlib import Path

# Cargar datos de todas las palabras
rostro_path = Path("output/glb/Rostro")
gestos_por_palabra = {}

for json_file in sorted(rostro_path.glob("*.json")):
    word = json_file.stem
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    shape_keys = list(data.get('shapeKeys', {}).keys())
    
    gestos_por_palabra[word] = {
        "expresion": data.get('expression', 'neutral'),
        "total_shape_keys": len(shape_keys),
        "shape_keys_activos": shape_keys
    }

# Agrupar por expresión
por_expresion = {}
for word, info in gestos_por_palabra.items():
    expr = info['expresion']
    if expr not in por_expresion:
        por_expresion[expr] = []
    por_expresion[expr].append(word)

# Definir qué hace cada expresión
EXPRESION_DESCRIPCION = {
    'neutral': 'Sin gestos faciales',
    'friendly': 'Sonrisa sutil (mouthSmile, eyeSquint)',
    'happy': 'Sonrisa amplia (mouthSmile alto, cheekSquint)',
    'sad': 'Tristeza (mouthFrown, browInner, eyeBlink)',
    'angry': 'Enojo (browDown, mouthPress, jawForward, noseSneer)',
    'surprised': 'Sorpresa (eyeWide, browInnerUp, jawOpen)',
    'thinking': 'Pensativo (mouthPucker, browDown leve, eyeSquint)',
    'tired': 'Cansado (eyeBlink, browDown)',
    'lsv_question': 'Pregunta LSV (browInnerUp, eyeWide)'
}

# Crear documento final
documento = {
    "resumen": {
        "total_palabras": len(gestos_por_palabra),
        "palabras_con_gestos": sum(1 for info in gestos_por_palabra.values() if info['total_shape_keys'] > 0),
        "palabras_neutrales": sum(1 for info in gestos_por_palabra.values() if info['total_shape_keys'] == 0),
        "expresiones_usadas": list(por_expresion.keys())
    },
    
    "expresiones": {
        expr: {
            "descripcion": EXPRESION_DESCRIPCION.get(expr, 'Desconocido'),
            "total_palabras": len(palabras),
            "palabras": palabras
        }
        for expr, palabras in sorted(por_expresion.items())
    },
    
    "palabras": gestos_por_palabra
}

# Guardar
output_file = Path("GESTOS_FACIALES_POR_PALABRA.json")
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(documento, f, ensure_ascii=False, indent=2)

print("✅ Documentación generada: GESTOS_FACIALES_POR_PALABRA.json")
print(f"\nRESUMEN:")
print(f"  Total palabras: {documento['resumen']['total_palabras']}")
print(f"  Con gestos: {documento['resumen']['palabras_con_gestos']}")
print(f"  Neutrales: {documento['resumen']['palabras_neutrales']}")
print(f"\nEXPRESIONES:")
for expr, info in documento['expresiones'].items():
    print(f"  {expr}: {info['total_palabras']} palabras - {info['descripcion']}")
