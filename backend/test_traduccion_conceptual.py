"""
TEST DE TRADUCCIÓN CONCEPTUAL LSV
Prueba las nuevas reglas de reformulación sin eliminar las existentes
"""

from api_optimizer import LSVOptimizer

def test_traduccion():
    optimizer = LSVOptimizer()
    
    # Casos de prueba con las nuevas reglas
    casos_test = [
        # Ejemplo del usuario
        {
            "texto": "Un aporte tecnológico para la integración de la comunidad sorda venezolana",
            "esperado": "TECNOLOGÍA DAR VENEZUELA SORDO COMUNIDAD INCLUIR"
        },
        # Defensa de trabajo
        {
            "texto": "Defensa del trabajo de grado",
            "esperado": "TRABAJO GRADO DEFENDER"
        },
        # Con tiempo (debe ir primero)
        {
            "texto": "Hoy voy a presentar mi proyecto de integración",
            "esperado": "HOY [presentar] [proyecto/trabajo] [incluir]"
        },
        # Con género (debe mantener regla existente)
        {
            "texto": "Ayer la ingeniera trabajó en la universidad",
            "esperado": "AYER INGENIERO MUJER TRABAJAR [universidad]"
        },
        # Con números (debe mantener regla existente)
        {
            "texto": "Tengo 25 años",
            "esperado": "MÍO 2 5 AÑO"
        },
        # Conceptos abstractos
        {
            "texto": "La accesibilidad es importante para la inclusión",
            "esperado": "ACCESO FÁCIL IMPORTANTE INCLUIR"
        },
        # Verbo conjugado (debe ir a infinitivo)
        {
            "texto": "Los estudiantes trabajaron ayer",
            "esperado": "AYER ESTUDIANTE TRABAJAR"
        }
    ]
    
    print("=" * 70)
    print("🧪 TEST DE TRADUCCIÓN CONCEPTUAL LSV")
    print("=" * 70)
    print()
    
    for i, caso in enumerate(casos_test, 1):
        print(f"{'─' * 70}")
        print(f"📝 TEST {i}")
        print(f"{'─' * 70}")
        print(f"Entrada: \"{caso['texto']}\"")
        print(f"Esperado: {caso['esperado']}")
        print()
        
        resultado = optimizer.translate_to_animations(
            caso['texto'],
            deletrear_desconocidas=True,
            corregir_ortografia=True
        )
        
        # Extraer glosas
        glosas = [anim['nombre'].upper() for anim in resultado['animaciones'] if not anim.get('es_deletreo', False)]
        glosas_str = ' '.join(glosas)
        
        print(f"✅ Resultado: {glosas_str}")
        print()
        
        # Mostrar detalles
        if resultado.get('correcciones'):
            print("📝 Correcciones:")
            for corr in resultado['correcciones']:
                print(f"   • {corr['original']} → {corr['corregida']} ({corr['tipo']})")
            print()
        
        if resultado.get('palabras_deletreadas'):
            print(f"🔡 Deletreadas: {', '.join(resultado['palabras_deletreadas'])}")
            print()
        
        print(f"📊 Total animaciones: {resultado['total_animaciones']}")
        print()
    
    print("=" * 70)
    print("✅ PRUEBAS COMPLETADAS")
    print("=" * 70)

if __name__ == "__main__":
    test_traduccion()
