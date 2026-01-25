"""
Listar animaciones pendientes de procesar para Carlos
"""
import json
from pathlib import Path

# Definir todas las animaciones que deben existir
CATEGORIAS = {
    'alfabeto': ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                 'uno', 'dos', 'tres'],
    'dias_semana': ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 
                    'domingo', 'manana', 'ayer'],
    'tiempo': ['dia', 'semana', 'mes', 'año', 'hora', 'minuto', 'segundo'],
    'pronombres': ['yo', 'tu', 'el', 'ella', 'nosotros', 'ustedes', 'ellos', 'ellas'],
    'saludos': ['hola', 'adios', 'buenos_dias', 'buenas_tardes', 'buenas_noches', 
                'bienvenido', 'hasta_luego', 'nos_vemos', 'mucho_gusto'],
    'cortesia': ['gracias', 'por_favor', 'perdon', 'disculpa', 'de_nada', 'lo_siento'],
    'preguntas': ['que', 'como'],
    'expresiones': ['si', 'no']
}

def main():
    # Archivo de progreso
    progreso_path = Path("test/output/glb/progreso_carlos.json")
    
    # Cargar progreso si existe
    procesados = set()
    if progreso_path.exists():
        with open(progreso_path, 'r', encoding='utf-8') as f:
            rutas_procesadas = json.load(f)
            # Extraer nombres de las rutas
            for ruta in rutas_procesadas:
                # Ejemplo: "...\\Carlos_resultado_hola.glb" -> "hola"
                nombre = Path(ruta).stem.replace('Carlos_resultado_', '')
                procesados.add(nombre)
    
    # Crear lista completa de animaciones necesarias
    todas = []
    for categoria, nombres in CATEGORIAS.items():
        todas.extend(nombres)
    
    # Identificar pendientes
    pendientes = sorted(set(todas) - procesados)
    
    # Mostrar resultados
    print("\n" + "="*60)
    print("ESTADO DE ANIMACIONES CARLOS")
    print("="*60)
    print(f"\nTotal animaciones: {len(todas)}")
    print(f"Procesadas: {len(procesados)}")
    print(f"Pendientes: {len(pendientes)}")
    print("\n" + "="*60)
    
    if pendientes:
        print("\nANIMACIONES PENDIENTES:")
        print("-"*60)
        
        # Agrupar por categoría
        for categoria, nombres in CATEGORIAS.items():
            pendientes_cat = [n for n in nombres if n in pendientes]
            if pendientes_cat:
                print(f"\n{categoria.upper()} ({len(pendientes_cat)}):")
                for i, nombre in enumerate(pendientes_cat, 1):
                    print(f"  {i:2d}. {nombre}")
        
        print("\n" + "="*60)
        print("COMANDOS PARA PROCESAR:")
        print("-"*60)
        print("\nPuedes usar cualquiera de estos comandos:")
        for nombre in pendientes[:10]:  # Mostrar primeros 10
            print(f"  generar_carlos.bat {nombre}")
        if len(pendientes) > 10:
            print(f"  ... y {len(pendientes) - 10} más")
    else:
        print("\n✓ ¡TODAS LAS ANIMACIONES ESTÁN PROCESADAS!")
    
    print("\n" + "="*60 + "\n")
    
    # Guardar lista de pendientes
    pendientes_path = Path("scripts/pendientes_carlos.txt")
    with open(pendientes_path, 'w', encoding='utf-8') as f:
        for nombre in pendientes:
            f.write(f"{nombre}\n")
    
    if pendientes:
        print(f"Lista guardada en: {pendientes_path}")
        print("="*60 + "\n")

if __name__ == "__main__":
    main()
