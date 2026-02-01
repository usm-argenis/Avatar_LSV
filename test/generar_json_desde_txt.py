"""
Genera archivos JSON desde archivos datos.txt
Formato entrada: NombreHueso W X Y Z (separado por espacios)
"""
import json
from pathlib import Path

def procesar_archivo_txt(ruta_txt):
    """Lee archivo datos.txt y extrae coordenadas"""
    datos = {}
    
    with open(ruta_txt, 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            if not linea or linea.startswith('#'):
                continue
            
            partes = linea.split()
            if len(partes) != 5:
                print(f"⚠️  Línea ignorada (formato incorrecto): {linea}")
                continue
            
            nombre = partes[0]
            w = float(partes[1])
            x = float(partes[2])
            y = float(partes[3])
            z = float(partes[4])
            
            datos[nombre] = {
                "w": w,
                "x": x,
                "y": y,
                "z": z
            }
            
            print(f"  ✅ {nombre}: W={w}, X={x}, Y={y}, Z={z}")
    
    return datos

def generar_json_carpetas(base_path):
    """Procesa todas las carpetas con datos.txt"""
    base = Path(base_path)
    carpetas = ["hoy", "mañana", "Miercoles", "permiso"]
    
    resultados = {}
    
    for nombre_carpeta in carpetas:
        carpeta = base / nombre_carpeta
        archivo_txt = carpeta / "datos.txt"
        
        print(f"\n{'='*60}")
        print(f"📁 {nombre_carpeta}")
        print(f"{'='*60}")
        
        if not archivo_txt.exists():
            print(f"⚠️  No se encontró datos.txt - saltando")
            continue
        
        datos = procesar_archivo_txt(archivo_txt)
        
        if datos:
            resultados[nombre_carpeta] = datos
            print(f"\n✅ {len(datos)} huesos procesados")
            
            # Guardar JSON individual
            json_salida = carpeta / f"{nombre_carpeta}_datos.json"
            with open(json_salida, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=2, ensure_ascii=False)
            print(f"💾 Guardado: {json_salida.name}")
    
    # Guardar JSON combinado
    if resultados:
        json_combinado = base / "todas_coordenadas.json"
        with open(json_combinado, 'w', encoding='utf-8') as f:
            json.dump(resultados, f, indent=2, ensure_ascii=False)
        
        print(f"\n{'='*60}")
        print(f"✅ JSON COMBINADO: {json_combinado.name}")
        print(f"📊 Total: {len(resultados)} palabras procesadas")
        print(f"{'='*60}")

if __name__ == "__main__":
    base_path = r"C:/Users/andre/OneDrive/Documentos/tesis/test/json"
    generar_json_carpetas(base_path)
