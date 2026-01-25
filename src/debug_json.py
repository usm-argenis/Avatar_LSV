import json
from pathlib import Path

# Leer archivo directamente
json_file = Path("data/keypoints/yo.json")
with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Archivo JSON yo.json:")
print(f"  Keys: {list(data.keys())}")
print(f"  sign_name: {data.get('sign_name')}")
print(f"  keyframes type: {type(data.get('keyframes'))}")
print(f"  keyframes length: {len(data.get('keyframes', []))}")

if data.get('keyframes'):
    print(f"\nPrimer keyframe:")
    print(f"  Keys: {list(data['keyframes'][0].keys())}")
    print(f"  frame: {data['keyframes'][0].get('frame')}")
    print(f"  time: {data['keyframes'][0].get('time')}")

# Simular carga como lo hace MotionGenerator
sign_database = {}
for json_path in Path("data/keypoints").glob("*.json"):
    with open(json_path, 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
        sign_name = json_path.stem
        sign_database[sign_name.lower()] = loaded_data

print(f"\nBase de datos cargada: {len(sign_database)} señas")
print(f"Señas: {list(sign_database.keys())}")

yo_from_db = sign_database.get('yo')
print(f"\nyo desde DB:")
print(f"  Type: {type(yo_from_db)}")
print(f"  Keys: {list(yo_from_db.keys()) if yo_from_db else 'None'}")
print(f"  keyframes: {yo_from_db.get('keyframes') if yo_from_db else 'None'}")
