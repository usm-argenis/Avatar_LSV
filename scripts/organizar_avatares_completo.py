"""
Script para organizar avatares y aplicar animaciones de Nina a otros modelos 3D
Pasos:
1. Organizar Nina con la misma estructura que Remy
2. Analizar huesos de cada avatar (Duvall, Luis, Nancy)
3. Aplicar animaciones de Nina a cada avatar
4. Generar archivos GLB finales
"""

import os
import shutil
import json
from pathlib import Path

# Rutas base
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis")
GLB_DIR = BASE_DIR / "test" / "output" / "glb"

# Categorías exactas de Remy
CATEGORIAS = [
    "alfabeto",
    "cortesia", 
    "dias_semana",
    "expresiones",
    "preguntas",
    "pronombres",
    "saludos",
    "tiempo"
]

# Mapeo de palabras a categorías (basado en Remy)
PALABRA_A_CATEGORIA = {
    # Alfabeto
    "a": "alfabeto", "b": "alfabeto", "c": "alfabeto", "ch": "alfabeto",
    "d": "alfabeto", "e": "alfabeto", "f": "alfabeto", "g": "alfabeto",
    "h": "alfabeto", "i": "alfabeto", "j": "alfabeto", "k": "alfabeto",
    "l": "alfabeto", "ll": "alfabeto", "m": "alfabeto", "n": "alfabeto",
    "ñ": "alfabeto", "o": "alfabeto", "p": "alfabeto", "q": "alfabeto",
    "r": "alfabeto", "rr": "alfabeto", "s": "alfabeto", "t": "alfabeto",
    "u": "alfabeto", "v": "alfabeto", "w": "alfabeto", "x": "alfabeto",
    "y": "alfabeto", "z": "alfabeto",
    
    # Cortesía
    "gracias": "cortesia", "muchas gracias": "cortesia", 
    "mucho gusto": "cortesia", "permiso": "cortesia",
    "a la orden": "cortesia", "buen provecho": "cortesia",
    "cortesia": "cortesia",
    
    # Días de la semana
    "lunes": "dias_semana", "martes": "dias_semana", "miercoles": "dias_semana",
    "jueves": "dias_semana", "viernes": "dias_semana", "sabado": "dias_semana",
    "domingo": "dias_semana",
    
    # Expresiones
    "saludas a": "expresiones", "expresiones": "expresiones",
    
    # Preguntas
    "como estas": "preguntas", "que tal": "preguntas",
    "cual es tu nombre": "preguntas", "cual es tu sena": "preguntas",
    
    # Pronombres
    "yo": "pronombres", "tu": "pronombres", "el": "pronombres",
    "ella": "pronombres", "nosotros": "pronombres", "ustedes": "pronombres",
    "ellos": "pronombres", "ellas": "pronombres",
    
    # Saludos
    "hola": "saludos", "adios": "saludos", "chao": "saludos",
    "buenos dias": "saludos", "buenas tardes": "saludos",
    "buenas noches": "saludos", "bienvenido": "saludos",
    
    # Tiempo
    "hoy": "tiempo", "ayer": "tiempo", "manana": "tiempo",
    "anteayer": "tiempo", "pasado manana": "tiempo",
    "semana": "tiempo", "mes": "tiempo", "fin de semana": "tiempo",
    "calendario": "tiempo"
}

def crear_estructura_carpetas(avatar_name):
    """Crea la estructura de carpetas para un avatar"""
    avatar_dir = GLB_DIR / avatar_name
    
    for categoria in CATEGORIAS:
        cat_dir = avatar_dir / categoria
        cat_dir.mkdir(parents=True, exist_ok=True)
        print(f"✅ Creada carpeta: {cat_dir}")
    
    return avatar_dir

def extraer_palabra_de_archivo(filename):
    """Extrae la palabra/seña del nombre de archivo"""
    # Remover extensión
    name = filename.replace(".glb", "")
    
    # Remover sufijos como _default, _def, etc
    name = name.replace("_default", "").replace("_def", "")
    
    # Remover espacios extras
    name = name.strip()
    
    return name

def organizar_nina():
    """Organiza los archivos de Nina en la estructura de carpetas"""
    print("\n🔄 Organizando archivos de Nina...")
    
    nina_dir = GLB_DIR / "Nina"
    archivos = list(nina_dir.glob("*.glb"))
    
    print(f"📁 Encontrados {len(archivos)} archivos GLB")
    
    movidos = 0
    no_categorizados = []
    
    for archivo in archivos:
        palabra = extraer_palabra_de_archivo(archivo.name)
        
        # Buscar categoría
        categoria = PALABRA_A_CATEGORIA.get(palabra.lower())
        
        if categoria:
            # Crear nombre nuevo: Nina_resultado_{palabra}.glb
            nuevo_nombre = f"Nina_resultado_{palabra}.glb"
            destino = nina_dir / categoria / nuevo_nombre
            
            # Mover archivo
            shutil.copy2(archivo, destino)
            print(f"  ✅ {palabra} → {categoria}/{nuevo_nombre}")
            movidos += 1
        else:
            no_categorizados.append(palabra)
    
    print(f"\n📊 Resumen:")
    print(f"  ✅ Archivos organizados: {movidos}")
    print(f"  ⚠️  No categorizados: {len(no_categorizados)}")
    
    if no_categorizados:
        print(f"\n⚠️  Archivos sin categoría:")
        for palabra in no_categorizados:
            print(f"    - {palabra}")
    
    return movidos

def main():
    print("=" * 60)
    print("🚀 ORGANIZADOR DE AVATARES")
    print("=" * 60)
    
    # Paso 1: Crear estructura de carpetas para Nina
    print("\n📁 Paso 1: Creando estructura de carpetas para Nina...")
    crear_estructura_carpetas("Nina")
    
    # Paso 2: Organizar archivos de Nina
    print("\n📦 Paso 2: Organizando archivos de Nina...")
    organizar_nina()
    
    print("\n" + "=" * 60)
    print("✅ ORGANIZACIÓN COMPLETADA")
    print("=" * 60)

if __name__ == "__main__":
    main()
