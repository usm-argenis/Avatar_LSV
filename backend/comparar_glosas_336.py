"""
Comparar las 336 glosas de glosas_duvall_completas.txt con data.json
"""

import json
from pathlib import Path

# Leer diccionario actual
data_path = Path(__file__).parent / 'scripts' / 'data.json'
with open(data_path, 'r', encoding='utf-8') as f:
    diccionario = json.load(f)

print(f"📚 Diccionario actual: {len(diccionario)} palabras")
print()

# Las 336 glosas base del archivo glosas_duvall_completas.txt
glosas_base_336 = {
    # ADVERBIOS LUGARES (9)
    'adverbios', 'al lado', 'atras', 'cerca', 'derecha', 'frente', 'izquierda', 'lejos', 'lugares',
    
    # ALFABETO (27)
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    
    # CORTESIA (7)
    'a la orden', 'buen provecho', 'cortesia', 'gracias', 'muchas gracias', 'mucho gusto', 'permiso',
    
    # DIAS SEMANA (7)
    'domingo', 'jueves', 'lunes', 'martes', 'miercoles', 'sabado', 'viernes',
    
    # ESTADO CIVIL (6)
    'casado', 'concubino', 'divorciado', 'separado', 'soltero', 'viudo',
    
    # EXPRESIONES (30)
    'abril', 'agosto', 'bien', 'como', 'cual', 'cuando', 'cuantos', 'de nada', 'diciembre', 
    'donde', 'donde (especifico)', 'enero', 'expresiones', 'febrero', 'interrogantes', 
    'julio', 'junio', 'mal', 'marzo', 'mayo', 'no', 'noviembre', 'octubre', 'porque', 
    'que', 'quien', 'regular', 'saludas a', 'septiembre', 'si',
    
    # HORARIO (8)
    'en punto', 'hora', 'horario', 'media hora', 'un cuarto', 'un minuto', 'un segundo', 'una hora',
    
    # MEDIOS TRANSPORTE - AEREO (8)
    'aeropuerto', 'aterrizar', 'avion', 'avioneta', 'boleto', 'despegar', 'helicoptero', 'piloto',
    
    # MEDIOS TRANSPORTE - MARITIMO (4)
    'barco', 'canoa', 'ferri', 'lancha',
    
    # MEDIOS TRANSPORTE - TERRESTRE (13)
    'autobus', 'bicicleta', 'cabletren', 'camioneta', 'carro', 'estacion', 'ferrocarril', 
    'metro', 'metrobus', 'moto', 'parada', 'taxi', 'tren',
    
    # NUEVO (33)
    'abuelo', 'antes', 'correr', 'cuñado', 'dividir', 'entrar', 'familia', 'fumar', 
    'habia una vez', 'hace rato', 'hermano', 'hijo', 'madre', 'madrina', 'mama', 
    'multiplicar', 'nieto', 'nombre', 'padre', 'padrino', 'papa', 'permitir', 'primo', 
    'prohibir', 'respetar', 'restar', 'seña', 'sobrino', 'stro', 'suegro', 'sumar', 'tio', 'viajar',
    
    # NUMEROS (12)
    '0', '1', '1m', '2', '3', '4', '5', '6', '7', '8', '9', '10',
    
    # NUMEROS ORDINALES (10)
    '1_o', '2_o', '3_o', '4_o', '5_o', '6_o', '7_o', '8_o', '9_o', '10_o',
    
    # PERSONAS (22)
    'adulto', 'amigo', 'anciano', 'bebe', 'ciego', 'compañero', 'hombre', 'joven', 'mayor', 
    'mayor de edad', 'menor de edad', 'mujer', 'niño', 'novio', 'oyente', 'persona', 
    'personas', 'señor', 'señorita', 'sordo', 'sordociego', 'viejo',
    
    # PREGUNTAS (4)
    'como estas', 'cual es tu nombre', 'cual es tu seña', 'que tal',
    
    # PREPOSICION (15)
    'algo', 'alguien', 'algun', 'bastante', 'cualquier', 'demasiado', 'mas', 'mucho', 
    'nada', 'nadie', 'ningun', 'otro', 'poco', 'quienquiera', 'todo',
    
    # PROFESION (47)
    'abogado', 'administrador', 'albañil', 'analista', 'auxiliar', 'barbero', 'carrera', 
    'chef', 'cocinero', 'conductor', 'constructor', 'contador', 'dentista', 'detective', 
    'dibujante', 'dibujante tecnico', 'director', 'economista', 'enfermera', 'escritor', 
    'fotografo', 'gerente', 'informatica', 'ingeniero', 'inspector', 'instructor', 'interprete', 
    'jefe', 'licenciado', 'maestro', 'medico', 'mensajero', 'mesonero', 'pasante', 'peluquera', 
    'pintor', 'policia', 'profesion', 'profesor', 'psicologo', 'secretaria', 'sistema', 
    'supervisor', 'tecnico', 'traductor', 'vendedor', 'vigilante',
    
    # PRONOMBRES (12)
    'el', 'ella', 'ellas', 'ellos', 'mio', 'nosotros', 'nuestro', 'suyo', 'tu', 'tuyo', 'ustedes', 'yo',
    
    # SALUDOS (7)
    'adios', 'bienvenido', 'buenas noches', 'buenas tardes', 'buenos dias', 'chao', 'hola',
    
    # TIEMPO (10)
    'anteayer', 'ayer', 'calendario', 'dia', 'fin de semana', 'hoy', 'mañana', 'mes', 
    'pasado mañana', 'semana',
    
    # TIPOS DE VIVIENDA (10)
    'apartamento', 'baño', 'casa', 'cocina', 'comedor', 'cuarto', 'edificio', 'piso', 'rancho', 'sala',
    
    # VERBOS (35)
    'agarrar', 'amar', 'atraer', 'ayudar', 'burlar', 'calmar', 'cansar', 'comer', 'conocer', 
    'decir', 'deletrear', 'dormir', 'engañar', 'estar', 'estudiar', 'guardar', 'invitar', 
    'llevar', 'pelear', 'preguntar', 'presentar', 'querer', 'regalar', 'responder', 'saludar', 
    'sentir', 'ser', 'sufrir', 'trabajar', 'traer', 'usar', 'ver', 'verbo', 'vestir', 'vivir',
}

print(f"🎯 Glosas base (archivo): {len(glosas_base_336)} glosas")
print()

# Encontrar glosas que faltan en el diccionario
glosas_faltantes = []
for glosa in sorted(glosas_base_336):
    if glosa not in diccionario:
        glosas_faltantes.append(glosa)

# Encontrar palabras en el diccionario que NO están en las 336 glosas base
palabras_extra = []
for palabra in sorted(diccionario.keys()):
    if palabra not in glosas_base_336:
        palabras_extra.append(palabra)

# RESULTADOS
print("=" * 80)
print("📊 ANÁLISIS DE COMPARACIÓN")
print("=" * 80)
print()

if glosas_faltantes:
    print(f"❌ GLOSAS FALTANTES EN EL DICCIONARIO ({len(glosas_faltantes)}):")
    print("=" * 80)
    for i, glosa in enumerate(glosas_faltantes, 1):
        print(f"   {i:3d}. {glosa}")
    print()
else:
    print("✅ Todas las 336 glosas base están en el diccionario!")
    print()

print("=" * 80)
print(f"➕ PALABRAS EXTRA EN EL DICCIONARIO ({len(palabras_extra)}):")
print("=" * 80)
print("(Estas son palabras agregadas para mejorar el sistema, como variantes,")
print(" conjugaciones, plurales, tecnología, etc.)")
print()
for i, palabra in enumerate(palabras_extra[:30], 1):  # Mostrar solo las primeras 30
    print(f"   {i:3d}. {palabra}")

if len(palabras_extra) > 30:
    print(f"   ... y {len(palabras_extra) - 30} más")

print()
print("=" * 80)
print("📈 RESUMEN:")
print("=" * 80)
print(f"   Glosas base (archivo):        {len(glosas_base_336)}")
print(f"   Palabras en diccionario:      {len(diccionario)}")
print(f"   Glosas faltantes:             {len(glosas_faltantes)}")
print(f"   Palabras extra (mejoras):     {len(palabras_extra)}")
print()

if len(glosas_faltantes) > 0:
    print("⚠️  ACCIÓN REQUERIDA: Agregar las glosas faltantes al diccionario")
else:
    print("✅ El diccionario contiene todas las 336 glosas base")
