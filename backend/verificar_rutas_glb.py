"""
Script para verificar que las rutas de los archivos GLB son correctas
según el mapeo de categorías
"""
from pathlib import Path
import json

# Cargar el diccionario
data_path = Path("C:/Users/andre/OneDrive/Documentos/tesis/backend/scripts/data.json")
with open(data_path, 'r', encoding='utf-8') as f:
    diccionario = json.load(f)

# Mapeo de categorías (data.json → carpetas físicas en Duvall)
# Algunas categorías pueden tener archivos en múltiples carpetas
MAPEO_CATEGORIAS = {
    # Categorías con una sola carpeta
    'alfabeto': ['alfabeto'],
    'numero': ['numero'],
    'expresiones': ['expresiones'],
    'cortesia': ['cortesia'],
    'saludos': ['saludos'],
    'personas': ['personas'],
    'pronombres': ['pronombres'],
    'ordinales': ['numeros ordinales'],
    'profesiones': ['profesion'],
    'adverbios': ['adverbios lugares'],
    'lugares': ['adverbios lugares'],
    'viviendas': ['tipos de vivienda'],
    'estado_civil': ['estado civil'],
    'interrogantes': ['preguntas'],
    'preposiciones': ['preposicion'],
    'dias_semana': ['dias_semana'],
    'transporte': ['medios transporte'],
    
    # Categorías con archivos en MÚLTIPLES carpetas
    'verbos': ['verbos', 'nuevo'],        # Mayoría en verbos, algunos en nuevo
    'tiempo': ['tiempo', 'nuevo'],        # Mayoría en tiempo, algunos en nuevo
    'general': ['horario', 'nuevo'],      # Algunos en horario, algunos en nuevo
    'familia': ['nuevo'],                 # TODAS en nuevo
    
    # Categorías SIN carpeta física (no hay archivos GLB):
    # 'educacion': objetivo
    # 'sustantivos': proyecto
    # 'tecnologia': computadora, computadoras
}

def obtener_carpetas(categoria):
    """Retorna lista de carpetas donde buscar archivos de una categoría"""
    return MAPEO_CATEGORIAS.get(categoria, [])

def obtener_nombre_carpeta(categoria):
    return MAPEO_CATEGORIAS.get(categoria, categoria)

# Ruta base
base_path = Path("C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Duvall")
avatar = "Duvall"

# Verificar archivos
print("=" * 70)
print("🔍 VERIFICACIÓN DE RUTAS DE ARCHIVOS GLB")
print("=" * 70)

categorias_encontradas = set()
categorias_problemas = set()
palabras_problema = []
palabras_ok = []

for palabra, info in diccionario.items():
    categoria = info['categoria']
    archivo = info['archivo']
    
    # Obtener nombre de carpeta mapeado
    nombre_carpeta = obtener_nombre_carpeta(categoria)
    categorias_encontradas.add((categoria, nombre_carpeta))
    
    # Construir ruta esperada
    ruta_esperada = base_path / nombre_carpeta / f"{avatar}_resultado_{archivo}.glb"
    
    # Verificar si existe
    if ruta_esperada.exists():
        palabras_ok.append(palabra)
    else:
        palabras_problema.append({
            'palabra': palabra,
            'categoria': categoria,
            'carpeta_mapeada': nombre_carpeta,
            'archivo': archivo,
            'ruta': str(ruta_esperada)
        })
        categorias_problemas.add((categoria, nombre_carpeta))

# Mostrar resultados
print(f"\n📊 RESUMEN:")
print(f"  Palabras en diccionario: {len(diccionario)}")
print(f"  Palabras con archivo encontrado: {len(palabras_ok)}")
print(f"  Palabras con archivo faltante: {len(palabras_problema)}")

print(f"\n🗂️ CATEGORÍAS MAPEADAS ({len(categorias_encontradas)}):")
for cat_orig, cat_mapeada in sorted(categorias_encontradas):
    if cat_orig == cat_mapeada:
        print(f"  ✅ {cat_orig}")
    else:
        print(f"  🔄 {cat_orig} → {cat_mapeada}")

if categorias_problemas:
    print(f"\n⚠️  CATEGORÍAS CON ARCHIVOS FALTANTES ({len(categorias_problemas)}):")
    for cat_orig, cat_mapeada in sorted(categorias_problemas):
        print(f"  ❌ {cat_orig} → {cat_mapeada}")

if palabras_problema:
    print(f"\n❌ PRIMERAS 10 PALABRAS CON ARCHIVOS FALTANTES:")
    for item in palabras_problema[:10]:
        print(f"  • {item['palabra']:20} → {item['carpeta_mapeada']:25} ({item['archivo']}.glb)")
    
    if len(palabras_problema) > 10:
        print(f"  ... y {len(palabras_problema) - 10} más")

# Verificar carpetas que existen realmente
print(f"\n📁 CARPETAS REALES EN {base_path}:")
if base_path.exists():
    carpetas_reales = sorted([d.name for d in base_path.iterdir() if d.is_dir()])
    for carpeta in carpetas_reales:
        # Contar archivos .glb
        num_archivos = len(list((base_path / carpeta).glob("*.glb")))
        print(f"  • {carpeta:30} ({num_archivos} archivos GLB)")
else:
    print(f"  ❌ La ruta no existe: {base_path}")

print("\n" + "=" * 70)
if len(palabras_problema) == 0:
    print("✅ TODAS LAS RUTAS SON CORRECTAS")
else:
    print(f"⚠️  {len(palabras_problema)} archivos no encontrados")
    print("   Esto puede ser normal si no tienes todas las animaciones creadas")
print("=" * 70)
