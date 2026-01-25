"""
Script para calcular cuántas palabras del vocabulario LSV faltan por animar
"""
import sys
from pathlib import Path

# Agregar backend al path
sys.path.insert(0, str(Path(__file__).parent.parent / 'backend'))

from lsv_optimizer import SENAS_CURSO_BASICO

def calcular_palabras_faltantes():
    # Directorio de animaciones
    glb_dir = Path(__file__).parent.parent / "test" / "output" / "glb"
    
    # Categorías
    categorias = [
        'alfabeto', 'dias_semana', 'tiempo', 'pronombres', 
        'saludos', 'cortesia', 'preguntas', 'expresiones'
    ]
    
    # Recopilar todas las animaciones disponibles
    animaciones_disponibles = set()
    
    # Animaciones en raíz
    for archivo in glb_dir.glob("Remy_resultado_*.glb"):
        nombre = archivo.stem.replace('Remy_resultado_', '')
        # Saltar versiones de prueba
        if not any(x in nombre for x in ['mejorado', 'FIXED', '_v2', '_v3', '_v4']):
            animaciones_disponibles.add(nombre.lower())
    
    # Animaciones en subcarpetas
    for categoria in categorias:
        categoria_dir = glb_dir / categoria
        if categoria_dir.exists():
            for archivo in categoria_dir.glob("Remy_resultado_*.glb"):
                nombre = archivo.stem.replace('Remy_resultado_', '')
                animaciones_disponibles.add(nombre.lower())
    
    print("=" * 80)
    print("📊 ANÁLISIS DE VOCABULARIO LSV")
    print("=" * 80)
    
    print(f"\n📚 Vocabulario total del Curso Básico LSV: {len(SENAS_CURSO_BASICO)} palabras")
    print(f"✅ Animaciones disponibles: {len(animaciones_disponibles)} palabras")
    
    # Calcular palabras faltantes
    palabras_faltantes = SENAS_CURSO_BASICO - animaciones_disponibles
    palabras_disponibles_en_vocabulario = animaciones_disponibles & SENAS_CURSO_BASICO
    
    print(f"\n🎯 Palabras del vocabulario con animación: {len(palabras_disponibles_en_vocabulario)}")
    print(f"⚠️  Palabras del vocabulario SIN animación: {len(palabras_faltantes)}")
    
    # Calcular porcentaje
    porcentaje_completado = (len(palabras_disponibles_en_vocabulario) / len(SENAS_CURSO_BASICO)) * 100
    porcentaje_faltante = 100 - porcentaje_completado
    
    print(f"\n📈 Progreso del sistema:")
    print(f"   ✅ Completado: {porcentaje_completado:.2f}%")
    print(f"   ⏳ Faltante: {porcentaje_faltante:.2f}%")
    
    # Barra de progreso
    barra_completada = int(porcentaje_completado / 2)
    barra = "█" * barra_completada + "░" * (50 - barra_completada)
    print(f"\n   [{barra}] {porcentaje_completado:.1f}%")
    
    # Categorías de palabras faltantes
    print(f"\n{'=' * 80}")
    print("🔍 PALABRAS FALTANTES MÁS COMUNES")
    print("=" * 80)
    
    # Mostrar primeras 50 palabras faltantes ordenadas
    palabras_faltantes_sorted = sorted(list(palabras_faltantes))[:50]
    
    for i in range(0, len(palabras_faltantes_sorted), 5):
        grupo = palabras_faltantes_sorted[i:i+5]
        print("   " + ", ".join(f"{p:15}" for p in grupo))
    
    if len(palabras_faltantes) > 50:
        print(f"\n   ... y {len(palabras_faltantes) - 50} palabras más")
    
    # Animaciones que NO están en el vocabulario (extras)
    animaciones_extras = animaciones_disponibles - SENAS_CURSO_BASICO
    
    if animaciones_extras:
        print(f"\n{'=' * 80}")
        print(f"➕ ANIMACIONES EXTRAS (no en vocabulario): {len(animaciones_extras)}")
        print("=" * 80)
        for palabra in sorted(animaciones_extras):
            print(f"   - {palabra}")
    
    # Estimación para sistema avanzado
    print(f"\n{'=' * 80}")
    print("🎯 ESTIMACIÓN PARA SISTEMA AVANZADO")
    print("=" * 80)
    
    print(f"""
📌 Nivel Actual: BÁSICO
   - Animaciones: {len(animaciones_disponibles)}
   - Cobertura vocabulario: {porcentaje_completado:.1f}%
   
🎯 Nivel INTERMEDIO (50% vocabulario):
   - Faltan: {int(len(SENAS_CURSO_BASICO) * 0.5) - len(palabras_disponibles_en_vocabulario)} animaciones
   
🎯 Nivel AVANZADO (75% vocabulario):
   - Faltan: {int(len(SENAS_CURSO_BASICO) * 0.75) - len(palabras_disponibles_en_vocabulario)} animaciones
   
🎯 Nivel COMPLETO (100% vocabulario):
   - Faltan: {len(palabras_faltantes)} animaciones
    """)
    
    print("=" * 80)
    print("✅ ANÁLISIS COMPLETADO")
    print("=" * 80)
    
    # Guardar reporte
    reporte_path = Path(__file__).parent.parent / "REPORTE_VOCABULARIO.txt"
    with open(reporte_path, 'w', encoding='utf-8') as f:
        f.write(f"VOCABULARIO LSV - REPORTE DE COBERTURA\n")
        f.write(f"{'=' * 80}\n\n")
        f.write(f"Vocabulario total: {len(SENAS_CURSO_BASICO)} palabras\n")
        f.write(f"Animaciones disponibles: {len(animaciones_disponibles)}\n")
        f.write(f"Cobertura: {porcentaje_completado:.2f}%\n\n")
        f.write(f"Palabras faltantes ({len(palabras_faltantes)}):\n")
        for palabra in sorted(palabras_faltantes):
            f.write(f"  - {palabra}\n")
    
    print(f"\n💾 Reporte guardado en: {reporte_path}")

if __name__ == "__main__":
    calcular_palabras_faltantes()
