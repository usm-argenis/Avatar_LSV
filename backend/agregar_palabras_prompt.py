"""
Agregar palabras críticas del prompt al diccionario LSV
"""
import json
from pathlib import Path

# Ruta el diccionario
DICT_PATH = Path(__file__).parent / 'scripts' / 'data.json'

# Cargar diccionario actual
with open(DICT_PATH, 'r', encoding='utf-8') as f:
    diccionario = json.load(f)

print(f"📚 Diccionario actual: {len(diccionario)} palabras\n")

# Palabras críticas del prompt que necesitamos agregar
nuevas_palabras = {
    # Saludos/inicio
    'bienvenir': {
        'categoria': 'saludos',
        'archivo': 'bienvenido'  # usar archivo existente si está disponible
    },
    
    # Palabras académicas
    'objetivo': {
        'categoria': 'educacion',
        'archivo': 'objetivo'
    },
    'crear': {
        'categoria': 'verbos',
        'archivo': 'crear'
    },
    
    # Lengua de señas
    'lengua': {
        'categoria': 'general',
        'archivo': 'lengua'
    },
    'señas': {
        'categoria': 'general',
        'archivo': 'señas'
    },
    'senas': {  # variante sin tilde
        'categoria': 'general',
        'archivo': 'señas'
    },
    
    # Comunicación
    'comunicacion': {
        'categoria': 'verbos',
        'archivo': 'comunicacion'
    },
    
    # Personas
    'persona': {
        'categoria': 'personas',
        'archivo': 'persona'
    },
    'personas': {
        'categoria': 'personas',
       'archivo': 'persona'  # mismo archivo, plural se maneja en normalizacion
    },
    
    # Ubicación social
    'social': {
        'categoria': 'general',
        'archivo': 'social'
    },
    'integracion': {
        'categoria': 'verbos',
        'archivo': 'integrar'
    },
    'participar': {
        'categoria': 'verbos',
        'archivo': 'participar'
    },
    'junto': {
        'categoria': 'general',
        'archivo': 'junto'
    },
    
    # Verbos de acción
    'buscar': {
        'categoria': 'verbos',
       'archivo': 'buscar'
    },
    'mejorar': {
        'categoria': 'verbos',
        'archivo': 'mejorar'
    },
    'existir': {
        'categoria': 'verbos',
        'archivo': 'existir'
    },
    
    # Importante/especial
    'importante': {
        'categoria': 'general',
        'archivo': 'importante'
    },
    
    # Este/demostrativos
    'este': {
        'categoria': 'general',
        'archivo': 'este'
    },
    'esta': {
        'categoria': 'general',
        'archivo': 'este'
    },
}

# Agregar solo las que no existen
agregadas = 0
ya_existen = 0

for palabra, info in nuevas_palabras.items():
    if palabra not in diccionario:
        diccionario[palabra] = info
        print(f"✅ Agregada: {palabra} → {info['categoria']}/{info['archivo']}")
        agregadas += 1
    else:
        print(f"⏭️  Ya existe: {palabra}")
        ya_existen += 1

print(f"\n{'='*80}")
print(f"📊 RESUMEN:")
print(f"   Palabras agregadas: {agregadas}")
print(f"   Ya existían: {ya_existen}")
print(f"   Total en diccionario: {len(diccionario)} palabras")
print(f"{'='*80}\n")

# Guardar diccionario actualizado
with open(DICT_PATH, 'w', encoding='utf-8') as f:
    json.dump(diccionario, f, ensure_ascii=False, indent=2)

print(f"💾 Diccionario guardado en: {DICT_PATH}")
