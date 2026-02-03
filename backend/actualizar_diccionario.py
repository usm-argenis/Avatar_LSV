"""
Generador AUTOMÁTICO de diccionario LSV desde carpeta Duvall
Extrae todas las palabras reales disponibles en GLBs
"""
import json
from pathlib import Path

# Ruta a la carpeta Duvall
DUVALL_PATH = Path(__file__).parent.parent / 'test' / 'output' / 'glb' / 'Duvall'

def generar_diccionario_desde_duvall():
    """
    Escanea carpeta Duvall y genera diccionario completo
    Estructura: {palabra: {categoria, archivo}}
    """
    diccionario = {}
    
    # Mapeo de nombres de carpetas a categorías
    mapeo_categorias = {
        'adverbios lugares': 'adverbios',
        'alfabeto': 'alfabeto',
        'cortesia': 'cortesia',
        'dias_semana': 'tiempo',
        'estado civil': 'estado_civil',
        'expresiones': 'expresiones',
        'medios transporte': 'transportes',
        'numero': 'numero',
        'numeros ordinales': 'ordinales',
        'personas': 'personas',
        'preguntas': 'interrogantes',
        'preposicion': 'preposiciones',
        'profesion': 'profesiones',
        'pronombres': 'pronombres',
        'saludos': 'saludos',
        'tiempo': 'tiempo',
        'tipos de vivienda': 'viviendas',
        'verbos': 'verbos'
    }
    
    # Recorrer todas las subcarpetas
    for carpeta in DUVALL_PATH.iterdir():
        if not carpeta.is_dir():
            continue
        
        categoria_original = carpeta.name
        categoria = mapeo_categorias.get(categoria_original, 'general')
        
        print(f"\n📁 Procesando: {categoria_original} → {categoria}")
        
        # Buscar todos los GLBs en la carpeta
        archivos_glb = list(carpeta.glob('*.glb'))
        
        for archivo_glb in archivos_glb:
            # Extraer nombre sin prefijo y extensión
            nombre_archivo = archivo_glb.stem  # "Duvall_resultado_hola"
            
            # Quitar prefijo "Duvall_resultado_"
            if nombre_archivo.startswith('Duvall_resultado_'):
                palabra = nombre_archivo.replace('Duvall_resultado_', '')
            else:
                palabra = nombre_archivo
            
            # Normalizar palabra
            palabra = palabra.lower().strip()
            
            # Agregar al diccionario
            diccionario[palabra] = {
                'categoria': categoria,
                'archivo': palabra  # Archivo sin prefijo
            }
            
            print(f"  ✅ {palabra} ({categoria})")
    
    print(f"\n📊 Total de palabras extraídas: {len(diccionario)}")
    
    # EXPANSIONES AUTOMÁTICAS
    print("\n🔧 Agregando expansiones automáticas...")
    
    # Sinónimos y variantes comunes
    expansiones = {}
    
    # Plurales que usan mismo signo
    for palabra in list(diccionario.keys()):
        info = diccionario[palabra]
        
        # Profesiones: singular y plural
        if info['categoria'] == 'profesiones':
            if not palabra.endswith('s'):
                plural = palabra + 's' if not palabra.endswith(('z', 's', 'x')) else palabra
                if plural != palabra and plural not in diccionario:
                    expansiones[plural] = info.copy()
                    print(f"  + {plural} → {palabra}")
        
        # Días de semana: plurales
        if info['categoria'] == 'tiempo' and palabra in ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']:
            # Los días ya terminan en s, pero agregar sin s para casos como "voy el lune"
            pass
    
    # Sinónimos específicos LSV
    sinonimos_lsv = {
        # Saludos informales
        'holi': 'hola',
        'holiwis': 'hola',
        'buenasnoches': 'buenas noches',
        'buenastardes': 'buenas tardes',
        'buenosdias': 'buenos dias',
        
        # Transportes variantes
        'bus': 'autobus',
        'buseta': 'autobus',
        'carro': 'carro',
        'auto': 'carro',
        'vehiculo': 'carro',
        
        # Profesiones variantes
        'profe': 'profesor',
        'doc': 'medico',
        'inge': 'ingeniero',
        'aboga': 'abogado',
        
        # Familia informal
        'pa': 'papa',
        'ma': 'mama',
        'tio/a': 'tio',
        'primo/a': 'primo',
        
        # Tiempos informales
        'ahorita': 'ahora',
        'horita': 'hoy',
        'mañanita': 'mañana',
    }
    
    for sinonimo, original in sinonimos_lsv.items():
        if original in diccionario and sinonimo not in diccionario:
            expansiones[sinonimo] = diccionario[original].copy()
            print(f"  + {sinonimo} → {original}")
    
    # Agregar expansiones al diccionario
    diccionario.update(expansiones)
    
    print(f"\n✅ Total final con expansiones: {len(diccionario)}")
    
    return diccionario

def guardar_diccionario(diccionario, ruta_salida):
    """Guardar diccionario en formato JSON"""
    # Ordenar por palabra
    diccionario_ordenado = dict(sorted(diccionario.items()))
    
    # Guardar
    with open(ruta_salida, 'w', encoding='utf-8') as f:
        json.dump(diccionario_ordenado, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 Diccionario guardado en: {ruta_salida}")
    
    # Estadísticas por categoría
    categorias = {}
    for palabra, info in diccionario_ordenado.items():
        cat = info['categoria']
        categorias[cat] = categorias.get(cat, 0) + 1
    
    print("\n📊 Palabras por categoría:")
    for cat, count in sorted(categorias.items()):
        print(f"  {cat}: {count}")

if __name__ == "__main__":
    print("🚀 Generando diccionario LSV desde carpeta Duvall...\n")
    
    # Generar diccionario
    diccionario = generar_diccionario_desde_duvall()
    
    # Guardar
    ruta_salida = Path(__file__).parent / 'scripts' / 'data.json'
    ruta_salida.parent.mkdir(exist_ok=True)
    guardar_diccionario(diccionario, ruta_salida)
    
    print("\n✅ ¡Diccionario generado exitosamente!")
    print(f"Total de palabras LSV: {len(diccionario)}")
