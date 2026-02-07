"""
Script para agregar palabras necesarias para la defensa del TEG
"""
import json
from pathlib import Path

# Palabras nuevas a agregar
nuevas_palabras = {
    # Para frases de defensa
    "defensa": {
        "categoria": "general",
        "archivo": "defensa"
    },
    "teg": {
        "categoria": "general",
        "archivo": "teg"
    },
    "trabajo": {
        "categoria": "general",
        "archivo": "trabajo"
    },
    "especial": {
        "categoria": "general",
        "archivo": "especial"
    },
    "grado": {
        "categoria": "general",
        "archivo": "grado"
    },
    "aporte": {
        "categoria": "general",
        "archivo": "aporte"
    },
    "tecnologico": {
        "categoria": "general",
        "archivo": "tecnologico"
    },
    "tecnologia": {
        "categoria": "general",
        "archivo": "tecnologia"
    },
    "integracion": {
        "categoria": "general",
        "archivo": "integracion"
    },
    "integrar": {
        "categoria": "verbos",
        "archivo": "integrar"
    },
    "comunidad": {
        "categoria": "general",
        "archivo": "comunidad"
    },
    "venezuela": {
        "categoria": "lugares",
        "archivo": "venezuela"
    },
    "venezolano": {
        "categoria": "general",
        "archivo": "venezolano"
    },
    "miembro": {
        "categoria": "general",
        "archivo": "miembro"
    },
    "miembros": {
        "categoria": "general",
        "archivo": "miembro"
    },
    "jurado": {
        "categoria": "general",
        "archivo": "jurado"
    },
    "presentacion": {
        "categoria": "general",
        "archivo": "presentacion"
    },
    "presentar": {
        "categoria": "verbos",
        "archivo": "presentar"
    },
    "traduccion": {
        "categoria": "general",
        "archivo": "traduccion"
    },
    "traducir": {
        "categoria": "verbos",
        "archivo": "traducir"
    },
    "lsv": {
        "categoria": "general",
        "archivo": "lsv"
    },
    "ayudar": {
        "categoria": "verbos",
        "archivo": "ayudar"
    }
}

def agregar_palabras():
    """Agregar palabras nuevas al diccionario"""
    
    # Cargar diccionario actual
    data_path = Path(__file__).parent / 'scripts' / 'data.json'
    
    if not data_path.exists():
        print(f"❌ No se encontró: {data_path}")
        return
    
    with open(data_path, 'r', encoding='utf-8') as f:
        diccionario = json.load(f)
    
    print(f"📚 Diccionario actual: {len(diccionario)} palabras")
    
    # Agregar nuevas palabras
    agregadas = 0
    ya_existen = 0
    
    for palabra, info in nuevas_palabras.items():
        if palabra not in diccionario:
            diccionario[palabra] = info
            agregadas += 1
            print(f"  ✅ {palabra}")
        else:
            ya_existen += 1
            print(f"  ⚠️  {palabra} (ya existe)")
    
    # Guardar diccionario actualizado
    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(diccionario, f, ensure_ascii=False, indent=2)
    
    print(f"\n📊 Resumen:")
    print(f"  Total anterior: {len(diccionario) - agregadas}")
    print(f"  Palabras agregadas: {agregadas}")
    print(f"  Ya existían: {ya_existen}")
    print(f"  Total final: {len(diccionario)}")
    print(f"\n✅ Diccionario actualizado guardado en: {data_path}")

if __name__ == "__main__":
    agregar_palabras()
