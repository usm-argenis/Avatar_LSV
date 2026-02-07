"""
Script para extraer automáticamente datos de rotación desde capturas de Blender usando OCR
"""
import json
import re
from pathlib import Path

try:
    from PIL import Image
    import pytesseract
    OCR_DISPONIBLE = True
except ImportError:
    OCR_DISPONIBLE = False
    print("⚠️  Instalando dependencias necesarias...")

def extraer_datos_imagen(imagen_path):
    """Extrae nombre de hueso y valores WXYZ de una captura de Blender"""
    try:
        img = Image.open(imagen_path)
        
        # OCR con configuración optimizada para números
        texto = pytesseract.image_to_string(img, config='--psm 6')
        
        # Buscar patrón: nombre de hueso seguido de valores numéricos
        lineas = texto.split('\n')
        
        for i, linea in enumerate(lineas):
            # Buscar líneas que contengan "Rotation" o valores de quaternion
            if 'Rotation' in linea or 'Quaternion' in linea:
                # El nombre del hueso suele estar unas líneas arriba
                for j in range(max(0, i-5), i):
                    # Buscar patrón de nombre de hueso (ej: LeftHand, RightHandIndex1, etc)
                    match = re.search(r'(Left|Right)(\w+)', lineas[j])
                    if match:
                        nombre_hueso = match.group(0)
                        
                        # Buscar valores W X Y Z en las siguientes líneas
                        for k in range(i, min(i+10, len(lineas))):
                            # Buscar 4 números decimales (pueden ser negativos)
                            numeros = re.findall(r'-?\d+\.\d+', lineas[k])
                            if len(numeros) >= 4:
                                return nombre_hueso, {
                                    'w': float(numeros[0]),
                                    'x': float(numeros[1]),
                                    'y': float(numeros[2]),
                                    'z': float(numeros[3])
                                }
        
        # Alternativa: buscar directamente 4 números consecutivos
        texto_limpio = ' '.join(lineas)
        numeros = re.findall(r'-?\d+\.\d+', texto_limpio)
        
        # Buscar nombre de hueso en todo el texto
        match_hueso = re.search(r'(Left|Right)(Hand|Arm|Leg|Foot|UpLeg)(\w*)', texto_limpio)
        
        if match_hueso and len(numeros) >= 4:
            # Tomar los últimos 4 números encontrados (suelen ser los valores de rotación)
            return match_hueso.group(0), {
                'w': float(numeros[-4]),
                'x': float(numeros[-3]),
                'y': float(numeros[-2]),
                'z': float(numeros[-1])
            }
        
        return None, None
        
    except Exception as e:
        print(f"    ❌ Error: {e}")
        return None, None

def procesar_carpeta(carpeta_path, nombre_sena):
    """Procesa todas las imágenes de una seña"""
    imagenes = sorted(Path(carpeta_path).glob('*.png'))
    datos = {}
    
    print(f"\n{'='*60}")
    print(f"📁 {nombre_sena.upper()}")
    print(f"{'='*60}")
    print(f"Procesando {len(imagenes)} imágenes...")
    
    for img_path in imagenes:
        print(f"\n  📸 {img_path.name}")
        nombre, valores = extraer_datos_imagen(img_path)
        
        if nombre and valores:
            datos[nombre] = valores
            print(f"    ✅ {nombre}: W={valores['w']:.3f}, X={valores['x']:.3f}, Y={valores['y']:.3f}, Z={valores['z']:.3f}")
        else:
            print(f"    ⚠️  No se detectaron datos")
    
    print(f"\n  🎯 Total huesos encontrados: {len(datos)}")
    return datos

def main():
    if not OCR_DISPONIBLE:
        print("\n" + "="*60)
        print("INSTALACIÓN REQUERIDA")
        print("="*60)
        print("\n1. Instala las dependencias Python:")
        print("   pip install pytesseract pillow")
        print("\n2. Instala Tesseract OCR:")
        print("   https://github.com/UB-Mannheim/tesseract/wiki")
        print("   Descarga: tesseract-ocr-w64-setup-5.3.3.20231005.exe")
        print("\n3. Ejecuta este script nuevamente")
        return
    
    # Configurar ruta de Tesseract (ajustar si está en otra ubicación)
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
    senas_config = {
        "miercoles": {"min": 20, "max": 110, "retencion": 80, "categoria": "dias_semana"},
        "viernes": {"min": 30, "max": 45, "retencion": 12, "categoria": "dias_semana"},
        "sabado": {"min": 32, "max": 74, "retencion": 38, "categoria": "dias_semana"},
        "buenas tardes": {"min": 48, "max": 80, "retencion": 28, "categoria": "saludos"},
        "expresiones": {"min": 18, "max": 42, "retencion": 20, "categoria": "expresiones"}
    }
    
    base_dir = Path(__file__).parent
    json_dir = base_dir / "json"
    
    datos_duvall = {}
    datos_carla = {}
    
    print("\n" + "="*60)
    print("EXTRACCIÓN AUTOMÁTICA DE DATOS DESDE IMÁGENES")
    print("="*60)
    
    for nombre_sena, config in senas_config.items():
        carpeta = json_dir / nombre_sena
        
        if not carpeta.exists():
            print(f"\n⚠️  Carpeta no encontrada: {carpeta}")
            continue
        
        # Extraer datos
        datos_huesos = procesar_carpeta(carpeta, nombre_sena)
        
        if not datos_huesos:
            print(f"    ⚠️  No se extrajeron datos, usando valores por defecto")
            datos_huesos = {}
        
        # Crear entradas JSON
        alcance = {"min": config["min"], "max": config["max"], "retencion": config["retencion"]}
        categoria = config["categoria"]
        
        ruta_duvall = f"C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Duvall/{categoria}/Duvall_resultado_{nombre_sena}.glb"
        ruta_carla = f"C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Carla/{categoria}/Carla_resultado_{nombre_sena}.glb"
        
        datos_duvall[ruta_duvall] = {"alcance": alcance, **datos_huesos}
        datos_carla[ruta_carla] = {"alcance": alcance, **datos_huesos}
    
    # Guardar archivos JSON
    output_duvall = base_dir / "datos_duvall.json"
    output_carla = base_dir / "datos_carla.json"
    
    with open(output_duvall, 'w', encoding='utf-8') as f:
        json.dump(datos_duvall, f, indent=2, ensure_ascii=False)
    
    with open(output_carla, 'w', encoding='utf-8') as f:
        json.dump(datos_carla, f, indent=2, ensure_ascii=False)
    
    print("\n" + "="*60)
    print("✅ ARCHIVOS JSON GENERADOS")
    print("="*60)
    print(f"📄 {output_duvall.name}")
    print(f"📄 {output_carla.name}")
    print("\n🚀 Ejecuta ahora: .\\GENERAR_MODIFICACIONES.bat")

if __name__ == "__main__":
    main()
