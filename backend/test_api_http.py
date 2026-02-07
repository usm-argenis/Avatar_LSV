"""
Script de prueba HTTP para API LSV
Prueba las frases de defensa del TEG
"""
import requests
import json

API_URL = "http://127.0.0.1:5000/api/translate"

def test_translation(frase, titulo=""):
    """Probar traducción vía API"""
    print(f"\n{'='*70}")
    print(f"🔵 {titulo}")
    print(f"{'='*70}")
    print(f"📝 ESPAÑOL: {frase}")
    
    try:
        response = requests.post(
            API_URL,
            json={
                "texto": frase,
                "deletrear_desconocidas": False,
                "corregir_ortografia": True
            }
        )
        
        if response.status_code == 200:
            resultado = response.json()
            
            # Mostrar correcciones
            if resultado.get('correcciones'):
                print(f"\n📋 CORRECCIONES ({len(resultado['correcciones'])}):")
                for corr in resultado['correcciones']:
                    print(f"  • {corr['original']} → {corr['corregida']} ({corr['tipo']})")
            
            # Mostrar glosas LSV
            glosas = [anim['nombre'] for anim in resultado['animaciones']]
            print(f"\n🤟 GLOSAS LSV:")
            print(f"  {' '.join(glosas)}")
            
            print(f"\n📈 Total animaciones: {resultado['total_animaciones']}")
            
            return True
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
            return False
            
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False

def main():
    """Ejecutar pruebas completas"""
    print("\n" + "="*70)
    print("🚀 PRUEBAS API HTTP - TRADUCCIÓN LSV")
    print("="*70)
    
    # Verificar que el servidor esté corriendo
    try:
        response = requests.get("http://127.0.0.1:5000/health")
        if response.status_code == 200:
            print("✅ Servidor LSV API funcionando correctamente")
        else:
            print("❌ Servidor no está respondiendo correctamente")
            return
    except:
        print("❌ Error: Servidor no está corriendo en http://127.0.0.1:5000")
        print("   Ejecutar: uvicorn main:app --reload --port 5000")
        return
    
    # Pruebas
    tests = [
        ("FRASE 1: Bienvenida defensa TEG", 
         "Bienvenidos a la defensa de nuestro TEG: Un aporte tecnológico para la integración de la comunidad sorda venezolana."),
        
        ("FRASE 2: Saludo al jurado", 
         "Buenos días a los miembros del jurado. Bienvenidos a la presentación de nuestro sistema de traducción LSV."),
        
        ("FRASE 3: Presentación simple", 
         "Hoy presentamos nuestro sistema de traducción"),
        
        ("FRASE 4: Con pronombre ÉL", 
         "Él es mi profesor y trabaja en la universidad"),
        
        ("FRASE 5: Tecnología y comunidad", 
         "Este es un aporte tecnológico para la comunidad sorda"),
    ]
    
    exitosos = 0
    for titulo, frase in tests:
        if test_translation(frase, titulo):
            exitosos += 1
    
    print("\n" + "="*70)
    print(f"📊 RESUMEN: {exitosos}/{len(tests)} pruebas exitosas")
    print("="*70)
    
    if exitosos == len(tests):
        print("✅ TODAS LAS PRUEBAS PASARON")
    else:
        print(f"⚠️  {len(tests) - exitosos} pruebas fallaron")

if __name__ == "__main__":
    main()
