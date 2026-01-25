"""
Generar TODAS las animaciones pendientes de Carlos
"""
import json
import subprocess
import sys
from pathlib import Path

# Definir todas las animaciones que deben existir
CATEGORIAS = {
    'alfabeto': ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                 'uno', 'dos', 'tres'],
    'dias_semana': ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 
                    'domingo', 'manana', 'ayer'],
    'tiempo': ['dia', 'semana', 'mes', 'año', 'hora', 'minuto', 'segundo'],
    'pronombres': ['yo', 'tu', 'el', 'ella', 'nosotros', 'ustedes', 'ellos', 'ellas'],
    'saludos': ['hola', 'adios', 'buenos_dias', 'buenas_tardes', 'buenas_noches', 
                'bienvenido', 'hasta_luego', 'nos_vemos', 'mucho_gusto'],
    'cortesia': ['gracias', 'por_favor', 'perdon', 'disculpa', 'de_nada', 'lo_siento'],
    'preguntas': ['que', 'como'],
    'expresiones': ['si', 'no']
}

BLENDER_PATH = r"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe"
SCRIPT_PATH = "scripts/generar_carlos_individual.py"

def obtener_pendientes():
    """Obtener lista de animaciones pendientes"""
    progreso_path = Path("test/output/glb/progreso_carlos.json")
    
    procesados = set()
    if progreso_path.exists():
        with open(progreso_path, 'r', encoding='utf-8') as f:
            rutas_procesadas = json.load(f)
            for ruta in rutas_procesadas:
                nombre = Path(ruta).stem.replace('Carlos_resultado_', '')
                procesados.add(nombre)
    
    # Crear lista completa
    todas = []
    for categoria, nombres in CATEGORIAS.items():
        todas.extend(nombres)
    
    pendientes = sorted(set(todas) - procesados)
    return pendientes, procesados

def procesar_animacion(nombre):
    """Procesar una animación individual"""
    try:
        cmd = [BLENDER_PATH, "--background", "--python", SCRIPT_PATH, "--", nombre]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print(f"⏱️ TIMEOUT: {nombre} (más de 2 minutos)")
        return False
    except Exception as e:
        print(f"❌ ERROR: {nombre} - {str(e)}")
        return False

def main():
    print("\n" + "="*60)
    print("GENERADOR AUTOMÁTICO DE ANIMACIONES CARLOS")
    print("="*60 + "\n")
    
    # Obtener pendientes
    pendientes, procesados = obtener_pendientes()
    
    if not pendientes:
        print("✅ ¡TODAS LAS ANIMACIONES YA ESTÁN PROCESADAS!")
        print(f"Total: {len(procesados)} animaciones")
        print("="*60 + "\n")
        return
    
    total = len(pendientes)
    print(f"📊 Estado actual:")
    print(f"   Procesadas: {len(procesados)}")
    print(f"   Pendientes: {total}")
    print("\n" + "="*60 + "\n")
    
    print("🚀 Iniciando procesamiento automático...\n")
    
    exitosos = 0
    errores = 0
    
    # Procesar por categoría
    for idx, (categoria, nombres) in enumerate(CATEGORIAS.items(), 1):
        pendientes_cat = [n for n in nombres if n in pendientes]
        
        if not pendientes_cat:
            continue
        
        print(f"\n[{idx}/8] 📁 CATEGORÍA: {categoria.upper()}")
        print("-" * 60)
        print(f"Pendientes en esta categoría: {len(pendientes_cat)}\n")
        
        for i, nombre in enumerate(pendientes_cat, 1):
            print(f"  [{i}/{len(pendientes_cat)}] Procesando: {nombre}...", end=" ", flush=True)
            
            if procesar_animacion(nombre):
                print("✅ OK")
                exitosos += 1
            else:
                print("❌ ERROR")
                errores += 1
    
    # Resumen final
    print("\n" + "="*60)
    print("RESUMEN FINAL")
    print("="*60)
    print(f"Total procesados: {exitosos + errores}")
    print(f"✅ Exitosos: {exitosos}")
    print(f"❌ Errores: {errores}")
    
    if errores > 0:
        print(f"\n⚠️ Algunos archivos fallaron ({errores})")
        print("Ejecuta de nuevo el script para reintentar los errores")
    else:
        print("\n🎉 ¡TODAS LAS ANIMACIONES GENERADAS EXITOSAMENTE!")
    
    print("\n📂 Archivos en: test/output/glb/Carlos/")
    print("="*60 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Proceso interrumpido por el usuario")
        print("El progreso se ha guardado automáticamente")
        sys.exit(1)
