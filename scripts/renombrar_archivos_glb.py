"""
Script para renombrar archivos GLB/FBX con nombres problemáticos
Soluciona:
- Espacios en nombres de archivo
- Caracteres especiales (acentos, ñ, etc.)
- Nombres muy largos

Convierte:
    "Remy_resultado_buenos dias.glb" → "Remy_resultado_buenos_dias.glb"
    "Remy_resultado_niño.glb" → "Remy_resultado_nino.glb"
    "Remy_resultado_adiós.glb" → "Remy_resultado_adios.glb"

Uso:
    python scripts/renombrar_archivos_glb.py
    python scripts/renombrar_archivos_glb.py --directorio ruta/custom
"""

import os
import re
import argparse
from pathlib import Path
import unicodedata

def normalizar_nombre(nombre):
    """
    Normaliza un nombre de archivo eliminando espacios y caracteres especiales
    
    Args:
        nombre: Nombre original del archivo
        
    Returns:
        Nombre normalizado
    """
    # Separar nombre y extensión
    ruta = Path(nombre)
    extension = ruta.suffix  # .glb, .fbx, etc.
    nombre_base = ruta.stem  # nombre sin extensión
    
    # 1. Convertir a minúsculas
    nombre_normalizado = nombre_base.lower()
    
    # 2. Reemplazar espacios por guiones bajos
    nombre_normalizado = nombre_normalizado.replace(' ', '_')
    nombre_normalizado = nombre_normalizado.replace('-', '_')
    
    # 3. Eliminar acentos y caracteres especiales
    # á → a, é → e, í → i, ó → o, ú → u, ñ → n
    nombre_normalizado = unicodedata.normalize('NFKD', nombre_normalizado)
    nombre_normalizado = nombre_normalizado.encode('ASCII', 'ignore').decode('ASCII')
    
    # 4. Eliminar caracteres no permitidos (solo letras, números, guión bajo)
    nombre_normalizado = re.sub(r'[^a-z0-9_]', '', nombre_normalizado)
    
    # 5. Eliminar guiones bajos múltiples consecutivos
    nombre_normalizado = re.sub(r'_+', '_', nombre_normalizado)
    
    # 6. Eliminar guiones bajos al inicio y final
    nombre_normalizado = nombre_normalizado.strip('_')
    
    # 7. Limitar longitud (máximo 50 caracteres)
    if len(nombre_normalizado) > 50:
        nombre_normalizado = nombre_normalizado[:50]
    
    # Reconstruir con extensión
    return nombre_normalizado + extension

def renombrar_archivos(directorio, dry_run=False, verbose=True):
    """
    Renombrar todos los archivos GLB/FBX en un directorio
    
    Args:
        directorio: Ruta al directorio
        dry_run: Si True, solo muestra qué haría sin renombrar
        verbose: Mostrar detalles
        
    Returns:
        Tupla (exitosos, sin_cambios, errores)
    """
    directorio = Path(directorio)
    
    if not directorio.exists():
        print(f"❌ Directorio no encontrado: {directorio}")
        return 0, 0, 0
    
    # Buscar archivos GLB y FBX
    archivos = list(directorio.glob("*.glb")) + list(directorio.glob("*.fbx"))
    archivos += list(directorio.glob("*.GLB")) + list(directorio.glob("*.FBX"))
    
    if not archivos:
        print(f"⚠️ No se encontraron archivos GLB/FBX en: {directorio}")
        return 0, 0, 0
    
    print("=" * 70)
    if dry_run:
        print("🔍 MODO PREVIEW - No se renombrará nada")
    else:
        print("🔄 RENOMBRANDO ARCHIVOS")
    print("=" * 70)
    print(f"📁 Directorio: {directorio.absolute()}")
    print(f"📊 Total de archivos: {len(archivos)}")
    print("=" * 70)
    
    exitosos = 0
    sin_cambios = 0
    errores = 0
    
    # Tabla de cambios
    cambios = []
    
    for archivo in sorted(archivos):
        nombre_original = archivo.name
        nombre_nuevo = normalizar_nombre(nombre_original)
        
        if nombre_original == nombre_nuevo:
            sin_cambios += 1
            if verbose:
                print(f"⚪ Sin cambios: {nombre_original}")
        else:
            ruta_nueva = archivo.parent / nombre_nuevo
            
            # Verificar si ya existe un archivo con el nuevo nombre
            if ruta_nueva.exists() and ruta_nueva != archivo:
                errores += 1
                print(f"❌ Conflicto: {nombre_original}")
                print(f"   → {nombre_nuevo} (ya existe)")
            else:
                cambios.append((archivo, ruta_nueva, nombre_original, nombre_nuevo))
    
    # Mostrar resumen de cambios
    if cambios:
        print(f"\n{'='*70}")
        print(f"📋 CAMBIOS A REALIZAR ({len(cambios)} archivos)")
        print("=" * 70)
        
        for i, (_, _, orig, nuevo) in enumerate(cambios, 1):
            print(f"{i:3}. {orig}")
            print(f"     → {nuevo}")
        
        if dry_run:
            print(f"\n{'='*70}")
            print("ℹ️  Esto es un PREVIEW. Para renombrar ejecuta sin --dry-run")
            print("=" * 70)
        else:
            print(f"\n{'='*70}")
            print("⚠️  ¿Continuar con el renombrado?")
            print("=" * 70)
            respuesta = input("Escribe 'si' para continuar: ").strip().lower()
            
            if respuesta in ['si', 'sí', 's', 'yes', 'y']:
                print(f"\n{'='*70}")
                print("🔄 Renombrando archivos...")
                print("=" * 70)
                
                for archivo_orig, archivo_nuevo, nombre_orig, nombre_nuevo in cambios:
                    try:
                        archivo_orig.rename(archivo_nuevo)
                        exitosos += 1
                        print(f"✅ {nombre_orig}")
                        print(f"   → {nombre_nuevo}")
                    except Exception as e:
                        errores += 1
                        print(f"❌ Error al renombrar {nombre_orig}: {e}")
            else:
                print("\n❌ Operación cancelada por el usuario")
                return 0, sin_cambios, len(cambios)
    
    # Resumen final
    print(f"\n{'='*70}")
    print("📊 RESUMEN")
    print("=" * 70)
    print(f"✅ Renombrados: {exitosos}")
    print(f"⚪ Sin cambios: {sin_cambios}")
    print(f"❌ Errores: {errores}")
    print("=" * 70)
    
    return exitosos, sin_cambios, errores

def mostrar_ejemplos():
    """Muestra ejemplos de transformaciones"""
    ejemplos = [
        "Remy_resultado_buenos dias.glb",
        "Remy_resultado_niño.glb",
        "Remy_resultado_adiós.glb",
        "Remy_resultado_café con leche.glb",
        "Remy_resultado_matemáticas.glb",
        "Remy resultado español.glb",
        "REMY_RESULTADO_MAYÚSCULAS.glb",
    ]
    
    print("=" * 70)
    print("💡 EJEMPLOS DE TRANSFORMACIONES")
    print("=" * 70)
    
    for ejemplo in ejemplos:
        transformado = normalizar_nombre(ejemplo)
        print(f"📄 Original:     {ejemplo}")
        print(f"✨ Transformado: {transformado}")
        print()

def main():
    parser = argparse.ArgumentParser(
        description='Renombrar archivos GLB/FBX eliminando espacios y caracteres especiales',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:

  # Preview de cambios sin renombrar (modo seguro)
  python scripts/renombrar_archivos_glb.py --dry-run

  # Renombrar archivos en test/output/glb
  python scripts/renombrar_archivos_glb.py

  # Renombrar en directorio personalizado
  python scripts/renombrar_archivos_glb.py --directorio "ruta/a/directorio"

  # Ver ejemplos de transformaciones
  python scripts/renombrar_archivos_glb.py --ejemplos

Transformaciones aplicadas:
  • Espacios → guiones bajos
  • Minúsculas
  • Sin acentos (á→a, é→e, etc.)
  • ñ → n
  • Solo letras, números y guión bajo
        """
    )
    
    parser.add_argument('--directorio', '-d', type=str, default='test/output/glb',
                       help='Directorio con archivos a renombrar (default: test/output/glb)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Mostrar preview sin renombrar archivos')
    parser.add_argument('--ejemplos', action='store_true',
                       help='Mostrar ejemplos de transformaciones')
    parser.add_argument('--quiet', '-q', action='store_true',
                       help='Modo silencioso (solo errores)')
    
    args = parser.parse_args()
    
    if args.ejemplos:
        mostrar_ejemplos()
        return
    
    # Renombrar archivos
    verbose = not args.quiet
    renombrar_archivos(args.directorio, dry_run=args.dry_run, verbose=verbose)

if __name__ == "__main__":
    main()
