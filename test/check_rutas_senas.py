import json
from pathlib import Path

# Cargar diccionario
d = json.loads(Path('C:/Users/andre/OneDrive/Documentos/tesis/backend/scripts/data.json').read_text(encoding='utf-8'))

# Mapeo de categorías
MAPEO_CATEGORIAS = {
    'dias_semana': 'dias_semana',
    'saludos': 'saludos',
    'expresiones': 'expresiones'
}

palabras = ['miercoles', 'viernes', 'sabado', 'buenas tardes', 'expresiones']

print('=' * 70)
print('RUTAS DE ARCHIVOS GLB PARA LAS SEÑAS')
print('=' * 70)

for p in palabras:
    if p in d:
        cat = d[p]['categoria']
        archivo = d[p]['archivo']
        carpeta = MAPEO_CATEGORIAS.get(cat, cat)
        
        ruta_duvall = f"C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Duvall/{carpeta}/Duvall_resultado_{archivo}.glb"
        ruta_carla = f"C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Carla/{carpeta}/Carla_resultado_{archivo}.glb"
        
        print(f"\n📌 {p.upper()}")
        print(f"   Categoría: {cat} → {carpeta}")
        print(f"   Archivo: {archivo}")
        print(f"   Duvall: {ruta_duvall}")
        print(f"   Carla: {ruta_carla}")
        
        # Verificar si existen
        existe_duvall = Path(ruta_duvall).exists()
        existe_carla = Path(ruta_carla).exists()
        print(f"   Existe Duvall: {'✅' if existe_duvall else '❌'}")
        print(f"   Existe Carla: {'✅' if existe_carla else '❌'}")
    else:
        print(f"\n❌ {p}: NO ENCONTRADO EN DICCIONARIO")

print('\n' + '=' * 70)
