import requests
import json

# URL del backend
API_URL = "http://localhost:5000/api/optimizar"

# Texto de prueba
texto = "buenos días mi nombre es argenis"

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("🧪 TEST: Endpoint /api/optimizar")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

print(f"📝 Texto: '{texto}'")
print(f"🌐 URL: {API_URL}\n")

try:
    # Hacer petición POST
    response = requests.post(API_URL, json={"texto": texto})
    
    if response.status_code == 200:
        data = response.json()
        
        print("✅ RESPUESTA EXITOSA:\n")
        print(f"  • Texto original: {data.get('texto_original')}")
        print(f"  • Texto corregido: {data.get('texto_corregido')}")
        print(f"  • Texto LSV: {data.get('texto_lsv')}")
        print(f"  • Palabras LSV: {data.get('palabras_lsv')}")
        print(f"  • Palabras disponibles: {data.get('palabras_disponibles')}")
        print(f"  • Palabras faltantes: {data.get('palabras_faltantes')}")
        print(f"  • Cobertura: {data.get('porcentaje_cobertura'):.1f}%")
        print(f"  • Total animaciones: {data.get('total_animaciones')}")
        
        # Mostrar correcciones
        if data.get('correcciones'):
            print(f"\n📝 Correcciones:")
            for corr in data['correcciones']:
                print(f"  → '{corr['original']}' → '{corr['corregida']}'")
        
        # Mostrar secuencia de animaciones
        if data.get('animaciones'):
            print(f"\n🎬 Secuencia de animaciones ({len(data['animaciones'])}):")
            secuencia = ' → '.join([anim['nombre'].upper() for anim in data['animaciones'][:20]])
            if len(data['animaciones']) > 20:
                secuencia += ' → ...'
            print(f"  {secuencia}")
        
    else:
        print(f"❌ Error HTTP: {response.status_code}")
        print(response.text)
        
except requests.exceptions.ConnectionError:
    print("❌ ERROR: No se pudo conectar al backend")
    print("   Asegúrate de que el backend esté corriendo:")
    print("   cd backend && python main.py")
    
except Exception as e:
    print(f"❌ ERROR: {e}")

print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
