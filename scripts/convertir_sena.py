"""
Script Automatizado: Transferir Animación de Seña a Avatar

Este script simplifica el proceso de transferir cualquier animación FBX
al avatar Standing Torch, haciendo retargeting automático de los huesos.

USO:
    python convertir_sena.py

Luego sigue las instrucciones en pantalla.
"""

import os
import sys
import subprocess
from pathlib import Path

# ====================
# CONFIGURACIÓN
# ====================

# Rutas por defecto
BLENDER_PATH = r"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe"
AVATAR_PATH = r"C:\Users\andre\Downloads\Standing Torch Light Torch.fbx"
SCRIPT_PATH = Path(__file__).parent / "simple_transfer.py"

# Directorio de salida por defecto
DEFAULT_OUTPUT_DIR = r"C:\Users\andre\Downloads\abecedario"

# ====================
# COLORES PARA CONSOLA
# ====================

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*70}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{text.center(70)}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*70}{Colors.ENDC}\n")

def print_success(text):
    print(f"{Colors.OKGREEN}✅ {text}{Colors.ENDC}")

def print_error(text):
    print(f"{Colors.FAIL}❌ {text}{Colors.ENDC}")

def print_info(text):
    print(f"{Colors.OKCYAN}ℹ️  {text}{Colors.ENDC}")

def print_warning(text):
    print(f"{Colors.WARNING}⚠️  {text}{Colors.ENDC}")

# ====================
# FUNCIONES
# ====================

def verificar_blender():
    """Verifica que Blender esté instalado"""
    if not os.path.exists(BLENDER_PATH):
        print_error("No se encontró Blender en la ruta configurada.")
        print_info(f"Ruta buscada: {BLENDER_PATH}")
        print_info("Por favor edita la variable BLENDER_PATH en este script.")
        return False
    return True

def verificar_avatar():
    """Verifica que el avatar existe"""
    if not os.path.exists(AVATAR_PATH):
        print_error("No se encontró el avatar Standing Torch.")
        print_info(f"Ruta buscada: {AVATAR_PATH}")
        print_info("Por favor edita la variable AVATAR_PATH en este script.")
        return False
    return True

def verificar_script_blender():
    """Verifica que el script de Blender existe"""
    if not SCRIPT_PATH.exists():
        print_error("No se encontró el script simple_transfer.py")
        print_info(f"Ruta buscada: {SCRIPT_PATH}")
        return False
    return True

def solicitar_archivo_animacion():
    """Solicita al usuario la ruta del archivo FBX con la animación"""
    print_info("Ingresa la ruta completa del archivo FBX con la animación de la seña:")
    print_info("Ejemplo: C:\\Users\\andre\\Downloads\\abecedario\\b_hXBrhdpmbtpo6dwf3zVGyw.fbx")
    print()
    
    while True:
        ruta = input(f"{Colors.OKCYAN}Ruta del FBX: {Colors.ENDC}").strip().strip('"').strip("'")
        
        if not ruta:
            print_error("La ruta no puede estar vacía.")
            continue
        
        if not os.path.exists(ruta):
            print_error(f"El archivo no existe: {ruta}")
            continuar = input("¿Intentar con otra ruta? (s/n): ").lower()
            if continuar != 's':
                return None
            continue
        
        if not ruta.lower().endswith('.fbx'):
            print_error("El archivo debe ser un FBX (.fbx)")
            continue
        
        return ruta

def solicitar_nombre_salida(ruta_animacion):
    """Solicita el nombre para el archivo de salida"""
    # Extraer nombre del archivo de animación
    nombre_base = Path(ruta_animacion).stem
    
    # Sugerir nombre basado en el archivo de entrada
    sugerencia = f"resultado_{nombre_base}.fbx"
    
    print()
    print_info(f"Nombre sugerido para el archivo de salida: {sugerencia}")
    print_info("Presiona ENTER para usar el nombre sugerido, o escribe uno nuevo:")
    
    nombre = input(f"{Colors.OKCYAN}Nombre: {Colors.ENDC}").strip()
    
    if not nombre:
        nombre = sugerencia
    
    if not nombre.lower().endswith('.fbx'):
        nombre += '.fbx'
    
    return nombre

def crear_script_temporal(ruta_animacion, ruta_salida):
    """Crea un script de Blender temporal con las rutas configuradas"""
    
    # Leer el script original
    with open(SCRIPT_PATH, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Reemplazar las rutas
    contenido_modificado = contenido.replace(
        'PIEL_FBX = r"C:\\Users\\andre\\Downloads\\Standing Torch Light Torch.fbx"',
        f'PIEL_FBX = r"{AVATAR_PATH}"'
    )
    
    contenido_modificado = contenido_modificado.replace(
        'ANIMACION_FBX = r"C:\\Users\\andre\\Downloads\\abecedario\\b_hXBrhdpmbtpo6dwf3zVGyw.fbx"',
        f'ANIMACION_FBX = r"{ruta_animacion}"'
    )
    
    contenido_modificado = contenido_modificado.replace(
        'OUTPUT_FBX = r"C:\\Users\\andre\\Downloads\\abecedario\\resultado_b.fbx"',
        f'OUTPUT_FBX = r"{ruta_salida}"'
    )
    
    # Guardar script temporal
    script_temp = SCRIPT_PATH.parent / "temp_transfer.py"
    with open(script_temp, 'w', encoding='utf-8') as f:
        f.write(contenido_modificado)
    
    return script_temp

def ejecutar_conversion(ruta_animacion, ruta_salida):
    """Ejecuta el proceso de conversión usando Blender"""
    
    print_header("EJECUTANDO CONVERSIÓN")
    
    # Crear script temporal
    print_info("Preparando script de Blender...")
    script_temp = crear_script_temporal(ruta_animacion, ruta_salida)
    
    # Comando de Blender
    comando = [
        BLENDER_PATH,
        '--background',
        '--python',
        str(script_temp)
    ]
    
    print_info("Ejecutando Blender...")
    print_info("(Esto puede tomar unos segundos...)")
    print()
    
    try:
        # Ejecutar Blender
        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )
        
        # Mostrar salida relevante
        if resultado.stdout:
            # Filtrar solo las líneas importantes
            lineas = resultado.stdout.split('\n')
            for linea in lineas:
                if any(keyword in linea for keyword in ['✓', '✅', '❌', '⚠️', 'PASO', 'Error', 'ERROR']):
                    print(linea)
        
        # Verificar si se creó el archivo
        if os.path.exists(ruta_salida):
            print()
            print_success("¡Conversión completada exitosamente!")
            print_info(f"Archivo generado: {ruta_salida}")
            
            # Mostrar tamaño del archivo
            tamaño = os.path.getsize(ruta_salida) / (1024 * 1024)  # MB
            print_info(f"Tamaño: {tamaño:.2f} MB")
            
            # Copiar al directorio test para visualización web
            try:
                test_dir = Path(__file__).parent.parent / "test"
                archivo_test = test_dir / Path(ruta_salida).name
                
                import shutil
                shutil.copy2(ruta_salida, archivo_test)
                
                print()
                print_success("Archivo copiado al visualizador web")
                print_info(f"Ruta: {archivo_test}")
                print_info("Puedes verlo en: http://localhost:8000/test/visualizador_senas.html")
            except Exception as e:
                print_warning(f"No se pudo copiar al directorio test: {e}")
            
            return True
        else:
            print()
            print_error("El proceso de Blender no generó el archivo de salida.")
            print_error("Revisa los mensajes de error arriba.")
            return False
        
    except Exception as e:
        print_error(f"Error al ejecutar Blender: {str(e)}")
        return False
    
    finally:
        # Limpiar script temporal
        if script_temp.exists():
            script_temp.unlink()

def mostrar_resumen(ruta_animacion, ruta_salida):
    """Muestra un resumen del proceso"""
    print_header("RESUMEN")
    
    print(f"{Colors.BOLD}Archivo de animación:{Colors.ENDC}")
    print(f"  {ruta_animacion}")
    print()
    
    print(f"{Colors.BOLD}Avatar utilizado:{Colors.ENDC}")
    print(f"  {AVATAR_PATH}")
    print()
    
    print(f"{Colors.BOLD}Archivo generado:{Colors.ENDC}")
    print(f"  {ruta_salida}")
    print()
    
    print_info("Próximos pasos:")
    print("  1. Importa el FBX en Blender para verificar")
    print("  2. Presiona ESPACIO para ver la animación")
    print("  3. Si todo está bien, úsalo en tu proyecto")
    print()

# ====================
# PROCESO PRINCIPAL
# ====================

def main():
    print_header("🎭 CONVERTIDOR DE SEÑAS - LSV")
    
    print("Este script automatiza la transferencia de animaciones FBX")
    print("al avatar Standing Torch con retargeting automático.")
    print()
    
    # Verificaciones previas
    print_info("Verificando requisitos...")
    
    if not verificar_blender():
        return 1
    print_success("Blender encontrado")
    
    if not verificar_avatar():
        return 1
    print_success("Avatar encontrado")
    
    if not verificar_script_blender():
        return 1
    print_success("Script de Blender encontrado")
    
    print()
    
    # Solicitar archivo de animación
    print_header("CONFIGURACIÓN")
    
    ruta_animacion = solicitar_archivo_animacion()
    if not ruta_animacion:
        print_error("Operación cancelada por el usuario.")
        return 1
    
    print_success(f"Archivo de animación: {Path(ruta_animacion).name}")
    
    # Solicitar nombre de salida
    nombre_salida = solicitar_nombre_salida(ruta_animacion)
    
    # Crear directorio de salida si no existe
    os.makedirs(DEFAULT_OUTPUT_DIR, exist_ok=True)
    ruta_salida = os.path.join(DEFAULT_OUTPUT_DIR, nombre_salida)
    
    print_success(f"Archivo de salida: {nombre_salida}")
    
    # Confirmar
    print()
    print_warning("¿Proceder con la conversión?")
    confirmar = input(f"{Colors.OKCYAN}(s/n): {Colors.ENDC}").lower()
    
    if confirmar != 's':
        print_info("Operación cancelada.")
        return 0
    
    # Ejecutar conversión
    exito = ejecutar_conversion(ruta_animacion, ruta_salida)
    
    if exito:
        mostrar_resumen(ruta_animacion, ruta_salida)
        return 0
    else:
        print_error("La conversión falló.")
        return 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print()
        print_warning("Operación cancelada por el usuario (Ctrl+C)")
        sys.exit(1)
    except Exception as e:
        print_error(f"Error inesperado: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
