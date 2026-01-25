#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filtrador de Palabras LSV
Limpia y filtra palabras extraídas del PDF para obtener vocabulario LSV válido
"""

import re
from pathlib import Path

def es_palabra_valida(palabra):
    """
    Determina si una palabra es válida para el vocabulario LSV
    
    Criterios:
    - Solo letras (sin números puros)
    - Mínimo 3 caracteres (excepto algunas excepciones)
    - No contiene texto largo explicativo
    - Puede tener letras con tildes
    """
    # Ignorar palabras muy cortas (excepto algunas útiles)
    excepciones_cortas = {'yo', 'tú', 'él', 'mi', 'tu', 'su', 'un', 'la', 'el', 'lo', 'te', 'me', 'se', 'no', 'si', 'or', 'ir', 'vi'}
    
    if len(palabra) < 3 and palabra not in excepciones_cortas:
        return False
    
    # Ignorar palabras muy largas (probablemente son frases)
    if len(palabra) > 30:
        return False
    
    # Ignorar números puros
    if palabra.isdigit():
        return False
    
    # Ignorar si tiene muchos números mezclados
    num_digits = sum(c.isdigit() for c in palabra)
    if num_digits > 2:
        return False
    
    # Ignorar palabras con caracteres especiales inusuales
    if any(c in palabra for c in ['@', '#', '$', '%', '&', '*', '(', ')', '[', ']', '{', '}', '=', '+', '<', '>']):
        return False
    
    # Debe tener al menos 2 letras
    num_letters = sum(c.isalpha() for c in palabra)
    if num_letters < 2:
        return False
    
    # Ignorar palabras que son solo fragmentos (ej: "aba", "ado", "ción" sin contexto)
    fragmentos_invalidos = {'aba', 'ado', 'ado', 'ción', 'mente', 'ente', 'ales', 'acia', 'ivo'}
    if palabra in fragmentos_invalidos:
        return False
    
    # Ignorar si contiene espacios (son frases, no palabras)
    if ' ' in palabra and len(palabra.split()) > 4:
        return False
    
    return True

def categorizar_palabra(palabra):
    """
    Categoriza la palabra según su tipo
    """
    # Pronombres personales
    pronombres = {'yo', 'tú', 'él', 'ella', 'nosotros', 'nosotras', 'ustedes', 'ellos', 'ellas', 
                  'mi', 'tu', 'su', 'nuestro', 'nuestra'}
    
    # Palabras interrogativas
    interrogativas = {'qué', 'quién', 'cómo', 'cuándo', 'dónde', 'por qué', 'cuál', 'cuánto', 'cuánta'}
    
    # Verbos comunes
    verbos_comunes = {'ser', 'estar', 'tener', 'hacer', 'ir', 'venir', 'comer', 'beber', 'dormir', 
                     'trabajar', 'estudiar', 'vivir', 'amar', 'querer', 'poder', 'deber', 'saber'}
    
    # Familia
    familia = {'mamá', 'papá', 'madre', 'padre', 'hermano', 'hermana', 'hijo', 'hija', 
               'abuelo', 'abuela', 'tío', 'tía', 'primo', 'prima', 'esposo', 'esposa'}
    
    # Números y tiempo
    tiempo = {'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 
              'septiembre', 'octubre', 'noviembre', 'diciembre', 'lunes', 'martes', 'miércoles', 
              'jueves', 'viernes', 'sábado', 'domingo', 'hoy', 'ayer', 'mañana'}
    
    palabra_lower = palabra.lower()
    
    if palabra_lower in pronombres:
        return 'pronombre'
    elif palabra_lower in interrogativas:
        return 'interrogativa'
    elif palabra_lower in verbos_comunes:
        return 'verbo'
    elif palabra_lower in familia:
        return 'familia'
    elif palabra_lower in tiempo:
        return 'tiempo'
    else:
        return 'sustantivo/otro'

def filtrar_palabras_lsv():
    """
    Lee el archivo de palabras extraídas y filtra para obtener vocabulario válido
    """
    print("=" * 60)
    print("     🧹 FILTRADOR DE PALABRAS LSV")
    print("=" * 60)
    
    # Rutas
    base_path = Path(__file__).parent.parent
    input_file = base_path / "data" / "palabras_lsv_curso_basico.txt"
    output_file = base_path / "data" / "palabras_lsv_filtradas.txt"
    output_code = base_path / "data" / "codigo_palabras_lsv_filtradas.py"
    
    print(f"\n📂 Leyendo: {input_file}")
    
    # Leer palabras originales
    with open(input_file, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
    
    # Filtrar palabras
    palabras_validas = set()
    palabras_por_categoria = {
        'pronombre': set(),
        'interrogativa': set(),
        'verbo': set(),
        'familia': set(),
        'tiempo': set(),
        'sustantivo/otro': set()
    }
    
    for linea in lineas:
        palabra = linea.strip()
        
        # Ignorar comentarios y líneas vacías
        if not palabra or palabra.startswith('#'):
            continue
        
        # Normalizar
        palabra = palabra.lower()
        
        # Validar
        if es_palabra_valida(palabra):
            palabras_validas.add(palabra)
            categoria = categorizar_palabra(palabra)
            palabras_por_categoria[categoria].add(palabra)
    
    print(f"\n📊 Palabras filtradas: {len(palabras_validas)}")
    print("\n📋 Por categorías:")
    for categoria, palabras in sorted(palabras_por_categoria.items()):
        print(f"  - {categoria.title()}: {len(palabras)}")
    
    # Guardar palabras filtradas
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Palabras LSV filtradas del Curso Básico 1\n")
        f.write(f"# Total: {len(palabras_validas)} palabras\n\n")
        
        for categoria, palabras in sorted(palabras_por_categoria.items()):
            if palabras:
                f.write(f"\n# {categoria.upper()}\n")
                for palabra in sorted(palabras):
                    f.write(f"{palabra}\n")
    
    print(f"\n✅ Palabras guardadas en: {output_file}")
    
    # Generar código Python
    with open(output_code, 'w', encoding='utf-8') as f:
        f.write("# Código para agregar a lsv_optimizer.py\n")
        f.write("# Palabras filtradas del Curso LSV Básico 1\n\n")
        f.write(f"# Total: {len(palabras_validas)} palabras LSV\n\n")
        f.write("SENAS_CURSO_BASICO = {\n")
        
        for palabra in sorted(palabras_validas):
            f.write(f"    '{palabra}',\n")
        
        f.write("}\n\n")
        f.write("# Para integrar en lsv_optimizer.py:\n")
        f.write("# 1. Copiar el set SENAS_CURSO_BASICO\n")
        f.write("# 2. En __init__(), agregar: self.senas_disponibles.update(SENAS_CURSO_BASICO)\n")
    
    print(f"✅ Código Python generado en: {output_code}")
    
    # Mostrar algunas palabras de ejemplo
    print("\n📝 Ejemplos de palabras válidas (primeras 30):")
    for i, palabra in enumerate(sorted(palabras_validas)[:30], 1):
        categoria = categorizar_palabra(palabra)
        print(f"  {i:2d}. {palabra:20s} ({categoria})")
    
    if len(palabras_validas) > 30:
        print(f"  ... y {len(palabras_validas) - 30} más")
    
    print("\n" + "=" * 60)
    print("     ✅ FILTRADO COMPLETADO")
    print("=" * 60)
    print(f"\nArchivos generados:")
    print(f"  1. {output_file}")
    print(f"  2. {output_code}")
    print(f"\nPróximo paso: Revisar palabras filtradas y agregar a lsv_optimizer.py")

if __name__ == "__main__":
    filtrar_palabras_lsv()
