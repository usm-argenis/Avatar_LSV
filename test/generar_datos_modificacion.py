"""
Script para extraer datos de rotación de huesos desde imágenes de Blender
y generar archivos JSON para modificaciones
"""
import json
from pathlib import Path
import re

# Configuración de señas
SENAS_CONFIG = {
    "miercoles": {
        "alcance": {"min": 20, "max": 110, "retencion": 80},
        "categoria": "dias_semana",
        "archivo": "miercoles"
    },
    "viernes": {
        "alcance": {"min": 30, "max": 45, "retencion": 12},
        "categoria": "dias_semana",
        "archivo": "viernes"
    },
    "sabado": {
        "alcance": {"min": 32, "max": 74, "retencion": 38},
        "categoria": "dias_semana",
        "archivo": "sabado"
    },
    "buenas tardes": {
        "alcance": {"min": 48, "max": 80, "retencion": 28},
        "categoria": "saludos",
        "archivo": "buenas tardes"
    },
    "expresiones": {
        "alcance": {"min": 18, "max": 42, "retencion": 20},
        "categoria": "expresiones",
        "archivo": "expresiones"
    }
}

def solicitar_datos_manual():
    """
    Solicitar datos manualmente al usuario para cada seña
    """
    print("=" * 70)
    print("GENERADOR DE DATOS DE MODIFICACIÓN DE SEÑAS")
    print("=" * 70)
    print("\nPara cada seña, ingresa los datos de los huesos desde las imágenes")
    print("Formato: NombreHueso W X Y Z")
    print("Ejemplo: LeftHand 0.982 -0.034 -0.103 0.154")
    print("Escribe 'FIN' cuando termines con una seña\n")
    
    datos_completos = {}
    
    for sena, config in SENAS_CONFIG.items():
        print(f"\n{'='*70}")
        print(f"📌 SEÑA: {sena.upper()}")
        print(f"{'='*70}")
        print(f"Alcance: min={config['alcance']['min']}, max={config['alcance']['max']}, retencion={config['alcance']['retencion']}")
        print(f"Carpeta: {config['categoria']}")
        print("\nIngresa los datos de los huesos (uno por línea):")
        print("Formato: NombreHueso W X Y Z")
        print("Escribe 'FIN' cuando termines\n")
        
        huesos = {}
        while True:
            linea = input(f"  {sena} > ").strip()
            
            if linea.upper() == 'FIN':
                break
            
            if not linea:
                continue
            
            # Parsear la línea
            partes = linea.split()
            if len(partes) != 5:
                print("  ❌ Error: Formato incorrecto. Debe ser: NombreHueso W X Y Z")
                continue
            
            nombre_hueso = partes[0]
            try:
                w = float(partes[1])
                x = float(partes[2])
                y = float(partes[3])
                z = float(partes[4])
                
                huesos[nombre_hueso] = {
                    "w": w,
                    "x": x,
                    "y": y,
                    "z": z
                }
                print(f"  ✅ {nombre_hueso}: W={w}, X={x}, Y={y}, Z={z}")
                
            except ValueError:
                print("  ❌ Error: Los valores W, X, Y, Z deben ser números")
                continue
        
        if huesos:
            # Construir ruta del archivo GLB para Duvall
            ruta_duvall = f"C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Duvall/{config['categoria']}/Duvall_resultado_{config['archivo']}.glb"
            
            datos_completos[ruta_duvall] = {
                "alcance": config["alcance"],
                **huesos
            }
            
            print(f"\n  ✅ {len(huesos)} huesos agregados para {sena}")
        else:
            print(f"\n  ⚠️ No se agregaron huesos para {sena}")
    
    return datos_completos

def generar_archivos_json(datos_duvall):
    """
    Generar archivos JSON para Duvall y Carla
    """
    # Generar datos para Carla (mismos datos, diferente ruta)
    datos_carla = {}
    for ruta_duvall, datos in datos_duvall.items():
        ruta_carla = ruta_duvall.replace("/Duvall/", "/Carla/").replace("Duvall_resultado_", "Carla_resultado_")
        datos_carla[ruta_carla] = datos
    
    # Guardar archivos
    test_dir = Path("C:/Users/andre/OneDrive/Documentos/tesis/test")
    
    # datos_duvall.json
    with open(test_dir / "datos_duvall.json", "w", encoding="utf-8") as f:
        json.dump(datos_duvall, f, indent=2, ensure_ascii=False)
    
    # datos_carla.json
    with open(test_dir / "datos_carla.json", "w", encoding="utf-8") as f:
        json.dump(datos_carla, f, indent=2, ensure_ascii=False)
    
    print("\n" + "=" * 70)
    print("✅ ARCHIVOS JSON GENERADOS")
    print("=" * 70)
    print(f"📄 {test_dir / 'datos_duvall.json'}")
    print(f"📄 {test_dir / 'datos_carla.json'}")
    print(f"\n📊 Total de señas: {len(datos_duvall)}")
    
    for ruta, datos in datos_duvall.items():
        nombre_archivo = Path(ruta).name
        num_huesos = len([k for k in datos.keys() if k != 'alcance'])
        print(f"  • {nombre_archivo}: {num_huesos} huesos")

def main():
    """
    Función principal
    """
    print("\n🚀 Iniciando generador de datos de modificación...\n")
    
    # Solicitar datos manualmente
    datos = solicitar_datos_manual()
    
    if datos:
        # Generar archivos JSON
        generar_archivos_json(datos)
        
        print("\n" + "=" * 70)
        print("🎯 PRÓXIMO PASO")
        print("=" * 70)
        print("Ejecuta el archivo BAT para generar los GLB modificados:")
        print("  GENERAR_MODIFICACIONES.bat")
    else:
        print("\n⚠️ No se generaron archivos. No se ingresaron datos.")

if __name__ == "__main__":
    main()
