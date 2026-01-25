"""
Script simple para convertir los archivos _skel.json existentes a formato SignAvatar.
"""
import sys
from pathlib import Path

# Agregar test al path para importar convert_to_signavatar
test_dir = Path(__file__).resolve().parents[1] / 'test'
sys.path.insert(0, str(test_dir))

from convert_to_signavatar import convert_to_signavatar_format

# Rutas
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_SKELETONS = PROJECT_ROOT / 'data' / 'skeletons'
TEST_OUTPUT = PROJECT_ROOT / 'test' / 'output'

# Videos a convertir
VIDEOS = ['b', 'c', 'd', 'e']

def main():
    print("🔄 Convirtiendo archivos esqueleto a formato SignAvatar...")
    
    TEST_OUTPUT.mkdir(parents=True, exist_ok=True)
    
    for video_name in VIDEOS:
        input_file = DATA_SKELETONS / f"{video_name}_skel.json"
        output_file = TEST_OUTPUT / f"{video_name}_signavatar.json"
        
        if not input_file.exists():
            print(f"❌ No existe: {input_file}")
            continue
        
        try:
            convert_to_signavatar_format(str(input_file), str(output_file))
            print(f"✅ {video_name}: {output_file}")
        except Exception as e:
            print(f"❌ Error en {video_name}: {e}")
    
    print("\n✅ Conversión completada")

if __name__ == "__main__":
    main()
