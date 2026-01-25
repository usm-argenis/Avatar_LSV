"""
Script de Verificación de Cobertura - Vocabulario LSV
Verifica qué palabras necesarias para el sistema IA están disponibles
"""

import sys
from pathlib import Path

# Agregar backend al path
sys.path.insert(0, str(Path(__file__).parent.parent / 'backend'))

from lsv_optimizer import LSVTextOptimizer

# Lista de palabras CRÍTICAS necesarias para los 70 ejemplos
PALABRAS_NECESARIAS = {
    # PRONOMBRES (9)
    'yo', 'tú', 'él', 'ella', 'nosotros', 'mi', 'mío', 'mía', 'tu',
    
    # VERBOS ESENCIALES (30)
    'tener', 'ir', 'ser', 'estar', 'graduar', 'trabajar', 'vivir', 
    'comprar', 'comer', 'dormir', 'sentir', 'gustar', 'querer', 'amar',
    'necesitar', 'doler', 'limpiar', 'hacer', 'estudiar', 'aprender',
    'ayudar', 'encontrar', 'poder', 'recoger', 'salir', 'correr', 
    'saltar', 'leer', 'ver', 'sonar',
    
    # SUSTANTIVOS (50)
    'profesión', 'años', 'edad', 'nombre', 'casa', 'tiempo', 'dinero',
    'hermano', 'hermana', 'mamá', 'papá', 'hijo', 'hija', 'ayuda', 
    'hora', 'problema', 'trabajo', 'amigo', 'amiga', 'compañero', 
    'compañera', 'profesora', 'maestro', 'banco', 'hospital', 'tienda',
    'mercado', 'comida', 'agua', 'pan', 'leche', 'arroz', 'carne',
    'cabeza', 'estómago', 'tarea', 'regalo', 'libro', 'película',
    'camisa', 'pantalón', 'perro', 'gato', 'teléfono', 'puerta',
    'carro', 'apoyo', 'día', 'acción',
    
    # PROFESIONES (10)
    'ingeniero', 'médico', 'abogado', 'profesor', 'enfermera', 'albañil',
    'secretaria', 'ejecutiva', 'contador', 'público',
    
    # ADJETIVOS (25)
    'grande', 'pequeño', 'pequeña', 'feliz', 'triste', 'cansado', 
    'enfermo', 'nuevo', 'bonito', 'bonita', 'rápido', 'alto', 'rojo',
    'roja', 'azul', 'picante', 'amargo', 'frío', 'fría', 'caliente',
    'sucio', 'sucia', 'abierta', 'este', 'esta',
    
    # MARCADORES TEMPORALES (8)
    'ahora', 'hoy', 'mañana', 'ayer', 'atrás', 'después', 'pasado', 'tarde',
    
    # INTERROGATIVOS (5)
    'qué', 'dónde', 'cuándo', 'cuántos', 'cuál',
    
    # DÍAS DE LA SEMANA (2 - mínimo para ejemplos)
    'viernes', 'sábado',
    
    # OTROS (5)
    'no', 'sí', 'mucho', 'poco', 'más'
}

def verificar_cobertura():
    """Verifica qué palabras están disponibles y cuáles faltan"""
    
    print("=" * 80)
    print("🔍 VERIFICACIÓN DE COBERTURA - VOCABULARIO LSV")
    print("=" * 80)
    
    # Inicializar optimizador
    optimizer = LSVTextOptimizer()
    
    print(f"\n📊 Estadísticas Generales:")
    print(f"   Vocabulario base disponible: {len(optimizer.senas_disponibles)} señas")
    print(f"   Palabras necesarias (críticas): {len(PALABRAS_NECESARIAS)} palabras")
    
    # Verificar disponibilidad
    disponibles = []
    faltantes = []
    
    for palabra in sorted(PALABRAS_NECESARIAS):
        if palabra in optimizer.senas_disponibles:
            disponibles.append(palabra)
        else:
            faltantes.append(palabra)
    
    # Calcular cobertura
    cobertura = (len(disponibles) / len(PALABRAS_NECESARIAS)) * 100
    
    print(f"\n✅ Palabras disponibles: {len(disponibles)}")
    print(f"❌ Palabras faltantes: {len(faltantes)}")
    print(f"📈 Cobertura: {cobertura:.1f}%")
    
    # Mostrar barra de progreso
    barra_llena = int(cobertura / 5)
    barra_vacia = 20 - barra_llena
    print(f"\n   [{'▓' * barra_llena}{'░' * barra_vacia}] {cobertura:.1f}%")
    
    # Listar palabras faltantes por categoría
    if faltantes:
        print("\n" + "=" * 80)
        print("❌ PALABRAS FALTANTES POR CATEGORÍA")
        print("=" * 80)
        
        # Categorizar faltantes
        faltantes_por_categoria = {
            'Pronombres': [],
            'Verbos': [],
            'Sustantivos': [],
            'Profesiones': [],
            'Adjetivos': [],
            'Marcadores Temporales': [],
            'Interrogativos': [],
            'Días': [],
            'Otros': []
        }
        
        pronombres = {'yo', 'tú', 'él', 'ella', 'nosotros', 'mi', 'mío', 'mía', 'tu'}
        verbos = {'tener', 'ir', 'ser', 'estar', 'graduar', 'trabajar', 'vivir', 
                  'comprar', 'comer', 'dormir', 'sentir', 'gustar', 'querer', 'amar',
                  'necesitar', 'doler', 'limpiar', 'hacer', 'estudiar', 'aprender',
                  'ayudar', 'encontrar', 'poder', 'recoger', 'salir', 'correr', 
                  'saltar', 'leer', 'ver', 'sonar'}
        profesiones = {'ingeniero', 'médico', 'abogado', 'profesor', 'enfermera', 
                       'albañil', 'secretaria', 'ejecutiva', 'contador', 'público'}
        marcadores = {'ahora', 'hoy', 'mañana', 'ayer', 'atrás', 'después', 'pasado', 'tarde'}
        interrogativos = {'qué', 'dónde', 'cuándo', 'cuántos', 'cuál'}
        dias = {'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo'}
        adjetivos = {'grande', 'pequeño', 'pequeña', 'feliz', 'triste', 'cansado', 
                     'enfermo', 'nuevo', 'bonito', 'bonita', 'rápido', 'alto', 'rojo',
                     'roja', 'azul', 'picante', 'amargo', 'frío', 'fría', 'caliente',
                     'sucio', 'sucia', 'abierta', 'este', 'esta'}
        
        for palabra in faltantes:
            if palabra in pronombres:
                faltantes_por_categoria['Pronombres'].append(palabra)
            elif palabra in verbos:
                faltantes_por_categoria['Verbos'].append(palabra)
            elif palabra in profesiones:
                faltantes_por_categoria['Profesiones'].append(palabra)
            elif palabra in marcadores:
                faltantes_por_categoria['Marcadores Temporales'].append(palabra)
            elif palabra in interrogativos:
                faltantes_por_categoria['Interrogativos'].append(palabra)
            elif palabra in dias:
                faltantes_por_categoria['Días'].append(palabra)
            elif palabra in adjetivos:
                faltantes_por_categoria['Adjetivos'].append(palabra)
            elif palabra in PALABRAS_NECESARIAS:
                # Verificar si es sustantivo (resto)
                if palabra not in ['no', 'sí', 'mucho', 'poco', 'más']:
                    faltantes_por_categoria['Sustantivos'].append(palabra)
                else:
                    faltantes_por_categoria['Otros'].append(palabra)
        
        # Mostrar por categoría
        for categoria, palabras in faltantes_por_categoria.items():
            if palabras:
                print(f"\n📌 {categoria} ({len(palabras)}):")
                for i, palabra in enumerate(sorted(palabras), 1):
                    print(f"   {i}. {palabra.upper()}")
        
        # Recomendaciones
        print("\n" + "=" * 80)
        print("💡 RECOMENDACIONES")
        print("=" * 80)
        print("\n1. Agregar las palabras faltantes al vocabulario base")
        print("2. Priorizar pronombres, verbos y marcadores temporales")
        print("3. Verificar si algunas palabras tienen variantes (género/número)")
        print("4. Considerar sinónimos para palabras faltantes")
        
    else:
        print("\n🎉 ¡EXCELENTE! Todas las palabras necesarias están disponibles.")
    
    # Palabras más usadas disponibles
    print("\n" + "=" * 80)
    print("✅ TOP 10 PALABRAS MÁS USADAS (Disponibles)")
    print("=" * 80)
    
    palabras_frecuentes = [
        ('yo', 30), ('mi', 18), ('tener', 12), ('años', 10), ('tú', 8),
        ('profesión', 6), ('ir', 6), ('no', 6), ('trabajo', 5), ('mucho', 5)
    ]
    
    for i, (palabra, freq) in enumerate(palabras_frecuentes, 1):
        disponible = "✅" if palabra in optimizer.senas_disponibles else "❌"
        print(f"   {i:2d}. {palabra.upper():15s} ({freq:2d} usos) {disponible}")
    
    # Resumen final
    print("\n" + "=" * 80)
    print("📋 RESUMEN FINAL")
    print("=" * 80)
    
    if cobertura >= 95:
        estado = "🟢 EXCELENTE"
        mensaje = "El sistema tiene cobertura casi completa"
    elif cobertura >= 85:
        estado = "🟡 BUENO"
        mensaje = "El sistema tiene buena cobertura pero puede mejorarse"
    elif cobertura >= 70:
        estado = "🟠 ACEPTABLE"
        mensaje = "Se requiere agregar más palabras para funcionamiento óptimo"
    else:
        estado = "🔴 INSUFICIENTE"
        mensaje = "Se necesita expandir significativamente el vocabulario"
    
    print(f"\n   Estado: {estado}")
    print(f"   Cobertura: {cobertura:.1f}%")
    print(f"   Mensaje: {mensaje}")
    print(f"\n   Palabras disponibles: {len(disponibles)}/{len(PALABRAS_NECESARIAS)}")
    print(f"   Vocabulario total: {len(optimizer.senas_disponibles)} señas")
    
    print("\n" + "=" * 80)
    
    return cobertura, disponibles, faltantes

if __name__ == '__main__':
    try:
        cobertura, disponibles, faltantes = verificar_cobertura()
        
        # Código de salida basado en cobertura
        if cobertura < 70:
            sys.exit(1)  # Error si cobertura muy baja
        else:
            sys.exit(0)  # OK
            
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
