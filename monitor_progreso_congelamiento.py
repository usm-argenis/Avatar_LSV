"""
Monitor de Progreso del Congelamiento de Tren Inferior
Muestra el progreso en tiempo real mientras se ejecuta el script de Blender
"""

import json
import time
import sys
from pathlib import Path
from datetime import datetime

PROGRESS_FILE = Path("freeze_progress.json")
LOG_FILE = Path("freeze_log.txt")
CARLA_FOLDER = Path("test") / "output" / "glb" / "Carla"

def clear_screen():
    """Limpia la pantalla"""
    print("\033[2J\033[H", end="")

def format_time_elapsed(seconds):
    """Formatea segundos a formato legible"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    
    if hours > 0:
        return f"{hours}h {minutes}m {secs}s"
    elif minutes > 0:
        return f"{minutes}m {secs}s"
    else:
        return f"{secs}s"

def estimate_time_remaining(processed, total, elapsed):
    """Estima tiempo restante"""
    if processed == 0:
        return "Calculando..."
    
    avg_time_per_file = elapsed / processed
    remaining_files = total - processed
    remaining_seconds = avg_time_per_file * remaining_files
    
    return format_time_elapsed(remaining_seconds)

def get_progress_bar(current, total, width=40):
    """Genera una barra de progreso"""
    if total == 0:
        return "[" + " " * width + "] 0%"
    
    percentage = current / total
    filled = int(width * percentage)
    bar = "█" * filled + "░" * (width - filled)
    
    return f"[{bar}] {percentage*100:.1f}%"

def get_last_log_lines(n=5):
    """Obtiene las últimas n líneas del log"""
    if not LOG_FILE.exists():
        return []
    
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return [line.strip() for line in lines[-n:]]
    except:
        return []

def monitor_progress():
    """Monitorea el progreso continuamente"""
    print("🔍 Monitor de Progreso - Congelamiento de Tren Inferior")
    print("=" * 80)
    print("\nPresiona Ctrl+C para salir del monitor")
    print("El proceso de Blender continuará ejecutándose en segundo plano\n")
    
    start_time = None
    last_processed = 0
    
    try:
        while True:
            clear_screen()
            
            print("=" * 80)
            print("🔒 MONITOR DE CONGELAMIENTO DE TREN INFERIOR")
            print("=" * 80)
            print()
            
            # Leer progreso
            if PROGRESS_FILE.exists():
                try:
                    with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                        progress = json.load(f)
                    
                    processed = progress.get('processed_count', 0)
                    failed = progress.get('failed_count', 0)
                    total = progress.get('total_files', 0)
                    last_file = Path(progress.get('last_processed_file', '')).name
                    timestamp = progress.get('timestamp', '')
                    
                    # Calcular tiempo transcurrido
                    if start_time is None:
                        start_time = time.time()
                    
                    elapsed = time.time() - start_time
                    
                    # Estado
                    print(f"📊 PROGRESO GENERAL:")
                    print(f"   {get_progress_bar(processed, total, 50)}")
                    print(f"   Procesados: {processed}/{total} archivos")
                    print(f"   Fallidos: {failed}")
                    print(f"   Éxito: {processed - failed}")
                    print()
                    
                    # Tiempo
                    print(f"⏱️  TIEMPO:")
                    print(f"   Transcurrido: {format_time_elapsed(elapsed)}")
                    print(f"   Estimado restante: {estimate_time_remaining(processed, total, elapsed)}")
                    print()
                    
                    # Archivo actual
                    print(f"📄 ÚLTIMO ARCHIVO:")
                    print(f"   {last_file}")
                    print(f"   Actualizado: {timestamp}")
                    print()
                    
                    # Velocidad
                    if elapsed > 0:
                        files_per_minute = (processed / elapsed) * 60
                        print(f"🚀 VELOCIDAD:")
                        print(f"   {files_per_minute:.2f} archivos/minuto")
                        if processed > 0:
                            avg_time = elapsed / processed
                            print(f"   ~{avg_time:.1f}s por archivo")
                        print()
                    
                    # Logs recientes
                    print(f"📝 ÚLTIMOS LOGS:")
                    logs = get_last_log_lines(5)
                    if logs:
                        for log in logs:
                            # Acortar logs muy largos
                            if len(log) > 100:
                                log = log[:97] + "..."
                            print(f"   {log}")
                    else:
                        print("   (sin logs recientes)")
                    
                except Exception as e:
                    print(f"⚠️  Error leyendo progreso: {e}")
            else:
                print("⏳ Esperando que comience el procesamiento...")
                print()
                print("   El archivo freeze_progress.json aún no existe.")
                print("   Esto es normal si el script acaba de iniciar.")
            
            print()
            print("=" * 80)
            print("Actualizando cada 2 segundos... (Ctrl+C para salir)")
            
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n\n👋 Monitor detenido. El proceso de Blender continúa ejecutándose.")
        print()

def show_final_summary():
    """Muestra resumen final del progreso"""
    print("\n" + "=" * 80)
    print("📊 RESUMEN FINAL")
    print("=" * 80)
    
    if PROGRESS_FILE.exists():
        try:
            with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                progress = json.load(f)
            
            processed = progress.get('processed_count', 0)
            failed = progress.get('failed_count', 0)
            total = progress.get('total_files', 0)
            
            print(f"\n✅ Procesados exitosamente: {processed - failed}")
            print(f"❌ Fallidos: {failed}")
            print(f"📊 Total: {processed}/{total}")
            
            if processed == total and failed == 0:
                print("\n🎉 ¡COMPLETADO EXITOSAMENTE!")
            elif processed < total:
                print(f"\n⏸️  Progreso guardado. Faltan {total - processed} archivos.")
                print("   Usa --reanudar para continuar")
            
        except Exception as e:
            print(f"\n⚠️  Error leyendo resumen: {e}")
    else:
        print("\n⚠️  No hay archivo de progreso disponible")
    
    print("=" * 80 + "\n")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--resumen":
        show_final_summary()
    else:
        try:
            monitor_progress()
        except Exception as e:
            print(f"\n❌ Error: {e}")
            import traceback
            traceback.print_exc()
