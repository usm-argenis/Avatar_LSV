"""
Script para copiar los archivos GLB funcionales a la carpeta Nancy
con el formato de nombres Nancy_resultado_[animacion].glb
"""

import shutil
from pathlib import Path

print("="*80)
print("COPIAR GLB FUNCIONALES A CARPETA NANCY")
print("="*80)

# Rutas
BLEND_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\blend1")
NANCY_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Luis")

# Categorías
CATEGORIAS = [
    "cortesia",
    "dias_semana", 
    "expresiones",
    "preguntas",
    "pronombres",
    "saludos",
    "tiempo"
]

# Contadores
copiados = 0
fallidos = 0
saltados = 0

print(f"\n📁 Origen: {BLEND_DIR}")
print(f"📁 Destino: {NANCY_DIR}\n")

for categoria in CATEGORIAS:
    print(f"\n{'='*80}")
    print(f"📂 CATEGORÍA: {categoria.upper()}")
    print(f"{'='*80}")
    
    origen_cat = BLEND_DIR / categoria
    destino_cat = NANCY_DIR / categoria
    
    # Crear carpeta destino si no existe
    destino_cat.mkdir(parents=True, exist_ok=True)
    
    if not origen_cat.exists():
        print(f"⚠️ No existe carpeta origen: {origen_cat}")
        continue
    
    # Buscar todos los archivos .glb en la categoría
    archivos_glb = list(origen_cat.glob("Luis_*.glb"))
    
    print(f"   Archivos encontrados: {len(archivos_glb)}")
    
    for archivo_origen in archivos_glb:
        # Extraer nombre de animación
        # De "Nancy_a la orden.glb" → "a la orden"
        nombre_animacion = archivo_origen.stem.replace("Luis_", "")
        
        # Crear nombre destino: "Nancy_resultado_a la orden.glb"
        nombre_destino = f"Luis_resultado_{nombre_animacion}.glb"
        archivo_destino = destino_cat / nombre_destino
        
        try:
            # Verificar si ya existe
            if archivo_destino.exists():
                # Comparar tamaños
                size_origen = archivo_origen.stat().st_size
                size_destino = archivo_destino.stat().st_size
                
                # Si el origen es más grande o diferente, sobrescribir
                if size_origen != size_destino:
                    shutil.copy2(archivo_origen, archivo_destino)
                    print(f"   ✅ Actualizado: {nombre_destino} ({size_origen/1024:.1f} KB)")
                    copiados += 1
                else:
                    print(f"   ⏭️ Ya existe (mismo tamaño): {nombre_destino}")
                    saltados += 1
            else:
                # Copiar archivo nuevo
                shutil.copy2(archivo_origen, archivo_destino)
                size = archivo_origen.stat().st_size
                print(f"   ✅ Copiado: {nombre_destino} ({size/1024:.1f} KB)")
                copiados += 1
                
        except Exception as e:
            print(f"   ❌ Error al copiar {nombre_animacion}: {str(e)}")
            fallidos += 1

# Resumen final
print(f"\n{'='*80}")
print(f"RESUMEN")
print(f"{'='*80}")
print(f"✅ Archivos copiados/actualizados: {copiados}")
print(f"⏭️ Archivos saltados (ya actualizados): {saltados}")
print(f"❌ Errores: {fallidos}")
print(f"\n📁 Archivos disponibles en: {NANCY_DIR}")
print(f"{'='*80}")
