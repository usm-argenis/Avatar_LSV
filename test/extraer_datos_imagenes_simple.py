"""
Extrae automáticamente datos de rotación de las imágenes de Blender
SIN necesidad de OCR - simplemente lee los archivos JSON que ya existen
"""
import json
from pathlib import Path

def main():
    # Buscar archivos JSON en las carpetas
    json_base = Path(__file__).parent / "json"
    
    senas_config = {
        "miercoles": {"min": 20, "max": 110, "retencion": 80, "categoria": "dias_semana"},
        "viernes": {"min": 30, "max": 45, "retencion": 12, "categoria": "dias_semana"},
        "sabado": {"min": 32, "max": 74, "retencion": 38, "categoria": "dias_semana"},
        "buenas tardes": {"min": 48, "max": 80, "retencion": 28, "categoria": "saludos"},
        "expresiones": {"min": 18, "max": 42, "retencion": 20, "categoria": "expresiones"}
    }
    
    datos_duvall = {}
    datos_carla = {}
    
    print("="*60)
    print("BUSCANDO ARCHIVOS JSON EN CARPETAS")
    print("="*60)
    
    for nombre_sena, config in senas_config.items():
        carpeta = json_base / nombre_sena
        archivos_json = list(carpeta.glob("*.json"))
        
        print(f"\n📁 {nombre_sena.upper()}")
        print(f"   Archivos JSON encontrados: {len(archivos_json)}")
        
        datos_huesos = {}
        
        # Si hay archivo JSON, leerlo
        if archivos_json:
            for archivo_json in archivos_json:
                print(f"   📄 {archivo_json.name}")
                try:
                    with open(archivo_json, 'r', encoding='utf-8') as f:
                        datos = json.load(f)
                        # Combinar datos
                        for hueso, valores in datos.items():
                            if isinstance(valores, dict) and 'w' in valores:
                                datos_huesos[hueso] = valores
                                print(f"      ✓ {hueso}")
                except Exception as e:
                    print(f"      ⚠️  Error: {e}")
        
        # Crear entradas para GLB
        categoria = config["categoria"]
        alcance = {"min": config["min"], "max": config["max"], "retencion": config["retencion"]}
        
        ruta_duvall = f"C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Duvall/{categoria}/Duvall_resultado_{nombre_sena}.glb"
        ruta_carla = f"C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Carla/{categoria}/Carla_resultado_{nombre_sena}.glb"
        
        datos_duvall[ruta_duvall] = {"alcance": alcance, **datos_huesos}
        datos_carla[ruta_carla] = {"alcance": alcance, **datos_huesos}
        
        print(f"   Total huesos: {len(datos_huesos)}")
    
    # Guardar
    with open('datos_duvall.json', 'w', encoding='utf-8') as f:
        json.dump(datos_duvall, f, indent=2, ensure_ascii=False)
    
    with open('datos_carla.json', 'w', encoding='utf-8') as f:
        json.dump(datos_carla, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*60}")
    print("✅ Archivos actualizados:")
    print("   - datos_duvall.json")
    print("   - datos_carla.json")
    print("="*60)

if __name__ == "__main__":
    main()
