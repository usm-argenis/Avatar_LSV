"""
Ejemplo de uso del exportador BLEND → GLB con animaciones
Este script muestra cómo usar export_blend_to_glb.py correctamente

Incluye diferentes casos de uso y soluciones a problemas comunes
"""

import subprocess
import sys
from pathlib import Path

# Configuración de rutas
BLENDER_PATH = r"C:\Program Files\Blender Foundation\Blender 4.0\blender.exe"  # Ajusta según tu instalación
SCRIPT_DIR = Path(__file__).parent
EXPORT_SCRIPT = SCRIPT_DIR / "export_blend_to_glb.py"
TEST_SCRIPT = SCRIPT_DIR / "test_glb_export.py"

def check_blender():
    """Verifica que Blender esté disponible"""
    blender_path = Path(BLENDER_PATH)
    if not blender_path.exists():
        print(f"❌ Blender no encontrado en: {BLENDER_PATH}")
        print(f"💡 Ajusta la ruta BLENDER_PATH en este script")
        return False
    
    print(f"✅ Blender encontrado: {blender_path}")
    return True

def export_blend_to_glb(blend_file, glb_file=None):
    """
    Exporta un archivo .blend a .glb preservando animaciones
    """
    
    blend_path = Path(blend_file)
    if not blend_path.exists():
        print(f"❌ Archivo .blend no encontrado: {blend_path}")
        return False
    
    if glb_file is None:
        glb_file = blend_path.with_suffix('.glb')
    
    print(f"🔄 Exportando: {blend_path.name} → {Path(glb_file).name}")
    
    # Comando de Blender
    cmd = [
        BLENDER_PATH,
        '--background',          # Sin interfaz
        str(blend_path),        # Archivo a abrir
        '--python',             # Ejecutar script Python
        str(EXPORT_SCRIPT),     # Nuestro script exportador
        '--',                   # Separador de argumentos
        str(glb_file)          # Archivo de salida
    ]
    
    try:
        print("🚀 Ejecutando Blender...")
        print("   (Esto puede tomar unos segundos...)")
        
        # Ejecutar comando
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )
        
        # Mostrar salida relevante
        if result.stdout:
            lines = result.stdout.split('\n')
            for line in lines:
                # Filtrar solo líneas importantes
                if any(keyword in line for keyword in ['✅', '❌', '🎬', '🎨', '📊', '💾', '🚀', 'Error', 'ERROR']):
                    print(f"   {line}")
        
        if result.stderr:
            error_lines = result.stderr.split('\n')
            for line in error_lines:
                if line.strip() and 'Warning' not in line:
                    print(f"   ⚠️  {line}")
        
        # Verificar éxito
        if Path(glb_file).exists():
            file_size = Path(glb_file).stat().st_size / (1024 * 1024)
            print(f"✅ Exportación exitosa!")
            print(f"   📄 Archivo: {glb_file}")
            print(f"   📏 Tamaño: {file_size:.2f} MB")
            return True
        else:
            print(f"❌ La exportación falló - no se creó el archivo GLB")
            return False
            
    except Exception as e:
        print(f"❌ Error ejecutando Blender: {str(e)}")
        return False

def validate_glb(glb_file):
    """
    Valida que el GLB exportado contenga animaciones
    """
    
    if not Path(glb_file).exists():
        print(f"❌ Archivo GLB no encontrado: {glb_file}")
        return False
    
    print(f"🔍 Validando: {Path(glb_file).name}")
    
    try:
        # Ejecutar validador
        result = subprocess.run([
            sys.executable,
            str(TEST_SCRIPT),
            str(glb_file)
        ], capture_output=True, text=True)
        
        print(result.stdout)
        
        if result.stderr:
            print(result.stderr)
        
        # Buscar indicadores de éxito/fallo
        if "ANIMACIONES: 0" in result.stdout:
            print("❌ El GLB NO contiene animaciones!")
            return False
        elif "ANIMACIONES:" in result.stdout and not "ANIMACIONES: 0" in result.stdout:
            print("✅ El GLB contiene animaciones correctamente")
            return True
        else:
            print("⚠️  No se pudo determinar el estado de las animaciones")
            return None
            
    except Exception as e:
        print(f"❌ Error validando GLB: {str(e)}")
        return False

def create_test_html():
    """
    Crea archivo HTML de prueba para visualizar GLB en navegador
    """
    print("🌐 Creando archivo de prueba HTML...")
    
    try:
        result = subprocess.run([
            sys.executable,
            str(TEST_SCRIPT)
        ], capture_output=True, text=True)
        
        print(result.stdout)
        return True
        
    except Exception as e:
        print(f"❌ Error creando archivo de prueba: {str(e)}")
        return False

def main():
    """
    Función principal con ejemplo de uso completo
    """
    
    print("="*80)
    print("🎯 EJEMPLO DE USO: EXPORTADOR BLEND → GLB CON ANIMACIONES")
    print("="*80)
    
    # 1. Verificar Blender
    if not check_blender():
        return
    
    # 2. Solicitar archivo .blend
    print(f"\n📁 Introduce la ruta del archivo .blend:")
    print(f"   (Debe contener una armature con animaciones)")
    
    blend_file = input("Archivo .blend: ").strip().strip('"')
    
    if not blend_file:
        print("❌ No se especificó archivo")
        return
    
    # 3. Exportar
    print(f"\n🔄 PASO 1: Exportando BLEND → GLB")
    print("-" * 40)
    
    success = export_blend_to_glb(blend_file)
    
    if not success:
        print(f"\n💥 La exportación falló")
        print(f"💡 Posibles causas:")
        print(f"   • El archivo .blend no existe o está corrupto")
        print(f"   • No hay animaciones en el archivo")
        print(f"   • Problemas con materiales no compatibles con glTF")
        print(f"   • Blender no se pudo ejecutar")
        return
    
    # 4. Validar GLB
    glb_file = Path(blend_file).with_suffix('.glb')
    
    print(f"\n🔍 PASO 2: Validando GLB exportado")
    print("-" * 40)
    
    validation_result = validate_glb(glb_file)
    
    if validation_result is False:
        print(f"\n💥 El GLB no contiene animaciones!")
        print(f"💡 Posibles soluciones:")
        print(f"   • Verifica que el .blend tenga una armature")
        print(f"   • Verifica que la armature tenga una acción asignada")
        print(f"   • Verifica que la acción tenga keyframes")
        print(f"   • Abre el .blend en Blender y presiona ESPACIO para ver la animación")
        return
    elif validation_result is True:
        print(f"\n🎉 ¡Éxito! El GLB contiene animaciones")
    
    # 5. Crear archivo de prueba HTML
    print(f"\n🌐 PASO 3: Creando visualizador web")
    print("-" * 40)
    
    create_test_html()
    
    # 6. Instrucciones finales
    print(f"\n🏁 PROCESO COMPLETADO")
    print("="*40)
    print(f"✅ Archivo GLB creado: {glb_file.name}")
    print(f"🌐 Archivo de prueba: test_glb_animation.html")
    print(f"\n📋 PRÓXIMOS PASOS:")
    print(f"   1. Abre test_glb_animation.html en un navegador")
    print(f"   2. Introduce el nombre del archivo GLB cuando se solicite")
    print(f"   3. Verifica que la animación se reproduce correctamente")
    print(f"\n💡 OTROS USOS:")
    print(f"   • Importa el GLB en Three.js")
    print(f"   • Úsalo en Unity, Unreal Engine, etc.")
    print(f"   • Visualízalo en VS Code con extensión glTF Tools")

if __name__ == "__main__":
    main()