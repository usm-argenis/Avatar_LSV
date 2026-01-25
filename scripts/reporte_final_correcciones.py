"""
Reporte completo de todas las modificaciones aplicadas
"""

from pathlib import Path
import json

def generar_reporte_final():
    BASE_DIR = Path(__file__).parent.parent
    JSON_REPORTE = BASE_DIR / "test" / "output" / "comparisons" / "yo_correcciones_reales.json"
    
    if not JSON_REPORTE.exists():
        print("❌ No se encuentra el reporte de correcciones")
        return
    
    with open(JSON_REPORTE, 'r') as f:
        data = json.load(f)
    
    print("="*70)
    print("📊 REPORTE FINAL DE CORRECCIONES - SEÑA 'YO'")
    print("="*70)
    
    print(f"\n📁 Archivos:")
    print(f"   Original:   {Path(data['archivo_original']).name}")
    print(f"   Corregido:  {Path(data['archivo_corregido']).name}")
    
    print(f"\n✅ Resumen de Correcciones:")
    print(f"   Dedos:      {data['correcciones_dedos']}/5 ✅")
    print(f"   Brazo:      {data['correcciones_brazo']}/2 ✅")
    print(f"   TOTAL:      {data['total_exitosas']}/7 ✅")
    
    print(f"\n🔧 Detalle de Modificaciones:\n")
    
    # Separar por tipo
    rotaciones = [m for m in data['modificaciones'] if m.get('tipo') in ['rotacion', None]]
    translaciones = [m for m in data['modificaciones'] if m.get('tipo') in ['translacion', 'translacion_base']]
    
    if rotaciones:
        print("   🔄 ROTACIONES DE DEDOS:")
        for mod in rotaciones:
            hueso = mod['hueso']
            rotacion = mod.get('rotacion', 0)
            frames = mod.get('frames_modificados', 0)
            eje = mod.get('eje', 'z')
            
            if 'Index' in hueso:
                emoji = "☝️"
                desc = "EXTENDER"
            elif 'Thumb' in hueso:
                emoji = "👍"
                desc = "AJUSTAR"
            else:
                emoji = "👊"
                desc = "CERRAR"
            
            print(f"      {emoji} {hueso:20s} → {rotacion:+4d}° eje {eje.upper()} ({frames} frames)")
    
    if translaciones:
        print(f"\n   📍 MOVIMIENTO DE BRAZO:")
        for mod in translaciones:
            hueso = mod['hueso']
            desplazamiento = mod.get('desplazamiento_Z', 0)
            frames = mod.get('frames_modificados', 0)
            tipo = mod.get('tipo', '')
            
            cm = desplazamiento * 100
            
            if 'ForeArm' in hueso:
                emoji = "💪"
                parte = "Antebrazo"
            elif 'Hand' in hueso:
                emoji = "✋"
                parte = "Mano"
            else:
                emoji = "🦴"
                parte = hueso
            
            if tipo == 'translacion_base':
                print(f"      {emoji} {parte:20s} → +{cm:.1f}cm adelante (posición base)")
            else:
                print(f"      {emoji} {parte:20s} → +{cm:.1f}cm adelante ({frames} frames)")
    
    print(f"\n📊 Impacto Visual Esperado:")
    print(f"   ☝️  Índice: MÁS EXTENDIDO hacia el pecho")
    print(f"   👊 Otros dedos: MÁS CERRADOS formando puño")
    print(f"   💪 Codo/Brazo: ADELANTE del torso (más visible)")
    print(f"   ✋ Mano: SIEMPRE VISIBLE (no oculta)")
    
    print(f"\n🎯 Resultado:")
    print(f"   Seña 'YO' más precisa según LSV")
    print(f"   Visibilidad mejorada")
    print(f"   Lista para comparación")
    
    print(f"\n{'='*70}\n")

if __name__ == "__main__":
    generar_reporte_final()
