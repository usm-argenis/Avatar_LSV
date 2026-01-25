"""
Script para organizar las animaciones GLB en carpetas por categorías
"""
import os
import shutil
from pathlib import Path

def organizar_animaciones():
    """Organiza los archivos GLB en carpetas por categoría"""
    
    # Directorio base
    base_dir = Path(__file__).resolve().parents[1] / "test" / "output" / "glb"
    
    # Definir categorías
    categorias = {
        'alfabeto': [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'll', 
            'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 'rr', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ],
        'dias_semana': [
            'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo',
            'fin de semana', 'semana'
        ],
        'tiempo': [
            'ayer', 'hoy', 'mañana', 'anteayer', 'pasado mañana', 'calendario', 'mes'
        ],
        'pronombres': [
            'yo', 'tu', 'el', 'ella', 'nosotros', 'ustedes', 'ellos', 'ellas'
        ],
        'saludos': [
            'hola', 'adios', 'chao', 'buenos dias', 'buenas tardes', 'buenas noches',
            'bienvenido', 'que tal', 'como estas'
        ],
        'cortesia': [
            'gracias', 'muchas gracias', 'por favor', 'permiso', 'mucho gusto',
            'a la orden', 'buen provecho', 'cortesia'
        ],
        'preguntas': [
            'cual es tu nombre', 'cual es tu sena'
        ],
        'expresiones': [
            'expresiones', 'saludas a'
        ]
    }
    
    print("=" * 70)
    print("🗂️  ORGANIZADOR DE ANIMACIONES LSV")
    print("=" * 70)
    print(f"\n📁 Directorio base: {base_dir}\n")
    
    # Crear carpetas de categorías
    for categoria in categorias.keys():
        categoria_dir = base_dir / categoria
        categoria_dir.mkdir(exist_ok=True)
        print(f"✅ Creada carpeta: {categoria}/")
    
    # Mover archivos
    archivos_movidos = 0
    archivos_sin_categoria = []
    
    for archivo in base_dir.glob("Remy_resultado_*.glb"):
        # Extraer el nombre de la señal
        nombre = archivo.stem.replace('Remy_resultado_', '')
        
        # Saltar archivos de prueba/mejoras
        if any(x in nombre for x in ['mejorado', 'FIXED', '_v2', '_v3', '_v4']):
            continue
        
        # Buscar en qué categoría va
        movido = False
        for categoria, palabras in categorias.items():
            if nombre in palabras:
                destino = base_dir / categoria / archivo.name
                
                # Si el archivo ya existe, no mover
                if destino.exists():
                    print(f"⚠️  Ya existe: {categoria}/{archivo.name}")
                else:
                    shutil.copy2(archivo, destino)
                    print(f"📦 {archivo.name} → {categoria}/")
                    archivos_movidos += 1
                
                movido = True
                break
        
        if not movido:
            archivos_sin_categoria.append(archivo.name)
    
    print(f"\n{'=' * 70}")
    print(f"✅ Archivos organizados: {archivos_movidos}")
    
    if archivos_sin_categoria:
        print(f"\n⚠️  Archivos sin categoría ({len(archivos_sin_categoria)}):")
        for archivo in archivos_sin_categoria:
            print(f"   - {archivo}")
        print("\n💡 Estos archivos permanecen en la carpeta raíz")
    
    print(f"\n{'=' * 70}")
    print("📊 Resumen por categoría:")
    print(f"{'=' * 70}")
    
    for categoria in categorias.keys():
        categoria_dir = base_dir / categoria
        count = len(list(categoria_dir.glob("*.glb")))
        print(f"  {categoria:20} {count:3} archivos")
    
    print(f"\n{'=' * 70}")
    print("✅ ORGANIZACIÓN COMPLETADA")
    print(f"{'=' * 70}")

if __name__ == "__main__":
    organizar_animaciones()
