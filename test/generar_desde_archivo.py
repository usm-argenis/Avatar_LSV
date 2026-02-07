"""
Script para generar datos desde un archivo de texto
Formato del archivo de texto:
=== MIERCOLES ===
LeftHand 0.982 -0.034 -0.103 0.154
LeftHandPinky1 0.964 0.081 0.031 0.249
...

=== VIERNES ===
LeftHand 0.997 0.022 -0.036 0.068
...
"""
import json
from pathlib import Path

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

def parsear_archivo_texto(ruta_archivo):
    """
    Parsear archivo de texto con datos de huesos
    """
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    datos_completos = {}
    sena_actual = None
    
    for linea in contenido.split('\n'):
        linea = linea.strip()
        
        if not linea:
            continue
        
        # Detectar inicio de seña
        if linea.startswith('===') and linea.endswith('==='):
            nombre_sena = linea.replace('=', '').strip().lower()
            if nombre_sena in SENAS_CONFIG:
                sena_actual = nombre_sena
                print(f"📌 Procesando: {sena_actual}")
            continue
        
        # Parsear línea de hueso
        if sena_actual:
            partes = linea.split()
            if len(partes) == 5:
                try:
                    nombre_hueso = partes[0]
                    w = float(partes[1])
                    x = float(partes[2])
                    y = float(partes[3])
                    z = float(partes[4])
                    
                    # Obtener configuración de la seña
                    config = SENAS_CONFIG[sena_actual]
                    ruta_duvall = f"C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Duvall/{config['categoria']}/Duvall_resultado_{config['archivo']}.glb"
                    
                    if ruta_duvall not in datos_completos:
                        datos_completos[ruta_duvall] = {
                            "alcance": config["alcance"]
                        }
                    
                    datos_completos[ruta_duvall][nombre_hueso] = {
                        "w": w,
                        "x": x,
                        "y": y,
                        "z": z
                    }
                    
                    print(f"  ✅ {nombre_hueso}: W={w}, X={x}, Y={y}, Z={z}")
                    
                except (ValueError, IndexError):
                    print(f"  ⚠️ Línea ignorada: {linea}")
    
    return datos_completos

def generar_archivos_json(datos_duvall):
    """
    Generar archivos JSON para Duvall y Carla
    """
    # Generar datos para Carla
    datos_carla = {}
    for ruta_duvall, datos in datos_duvall.items():
        ruta_carla = ruta_duvall.replace("/Duvall/", "/Carla/").replace("Duvall_resultado_", "Carla_resultado_")
        datos_carla[ruta_carla] = datos
    
    # Guardar archivos
    test_dir = Path("C:/Users/andre/OneDrive/Documentos/tesis/test")
    
    with open(test_dir / "datos_duvall.json", "w", encoding="utf-8") as f:
        json.dump(datos_duvall, f, indent=2, ensure_ascii=False)
    
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

if __name__ == "__main__":
    print("=" * 70)
    print("GENERADOR DE DATOS DESDE ARCHIVO DE TEXTO")
    print("=" * 70)
    
    ruta_archivo = input("\nRuta del archivo de texto con los datos: ").strip()
    
    if not ruta_archivo:
        ruta_archivo = "C:/Users/andre/OneDrive/Documentos/tesis/test/datos_huesos.txt"
        print(f"Usando ruta por defecto: {ruta_archivo}")
    
    ruta_path = Path(ruta_archivo)
    
    if not ruta_path.exists():
        print(f"\n❌ El archivo no existe: {ruta_archivo}")
        print("\nCrea un archivo de texto con el siguiente formato:")
        print("""
=== MIERCOLES ===
LeftHand 0.982 -0.034 -0.103 0.154
LeftHandPinky1 0.964 0.081 0.031 0.249

=== VIERNES ===
LeftHand 0.997 0.022 -0.036 0.068
        """)
    else:
        datos = parsear_archivo_texto(ruta_path)
        if datos:
            generar_archivos_json(datos)
            print("\n✅ Proceso completado!")
        else:
            print("\n⚠️ No se encontraron datos válidos en el archivo")
