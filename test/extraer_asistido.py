"""
Extractor manual asistido - muestra las imágenes para que copies los valores
"""
import json
import os
from pathlib import Path

def obtener_datos_interactivo(carpeta_path, nombre_sena):
    """Guía interactiva para ingresar datos viendo las imágenes"""
    imagenes = sorted(Path(carpeta_path).glob('*.png'))
    
    print(f"\n{'='*60}")
    print(f"📁 {nombre_sena.upper()}")
    print(f"{'='*60}")
    print(f"Encontradas {len(imagenes)} imágenes")
    print(f"\n🔍 Abre la carpeta: json\\{nombre_sena}\\")
    print(f"📂 Comando: explorer json\\{nombre_sena}")
    
    # Abrir carpeta automáticamente
    os.startfile(carpeta_path)
    
    datos = {}
    
    print(f"\n📋 Para cada imagen, ingresa:")
    print("   Formato: NombreHueso W X Y Z")
    print("   Ejemplo: LeftHand 0.982 -0.034 -0.103 0.154")
    print("   Escribe 'fin' cuando termines esta seña\n")
    
    contador = 1
    while True:
        entrada = input(f"  [{contador}] Hueso {contador}: ").strip()
        
        if entrada.lower() == 'fin':
            break
        
        partes = entrada.split()
        if len(partes) == 5:
            nombre = partes[0]
            try:
                w, x, y, z = float(partes[1]), float(partes[2]), float(partes[3]), float(partes[4])
                datos[nombre] = {'w': w, 'x': x, 'y': y, 'z': z}
                print(f"       ✅ {nombre} agregado")
                contador += 1
            except ValueError:
                print(f"       ❌ Error: valores numéricos inválidos")
        else:
            print(f"       ❌ Formato incorrecto (necesita: Nombre W X Y Z)")
    
    print(f"\n  🎯 Total: {len(datos)} huesos")
    return datos

def main():
    senas = {
        "miercoles": {"min": 20, "max": 110, "retencion": 80, "cat": "dias_semana"},
        "viernes": {"min": 30, "max": 45, "retencion": 12, "cat": "dias_semana"},
        "sabado": {"min": 32, "max": 74, "retencion": 38, "cat": "dias_semana"},
        "buenas tardes": {"min": 48, "max": 80, "retencion": 28, "cat": "saludos"},
        "expresiones": {"min": 18, "max": 42, "retencion": 20, "cat": "expresiones"}
    }
    
    base = Path(__file__).parent
    json_dir = base / "json"
    
    datos_duvall = {}
    datos_carla = {}
    
    print("\n" + "="*60)
    print("EXTRACTOR ASISTIDO DE DATOS")
    print("="*60)
    print("\nSe abrirán las carpetas con imágenes.")
    print("Mira cada imagen y copia los valores aquí.\n")
    
    for nombre_sena, cfg in senas.items():
        carpeta = json_dir / nombre_sena
        
        if not carpeta.exists():
            print(f"\n⚠️  Carpeta no existe: {carpeta}")
            continue
        
        huesos = obtener_datos_interactivo(carpeta, nombre_sena)
        
        alc = {"min": cfg["min"], "max": cfg["max"], "retencion": cfg["retencion"]}
        
        ruta_d = f"C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Duvall/{cfg['cat']}/Duvall_resultado_{nombre_sena}.glb"
        ruta_c = f"C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Carla/{cfg['cat']}/Carla_resultado_{nombre_sena}.glb"
        
        datos_duvall[ruta_d] = {"alcance": alc, **huesos}
        datos_carla[ruta_c] = {"alcance": alc, **huesos}
    
    # Guardar
    with open('datos_duvall.json', 'w', encoding='utf-8') as f:
        json.dump(datos_duvall, f, indent=2, ensure_ascii=False)
    
    with open('datos_carla.json', 'w', encoding='utf-8') as f:
        json.dump(datos_carla, f, indent=2, ensure_ascii=False)
    
    print("\n" + "="*60)
    print("✅ ARCHIVOS GENERADOS")
    print("="*60)
    print("📄 datos_duvall.json")
    print("📄 datos_carla.json")
    print("\n🚀 Ejecuta: .\\GENERAR_MODIFICACIONES.bat")

if __name__ == "__main__":
    main()
