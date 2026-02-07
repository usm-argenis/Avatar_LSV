"""
Actualizar animation_mobile.html con el diccionario completo desde data.json
"""

import json
import re
from pathlib import Path

# Leer data.json
data_path = Path(__file__).parent / 'scripts' / 'data.json'
with open(data_path, 'r', encoding='utf-8') as f:
    diccionario = json.load(f)

print(f"Palabras en data.json: {len(diccionario)}")

# Generar el código JavaScript del diccionario
js_lines = []
js_lines.append("        const DICCIONARIO = {")
js_lines.append(f"            // Generado automaticamente desde backend/scripts/data.json ({len(diccionario)} palabras)")

# Ordenar por palabra
palabras_ordenadas = sorted(diccionario.items())

for palabra, info in palabras_ordenadas:
    categoria = info['categoria']
    archivo = info['archivo']
    palabra_escaped = palabra.replace("'", "\\'").replace("\\", "\\\\")
    archivo_escaped = archivo.replace("'", "\\'").replace("\\", "\\\\")
    js_lines.append(f"            '{palabra_escaped}': {{ categoria: '{categoria}', archivo: '{archivo_escaped}' }},")

# Remover última coma
if js_lines[-1].endswith(','):
    js_lines[-1] = js_lines[-1][:-1]

js_lines.append("        };")

diccionario_js = '\n'.join(js_lines)

# Leer animation_mobile.html
html_path = Path(__file__).parent.parent / 'animation_mobile.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

print(f"Leyendo {html_path}")

# Buscar y reemplazar el diccionario usando regex
# Patrón: desde "const DICCIONARIO = {" hasta el "};", antes del comentario MAPEO
pattern = r'const DICCIONARIO = \{[^}]*?// 📌[^\}]*?\};'

# Reemplazo
replacement = diccionario_js

# Verificar si encontró el patrón
if re.search(pattern, html_content, re.DOTALL):
    html_actualizado = re.sub(pattern, replacement, html_content, flags=re.DOTALL)
    print("Diccionario encontrado y reemplazado")
else:
    print("ERROR: No se encontro el diccionario en el HTML")
    print("Buscando patron alternativo...")
    # Patrón alternativo más simple
    pattern2 = r'(const DICCIONARIO = \{).*?(\n\s+\};)'
    if re.search(pattern2, html_content, re.DOTALL):
        html_actualizado = re.sub(pattern2, replacement, html_content, flags=re.DOTALL)
        print("Diccionario encontrado con patron alternativo y reemplazado")
    else:
        print("ERROR: Patron no encontrado")
        exit(1)

# Guardar el archivo actualizado
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_actualizado)

print(f"Archivo actualizado: {html_path}")
print(f"Diccionario actualizado: {len(diccionario)} palabras")
print()

# También actualizar el MAPEO_CATEGORIAS para incluir las nuevas categorías
mapeo_actualizado = """        // MAPEO DE CATEGORIAS: Diccionario -> Carpetas Duvall
        // Las categorias en el diccionario no siempre coinciden con los nombres de carpetas
        const MAPEO_CATEGORIAS = {
            // Categorias que coinciden exactamente
            'alfabeto': 'alfabeto',
            'verbos': 'verbos',
            'numero': 'numero',
            'expresiones': 'expresiones',
            'cortesia': 'cortesia',
            'saludos': 'saludos',
            'personas': 'personas',
            'pronombres': 'pronombres',
            
            // Categorias que necesitan mapeo
            'ordinales': 'numeros ordinales',         // ordinales -> numeros ordinales
            'profesiones': 'profesion',               // profesiones -> profesion
            'adverbios': 'adverbios lugares',         // adverbios -> adverbios lugares
            'viviendas': 'tipos de vivienda',         // viviendas -> tipos de vivienda
            'estado_civil': 'estado civil',           // estado_civil -> estado civil
            'interrogantes': 'preguntas',             // interrogantes -> preguntas
            'preposiciones': 'preposicion',           // preposiciones -> preposicion
            
            // Dias de la semana y tiempo
            'dias_semana': 'dias_semana',
            'tiempo': 'tiempo',                       // tiempo -> tiempo
            
            // Lugares
            'lugares': 'lugares',
            
            // Medios de transporte (CRITICO: palabras faltantes)
            'transporte_aereo': 'medios transporte - aereo',
            'transporte_maritimo': 'medios transporte - maritimo',
            'transporte_terrestre': 'medios transporte - terrestre',
            
            // Categoria FAMILIA (antes NUEVO) - palabras de familia
            'familia': 'nuevo',
            
            // Tecnologia
            'tecnologia': 'horario',
            
            // Sustantivos y educacion
            'sustantivos': 'nuevo',
            'educacion': 'nuevo',
            
            // Horario y palabras generales nuevas
            'general': 'horario'                      // general -> horario (para palabras de tiempo)
        };"""

print("MAPEO DE CATEGORIAS ACTUALIZADO:")
print(mapeo_actualizado)
print()
print("Actualizacion completada exitosamente!")
