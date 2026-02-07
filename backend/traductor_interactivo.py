"""
🤟 TRADUCTOR LSV INTERACTIVO
Prueba el sistema de traducción conceptual con tus propias frases
"""

from api_optimizer import LSVOptimizer
import sys

def mostrar_resultado(resultado):
    """Mostrar resultado de traducción de forma clara"""
    print("\n" + "─" * 70)
    print("📋 RESULTADO DE TRADUCCIÓN")
    print("─" * 70)
    
    # Texto original vs corregido
    print(f"\n📝 Original:  \"{resultado['texto_original']}\"")
    if resultado['texto_original'] != resultado['texto_corregido']:
        print(f"✏️  Corregido: \"{resultado['texto_corregido']}\"")
    
    # Correcciones aplicadas
    if resultado.get('correcciones'):
        print(f"\n📝 Correcciones aplicadas ({len(resultado['correcciones'])}):")
        for corr in resultado['correcciones']:
            tipo_emoji = "🔄" if corr['tipo'] == 'normalización' else "✏️"
            print(f"   {tipo_emoji} {corr['original']} → {corr['corregida']} ({corr['tipo']})")
    
    # Glosas LSV
    print("\n🤟 LSV (Glosas):")
    glosas = []
    for anim in resultado['animaciones']:
        if not anim.get('es_deletreo', False):
            glosas.append(anim['nombre'].upper())
    
    if glosas:
        print(f"   {' '.join(glosas)}")
    else:
        print("   (solo deletreo)")
    
    # Palabras deletreadas
    if resultado.get('palabras_deletreadas'):
        print(f"\n🔡 Deletreadas: {', '.join(resultado['palabras_deletreadas'])}")
    
    # Estadísticas
    print(f"\n📊 Total animaciones: {resultado['total_animaciones']}")
    
    # Desglose por categoría
    categorias = {}
    for anim in resultado['animaciones']:
        if not anim.get('es_deletreo', False):
            cat = anim.get('categoria', 'sin_categoria')
            categorias[cat] = categorias.get(cat, 0) + 1
    
    if categorias:
        print(f"\n📂 Por categoría:")
        for cat, count in sorted(categorias.items()):
            print(f"   • {cat}: {count}")
    
    print("─" * 70 + "\n")


def main():
    print("=" * 70)
    print("🤟 TRADUCTOR LSV INTERACTIVO - Sistema de Traducción Conceptual")
    print("=" * 70)
    print()
    print("Este sistema traduce español a Lengua de Señas Venezolana (LSV)")
    print("usando reformulación conceptual inteligente.")
    print()
    print("Características:")
    print("  ✅ Reformula conceptos abstractos usando señas existentes")
    print("  ✅ Aplica orden gramatical LSV (TIEMPO → LUGAR → SUJETO → VERBO)")
    print("  ✅ Normaliza verbos, género y plurales")
    print("  ✅ Solo deletrea como último recurso")
    print()
    print("Ejemplos de prueba:")
    print('  • "Ayer la ingeniera trabajó en su proyecto"')
    print('  • "La integración de la comunidad sorda es importante"')
    print('  • "Defensa del trabajo de grado"')
    print()
    print("─" * 70)
    
    # Inicializar optimizador
    optimizer = LSVOptimizer()
    
    # Modo interactivo
    while True:
        try:
            print("\n💬 Escribe una frase (o 'salir' para terminar):")
            texto = input("> ").strip()
            
            if not texto:
                continue
            
            if texto.lower() in ['salir', 'exit', 'quit', 'q']:
                print("\n👋 ¡Hasta luego!")
                break
            
            # Traducir
            resultado = optimizer.translate_to_animations(
                texto,
                deletrear_desconocidas=True,
                corregir_ortografia=True,
                velocidad_deletreo=1.2
            )
            
            # Mostrar resultado
            mostrar_resultado(resultado)
            
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
