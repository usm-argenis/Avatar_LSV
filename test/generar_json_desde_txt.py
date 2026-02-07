"""
Script para generar datos_duvall.json y datos_carla.json
desde archivos de texto con rotaciones
"""
import json
import re
from pathlib import Path

def leer_archivo_rotaciones(archivo_path):
    """Lee un archivo de texto con datos de rotaciones"""
    datos = {}
    
    with open(archivo_path, 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            
            # Ignorar comentarios y líneas vacías
            if not linea or linea.startswith('#'):
                continue
            
            # Parsear línea: NombreHueso W X Y Z
            partes = linea.split()
            if len(partes) >= 5:
                nombre = partes[0]
                try:
                    w, x, y, z = float(partes[1]), float(partes[2]), float(partes[3]), float(partes[4])
                    datos[nombre] = {'w': w, 'x': x, 'y': y, 'z': z}
                    print(f"  ✓ {nombre}: W={w:.3f}, X={x:.3f}, Y={y:.3f}, Z={z:.3f}")
                except ValueError:
                    print(f"  ⚠️  Error en línea: {linea}")
    
    return datos

def main():
    senas_config = {
        "miercoles": {
            "archivo": "rotaciones_miercoles.txt",
            "alcance": {"min": 20, "max": 110, "retencion": 80},
            "categoria": "dias_semana"
        },
        "viernes": {
            "archivo": "rotaciones_viernes.txt",
            "alcance": {"min": 30, "max": 45, "retencion": 12},
            "categoria": "dias_semana"
        },
        "sabado": {
            "archivo": "rotaciones_sabado.txt",
            "alcance": {"min": 32, "max": 74, "retencion": 38},
            "categoria": "dias_semana"
        },
        "buenas tardes": {
            "archivo": "rotaciones_buenas_tardes.txt",
            "alcance": {"min": 48, "max": 80, "retencion": 28},
            "categoria": "saludos"
        },
        "expresiones": {
            "archivo": "rotaciones_expresiones.txt",
            "alcance": {"min": 18, "max": 42, "retencion": 20},
            "categoria": "expresiones"
        }
    }
    
    base_dir = Path(__file__).parent
    datos_duvall = {}
    datos_carla = {}
    
    print("="*60)
    print("GENERANDO DATOS DE ROTACIÓN DESDE ARCHIVOS .TXT")
    print("="*60)
    
    for nombre_sena, config in senas_config.items():
        archivo_path = base_dir / config["archivo"]
        
        print(f"\n📄 Procesando: {nombre_sena.upper()}")
        
        if not archivo_path.exists():
            print(f"  ⚠️  Archivo no encontrado: {archivo_path}")
            continue
        
        datos_huesos = leer_archivo_rotaciones(archivo_path)
        
        # Rutas GLB
        categoria = config["categoria"]
        ruta_duvall = f"C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Duvall/{categoria}/Duvall_resultado_{nombre_sena}.glb"
        ruta_carla = f"C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Carla/{categoria}/Carla_resultado_{nombre_sena}.glb"
        
        datos_duvall[ruta_duvall] = {
            "alcance": config["alcance"],
            **datos_huesos
        }
        
        datos_carla[ruta_carla] = {
            "alcance": config["alcance"],
            **datos_huesos
        }
    
    # Guardar JSON
    output_duvall = base_dir / "datos_duvall.json"
    output_carla = base_dir / "datos_carla.json"
    
    with open(output_duvall, 'w', encoding='utf-8') as f:
        json.dump(datos_duvall, f, indent=2, ensure_ascii=False)
    
    with open(output_carla, 'w', encoding='utf-8') as f:
        json.dump(datos_carla, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*60}")
    print("✅ ARCHIVOS GENERADOS:")
    print(f"{'='*60}")
    print(f"  📄 {output_duvall.name}")
    print(f"  📄 {output_carla.name}")
    print(f"\n🔄 Ahora ejecuta: .\\GENERAR_MODIFICACIONES.bat")

if __name__ == "__main__":
    main()
    
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
