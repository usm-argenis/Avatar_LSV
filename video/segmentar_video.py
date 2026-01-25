"""
Script para segmentar videos
Permite cortar múltiples segmentos de un video especificando inicio y fin en segundos
Requiere: pip install moviepy
"""

from moviepy.editor import VideoFileClip
import os
from pathlib import Path


def segmentar_video(video_path, segmentos, carpeta_salida="output"):
    """
    Segmenta un video en múltiples clips
    
    Args:
        video_path (str): Ruta al video original
        segmentos (list): Lista de diccionarios con formato:
            [
                {"inicio": 0, "fin": 5, "nombre": "segmento1"},
                {"inicio": 10, "fin": 15, "nombre": "segmento2"},
            ]
        carpeta_salida (str): Carpeta donde guardar los segmentos
    """
    
    # Verificar que el video existe
    if not os.path.exists(video_path):
        print(f"❌ Error: El video '{video_path}' no existe")
        return
    
    # Crear carpeta de salida si no existe
    Path(carpeta_salida).mkdir(parents=True, exist_ok=True)
    
    print(f"📹 Cargando video: {video_path}")
    
    video = None
    try:
        # Cargar el video
        video = VideoFileClip(video_path)
        duracion_total = video.duration
        
        print(f"⏱️  Duración del video: {duracion_total:.2f} segundos")
        print(f"🎬 Procesando {len(segmentos)} segmento(s)...\n")
        
        # Procesar cada segmento
        segmentos_exitosos = 0
        segmentos_fallidos = 0
        
        for i, segmento in enumerate(segmentos, 1):
            inicio = segmento.get("inicio", 0)
            fin = segmento.get("fin", duracion_total)
            nombre = segmento.get("nombre", f"segmento_{i}")
            
            # Validar tiempos
            if inicio < 0 or fin > duracion_total or inicio >= fin:
                print(f"⚠️  Segmento {i} '{nombre}': Tiempos inválidos (inicio: {inicio}s, fin: {fin}s)")
                segmentos_fallidos += 1
                continue
            
            try:
                # Extraer el segmento
                print(f"✂️  Cortando segmento {i}/{len(segmentos)}: '{nombre}'")
                print(f"   Desde {inicio}s hasta {fin}s (duración: {fin-inicio}s)")
                
                clip = video.subclip(inicio, fin)
                
                # Guardar el segmento
                nombre_archivo = f"{nombre}.mp4"
                ruta_salida = os.path.join(carpeta_salida, nombre_archivo)
                
                # Configuración mejorada para evitar errores
                clip.write_videofile(
                    ruta_salida,
                    codec='libx264',
                    audio_codec='aac',
                    temp_audiofile=f'temp-audio-{i}.m4a',
                    remove_temp=True,
                    verbose=False,
                    logger=None,
                    threads=4,
                    preset='ultrafast'
                )
                
                print(f"✅ Guardado: {ruta_salida}\n")
                segmentos_exitosos += 1
                
                # Liberar memoria del clip
                clip.close()
                del clip
                
            except Exception as e:
                print(f"❌ Error en segmento '{nombre}': {e}")
                print(f"   Continuando con el siguiente segmento...\n")
                segmentos_fallidos += 1
                continue
        
        # Resumen final
        print("=" * 50)
        print(f"🎉 ¡Proceso completado!")
        print(f"✅ Segmentos exitosos: {segmentos_exitosos}/{len(segmentos)}")
        if segmentos_fallidos > 0:
            print(f"❌ Segmentos con errores: {segmentos_fallidos}/{len(segmentos)}")
        print(f"📁 Archivos guardados en: {os.path.abspath(carpeta_salida)}")
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ Error al procesar el video: {e}")
        import traceback
        traceback.print_exc()
    finally:
        # Asegurar que el video se cierre siempre
        if video is not None:
            try:
                video.close()
                del video
            except:
                pass


def ejemplo_uso():
    """
    Ejemplo de cómo usar el script
    """
    
    # Ruta al video original
    VIDEO_ORIGINAL = "mi_video.mp4"  # Cambia esto por tu video
    
    # Definir los segmentos a cortar
    # Puedes agregar tantos como quieras
    segmentos = [
        {
            "inicio": 0,      # Segundo inicial
            "fin": 5,         # Segundo final
            "nombre": "intro" # Nombre del archivo de salida
        },
        {
            "inicio": 10,
            "fin": 20,
            "nombre": "segunda_parte"
        },
        {
            "inicio": 30,
            "fin": 45,
            "nombre": "tercera_parte"
        },
        # Agrega más segmentos aquí...
    ]
    
    # Carpeta donde se guardarán los videos
    CARPETA_SALIDA = "videos_segmentados"
    
    # Ejecutar la segmentación
    segmentar_video(VIDEO_ORIGINAL, segmentos, CARPETA_SALIDA)


# Modo interactivo
def modo_interactivo():
    """
    Permite al usuario ingresar los datos manualmente
    """
    print("=" * 50)
    print("🎬 SEGMENTADOR DE VIDEOS")
    print("=" * 50)
    
    # Solicitar ruta del video
    video_path = input("\n📹 Ingresa la ruta del video: ").strip()
    
    # Solicitar carpeta de salida
    carpeta_salida = input("📁 Carpeta de salida (Enter para 'output'): ").strip()
    if not carpeta_salida:
        carpeta_salida = "output"
    
    # Solicitar cantidad de segmentos
    try:
        num_segmentos = int(input("\n✂️  ¿Cuántos segmentos quieres crear?: "))
    except ValueError:
        print("❌ Número inválido")
        return
    
    segmentos = []
    
    print("\n" + "=" * 50)
    print("Ingresa los datos de cada segmento:")
    print("=" * 50)
    
    for i in range(num_segmentos):
        print(f"\n--- Segmento {i+1} ---")
        
        try:
            inicio = float(input("⏱️  Segundo de inicio: "))
            fin = float(input("⏱️  Segundo de fin: "))
            nombre = input("📝 Nombre del segmento: ").strip()
            
            if not nombre:
                nombre = f"segmento_{i+1}"
            
            segmentos.append({
                "inicio": inicio,
                "fin": fin,
                "nombre": nombre
            })
            
        except ValueError:
            print("⚠️  Valores inválidos, segmento omitido")
    
    if segmentos:
        print("\n" + "=" * 50)
        segmentar_video(video_path, segmentos, carpeta_salida)
    else:
        print("❌ No hay segmentos para procesar")


if __name__ == "__main__":
    # Descomentar la opción que quieras usar:
    
    # Opción 1: Modo interactivo (recomendado para principiantes)
    modo_interactivo()
    
    # Opción 2: Usar el ejemplo predefinido
    # ejemplo_uso()
    
    # Opción 3: Personalizar directamente aquí
    """
    segmentar_video(
        video_path="mi_video.mp4",
        segmentos=[
            {"inicio": 0, "fin": 10, "nombre": "primera_seña"},
            {"inicio": 15, "fin": 25, "nombre": "segunda_seña"},
            {"inicio": 30, "fin": 40, "nombre": "tercera_seña"},
        ],
        carpeta_salida="senas_cortadas"
    )
    """
