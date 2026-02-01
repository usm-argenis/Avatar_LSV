"""
Script para extraer coordenadas de rotación de imágenes de Blender
y generar archivos JSON con el formato requerido
"""
import os
import json
import re
from pathlib import Path
try:
    from PIL import Image
    import easyocr
except ImportError:
    print("Instalando dependencias necesarias...")
    import subprocess
    subprocess.run(["pip", "install", "pillow", "easyocr"])
    from PIL import Image
    import easyocr

# Inicializar lector OCR (solo inglés para mayor velocidad)
print("Inicializando OCR...")
reader = easyocr.Reader(['en'], gpu=False)

def extraer_datos_imagen(ruta_imagen):
    """Extraer nombre de hueso y valores WXYZ de una imagen de Blender"""
    try:
        # Leer imagen con OCR
        resultados = reader.readtext(str(ruta_imagen))
        
        # Unir todo el texto detectado
        texto = ' '.join([res[1] for res in resultados])
        
        print(f"\n📄 {Path(ruta_imagen).name}")
        print(f"   Texto detectado: {texto[:100]}...")
        
        # Buscar nombre del hueso (formato: Armature.030 : NombreHueso)
        match_nombre = re.search(r'(?:Armature[.\d]+\s*[:]\s*)?(\w*Hand\w+\d+)', texto)
        if not match_nombre:
            # Intentar solo nombre del hueso sin Armature
            match_nombre = re.search(r'(RightHand\w+\d+|LeftHand\w+\d+)', texto)
        
        if not match_nombre:
            print(f"   ⚠️  No se encontró nombre de hueso")
            return None
        
        nombre_hueso = match_nombre.group(1)
        
        # Buscar valores de rotación (W, X, Y, Z)
        valores = {}
        
        # Extraer W, X, Y, Z (buscar patrones como "W 0.994" o "W: 0.994" o "W-0.069")
        for coord in ['W', 'X', 'Y', 'Z']:
            pattern = rf'{coord}\s*[:=]?\s*(-?\d+\.?\d*)'
            match = re.search(pattern, texto, re.IGNORECASE)
            if match:
                valores[coord.lower()] = float(match.group(1))
        
        if len(valores) == 4:
            print(f"   ✅ {nombre_hueso}: W={valores['w']:.3f}, X={valores['x']:.3f}, Y={valores['y']:.3f}, Z={valores['z']:.3f}")
            return nombre_hueso, valores
        else:
            print(f"   ⚠️  Valores incompletos: {valores}")
            return None
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return None

def procesar_carpeta(ruta_carpeta):
    """Procesar todas las imágenes de una carpeta y generar JSON"""
    carpeta = Path(ruta_carpeta)
    nombre_carpeta = carpeta.name
    
    print(f"\n{'='*80}")
    print(f"📁 Procesando carpeta: {nombre_carpeta}")
    print(f"{'='*80}")
    
    # Buscar todas las imágenes PNG
    imagenes = sorted(carpeta.glob("*.png"))
    
    if not imagenes:
        print(f"⚠️  No se encontraron imágenes PNG en {nombre_carpeta}")
        return None
    
    print(f"📸 Encontradas {len(imagenes)} imágenes")
    
    # Extraer datos de cada imagen
    datos_huesos = {}
    
    for img in imagenes:
        resultado = extraer_datos_imagen(img)
        if resultado:
            nombre_hueso, valores = resultado
            datos_huesos[nombre_hueso] = valores
    
    if not datos_huesos:
        print(f"❌ No se pudieron extraer datos de {nombre_carpeta}")
        return None
    
    print(f"\n✅ Extraídos {len(datos_huesos)} huesos correctamente")
    return datos_huesos

def generar_json_completo(carpetas_base, archivo_salida):
    """Generar JSON con formato completo para múltiples carpetas"""
    
    # Estructura base (puedes modificar estos valores)
    json_completo = {}
    
    for carpeta in carpetas_base:
        if not carpeta.exists():
            print(f"⚠️  Carpeta no encontrada: {carpeta}")
            continue
        
        datos = procesar_carpeta(carpeta)
        
        if datos:
            nombre = carpeta.name
            # Crear entrada para cada carpeta
            json_completo[nombre] = datos
    
    # Guardar JSON
    ruta_salida = Path(archivo_salida)
    with open(ruta_salida, 'w', encoding='utf-8') as f:
        json.dump(json_completo, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*80}")
    print(f"✅ JSON generado: {ruta_salida}")
    print(f"{'='*80}")
    
    return json_completo

if __name__ == "__main__":
    # Carpeta base con las subcarpetas
    base = Path(r"C:/Users/andre/OneDrive/Documentos/tesis/test/json")
    
    # Subcarpetas a procesar
    carpetas = [
        base / "hoy",
        base / "mañana",
        base / "Miercoles",
        base / "permiso"
    ]
    
    # Generar JSON
    resultado = generar_json_completo(carpetas, base / "coordenadas_extraidas.json")
    
    if resultado:
        print(f"\n📊 Total de carpetas procesadas: {len(resultado)}")
        for carpeta, huesos in resultado.items():
            print(f"  - {carpeta}: {len(huesos)} huesos")
