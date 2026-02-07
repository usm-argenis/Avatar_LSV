"""
Script para extraer datos de rotación de huesos desde capturas de pantalla de Blender
usando OCR (Tesseract)
"""
import json
import re
from pathlib import Path
from PIL import Image
import pytesseract

# Configurar ruta de Tesseract si es necesario
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extraer_datos_imagen(imagen_path):
    """Extrae datos de rotación de una imagen de Blender"""
    try:
        img = Image.open(imagen_path)
        
        # Extraer texto con OCR
        texto = pytesseract.image_to_string(img, lang='eng')
        
        # Buscar nombre del hueso y valores WXYZ
        # Formato esperado: "Armature.XXX : NombreHueso" y líneas con W X Y Z
        lineas = texto.split('\n')
        
        datos = {}
        nombre_hueso = None
        
        for i, linea in enumerate(lineas):
            # Buscar nombre del hueso
            match_nombre = re.search(r'Armature.*?:\s*(\w+)', linea)
            if match_nombre:
                nombre_hueso = match_nombre.group(1)
                
            # Buscar valores de rotación (W X Y Z)
            # Formato: número decimal, pueden ser negativos
            if nombre_hueso and 'Rotation' in linea:
                # Buscar en las siguientes líneas los valores W X Y Z
                for j in range(i+1, min(i+5, len(lineas))):
                    valores = re.findall(r'-?\d+\.\d+', lineas[j])
                    if len(valores) >= 4:
                        datos[nombre_hueso] = {
                            'w': float(valores[0]),
                            'x': float(valores[1]),
                            'y': float(valores[2]),
                            'z': float(valores[3])
                        }
                        nombre_hueso = None
                        break
        
        return datos, texto
        
    except Exception as e:
        print(f"Error procesando {imagen_path.name}: {e}")
        return {}, ""

def procesar_carpeta_sena(carpeta_path, nombre_sena):
    """Procesa todas las imágenes de una seña"""
    carpeta = Path(carpeta_path)
    imagenes = sorted(carpeta.glob('*.png'))
    
    print(f"\n{'='*60}")
    print(f"Procesando: {nombre_sena.upper()}")
    print(f"{'='*60}")
    print(f"Encontradas {len(imagenes)} imágenes")
    
    datos_consolidados = {}
    
    for img_path in imagenes:
        print(f"\n  📸 {img_path.name}")
        datos, texto_ocr = extraer_datos_imagen(img_path)
        
        if datos:
            for hueso, valores in datos.items():
                print(f"    ✓ {hueso}: W={valores['w']:.3f}, X={valores['x']:.3f}, Y={valores['y']:.3f}, Z={valores['z']:.3f}")
                datos_consolidados[hueso] = valores
        else:
            # Mostrar texto OCR para debug
            print(f"    ⚠️  No se detectaron datos. Texto OCR:")
            print(f"    {texto_ocr[:200]}...")
    
    return datos_consolidados

def main():
    # Rutas base
    json_dir = Path(__file__).parent / "json"
    
    # Configuración de señas con sus rangos
    senas_config = {
        "miercoles": {"min": 20, "max": 110, "retencion": 80},
        "viernes": {"min": 30, "max": 45, "retencion": 12},
        "sabado": {"min": 32, "max": 74, "retencion": 38},
        "buenas tardes": {"min": 48, "max": 80, "retencion": 28},
        "expresiones": {"min": 18, "max": 42, "retencion": 20}
    }
    
    # Procesar cada seña
    datos_duvall = {}
    datos_carla = {}
    
    for carpeta_nombre, alcance in senas_config.items():
        carpeta_path = json_dir / carpeta_nombre
        
        if not carpeta_path.exists():
            print(f"⚠️  No existe carpeta: {carpeta_path}")
            continue
        
        # Extraer datos de imágenes
        datos_huesos = procesar_carpeta_sena(carpeta_path, carpeta_nombre)
        
        # Mapear a rutas de archivos GLB
        nombre_archivo = carpeta_nombre.replace(" ", " ")
        
        # Determinar carpeta según seña
        if carpeta_nombre in ["miercoles", "viernes", "sabado"]:
            categoria = "dias_semana"
        elif carpeta_nombre == "buenas tardes":
            categoria = "saludos"
        else:
            categoria = "expresiones"
        
        # Crear entrada para Duvall
        ruta_duvall = f"C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Duvall/{categoria}/Duvall_resultado_{carpeta_nombre}.glb"
        datos_duvall[ruta_duvall] = {
            "alcance": alcance,
            **datos_huesos
        }
        
        # Crear entrada para Carla
        ruta_carla = f"C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Carla/{categoria}/Carla_resultado_{carpeta_nombre}.glb"
        datos_carla[ruta_carla] = {
            "alcance": alcance,
            **datos_huesos
        }
    
    # Guardar archivos JSON
    output_duvall = Path(__file__).parent / "datos_duvall.json"
    output_carla = Path(__file__).parent / "datos_carla.json"
    
    with open(output_duvall, 'w', encoding='utf-8') as f:
        json.dump(datos_duvall, f, indent=2, ensure_ascii=False)
    
    with open(output_carla, 'w', encoding='utf-8') as f:
        json.dump(datos_carla, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*60}")
    print(f"✅ ARCHIVOS GENERADOS:")
    print(f"{'='*60}")
    print(f"  📄 {output_duvall}")
    print(f"  📄 {output_carla}")
    print(f"\nTotal señas procesadas: {len(senas_config)}")

if __name__ == "__main__":
    try:
        import pytesseract
        from PIL import Image
        main()
    except ImportError as e:
        print(f"❌ Error: Faltan dependencias")
        print(f"   Ejecuta: pip install pytesseract pillow")
        print(f"   Además necesitas instalar Tesseract OCR desde: https://github.com/UB-Mannheim/tesseract/wiki")
