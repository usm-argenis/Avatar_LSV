"""
OPCIÓN 1: Eliminar palabras SIN archivos GLB de data.json
Esto hace que se deletreen automáticamente con el alfabeto
"""

import json
from pathlib import Path

# Lista exacta de palabras SIN archivos GLB (categoría general)
palabras_sin_glb_general = [
    'aporte', 'comunidad', 'defensa', 'edad', 'especial', 'esta', 'este',
    'grado', 'importante', 'integracion', 'junto', 'jurado', 'lengua', 'lsv',
    'miembro', 'miembros', 'presentacion', 'senas', 'señas', 'social',
    'tecnologia', 'tecnologico', 'teg', 'trabajo', 'traduccion', 'venezolano'
]

# Otras palabras sin GLB (otras categorías)
otras_palabras_sin_glb = [
    'objetivo', 'computadora', 'computadoras', 'año', 'años',
    'venezuela', 'universidad',
    # Verbos extras
    'buscar', 'busca', 'buscamos', 'buscan', 'buscas',
    'integrar', 'mejorar', 'mejora', 'mejor',
    'entender', 'entiende', 'entiendes', 'entiendo',
    'facilitar', 'facilita', 'facilitamos', 'facilitan', 'facilitas', 'facilite',
    'crear', 'llamar', 'llamo', 'participar', 'existir', 'evaluar',
    'comunicacion', 'doc', 'enganar', 'inge', 'profe',
    # Pronombres
    'eres', 'soy',
    # Saludos extras
    'bienvenir', 'holiwis', 'horita', 'mañanita',
    # Plurales extras sin verificar
    'aboga', 'administradors', 'albañils', 'analistas', 'auxiliars', 'barberos',
    'carreras', 'chefs', 'cocineros', 'conductors', 'constructors', 'contadors',
    'dentistas', 'detectives', 'dibujante tecnicos', 'dibujantes', 'directors',
    'economistas', 'enfermeras', 'escritors', 'fotografos', 'gerentes',
    'informaticas', 'ingenieros', 'inspectors', 'instructors', 'interpretes',
    'jefes', 'licenciados', 'maestros', 'medicos', 'mensajeros', 'mesoneros',
    'pasantes', 'peluqueras', 'pintors', 'policias', 'profesions', 'profesors',
    'psicologos', 'secretarias', 'sistemas', 'sordas', 'sordos', 'supervisors',
    'tecnicos', 'traductors', 'vendedors', 'vigilantes',
    # Conjugaciones verbales: ir, tener
    'ir', 'va', 'vamos', 'van', 'vas', 'voy',
    'tener', 'tengo', 'tiene', 'tienes'
]

todas_palabras_eliminar = set(palabras_sin_glb_general + otras_palabras_sin_glb)

# Leer data.json
data_path = Path(__file__).parent / 'scripts' / 'data.json'
with open(data_path, 'r', encoding='utf-8') as f:
    diccionario = json.load(f)

print(f"Diccionario original: {len(diccionario)} palabras")
print()

# Crear respaldo
backup_path = data_path.parent / 'data_BACKUP_COMPLETO.json'
with open(backup_path, 'w', encoding='utf-8') as f:
    json.dump(diccionario, f, indent=2, ensure_ascii=False)
print(f"✅ Respaldo creado: {backup_path.name}")
print()

# Filtrar diccionario
diccionario_limpio = {}
eliminadas = []

for palabra, info in diccionario.items():
    if palabra in todas_palabras_eliminar:
        eliminadas.append(f"{palabra} ({info['categoria']})")
    else:
        diccionario_limpio[palabra] = info

print(f"📋 Palabras a eliminar: {len(eliminadas)}")
for p in sorted(eliminadas)[:30]:  # Mostrar primeras 30
    print(f"   - {p}")
if len(eliminadas) > 30:
    print(f"   ... y {len(eliminadas) - 30} más")

print()
print(f"Antes:  {len(diccionario)} palabras")
print(f"Ahora:  {len(diccionario_limpio)} palabras")
print(f"Eliminadas: {len(eliminadas)} palabras")
print()

# Guardar diccionario limpio
with open(data_path, 'w', encoding='utf-8') as f:
    json.dump(diccionario_limpio, f, indent=2, ensure_ascii=False)

print("✅ data.json actualizado!")
print()
print("RESULTADO: Estas palabras ahora se DELETREARÁN automáticamente")
