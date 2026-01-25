"""
Test del optimizador LSV mejorado
"""
import sys
from pathlib import Path

# Agregar backend al path
sys.path.insert(0, str(Path(__file__).parent.parent / 'backend'))

from lsv_optimizer import LSVTextOptimizer

def test_optimizador():
    optimizer = LSVTextOptimizer()
    
    print("=" * 70)
    print("PRUEBA DEL OPTIMIZADOR LSV MEJORADO")
    print("=" * 70)
    
    casos_prueba = [
        ("mañana ire en metro a trabajar", "mañana yo metro trabajar"),
        ("¿que haces?", "tu que haces"),
        ("¿como estas?", "tu como estar"),
        ("yo tengo hambre", "yo hambre"),
        ("ella va a la escuela", "ella escuela"),
    ]
    
    for texto_input, esperado in casos_prueba:
        resultado = optimizer.procesar_texto(texto_input)
        
        print(f"\n📝 Input:    {texto_input}")
        print(f"✅ Esperado: {esperado}")
        print(f"🔄 Output:   {resultado['texto_lsv']}")
        
        # Verificar si coincide
        if resultado['texto_lsv'] == esperado:
            print("✅ CORRECTO")
        else:
            print("❌ DIFERENTE")
        
        print(f"📊 Cobertura: {resultado.get('cobertura', 0):.1f}%")
        if resultado.get('palabras_faltantes'):
            print(f"⚠️  Faltantes: {', '.join(resultado['palabras_faltantes'])}")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    test_optimizador()
