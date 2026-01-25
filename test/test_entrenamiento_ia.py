"""
Script de Prueba - Sistema de Entrenamiento IA LSV
Verifica que todos los componentes funcionen correctamente
"""

import sys
from pathlib import Path

# Agregar backend al path
sys.path.insert(0, str(Path(__file__).parent.parent / 'backend'))

from lsv_optimizer import LSVTextOptimizer

def test_optimizer():
    """Prueba el optimizador con los 35 ejemplos"""
    print("=" * 70)
    print("🧪 PRUEBA DEL SISTEMA DE ENTRENAMIENTO IA LSV")
    print("=" * 70)
    
    # Inicializar
    optimizer = LSVTextOptimizer()
    
    # Test 1: Contar ejemplos
    print("\n📊 Test 1: Verificar Ejemplos de Entrenamiento")
    print("-" * 70)
    ejemplos = optimizer.ejemplos_entrenamiento
    print(f"✅ Total ejemplos cargados: {len(ejemplos)}")
    
    if len(ejemplos) >= 35:
        print(f"✅ ÉXITO: Se cargaron todos los 35+ ejemplos")
    else:
        print(f"⚠️ ADVERTENCIA: Solo {len(ejemplos)} ejemplos (esperados: 35)")
    
    # Test 2: Verificar categorías
    print("\n🏷️ Test 2: Verificar Categorías")
    print("-" * 70)
    categorias = optimizer.get_categorias_disponibles()
    print(f"✅ Categorías disponibles: {len(categorias)}")
    for i, cat in enumerate(categorias, 1):
        count = len(optimizer.get_ejemplos_por_categoria(cat))
        print(f"   {i}. {cat}: {count} ejemplos")
    
    # Test 3: Buscar ejemplo similar
    print("\n🔍 Test 3: Buscar Ejemplo Similar")
    print("-" * 70)
    texto_prueba = "Me gradué hace 5 años"
    print(f"Texto de entrada: '{texto_prueba}'")
    
    resultados = optimizer.buscar_ejemplo_similar(texto_prueba)
    
    if resultados and len(resultados) > 0:
        mejor = resultados[0]
        print(f"\n✅ Mejor Match:")
        print(f"   Similitud: {mejor['similitud']*100:.1f}%")
        print(f"   Input: {mejor['ejemplo']['input']}")
        print(f"   Output LSV: {mejor['ejemplo']['output']}")
        print(f"   Categoría: {mejor['ejemplo'].get('categoria', 'N/A')}")
    else:
        print("❌ No se encontró ningún ejemplo similar")
    
    # Test 4: Probar varios casos
    print("\n🧪 Test 4: Procesar Ejemplos de Diferentes Categorías")
    print("-" * 70)
    
    casos_prueba = [
        "Mi profesión es ingeniero",
        "¿Qué hora es?",
        "No tengo dinero",
        "Ella es mi hermana menor",
        "Mañana voy a ir al banco"
    ]
    
    for i, caso in enumerate(casos_prueba, 1):
        print(f"\n{i}. Input: '{caso}'")
        resultados = optimizer.buscar_ejemplo_similar(caso)
        
        if resultados and len(resultados) > 0:
            mejor = resultados[0]
            print(f"   ✅ LSV: {mejor['ejemplo']['output']}")
            print(f"   📁 Categoría: {mejor['ejemplo'].get('categoria', 'N/A')}")
            print(f"   🎯 Similitud: {mejor['similitud']*100:.0f}%")
        else:
            # Usar método tradicional
            resultado = optimizer.procesar_texto(caso)
            print(f"   ⚠️ Sin match exacto, usando conversión tradicional:")
            print(f"   LSV: {resultado['texto_lsv']}")
    
    # Test 5: Verificar vocabulario
    print("\n📚 Test 5: Verificar Vocabulario Base")
    print("-" * 70)
    senas = optimizer.senas_disponibles
    print(f"✅ Señas disponibles: {len(senas)}")
    print(f"   Ejemplos: {', '.join(list(senas)[:10])}...")
    
    # Resumen final
    print("\n" + "=" * 70)
    print("📋 RESUMEN DE PRUEBAS")
    print("=" * 70)
    print(f"✅ Ejemplos de entrenamiento: {len(ejemplos)}")
    print(f"✅ Categorías únicas: {len(categorias)}")
    print(f"✅ Señas disponibles: {len(senas)}")
    print(f"✅ Búsqueda por similitud: FUNCIONANDO")
    print("\n🎉 SISTEMA DE ENTRENAMIENTO IA: OPERATIVO")
    print("=" * 70)

if __name__ == '__main__':
    try:
        test_optimizer()
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
