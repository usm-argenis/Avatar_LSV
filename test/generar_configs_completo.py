"""
Genera archivos JSON de configuración para todas las carpetas de Duvall y Carla
"""
import json
from pathlib import Path

# Configuración base para las modificaciones de huesos
MODIFICACIONES_BASE = {
    "Spine": {"w": 1.000, "x": 0.000644, "y": -0.013, "z": 0.001},
    "Hips": {"w": 0.998, "x": 0.024, "y": 0.062, "z": 0.006},
    "LeftUpLeg": {"w": 0.997, "x": 0.072, "y": -0.002, "z": -0.031},
    "RightUpLeg": {"w": 0.996, "x": 0.082, "y": 0.002, "z": 0.032},
    "RightLeg": {"w": 0.986, "x": -0.168, "y": 0.000056, "z": -0.000737},
    "LeftLeg": {"w": 0.989, "x": -0.148, "y": -0.002, "z": 0.000932},
    "RightFoot": {"w": 1.000, "x": 0.004, "y": -0.005, "z": -0.023},
    "LeftFoot": {"w": 1.000, "x": -0.007, "y": -0.010, "z": 0.008},
    "LeftToe_End": {"w": 1.000, "x": -0.000000, "y": 0.000, "z": -0.000000},
    "LeftToeBase": {"w": 0.954, "x": 0.297, "y": -0.013, "z": -0.034},
    "RightToe_End": {"w": 1.000, "x": 0.000000, "y": -0.000002, "z": 0.000000},
    "RightToeBase": {"w": 0.954, "x": 0.297, "y": 0.013, "z": 0.034}
}

# Lista de carpetas a procesar (nombres sin espacios para archivos)
CARPETAS = [
    ("alfabeto", "alfabeto"),
    ("cortesia", "cortesia"),
    ("dias_semana", "dias_semana"),
    ("estado civil", "estado_civil"),
    ("expresiones", "expresiones"),
    ("numero", "numero"),
    ("numeros ordinales", "numeros_ordinales"),
    ("personas", "personas"),
    ("preguntas", "preguntas"),
    ("preposicion", "preposicion"),
    ("profesion", "profesion"),
    ("pronombres", "pronombres"),
    ("saludos", "saludos"),
    ("tiempo", "tiempo"),
    ("verbos", "verbos"),
    ("adverbios lugares", "adverbios_lugares"),
    ("tipos de vivienda", "tipos_vivienda")
]

BASE_PATH = "C:/Users/andre/OneDrive/Documentos/tesis/test"

def generar_json(personaje, carpeta_real, carpeta_archivo):
    """Genera un archivo JSON de configuración"""
    
    config = {
        "carpeta_entrada": f"{BASE_PATH}/output/glb/{personaje}/{carpeta_real}",
        "carpeta_salida": f"{BASE_PATH}/output/glb/{personaje}/nuevos_{carpeta_archivo}",
        "patron": "*.glb",
        "excluir": ["*_modif.glb", "*_modificado.glb", "*_MANOS*.glb"],
        "sufijo_salida": "",
        "alcance": {
            "min": 0,
            "max": "fin",
            "retencion": "fin"
        }
    }
    
    # Agregar modificaciones de huesos
    config.update(MODIFICACIONES_BASE)
    
    # Nombre del archivo
    nombre_archivo = f"datos_{personaje.lower()}_{carpeta_archivo}.json"
    ruta_archivo = Path(BASE_PATH) / nombre_archivo
    
    # Guardar
    with open(ruta_archivo, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Creado: {nombre_archivo}")
    
    return nombre_archivo

if __name__ == "__main__":
    print("🔧 Generando archivos JSON de configuración...\n")
    
    archivos_creados = []
    
    # Generar para Duvall
    print("📁 Duvall:")
    for carpeta_real, carpeta_archivo in CARPETAS:
        nombre = generar_json("Duvall", carpeta_real, carpeta_archivo)
        archivos_creados.append(nombre)
    
    print(f"\n📁 Carla:")
    # Generar para Carla
    for carpeta_real, carpeta_archivo in CARPETAS:
        nombre = generar_json("Carla", carpeta_real, carpeta_archivo)
        archivos_creados.append(nombre)
    
    print(f"\n{'='*60}")
    print(f"✨ Generados {len(archivos_creados)} archivos JSON")
    print(f"{'='*60}")
    print(f"\n📋 Archivos creados:")
    for archivo in archivos_creados:
        print(f"   • {archivo}")
    
    print(f"\n✅ ¡Listo! Ahora puedes ejecutar GENERAR_MODIFICACIONES_COMPLETO.bat")
