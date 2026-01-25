"""
Ejemplo de uso con datos predefinidos
Edita los valores según tus necesidades y ejecuta este archivo
"""

from segmentar_video import segmentar_video

# ========================================
# CONFIGURACIÓN
# ========================================

# Ruta al video original
VIDEO_ORIGINAL = "pronombres.mp4"  # 👈 CAMBIA ESTO

# Carpeta donde se guardarán los segmentos
CARPETA_SALIDA = "videos_segmentados"  # 👈 CAMBIA ESTO si quieres

# ========================================
# DEFINE TUS SEGMENTOS AQUÍ
# ========================================

segmentos = [
    # Ejemplo 1: Letras del alfabeto
    {"inicio": 3, "fin": 5, "nombre": "tu"},
    {"inicio": 5, "fin": 7, "nombre": "yo"},
    {"inicio": 7, "fin": 9, "nombre": "el"},
    {"inicio": 9, "fin": 12, "nombre": "ella"},
    {"inicio": 12, "fin": 14, "nombre": "nosotros"},
    
    # Agrega más segmentos copiando el formato:
    # {"inicio": SEGUNDO_INICIO, "fin": SEGUNDO_FIN, "nombre": "nombre_archivo"},
]

# ========================================
# OTROS EJEMPLOS (Comenta/Descomenta)
# ========================================

# Ejemplo 2: Palabras completas
"""
segmentos = [
    {"inicio": 0, "fin": 5, "nombre": "hola"},
    {"inicio": 5, "fin": 10, "nombre": "buenos_dias"},
    {"inicio": 10, "fin": 15, "nombre": "gracias"},
    {"inicio": 15, "fin": 20, "nombre": "por_favor"},
    {"inicio": 20, "fin": 25, "nombre": "adios"},
]
"""

# Ejemplo 3: Números
"""
segmentos = [
    {"inicio": 0, "fin": 3, "nombre": "numero_1"},
    {"inicio": 3, "fin": 6, "nombre": "numero_2"},
    {"inicio": 6, "fin": 9, "nombre": "numero_3"},
    {"inicio": 9, "fin": 12, "nombre": "numero_4"},
    {"inicio": 12, "fin": 15, "nombre": "numero_5"},
]
"""

# Ejemplo 4: Con decimales (precisión)
"""
segmentos = [
    {"inicio": 0.5, "fin": 3.2, "nombre": "seña_1"},
    {"inicio": 5.8, "fin": 9.1, "nombre": "seña_2"},
    {"inicio": 12.3, "fin": 15.7, "nombre": "seña_3"},
]
"""

# ========================================
# EJECUTAR
# ========================================

if __name__ == "__main__":
    print("🎬 Iniciando segmentación de video...")
    print(f"📹 Video: {VIDEO_ORIGINAL}")
    print(f"📁 Salida: {CARPETA_SALIDA}")
    print(f"✂️  Segmentos a crear: {len(segmentos)}\n")
    
    segmentar_video(VIDEO_ORIGINAL, segmentos, CARPETA_SALIDA)
