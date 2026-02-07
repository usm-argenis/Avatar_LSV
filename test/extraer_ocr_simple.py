"""
Extractor simple de datos de imágenes usando EasyOCR
"""
import json
import re
from pathlib import Path

try:
    import easyocr
    from PIL import Image
    OCR_OK = True
except ImportError:
    OCR_OK = False

def extraer_con_easyocr(img_path, reader):
    """Extrae texto de imagen con EasyOCR"""
    resultado = reader.readtext(str(img_path), detail=0)
    texto_completo = ' '.join(resultado)
    
    # Buscar nombre de hueso
    match_hueso = re.search(r'(Left|Right)(Hand|Arm|Leg|Foot|UpLeg|Shoulder)(\w*)', texto_completo, re.IGNORECASE)
    
    # Buscar 4 números consecutivos (W X Y Z)
    numeros = re.findall(r'-?\d+\.?\d*', texto_completo)
    numeros_float = [float(n) for n in numeros if '.' in n or abs(float(n)) < 2]
    
    if match_hueso and len(numeros_float) >= 4:
        nombre = match_hueso.group(0)
        # Limpiar nombre
        nombre = nombre.replace(' ', '').replace('_', '')
        
        # Tomar los últimos 4 números (suelen ser los valores de rotación)
        return nombre, {
            'w': numeros_float[-4],
            'x': numeros_float[-3],
            'y': numeros_float[-2],
            'z': numeros_float[-1]
        }
    
    return None, None

def procesar_carpeta(carpeta_path, nombre_sena, reader):
    """Procesa imágenes de una seña"""
    imagenes = sorted(Path(carpeta_path).glob('*.png'))
    datos = {}
    
    print(f"\n{'='*60}")
    print(f"📁 {nombre_sena.upper()} - {len(imagenes)} imágenes")
    print(f"{'='*60}")
    
    for img in imagenes:
        print(f"  📸 {img.name}...", end=' ')
        nombre, valores = extraer_con_easyocr(img, reader)
        
        if nombre and valores:
            datos[nombre] = valores
            print(f"✅ {nombre}")
        else:
            print("⚠️")
    
    print(f"  🎯 {len(datos)} huesos extraídos")
    return datos

def main():
    if not OCR_OK:
        print("Instalando EasyOCR...")
        import subprocess
        subprocess.run(["pip", "install", "easyocr"], check=True)
        print("✅ Reinicia el script")
        return
    
    print("Inicializando EasyOCR...")
    reader = easyocr.Reader(['en'], gpu=False)
    
    senas = {
        "miercoles": {"min": 20, "max": 110, "retencion": 80, "cat": "dias_semana"},
        "viernes": {"min": 30, "max": 45, "retencion": 12, "cat": "dias_semana"},
        "sabado": {"min": 32, "max": 74, "retencion": 38, "cat": "dias_semana"},
        "buenas tardes": {"min": 48, "max": 80, "retencion": 28, "cat": "saludos"},
        "expresiones": {"min": 18, "max": 42, "retencion": 20, "cat": "expresiones"}
    }
    
    base = Path(__file__).parent
    datos_d = {}
    datos_c = {}
    
    for sena, cfg in senas.items():
        carpeta = base / "json" / sena
        if not carpeta.exists():
            continue
        
        huesos = procesar_carpeta(carpeta, sena, reader)
        alc = {"min": cfg["min"], "max": cfg["max"], "retencion": cfg["retencion"]}
        
        ruta_d = f"C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Duvall/{cfg['cat']}/Duvall_resultado_{sena}.glb"
        ruta_c = f"C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Carla/{cfg['cat']}/Carla_resultado_{sena}.glb"
        
        datos_d[ruta_d] = {"alcance": alc, **huesos}
        datos_c[ruta_c] = {"alcance": alc, **huesos}
    
    with open('datos_duvall.json', 'w') as f:
        json.dump(datos_d, f, indent=2)
    with open('datos_carla.json', 'w') as f:
        json.dump(datos_c, f, indent=2)
    
    print("\n✅ Archivos generados: datos_duvall.json, datos_carla.json")

if __name__ == "__main__":
    main()
