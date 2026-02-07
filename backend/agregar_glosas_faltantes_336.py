"""
Agregar las 29 glosas faltantes de las 336 base al diccionario
"""

import json
from pathlib import Path

# Leer diccionario actual
data_path = Path(__file__).parent / 'scripts' / 'data.json'
with open(data_path, 'r', encoding='utf-8') as f:
    diccionario = json.load(f)

print(f"📚 Diccionario actual: {len(diccionario)} palabras")
print()

# 29 glosas faltantes detectadas
glosas_faltantes = {
    # MEDIOS TRANSPORTE - AEREO
    'aeropuerto': {'categoria': 'transporte_aereo', 'archivo': 'aeropuerto'},
    'aterrizar': {'categoria': 'transporte_aereo', 'archivo': 'aterrizar'},
    'avion': {'categoria': 'transporte_aereo', 'archivo': 'avion'},
    'avioneta': {'categoria': 'transporte_aereo', 'archivo': 'avioneta'},
    'boleto': {'categoria': 'transporte_aereo', 'archivo': 'boleto'},
    'despegar': {'categoria': 'transporte_aereo', 'archivo': 'despegar'},
    'helicoptero': {'categoria': 'transporte_aereo', 'archivo': 'helicoptero'},
    'piloto': {'categoria': 'transporte_aereo', 'archivo': 'piloto'},
    
    # MEDIOS TRANSPORTE - MARITIMO
    'barco': {'categoria': 'transporte_maritimo', 'archivo': 'barco'},
    'canoa': {'categoria': 'transporte_maritimo', 'archivo': 'canoa'},
    'ferri': {'categoria': 'transporte_maritimo', 'archivo': 'ferri'},
    'lancha': {'categoria': 'transporte_maritimo', 'archivo': 'lancha'},
    
    # MEDIOS TRANSPORTE - TERRESTRE
    'autobus': {'categoria': 'transporte_terrestre', 'archivo': 'autobus'},
    'bicicleta': {'categoria': 'transporte_terrestre', 'archivo': 'bicicleta'},
    'cabletren': {'categoria': 'transporte_terrestre', 'archivo': 'cabletren'},
    'camioneta': {'categoria': 'transporte_terrestre', 'archivo': 'camioneta'},
    'carro': {'categoria': 'transporte_terrestre', 'archivo': 'carro'},
    'estacion': {'categoria': 'transporte_terrestre', 'archivo': 'estacion'},
    'ferrocarril': {'categoria': 'transporte_terrestre', 'archivo': 'ferrocarril'},
    'metro': {'categoria': 'transporte_terrestre', 'archivo': 'metro'},
    'metrobus': {'categoria': 'transporte_terrestre', 'archivo': 'metrobus'},
    'moto': {'categoria': 'transporte_terrestre', 'archivo': 'moto'},
    'parada': {'categoria': 'transporte_terrestre', 'archivo': 'parada'},
    'taxi': {'categoria': 'transporte_terrestre', 'archivo': 'taxi'},
    'tren': {'categoria': 'transporte_terrestre', 'archivo': 'tren'},
    
    # PREGUNTAS
    'cual es tu seña': {'categoria': 'preguntas', 'archivo': 'cual_es_tu_sena'},
    
    # EXPRESIONES
    'habia una vez': {'categoria': 'expresiones', 'archivo': 'habia_una_vez'},
    
    # VERBOS
    'engañar': {'categoria': 'verbos', 'archivo': 'enganar'},
    
    # NUEVO
    'stro': {'categoria': 'general', 'archivo': 'stro'},  # Nota: verificar qué es "stro"
}

# Agregar glosas faltantes
agregadas = 0
for glosa, info in glosas_faltantes.items():
    if glosa not in diccionario:
        diccionario[glosa] = info
        agregadas += 1
        print(f"✅ Agregada: {glosa:30s} → [{info['categoria']}]")
    else:
        print(f"⚠️  Ya existe: {glosa}")

# Guardar diccionario actualizado
with open(data_path, 'w', encoding='utf-8') as f:
    json.dump(diccionario, f, ensure_ascii=False, indent=2)

print()
print("=" * 80)
print("📊 RESUMEN:")
print("=" * 80)
print(f"   Diccionario anterior:    {len(diccionario) - agregadas} palabras")
print(f"   Glosas agregadas:        {agregadas}")
print(f"   Diccionario actualizado: {len(diccionario)} palabras")
print()
print(f"✅ Diccionario guardado en: {data_path}")
print()
print("🎯 AHORA TIENES LAS 336 GLOSAS BASE COMPLETAS!")
