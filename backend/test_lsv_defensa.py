"""
Script de pruebas para verificar traducción LSV correcta
Prueba las frases de defensa del TEG
"""
import sys
from pathlib import Path

# Agregar el directorio backend al path
sys.path.insert(0, str(Path(__file__).parent))

from api_optimizer import LSVOptimizer

def probar_frase(optimizer, frase_original, titulo=""):
    """Probar traducción de una frase"""
    print(f"\n{'='*70}")
    print(f"🔵 {titulo}")
    print(f"{'='*70}")
    print(f"📝 ESPAÑOL: {frase_original}")
    print()
    
    resultado = optimizer.translate_to_animations(
        texto=frase_original,
        deletrear_desconocidas=False,
        corregir_ortografia=True
    )
    
    # Mostrar correcciones
    if resultado['correcciones']:
        print("📋 CORRECCIONES:")
        for corr in resultado['correcciones']:
            print(f"  • {corr['original']} → {corr['corregida']} ({corr['tipo']})")
        print()
    
    # Mostrar glosas LSV
    glosas = [anim['nombre'] for anim in resultado['animaciones']]
    print("🤟 GLOSAS LSV:")
    print(f"  {' '.join(glosas)}")
    print()
    
    # Mostrar análisis detallado
    print("📊 ANÁLISIS DETALLADO:")
    for i, anim in enumerate(resultado['animaciones'], 1):
        es_deletreo = " (DELETREO)" if anim.get('es_deletreo') else ""
        print(f"  {i}. {anim['nombre']:20} → {anim['categoria']:15} {es_deletreo}")
    
    print(f"\n📈 Total animaciones: {resultado['total_animaciones']}")
    
    if resultado['palabras_deletreadas']:
        print(f"⚠️  Palabras deletreadas: {', '.join(resultado['palabras_deletreadas'])}")
    
    return glosas

def main():
    """Ejecutar pruebas completas"""
    print("\n" + "="*70)
    print("🚀 SISTEMA DE PRUEBAS - TRADUCCIÓN LSV PARA DEFENSA TEG")
    print("="*70)
    
    # Inicializar optimizador
    optimizer = LSVOptimizer()
    
    # Frases a probar
    frases_test = [
        {
            "titulo": "FRASE 1: Bienvenida a defensa del TEG",
            "frase": "Bienvenidos a la defensa de nuestro TEG: Un aporte tecnológico para la integración de la comunidad sorda venezolana.",
            "glosas_esperadas": [
                "bienvenido", "defensa", "nuestro", "teg", "aporte", 
                "tecnologico", "integracion", "comunidad", "sordo", "venezuela"
            ]
        },
        {
            "titulo": "FRASE 2: Saludo al jurado",
            "frase": "Buenos días a los miembros del jurado. Bienvenidos a la presentación de nuestro sistema de traducción LSV.",
            "glosas_esperadas": [
                "buenos dias", "miembro", "jurado", "bienvenido", 
                "presentacion", "nuestro", "sistema", "traduccion", "lsv"
            ]
        },
        {
            "titulo": "FRASE 3: Presentación simple",
            "frase": "Hoy presentamos nuestro sistema de traducción",
            "glosas_esperadas": [
                "hoy", "presentar", "nuestro", "sistema", "traduccion"
            ]
        },
        {
            "titulo": "FRASE 4: Sobre la tecnología",
            "frase": "Este es un aporte tecnológico para la comunidad sorda",
            "glosas_esperadas": [
                "aporte", "tecnologico", "comunidad", "sordo"
            ]
        },
        {
            "titulo": "FRASE 5: Ejemplo con pronombre ÉL",
            "frase": "Él es mi profesor y trabaja en la universidad",
            "glosas_esperadas": [
                "el", "profesor", "trabajar", "universidad"
            ]
        }
    ]
    
    # Ejecutar pruebas
    resultados = []
    for test in frases_test:
        glosas_resultado = probar_frase(
            optimizer,
            test["frase"],
            test["titulo"]
        )
        resultados.append({
            "titulo": test["titulo"],
            "resultado": glosas_resultado,
            "esperado": test.get("glosas_esperadas", [])
        })
    
    # Resumen final
    print("\n" + "="*70)
    print("📊 RESUMEN DE PRUEBAS")
    print("="*70)
    
    for i, res in enumerate(resultados, 1):
        print(f"\n{i}. {res['titulo']}")
        print(f"   Glosas generadas: {len(res['resultado'])}")
        if res['esperado']:
            coincidencias = sum(1 for g in res['esperado'] if g in res['resultado'])
            print(f"   Palabras clave encontradas: {coincidencias}/{len(res['esperado'])}")
    
    print("\n" + "="*70)
    print("✅ PRUEBAS COMPLETADAS")
    print("="*70)

if __name__ == "__main__":
    main()
