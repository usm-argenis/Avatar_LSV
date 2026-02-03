"""
Test de signos de puntuación en API LSV
Verifica que todos los signos se limpien correctamente
"""
from api_optimizer import LSVOptimizer

def test_signos_puntuacion():
    optimizer = LSVOptimizer()
    
    print("\n" + "="*70)
    print("🧪 TEST DE SIGNOS DE PUNTUACIÓN")
    print("="*70)
    
    # Pruebas con diferentes signos
    pruebas = [
        # Signos básicos
        ("hola, como estas?", "HOLA → COMER → ESTAR"),
        ("¿hola como estas?", "HOLA → COMER → ESTAR"),
        ("hola. como estas.", "HOLA → COMER → ESTAR"),
        ("¡hola! ¿como estas?", "HOLA → COMER → ESTAR"),
        
        # Signos múltiples
        ("hola,,,como...estas???", "HOLA → COMER → ESTAR"),
        ("hola; como: estas", "HOLA → COMER → ESTAR"),
        
        # Comillas y paréntesis
        ('"hola" como estas', "HOLA → COMER → ESTAR"),
        ("'hola' como estas", "HOLA → COMER → ESTAR"),
        ("hola (como estas)", "HOLA → COMER → ESTAR"),
        ("[hola] {como} estas", "HOLA → COMER → ESTAR"),
        
        # Frases reales con puntuación
        ("yo soy ingeniera.", "YO → INGENIERO → MUJER"),
        ("¿ella es doctora?", "ELLA → MEDICO → MUJER"),
        ("ayer, yo trabaje en la universidad.", "AYER → YO → TRABAJAR → ..."),
        ("buenas tardes!", "BUENAS TARDES"),
        ("muchas gracias.", "MUCHO → GRACIAS"),
        
        # Mezcla compleja
        ("¡hola! ¿como estas? bien, gracias.", "HOLA → COMER → ESTAR → BIEN → GRACIAS"),
    ]
    
    for i, (entrada, esperado) in enumerate(pruebas, 1):
        print(f"\n{'─'*70}")
        print(f"Prueba {i}: \"{entrada}\"")
        print(f"Esperado: {esperado}")
        print('─'*70)
        
        resultado = optimizer.translate_to_animations(
            entrada,
            deletrear_desconocidas=False,  # Sin deletreo para estas pruebas
            corregir_ortografia=True
        )
        
        # Mostrar secuencia real
        secuencia = " → ".join([anim['nombre'].upper() for anim in resultado['animaciones']])
        print(f"Resultado: {secuencia}")
        print(f"Total señas: {resultado['total_animaciones']}")
        
        # Verificar que no haya signos en las animaciones
        signos_prohibidos = '¿?¡!,.;:"\'\(\)\[\]{}'
        for anim in resultado['animaciones']:
            if any(signo in anim['nombre'] for signo in signos_prohibidos):
                print(f"❌ ERROR: Signo encontrado en '{anim['nombre']}'")
                break
        else:
            print("✅ Sin signos de puntuación en animaciones")
    
    print("\n" + "="*70)
    print("✅ TEST COMPLETADO")
    print("="*70)

if __name__ == "__main__":
    test_signos_puntuacion()
