"""
Script para extraer SOLO las animaciones de los archivos GLB de Remy
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
    print("🎬 EXTRACTOR DE ANIMACIONES - REMY")
    print("=" * 60)
    print()
    
    # Rutas base - Remy tiene archivos en la raíz con formato Remy_resultado_xxx.glb
    base_remy = "."  # Raíz actual
    carpeta_salida = "Remy_animation"
    
    # Crear carpeta de salida
    os.makedirs(carpeta_salida, exist_ok=True)
    
    # Mapeo de archivos Remy a categorías
    MAPEO_CATEGORIAS = {
        'cortesia': ['a_la_orden', 'buen provecho', 'cortesia', 'gracias', 'muchas gracias', 'mucho gusto', 'permiso'],
        'dias_semana': ['domingo', 'jueves', 'lunes', 'martes', 'miercoles', 'sabado', 'viernes'],
        'expresiones': ['expresiones', 'saludas a'],
        'preguntas': ['como estas', 'cual es tu nombre', 'cual es tu sena', 'que tal'],
        'pronombres': ['el', 'ella', 'ellas', 'ellos', 'nosotros', 'tu', 'ustedes', 'yo'],
        'saludos': ['adios', 'bienvenido', 'buenas noches', 'buenas tardes', 'buenos dias', 'chao', 'hola'],
        'tiempo': ['anteayer', 'ayer', 'calendario', 'fin de semana', 'hoy', 'mañana', 'mes', 'pasado mañana', 'semana']
    }
    
    total_procesados = 0
    total_exitosos = 0
    
    for categoria, palabras in MAPEO_CATEGORIAS.items():
        print(f"\n📁 Procesando: {categoria}")
        print("-" * 60)
        
        # Crear subcarpeta de destino
        subcarpeta_destino = os.path.join(carpeta_salida, categoria)
        os.makedirs(subcarpeta_destino, exist_ok=True)
        
        for palabra in palabras:
            # Buscar archivo con diferentes variantes
            posibles_nombres = [
                f"Remy_resultado_{palabra}.glb",
                f"Remy_resultado_{palabra.replace(' ', '_')}.glb"
            ]
            
            archivo_encontrado = None
            for nombre in posibles_nombres:
                if os.path.exists(nombre):
                    archivo_encontrado = nombre
                    break
            
            if not archivo_encontrado:
                print(f"⚠️  No encontrado: {palabra}")
                continue
            
            # Nombre de salida
            nombre_salida = os.path.basename(archivo_encontrado)
            ruta_salida = os.path.join(subcarpeta_destino, nombre_salida)
            
            total_procesados += 1
            
            size, reduction = extraer_solo_animaciones(archivo_encontrado, ruta_salida)
            
            if size is not None:
                print(f"✅ {categoria}/{nombre_salida} ({size:.0f}KB, -{reduction:.1f}%)")
                total_exitosos += 1
            else:
                print(f"❌ {categoria}/{nombre_salida}")
    
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
