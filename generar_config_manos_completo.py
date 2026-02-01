import os
import json
from pathlib import Path

def generar_configuracion_manos_completa():
    """
    Genera configuración para procesar TODOS los videos de manos
    y aplicar modificaciones a GLB de Duvall y Carla
    """
    
    base_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis")
    videos_path = base_path / "test" / "output" / "videos"
    output_hand_analysis = base_path / "output" / "hand_analysis"
    
    # Carpetas a procesar en Duvall y Carla
    categorias = [
        "dias_semana",
        "saludos",
        "cortesia",
        "expresiones",
        "tiempo",
        "personas",
        "profesion",
        "preguntas",
        "pronombres",
        "numero",
        "numeros ordinales",
        "verbos",
        "alfabeto",
        "adverbios lugares",
        "estado civil",
        "medios transporte",
        "preposicion",
        "tipos de vivienda"
    ]
    
    # Recopilar todos los videos .mp4
    videos = []
    for video_file in videos_path.glob("*.mp4"):
        # Excluir videos de alfabeto (están en subcarpeta)
        video_name = video_file.stem
        videos.append(video_name)
    
    print(f"✅ Encontrados {len(videos)} videos")
    
    # Crear configuración para procesar videos
    config_videos = {
        "videos": [],
        "output_dir": str(output_hand_analysis)
    }
    
    for video_name in sorted(videos):
        video_path = videos_path / f"{video_name}.mp4"
        if video_path.exists():
            config_videos["videos"].append({
                "nombre": video_name,
                "path": str(video_path),
                "json_output": str(output_hand_analysis / f"{video_name}_hands.json")
            })
    
    # Guardar configuración de videos
    config_videos_path = base_path / "config_procesar_videos_manos.json"
    with open(config_videos_path, 'w', encoding='utf-8') as f:
        json.dump(config_videos, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Guardado: {config_videos_path}")
    print(f"   Total videos: {len(config_videos['videos'])}")
    
    # Crear configuración para aplicar a GLB
    # Para cada categoría, buscar archivos GLB en Duvall y Carla
    
    glb_base_duvall = base_path / "test" / "output" / "glb" / "Duvall"
    glb_base_carla = base_path / "test" / "output" / "glb" / "Carla"
    
    config_aplicar = {
        "Duvall": {},
        "Carla": {}
    }
    
    for categoria in categorias:
        # Duvall
        cat_path_duvall = glb_base_duvall / categoria
        if cat_path_duvall.exists():
            glb_files = list(cat_path_duvall.glob("Duvall_resultado_*.glb"))
            # Excluir archivos ya modificados
            glb_files = [f for f in glb_files if "_MANOS" not in f.stem and "_modif" not in f.stem]
            
            if glb_files:
                config_aplicar["Duvall"][categoria] = {
                    "carpeta": str(cat_path_duvall),
                    "archivos": [f.name for f in sorted(glb_files)]
                }
        
        # Carla
        cat_path_carla = glb_base_carla / categoria
        if cat_path_carla.exists():
            glb_files = list(cat_path_carla.glob("Carla_resultado_*.glb"))
            glb_files = [f for f in glb_files if "_MANOS" not in f.stem and "_modif" not in f.stem]
            
            if glb_files:
                config_aplicar["Carla"][categoria] = {
                    "carpeta": str(cat_path_carla),
                    "archivos": [f.name for f in sorted(glb_files)]
                }
    
    # Guardar configuración de aplicación
    config_aplicar_path = base_path / "config_aplicar_manos_glb.json"
    with open(config_aplicar_path, 'w', encoding='utf-8') as f:
        json.dump(config_aplicar, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Guardado: {config_aplicar_path}")
    
    # Contar archivos
    total_duvall = sum(len(cat['archivos']) for cat in config_aplicar['Duvall'].values())
    total_carla = sum(len(cat['archivos']) for cat in config_aplicar['Carla'].values())
    
    print(f"   Duvall: {len(config_aplicar['Duvall'])} categorías, {total_duvall} archivos GLB")
    print(f"   Carla: {len(config_aplicar['Carla'])} categorías, {total_carla} archivos GLB")
    
    print(f"\n{'='*60}")
    print("✅ CONFIGURACIONES GENERADAS")
    print(f"{'='*60}")
    print(f"1. {config_videos_path.name}")
    print(f"2. {config_aplicar_path.name}")
    print(f"{'='*60}\n")
    
    return config_videos_path, config_aplicar_path


if __name__ == "__main__":
    generar_configuracion_manos_completa()
