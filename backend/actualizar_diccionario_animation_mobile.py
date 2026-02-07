"""
Actualizar el diccionario en animation_mobile.html con todas las palabras de data.json
incluyendo las palabras de la categoría "nuevo" y transporte
"""

import json
from pathlib import Path

# Leer data.json actual
data_path = Path(__file__).parent / 'scripts' / 'data.json'
with open(data_path, 'r', encoding='utf-8') as f:
    diccionario = json.load(f)

print(f"Palabras en data.json: {len(diccionario)}")

# Generar el código JavaScript para el diccionario
js_lines = []
js_lines.append("        const DICCIONARIO = {")
js_lines.append(f"            // Generado automaticamente desde backend/scripts/data.json ({len(diccionario)} palabras)")

# Ordenar por palabra para facilitar búsqueda
palabras_ordenadas = sorted(diccionario.items())

for palabra, info in palabras_ordenadas:
    categoria = info['categoria']
    archivo = info['archivo']
    # Escapar comillas simples en la palabra y archivo
    palabra_escaped = palabra.replace("'", "\\'")
    archivo_escaped = archivo.replace("'", "\\'")
    js_lines.append(f"            '{palabra_escaped}': {{ categoria: '{categoria}', archivo: '{archivo_escaped}' }},")

# Remover la última coma
if js_lines[-1].endswith(','):
    js_lines[-1] = js_lines[-1][:-1]

js_lines.append("        };")

# Unir todas las líneas
diccionario_js = '\n'.join(js_lines)

print("Diccionario JavaScript generado")
print(f"   Total lineas: {len(js_lines)}")
print()

# Generar mapeo actualizado de categorías incluyendo "nuevo"
mapeo_categorias_js = """        // MAPEO DE CATEGORIAS: Diccionario -> Carpetas Duvall
        // Las categorías en el diccionario no siempre coinciden con los nombres de carpetas
        const MAPEO_CATEGORIAS = {
            // Categorías que coinciden exactamente
            'alfabeto': 'alfabeto',
            'verbos': 'verbos',
            'numero': 'numero',
            'expresiones': 'expresiones',
            'cortesia': 'cortesia',
            'saludos': 'saludos',
            'personas': 'personas',
            'pronombres': 'pronombres',
            
            // Categorías que necesitan mapeo
            'ordinales': 'numeros ordinales',         // ordinales → numeros ordinales
            'profesiones': 'profesion',               // profesiones → profesion
            'adverbios': 'adverbios lugares',         // adverbios → adverbios lugares
            'viviendas': 'tipos de vivienda',         // viviendas → tipos de vivienda
            'estado_civil': 'estado civil',           // estado_civil → estado civil
            'interrogantes': 'preguntas',             // interrogantes → preguntas
            'preposiciones': 'preposicion',           // preposiciones → preposicion
            
            // Días de la semana y tiempo
            'dias_semana': 'dias_semana',
            'tiempo': 'tiempo',                       // tiempo → tiempo (pero algunos días están en dias_semana)
            
            // Lugares
            'lugares': 'lugares',
            
            // Medios de transporte (CRÍTICO: palabras faltantes)
            'transporte_aereo': 'medios transporte - aereo',
            'transporte_maritimo': 'medios transporte - maritimo',
            'transporte_terrestre': 'medios transporte - terrestre',
            
            // Categoría NUEVO - 33 glosas importantes
            'nuevo': 'nuevo',
            
            // Horario y palabras generales nuevas
            'general': 'horario'                      // general -> horario (para palabras de tiempo)
        };"""

print("RESULTADO - Copiar este codigo JavaScript:")
print("=" * 100)
print()
print(diccionario_js)
print()
print(mapeo_categorias_js)
print()
print("=" * 100)

# Mostrar estadísticas por categoría
print("\nESTADISTICAS POR CATEGORIA:")
print("=" * 100)

categorias_count = {}
for palabra, info in diccionario.items():
    cat = info['categoria']
    categorias_count[cat] = categorias_count.get(cat, 0) + 1

for cat in sorted(categorias_count.keys()):
    count = categorias_count[cat]
    print(f"   {cat:30s}: {count:3d} palabras")

print()
print(f"TOTAL: {len(diccionario)} palabras en data.json")
print()

# Verificar palabras de la categoría "nuevo" que DEBEN estar
palabras_nuevo_esperadas = [
    'abuelo', 'antes', 'correr', 'cuñado', 'dividir', 'entrar', 'familia', 'fumar',
    'habia una vez', 'hace rato', 'hermano', 'hijo', 'madre', 'madrina', 'mama',
    'multiplicar', 'nieto', 'nombre', 'padre', 'padrino', 'papa', 'permitir', 'primo',
    'prohibir', 'respetar', 'restar', 'seña', 'sobrino', 'stro', 'suegro', 'sumar', 'tio', 'viajar'
]

print("VERIFICACION - Palabras de categoria NUEVO:")
print("=" * 100)
nuevo_faltantes = []
nuevo_presentes = []

for palabra in palabras_nuevo_esperadas:
    if palabra in diccionario:
        nuevo_presentes.append(palabra)
        print(f"   OK {palabra:20s} - categoria: {diccionario[palabra]['categoria']}")
    else:
        nuevo_faltantes.append(palabra)
        print(f"   FALTA {palabra:20s}")

print()
if nuevo_faltantes:
    print(f"{len(nuevo_faltantes)} palabras de NUEVO faltan en data.json:")
    for palabra in nuevo_faltantes:
        print(f"   - {palabra}")
else:
    print("Todas las 33 palabras de categoria NUEVO estan presentes")

print()
