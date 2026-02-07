"""
Script interactivo simple para ingresar datos de rotación de huesos manualmente
Abre cada imagen y copia los valores aquí
"""
import json
from pathlib import Path

def ingresar_hueso():
    """Solicita datos de un hueso"""
    print("\nIngresa los datos del hueso (o 'fin' para terminar):")
    nombre = input("  Nombre del hueso: ").strip()
    
    if nombre.lower() == 'fin':
        return None
    
    try:
        w = float(input("  W: "))
        x = float(input("  X: "))
        y = float(input("  Y: "))
        z = float(input("  Z: "))
        
        return nombre, {'w': w, 'x': x, 'y': y, 'z': z}
    except ValueError:
        print("  ❌ Valores inválidos, intenta de nuevo")
        return ingresar_hueso()

def procesar_sena(nombre_sena, alcance):
    """Procesa datos de una seña"""
    print(f"\n{'='*60}")
    print(f"SEÑA: {nombre_sena.upper()}")
    print(f"{'='*60}")
    print(f"Rango de frames: {alcance['min']}-{alcance['max']} (retención: {alcance['retencion']})")
    print("\nAbre las imágenes de la carpeta json/{nombre_sena}/")
    print("Por cada hueso que veas, ingresa sus valores de rotación\n")
    
    datos = {}
    
    while True:
        resultado = ingresar_hueso()
        if resultado is None:
            break
        nombre, valores = resultado
        datos[nombre] = valores
        print(f"  ✓ Agregado: {nombre}")
    
    return datos

def main():
    senas_config = {
        "miercoles": {"min": 20, "max": 110, "retencion": 80, "categoria": "dias_semana"},
        "viernes": {"min": 30, "max": 45, "retencion": 12, "categoria": "dias_semana"},
        "sabado": {"min": 32, "max": 74, "retencion": 38, "categoria": "dias_semana"},
        "buenas tardes": {"min": 48, "max": 80, "retencion": 28, "categoria": "saludos"},
        "expresiones": {"min": 18, "max": 42, "retencion": 20, "categoria": "expresiones"}
    }
    
    print("="*60)
    print("GENERADOR DE DATOS DE ROTACIÓN - MODO MANUAL")
    print("="*60)
    
    datos_duvall = {}
    datos_carla = {}
    
    for nombre_sena, config in senas_config.items():
        alcance = {"min": config["min"], "max": config["max"], "retencion": config["retencion"]}
        datos_huesos = procesar_sena(nombre_sena, alcance)
        
        # Rutas GLB
        categoria = config["categoria"]
        ruta_duvall = f"C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Duvall/{categoria}/Duvall_resultado_{nombre_sena}.glb"
        ruta_carla = f"C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Carla/{categoria}/Carla_resultado_{nombre_sena}.glb"
        
        datos_duvall[ruta_duvall] = {"alcance": alcance, **datos_huesos}
        datos_carla[ruta_carla] = {"alcance": alcance, **datos_huesos}
    
    # Guardar
    with open('datos_duvall.json', 'w', encoding='utf-8') as f:
        json.dump(datos_duvall, f, indent=2, ensure_ascii=False)
    
    with open('datos_carla.json', 'w', encoding='utf-8') as f:
        json.dump(datos_carla, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*60}")
    print("✅ Archivos generados:")
    print("  - datos_duvall.json")
    print("  - datos_carla.json")
    print("="*60)

if __name__ == "__main__":
    main()
