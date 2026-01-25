"""
Script para extraer SOLO las animaciones de los archivos GLB de Duvall
Elimina meshes, materiales, texturas - conserva solo animaciones
"""

from pygltflib import GLTF2
import os

def extraer_solo_animaciones(glb_input, glb_output):
    """
    Extrae solo las animaciones de un archivo GLB, eliminando geometría pesada
    """
    try:
        # Cargar GLB
        gltf = GLTF2().load(glb_input)
        
        # Eliminar toda la geometría y materiales (conservar solo animaciones)
        gltf.meshes = []
        gltf.materials = []
        gltf.images = []
        gltf.textures = []
        gltf.samplers = []
        
        # Las animaciones, nodes y skins se conservan automáticamente
        
        # Guardar archivo optimizado
        gltf.save(glb_output)
        
        # Obtener tamaños
        size_input = os.path.getsize(glb_input) / 1024  # KB
        size_output = os.path.getsize(glb_output) / 1024  # KB
        reduction = ((size_input - size_output) / size_input) * 100
        
        return size_output, reduction
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None, None

def procesar_carpeta(carpeta_origen, carpeta_destino, categoria):
    """
    Procesa todos los archivos GLB de una carpeta
    """
    archivos_procesados = 0
    archivos_exitosos = 0
    
    if not os.path.exists(carpeta_origen):
        print(f"⚠️  Carpeta no existe: {carpeta_origen}")
        return 0, 0
    
    archivos = [f for f in os.listdir(carpeta_origen) if f.endswith('.glb')]
    
    if not archivos:
        print(f"⚠️  Sin archivos en: {categoria}")
        return 0, 0
    
    # Crear subcarpeta de destino
    subcarpeta_destino = os.path.join(carpeta_destino, categoria)
    os.makedirs(subcarpeta_destino, exist_ok=True)
    
    for archivo in archivos:
        ruta_entrada = os.path.join(carpeta_origen, archivo)
        
        # Mantener el nombre original pero en la subcarpeta
        ruta_salida = os.path.join(subcarpeta_destino, archivo)
        
        archivos_procesados += 1
        
        size, reduction = extraer_solo_animaciones(ruta_entrada, ruta_salida)
        
        if size is not None:
            print(f"✅ {categoria}/{archivo} ({size:.0f}KB, -{reduction:.1f}%)")
            archivos_exitosos += 1
        else:
            print(f"❌ {categoria}/{archivo}")
    
    return archivos_procesados, archivos_exitosos

def main():
    print("=" * 60)
    print("🎬 EXTRACTOR DE ANIMACIONES - DUVALL")
    print("=" * 60)
    print()
    
    # Buscar primero en nueva estructura por género
    base_paths = ["Hombre", "Duvall"]  # Nueva estructura, luego fallback
    base_duvall = None
    
    for path in base_paths:
        if os.path.exists(path):
            base_duvall = path
            print(f"✅ Usando estructura: {base_duvall}")
            break
    
    if not base_duvall:
        print(f"❌ No existe ninguna carpeta: {base_paths}")
        return
    
    carpeta_salida = "Duvall_animation"
    
    # Crear carpeta de salida
    os.makedirs(carpeta_salida, exist_ok=True)
    
    # Categorías a procesar
    CATEGORIAS = [
        'alfabeto',
        'cortesia',
        'dias_semana',
        'expresiones',
        'preguntas',
        'pronombres',
        'saludos',
        'tiempo'
    ]
    
    total_procesados = 0
    total_exitosos = 0
    
    for categoria in CATEGORIAS:
        print(f"\n📁 Procesando: {categoria}")
        print("-" * 60)
        
        carpeta_origen = os.path.join(base_duvall, categoria)
        procesados, exitosos = procesar_carpeta(carpeta_origen, carpeta_salida, categoria)
        
        total_procesados += procesados
        total_exitosos += exitosos
    
    # Resumen final
    print()
    print("=" * 60)
    print("📊 RESUMEN")
    print("=" * 60)
    print(f"✅ Procesados: {total_procesados}")
    print(f"✅ Exitosos: {total_exitosos}")
    print(f"❌ Fallidos: {total_procesados - total_exitosos}")
    print()
    print(f"📂 Carpeta de salida: {carpeta_salida}/")
    print()

if __name__ == "__main__":
    main()
