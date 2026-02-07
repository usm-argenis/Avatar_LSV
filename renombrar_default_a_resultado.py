import os
from pathlib import Path
import shutil

def renombrar_archivos_default(carpeta):
    """
    Renombra archivos con patrón *_default.glb a Duvall_resultado_*.glb
    
    Ejemplo:
        hola_default.glb -> Duvall_resultado_hola.glb
        cosa_default.glb -> Duvall_resultado_cosa.glb
    """
    carpeta_path = Path(carpeta)
    
    if not carpeta_path.exists():
        print(f"❌ ERROR: La carpeta no existe: {carpeta}")
        return
    
    # Buscar todos los archivos *_default.glb
    archivos_default = list(carpeta_path.glob("*_default.glb"))
    
    if not archivos_default:
        print(f"⚠️ No se encontraron archivos *_default.glb en: {carpeta}")
        return
    
    print(f"📁 Carpeta: {carpeta}")
    print(f"📊 Archivos encontrados: {len(archivos_default)}")
    print("\n" + "="*70)
    
    renombrados = 0
    errores = 0
    
    for archivo in archivos_default:
        # Obtener el nombre sin la extensión
        nombre_original = archivo.stem  # ej: "hola_default"
        
        # Remover "_default" del final
        if nombre_original.endswith("_default"):
            palabra = nombre_original[:-8]  # Quitar "_default" (8 caracteres)
            
            # Crear nuevo nombre
            nuevo_nombre = f"Duvall_resultado_{palabra}.glb"
            nuevo_path = archivo.parent / nuevo_nombre
            
            # Verificar si ya existe
            if nuevo_path.exists():
                print(f"⚠️ Ya existe: {nuevo_nombre}")
                print(f"   Saltando: {archivo.name}")
                continue
            
            try:
                # Renombrar archivo
                archivo.rename(nuevo_path)
                print(f"✅ {archivo.name}")
                print(f"   → {nuevo_nombre}")
                renombrados += 1
            except Exception as e:
                print(f"❌ ERROR al renombrar {archivo.name}: {e}")
                errores += 1
        else:
            print(f"⚠️ Archivo no tiene patrón esperado: {archivo.name}")
    
    print("\n" + "="*70)
    print(f"\n📊 RESUMEN:")
    print(f"   ✅ Renombrados: {renombrados}")
    if errores > 0:
        print(f"   ❌ Errores: {errores}")
    print(f"   Total procesados: {len(archivos_default)}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("❌ ERROR: Debes especificar la carpeta")
        print("\nUso:")
        print("  python renombrar_default_a_resultado.py <carpeta>")
        print("\nEjemplo:")
        print("  python renombrar_default_a_resultado.py C:\\Users\\andre\\Downloads")
        print("  python renombrar_default_a_resultado.py test/output/glb/Duvall/deepmotion")
        sys.exit(1)
    
    carpeta = sys.argv[1]
    renombrar_archivos_default(carpeta)
