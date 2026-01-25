"""
Script para procesar múltiples videos a la vez
Útil cuando tienes varios videos de señas y quieres cortarlos todos
"""

from segmentar_video import segmentar_video
import os

# ========================================
# LISTA DE VIDEOS A PROCESAR
# ========================================

videos_a_procesar = [
    {
        "video": "alfabeto_parte1.mp4",
        "carpeta_salida": "alfabeto",
        "segmentos": [
            {"inicio": 0, "fin": 2, "nombre": "a"},
            {"inicio": 2, "fin": 4, "nombre": "b"},
            {"inicio": 4, "fin": 6, "nombre": "c"},
            {"inicio": 6, "fin": 8, "nombre": "d"},
            {"inicio": 8, "fin": 10, "nombre": "e"},
        ]
    },
    {
        "video": "numeros.mp4",
        "carpeta_salida": "numeros",
        "segmentos": [
            {"inicio": 0, "fin": 3, "nombre": "uno"},
            {"inicio": 3, "fin": 6, "nombre": "dos"},
            {"inicio": 6, "fin": 9, "nombre": "tres"},
            {"inicio": 9, "fin": 12, "nombre": "cuatro"},
            {"inicio": 12, "fin": 15, "nombre": "cinco"},
        ]
    },
    {
        "video": "saludos.mp4",
        "carpeta_salida": "saludos",
        "segmentos": [
            {"inicio": 0, "fin": 5, "nombre": "hola"},
            {"inicio": 5, "fin": 10, "nombre": "buenos_dias"},
            {"inicio": 10, "fin": 15, "nombre": "buenas_tardes"},
            {"inicio": 15, "fin": 20, "nombre": "buenas_noches"},
            {"inicio": 20, "fin": 25, "nombre": "adios"},
        ]
    },
    # Agrega más videos aquí...
]

# ========================================
# FUNCIÓN PARA PROCESAR TODOS
# ========================================

def procesar_todos_los_videos():
    """
    Procesa todos los videos definidos en la lista
    """
    total_videos = len(videos_a_procesar)
    
    print("=" * 60)
    print("🎬 PROCESADOR MASIVO DE VIDEOS")
    print("=" * 60)
    print(f"\n📊 Total de videos a procesar: {total_videos}\n")
    
    videos_exitosos = 0
    videos_fallidos = 0
    
    for i, config in enumerate(videos_a_procesar, 1):
        video = config["video"]
        carpeta_salida = config["carpeta_salida"]
        segmentos = config["segmentos"]
        
        print("\n" + "=" * 60)
        print(f"📹 VIDEO {i}/{total_videos}: {video}")
        print("=" * 60)
        
        # Verificar si el video existe
        if not os.path.exists(video):
            print(f"⚠️  ADVERTENCIA: El video '{video}' no existe. Omitiendo...")
            videos_fallidos += 1
            continue
        
        try:
            segmentar_video(video, segmentos, carpeta_salida)
            videos_exitosos += 1
        except Exception as e:
            print(f"❌ Error procesando '{video}': {e}")
            videos_fallidos += 1
    
    # Resumen final
    print("\n" + "=" * 60)
    print("📊 RESUMEN FINAL")
    print("=" * 60)
    print(f"✅ Videos procesados exitosamente: {videos_exitosos}/{total_videos}")
    if videos_fallidos > 0:
        print(f"❌ Videos con errores: {videos_fallidos}/{total_videos}")
    print("=" * 60)


# ========================================
# EJECUTAR
# ========================================

if __name__ == "__main__":
    procesar_todos_los_videos()
