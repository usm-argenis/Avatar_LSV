"""
Script para verificar TODAS las palabras del diccionario y cuáles tienen GLB
Genera reporte completo por categoría
"""
import json
from pathlib import Path
from collections import defaultdict

# Cargar diccionario
data_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\backend\scripts\data.json")
with open(data_path, 'r', encoding='utf-8') as f:
    diccionario = json.load(f)

# Ruta base de GLB
base_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall")

# Mapeo de categorías actualizado
MAPEO_CATEGORIAS = {
    'alfabeto': 'alfabeto',
    'verbos': 'verbos',
    'numero': 'numero',
    'tiempo': 'tiempo',
    'expresiones': 'expresiones',
    'cortesia': 'cortesia',
    'saludos': 'saludos',
    'personas': 'personas',
    'pronombres': 'pronombres',
    'ordinales': 'numeros ordinales',
    'profesiones': 'profesion',
    'adverbios': 'adverbios lugares',
    'lugares': 'adverbios lugares',
    'viviendas': 'tipos de vivienda',
    'estado_civil': 'estado civil',
    'interrogantes': 'preguntas',
    'preposiciones': 'preposicion',
    'dias_semana': 'dias_semana',
    'transporte': 'medios transporte'
}

# Organizar palabras por categoría
palabras_por_categoria = defaultdict(list)
for palabra, info in diccionario.items():
    categoria = info['categoria']
    archivo = info['archivo']
    palabras_por_categoria[categoria].append((palabra, archivo))

# Verificar existencia de GLB
print("="*80)
print("📊 REPORTE COMPLETO: PALABRAS CON/SIN ARCHIVO GLB")
print("="*80)

total_palabras = len(diccionario)
total_con_glb = 0
total_sin_glb = 0

categorias_sin_carpeta = []
categorias_con_carpeta = []

for categoria in sorted(palabras_por_categoria.keys()):
    palabras = palabras_por_categoria[categoria]
    
    print(f"\n{'='*80}")
    print(f"📁 CATEGORÍA: {categoria.upper()}")
    print(f"   Total palabras: {len(palabras)}")
    
    # Verificar si la categoría tiene carpeta
    carpeta = MAPEO_CATEGORIAS.get(categoria)
    
    if carpeta:
        carpeta_path = base_path / carpeta
        if not carpeta_path.exists():
            print(f"   ⚠️  Carpeta mapeada NO EXISTE: {carpeta}")
            carpeta = None
    
    if not carpeta:
        print(f"   ❌ SIN CARPETA FÍSICA - Todas las palabras SIN GLB")
        categorias_sin_carpeta.append(categoria)
        total_sin_glb += len(palabras)
        
        # Mostrar palabras
        for palabra, archivo in sorted(palabras):
            print(f"      • {palabra}")
    else:
        print(f"   ✅ Carpeta: {carpeta}")
        categorias_con_carpeta.append(categoria)
        
        # Verificar cada palabra
        con_glb = []
        sin_glb = []
        
        for palabra, archivo in palabras:
            glb_path = base_path / carpeta / f"{archivo}.glb"
            if glb_path.exists():
                con_glb.append(palabra)
                total_con_glb += 1
            else:
                sin_glb.append(palabra)
                total_sin_glb += 1
        
        # Mostrar resultados
        if con_glb:
            print(f"\n   ✓ Con GLB ({len(con_glb)}):")
            for palabra in sorted(con_glb):
                print(f"      • {palabra}")
        
        if sin_glb:
            print(f"\n   ✗ Sin GLB ({len(sin_glb)}):")
            for palabra in sorted(sin_glb):
                print(f"      • {palabra}")

# Resumen final
print(f"\n{'='*80}")
print(f"📊 RESUMEN FINAL")
print(f"{'='*80}")
print(f"Total palabras en diccionario: {total_palabras}")
print(f"✅ Palabras CON archivo GLB: {total_con_glb} ({total_con_glb/total_palabras*100:.1f}%)")
print(f"❌ Palabras SIN archivo GLB: {total_sin_glb} ({total_sin_glb/total_palabras*100:.1f}%)")
print(f"\n📁 Categorías CON carpeta física: {len(categorias_con_carpeta)}")
print(f"   {', '.join(sorted(categorias_con_carpeta))}")
print(f"\n❌ Categorías SIN carpeta física: {len(categorias_sin_carpeta)}")
print(f"   {', '.join(sorted(categorias_sin_carpeta))}")

# Generar lista de palabras sin GLB
print(f"\n{'='*80}")
print(f"📋 LISTA DE PALABRAS SIN GLB (para eliminar o generar)")
print(f"{'='*80}")
palabras_sin_glb = []

for categoria in sorted(palabras_por_categoria.keys()):
    carpeta = MAPEO_CATEGORIAS.get(categoria)
    palabras = palabras_por_categoria[categoria]
    
    if not carpeta:
        # Toda la categoría sin carpeta
        palabras_sin_glb.extend([p[0] for p in palabras])
    else:
        # Verificar palabra por palabra
        for palabra, archivo in palabras:
            glb_path = base_path / carpeta / f"{archivo}.glb"
            if not glb_path.exists():
                palabras_sin_glb.append(palabra)

print("\nPalabras para eliminar de data.json (o generar GLB):")
for palabra in sorted(palabras_sin_glb):
    print(f"  - {palabra}")

print(f"\n✅ Reporte completo generado")
