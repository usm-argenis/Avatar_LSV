# Script para generar diccionario JSON desde glosas_completas.txt
import json
import os

# Cambiar al directorio raíz del proyecto
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
os.chdir(project_root)

# Leer glosas
with open('glosas_completas.txt', 'r', encoding='utf-8') as f:
    contenido = f.read()

diccionario = {}

# Números 0-10
for i in range(11):
    diccionario[str(i)] = {'categoria': 'numero', 'archivo': str(i)}

# 1M
diccionario['1m'] = {'categoria': 'numero', 'archivo': '1M'}

# Alfabeto
for letra in 'abcdefghijklmnopqrstuvwxyz':
    diccionario[letra] = {'categoria': 'alfabeto', 'archivo': letra}
diccionario['ñ'] = {'categoria': 'alfabeto', 'archivo': 'ñ'}

# Lista manual de palabras importantes con sus categorías
glosas_basicas = {
    # Saludos
    'hola': 'saludos', 'adios': 'saludos', 'buenos dias': 'saludos',
    'buenas tardes': 'saludos', 'buenas noches': 'saludos',
    'bienvenido': 'saludos', 'chao': 'saludos',
    
    # Cortesía
    'gracias': 'cortesia', 'muchas gracias': 'cortesia',
    'por favor': 'cortesia', 'permiso': 'cortesia',
    'de nada': 'expresiones', 'a la orden': 'cortesia',
    'buen provecho': 'cortesia', 'mucho gusto': 'cortesia',
    
    # Verbos comunes
    'trabajar': 'verbos', 'estudiar': 'verbos', 'comer': 'verbos',
    'vivir': 'verbos', 'dormir': 'verbos', 'ver': 'verbos',
    'estar': 'verbos', 'ser': 'verbos', 'ayudar': 'verbos',
    'deletrear': 'verbos', 'amar': 'verbos', 'conocer': 'verbos',
    'decir': 'verbos', 'preguntar': 'verbos',
    
    # Personas
    'yo': 'pronombres', 'tu': 'pronombres', 'el': 'pronombres',
    'ella': 'pronombres', 'nosotros': 'pronombres',
    'ustedes': 'pronombres', 'ellos': 'pronombres',
    'mio': 'pronombres', 'tuyo': 'pronombres', 'suyo': 'pronombres',
    'nuestro': 'pronombres',
    
    # Personas
    'niño': 'personas', 'hombre': 'personas', 'mujer': 'personas',
    'persona': 'personas', 'amigo': 'personas', 'hermano': 'familia',
    'padre': 'familia', 'hijo': 'familia', 'abuelo': 'familia',
    'nieto': 'familia', 'tio': 'familia', 'primo': 'familia',
    'sobrino': 'familia', 'suegro': 'familia', 'cuñado': 'familia',
    'anciano': 'personas', 'adulto': 'personas', 'joven': 'personas',
    'bebe': 'personas', 'viejo': 'personas', 'novio': 'personas',
    'señor': 'personas', 'compañero': 'personas',
    'ciego': 'personas', 'sordo': 'personas', 'sordociego': 'personas',
    'oyente': 'personas',
    
    # Estado civil
    'casado': 'estado_civil', 'soltero': 'estado_civil',
    'divorciado': 'estado_civil', 'separado': 'estado_civil',
    'viudo': 'estado_civil', 'concubino': 'estado_civil',
    
    # Profesiones
    'maestro': 'profesion', 'profesor': 'profesion', 'medico': 'profesion',
    'ingeniero': 'profesion', 'doctor': 'profesion', 'enfermera': 'profesion',
    'abogado': 'profesion', 'contador': 'profesion', 'secretaria': 'profesion',
    
    # Tiempo
    'ayer': 'tiempo', 'hoy': 'tiempo', 'mañana': 'tiempo',
    'manana': 'tiempo',
    
    # Lugares
    'casa': 'tipos de vivienda', 'universidad': 'lugares',
    'escuela': 'lugares', 'colegio': 'lugares', 'trabajo': 'lugares',
    
    # Educación y carreras
    'sistema': 'educacion', 'sistemas': 'educacion',
    'informatica': 'educacion', 'computacion': 'educacion',
    'administracion': 'educacion', 'contaduria': 'educacion',
    'derecho': 'educacion', 'medicina': 'educacion',
    'enfermeria': 'educacion', 'educacion': 'educacion',
    'psicologia': 'educacion', 'matematica': 'educacion',
    'matematicas': 'educacion', 'fisica': 'educacion',
    'quimica': 'educacion', 'biologia': 'educacion',
    'ingenieria': 'educacion',  # IMPORTANTE: carrera, NO persona
    
    # Expresiones MUY COMUNES (prioridad alta)
    'si': 'expresiones', 'no': 'expresiones',
    'bien': 'expresiones', 'mal': 'expresiones',
    'como': 'expresiones', 'donde': 'expresiones',
    'cuando': 'expresiones', 'que': 'expresiones',
    'quien': 'expresiones', 'cual': 'expresiones',
    'porque': 'expresiones',
    
    # Preposiciones/cuantificadores
    'todo': 'preposicion', 'mucho': 'preposicion',
    'poco': 'preposicion', 'nada': 'preposicion',
    'algun': 'preposicion', 'ningun': 'preposicion',
    'otro': 'preposicion', 'bastante': 'preposicion',
}

for palabra, categoria in glosas_basicas.items():
    diccionario[palabra] = {
        'categoria': categoria,
        'archivo': palabra
    }

# Mapeos especiales: palabras que usan archivo de otra glosa
mapeos_especiales = {
    'ingenieria': 'ingeniero',  # La carrera usa la seña de ingeniero
    'sistemas': 'sistema',  # Plural usa singular
    'matematicas': 'matematica',  # Plural usa singular
}

for palabra, archivo_destino in mapeos_especiales.items():
    if palabra in diccionario:
        diccionario[palabra]['archivo'] = archivo_destino

# Guardar
with open('backend/scripts/data.json', 'w', encoding='utf-8') as f:
    json.dump(diccionario, f, ensure_ascii=False, indent=2)

print(f"✅ Diccionario generado con {len(diccionario)} entradas")
print("📁 Guardado en: backend/scripts/data.json")
