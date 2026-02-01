"""
Generador COMPLETO de diccionario LSV
Extrae TODAS las palabras de glosas_completas.txt automáticamente
"""
import json
import re
from pathlib import Path

# Leer archivo completo
with open('glosas_completas.txt', 'r', encoding='utf-8') as f:
    lineas = f.readlines()

diccionario = {}
categoria_actual = "general"

# Detectar categorías y palabras
for linea in lineas:
    linea = linea.strip()
    
    # Saltar líneas vacías o separadores
    if not linea or linea.startswith('='):
        continue
    
    # Detectar categorías (líneas que empiezan con ==)
    if linea.startswith('=='):
        categoria_actual = linea.replace('==', '').strip().lower()
        categoria_actual = re.sub(r'[^\w\s]', '', categoria_actual).replace(' ', '_')
        continue
    
    # Extraer palabra principal
    palabra = linea.lower()
    
    # Limpiar caracteres especiales pero mantener espacios
    palabra = re.sub(r'[^a-záéíóúñü\s]', '', palabra).strip()
    
    if not palabra:
        continue
    
    # Agregar al diccionario
    diccionario[palabra] = {
        'categoria': categoria_actual,
        'archivo': palabra
    }

# NÚMEROS 0-10
for i in range(11):
    diccionario[str(i)] = {'categoria': 'numero', 'archivo': str(i)}

# 1M
diccionario['1m'] = {'categoria': 'numero', 'archivo': '1M'}

# ALFABETO
for letra in 'abcdefghijklmnopqrstuvwxyz':
    diccionario[letra] = {'categoria': 'alfabeto', 'archivo': letra}
diccionario['ñ'] = {'categoria': 'alfabeto', 'archivo': 'ñ'}

# SINÓNIMOS - Palabras que usan la misma seña
sinonimos = {
    # Profesión/Carrera
    'carrera': 'profesion',
    'carreras': 'profesion',
    'profesiones': 'profesion',
    'trabajo': 'profesion',
    'trabajos': 'profesion',
    'ocupacion': 'profesion',
    
    # Educación
    'ingenieria': 'ingeniero',
    'ingenierias': 'ingeniero',
    'sistemas': 'sistema',
    'matematicas': 'matematica',
    'ciencias': 'ciencia',
    
    # Lugares
    'escuela': 'colegio',
    'liceo': 'colegio',
    'centro': 'centro comercial',
    'centros': 'centro comercial',
    
    # Familia (plurales)
    'padres': 'padre',
    'madres': 'madre',
    'hijos': 'hijo',
    'hermanos': 'hermano',
    'abuelos': 'abuelo',
    'tios': 'tio',
    'primos': 'primo',
    'sobrinos': 'sobrino',
    'nietos': 'nieto',
    
    # Personas (plurales)
    'niños': 'niño',
    'hombres': 'hombre',
    'mujeres': 'mujer',
    'personas': 'persona',
    'amigos': 'amigo',
    'ancianos': 'anciano',
    'jovenes': 'joven',
    'bebes': 'bebe',
    'adultos': 'adulto',
    'novios': 'novio',
    'compañeros': 'compañero',
    'señores': 'señor',
    'viejos': 'viejo',
    
    # Transporte
    'carros': 'carro',
    'autos': 'carro',
    'automovil': 'carro',
    'automoviles': 'carro',
    'autobuses': 'autobus',
    'buses': 'autobus',
    'camiones': 'camioneta',
    'motos': 'moto',
    'motocicleta': 'moto',
    'motocicletas': 'moto',
    'bicicletas': 'bicicleta',
    'bicis': 'bicicleta',
    'taxis': 'taxi',
    'trenes': 'tren',
    'metros': 'metro',
    'aviones': 'avion',
    'barcos': 'barco',
    
    # Lugares (plurales y sinónimos)
    'casas': 'casa',
    'hogares': 'casa',
    'edificios': 'edificio',
    'apartamentos': 'apartamento',
    'deptos': 'apartamento',
    'cuartos': 'cuarto',
    'habitaciones': 'cuarto',
    'baños': 'baño',
    'cocinas': 'cocina',
    'comedores': 'comedor',
    'salas': 'sala',
    'calles': 'calle',
    'avenidas': 'avenida',
    'plazas': 'plaza',
    'parques': 'parque',
    'tiendas': 'tienda',
    'comercios': 'tienda',
    'hospitales': 'hospital',
    'clinicas': 'clinica',
    'bancos': 'banco',
    'iglesias': 'iglesia catolica',
    'templos': 'iglesia catolica',
    'universidades': 'universidad',
    'colegios': 'colegio',
    'escuelas': 'colegio',
    'restaurantes': 'restaurante',
    
    # Verbos (participios y gerundios comunes)
    'comiendo': 'comer',
    'corriendo': 'correr',
    'estudiando': 'estudiar',
    'trabajando': 'trabajar',
    'viviendo': 'vivir',
    'durmiendo': 'dormir',
    'viendo': 'ver',
    'ayudando': 'ayudar',
    'amando': 'amar',
    'conociendo': 'conocer',
    'diciendo': 'decir',
    'preguntando': 'preguntar',
    'presentando': 'presentar',
    'respondiendo': 'responder',
    'saludando': 'saludar',
    'sintiendo': 'sentir',
    'queriendo': 'querer',
    
    # Expresiones comunes
    'holas': 'hola',
    'chau': 'chao',
    'adiós': 'adios',
    'buendía': 'buenos dias',
    'buen día': 'buenos dias',
    'ok': 'bien',
    'vale': 'bien',
}

# Agregar sinónimos al diccionario
for sinonimo, palabra_base in sinonimos.items():
    if palabra_base in diccionario:
        diccionario[sinonimo] = {
            'categoria': diccionario[palabra_base]['categoria'],
            'archivo': diccionario[palabra_base]['archivo']
        }
    else:
        # Si la palabra base no existe, usar como archivo
        diccionario[sinonimo] = {
            'categoria': 'general',
            'archivo': palabra_base
        }

# PALABRAS ADICIONALES IMPORTANTES
extras = {
    'yo': 'pronombres', 'tu': 'pronombres', 'el': 'pronombres',
    'ella': 'pronombres', 'nosotros': 'pronombres', 'ustedes': 'pronombres',
    'ellos': 'pronombres', 'ellas': 'pronombres',
    'mio': 'pronombres', 'tuyo': 'pronombres', 'suyo': 'pronombres',
    'nuestro': 'pronombres',
    
    'hola': 'saludos', 'adios': 'saludos', 'chao': 'saludos',
    'buenos dias': 'saludos', 'buenas tardes': 'saludos',
    'buenas noches': 'saludos', 'bienvenido': 'saludos',
    
    'gracias': 'cortesia', 'muchas gracias': 'cortesia',
    'por favor': 'cortesia', 'permiso': 'cortesia',
    'de nada': 'cortesia', 'a la orden': 'cortesia',
    'buen provecho': 'cortesia', 'mucho gusto': 'cortesia',
    
    'si': 'expresiones', 'no': 'expresiones',
    'bien': 'expresiones', 'mal': 'expresiones',
    'como': 'expresiones', 'donde': 'expresiones',
    'cuando': 'expresiones', 'que': 'expresiones',
    'quien': 'expresiones', 'cual': 'expresiones',
    'porque': 'expresiones', 'regular': 'expresiones',
    
    'deletrear': 'verbos',
    'trabajar': 'verbos', 'estudiar': 'verbos', 'comer': 'verbos',
    'vivir': 'verbos', 'dormir': 'verbos', 'ver': 'verbos',
    'estar': 'verbos', 'ser': 'verbos', 'ayudar': 'verbos',
    'amar': 'verbos', 'conocer': 'verbos', 'decir': 'verbos',
    'preguntar': 'verbos', 'presentar': 'verbos', 'responder': 'verbos',
    'saludar': 'verbos', 'sentir': 'verbos', 'querer': 'verbos',
    'invitar': 'verbos', 'cansar': 'verbos',
    
    'todo': 'preposicion', 'mucho': 'preposicion',
    'poco': 'preposicion', 'nada': 'preposicion',
    'algun': 'preposicion', 'ningun': 'preposicion',
    'otro': 'preposicion', 'bastante': 'preposicion',
}

for palabra, categoria in extras.items():
    if palabra not in diccionario:
        diccionario[palabra] = {
            'categoria': categoria,
            'archivo': palabra
        }

print(f"\n{'='*70}")
print(f"📚 DICCIONARIO COMPLETO DE LSV")
print(f"{'='*70}")
print(f"✅ Total de palabras: {len(diccionario)}")
print(f"📁 Guardando en: backend/scripts/data.json")

# Guardar
with open('backend/scripts/data.json', 'w', encoding='utf-8') as f:
    json.dump(diccionario, f, ensure_ascii=False, indent=2)

print(f"✅ Diccionario generado exitosamente!")
print(f"{'='*70}\n")

# Mostrar estadísticas por categoría
from collections import Counter
categorias = Counter([v['categoria'] for v in diccionario.values()])
print("📊 Palabras por categoría:")
for cat, count in sorted(categorias.items(), key=lambda x: -x[1])[:15]:
    print(f"   {cat}: {count}")
