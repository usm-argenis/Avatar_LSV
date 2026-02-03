"""
Test completo del sistema LSV optimizado
Prueba todas las reglas lingüísticas
"""
from api_optimizer import LSVOptimizer

def test_completo():
    optimizer = LSVOptimizer()
    
    print("\n" + "="*70)
    print("🧪 PRUEBA SISTEMA LSV COMPLETO")
    print("="*70)
    
    # Lista de pruebas completas
    pruebas = [
        # Básico
        "hola como estas",
        
        # Género femenino
        "yo soy ingeniera",
        "ella es doctora",
        "mi amiga es profesora",
        
        # Tiempo al inicio
        "ayer yo trabaje en la universidad",
        "mañana voy a estudiar",
        "el lunes tengo clase",
        
        # Frases compuestas
        "buenas tardes",
        "muchas gracias",
        "cual es tu nombre",
        
        # Verbos conjugados → infinitivo
        "yo trabajo todos los dias",
        "ella estudia ingenieria",
        "nosotros comemos juntos",
        
        # Profesiones plurales
        "hay muchos ingenieros",
        "las doctoras trabajan",
        
        # Corrección ortográfica
        "ola como estas",  # hola
        "asia calor",  # hacia
        "ingeniera", # correcto
        
        # Números
        "tengo 25 años",
        "son las 3",
        
        # Palabras desconocidas
        "me gusta el blockchain",
        
        # Expresión venezolana completa
        "buen provecho mi pana",
        
        # Mezcla de todo
        "ayer mi mama trabajo como doctora en el hospital",
    ]
    
    for i, texto in enumerate(pruebas, 1):
        print(f"\n{'─'*70}")
        print(f"Prueba {i}: {texto}")
        print('─'*70)
        
        resultado = optimizer.translate_to_animations(
            texto,
            deletrear_desconocidas=True,
            corregir_ortografia=True
        )
        
        # Mostrar correcciones
        if resultado['correcciones']:
            print("\n📝 Correcciones:")
            for corr in resultado['correcciones']:
                tipo_icon = "🔧" if corr['tipo'] == 'normalización' else "✏️"
                print(f"  {tipo_icon} '{corr['original']}' → '{corr['corregida']}' ({corr['confianza']}%)")
        
        # Mostrar secuencia de señas
        print(f"\n🤟 Secuencia LSV ({resultado['total_animaciones']} señas):")
        for j, anim in enumerate(resultado['animaciones'], 1):
            icon = "🔤" if anim['es_deletreo'] else "✋"
            mujer_tag = " [+MUJER]" if anim['nombre'] == 'mujer' else ""
            print(f"  {j}. {icon} {anim['nombre'].upper()}{mujer_tag} ({anim['categoria']})")
        
        # Palabras deletreadas
        if resultado['palabras_deletreadas']:
            print(f"\n🔤 Deletreadas: {', '.join(resultado['palabras_deletreadas'])}")
    
    print("\n" + "="*70)
    print("✅ PRUEBAS COMPLETADAS")
    print("="*70)
    
    # Estadísticas del diccionario
    print(f"\n📊 DICCIONARIO LSV:")
    print(f"   Total palabras: {len(optimizer.diccionario)}")
    
    # Contar por categoría
    categorias = {}
    for palabra, info in optimizer.diccionario.items():
        cat = info['categoria']
        categorias[cat] = categorias.get(cat, 0) + 1
    
    print(f"\n   Por categoría:")
    for cat, count in sorted(categorias.items()):
        print(f"   - {cat}: {count} palabras")

if __name__ == "__main__":
    test_completo()
