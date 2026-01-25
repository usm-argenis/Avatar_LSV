"""
Verificador de avatares para la aplicación móvil
Comprueba que todos los avatares tengan sus animaciones correctamente.
"""

from pathlib import Path
import json

def verificar_avatares():
    """Verifica que todos los avatares estén listos para la app"""
    
    base_path = Path(__file__).parent.parent / "test" / "output" / "glb"
    
    # Avatares que debe tener la app
    avatares_esperados = ['Remy', 'Carlos', 'Nancy', 'Nina', 'Luis', 'Duvall']
    
    # Categorías esperadas
    categorias_esperadas = [
        'alfabeto', 'dias_semana', 'tiempo', 'pronombres',
        'saludos', 'cortesia', 'preguntas', 'expresiones'
    ]
    
    print("=" * 70)
    print("🔍 VERIFICACIÓN DE AVATARES PARA APP MÓVIL")
    print("=" * 70)
    print()
    
    resultados = {}
    
    for avatar in avatares_esperados:
        avatar_path = base_path / avatar
        
        if not avatar_path.exists():
            print(f"❌ {avatar}: Carpeta no encontrada")
            resultados[avatar] = {'status': 'missing', 'archivos': 0}
            continue
        
        total_archivos = 0
        categorias = {}
        
        for categoria in categorias_esperadas:
            categoria_path = avatar_path / categoria
            if categoria_path.exists():
                archivos_glb = list(categoria_path.glob(f"{avatar}_resultado_*.glb"))
                categorias[categoria] = len(archivos_glb)
                total_archivos += len(archivos_glb)
            else:
                categorias[categoria] = 0
        
        resultados[avatar] = {
            'status': 'ready',
            'archivos': total_archivos,
            'categorias': categorias
        }
        
        print(f"✅ {avatar}: {total_archivos} archivos GLB")
        
        # Mostrar categorías con archivos
        for cat, count in categorias.items():
            if count > 0:
                icon = "📁"
                print(f"   {icon} {cat}: {count} animaciones")
        print()
    
    # Resumen
    print("=" * 70)
    print("📊 RESUMEN")
    print("=" * 70)
    
    total_avatares = len([r for r in resultados.values() if r['status'] == 'ready'])
    total_archivos_global = sum(r['archivos'] for r in resultados.values())
    
    print(f"✅ Avatares disponibles: {total_avatares}/{len(avatares_esperados)}")
    print(f"📦 Total de animaciones: {total_archivos_global}")
    print()
    
    # Verificar configuración de archivos
    print("=" * 70)
    print("🔧 ARCHIVOS DE CONFIGURACIÓN")
    print("=" * 70)
    
    archivos_config = {
        'AvatarSelector.js': Path(__file__).parent.parent / 'mobile_app' / 'lengua-de-senas' / 'components' / 'AvatarSelector.js',
        'HomeScreen.js': Path(__file__).parent.parent / 'mobile_app' / 'lengua-de-senas' / 'screens' / 'HomeScreen.js',
        'api_optimizer.py': Path(__file__).parent.parent / 'backend' / 'api_optimizer.py',
        'prueba.html': Path(__file__).parent.parent / 'test' / 'prueba.html'
    }
    
    for nombre, path in archivos_config.items():
        if path.exists():
            # Verificar si contiene los nombres de los avatares
            contenido = path.read_text(encoding='utf-8')
            avatares_encontrados = [a for a in avatares_esperados if a in contenido]
            
            if len(avatares_encontrados) == len(avatares_esperados):
                print(f"✅ {nombre}: Todos los avatares configurados ({len(avatares_encontrados)}/6)")
            else:
                faltantes = set(avatares_esperados) - set(avatares_encontrados)
                print(f"⚠️  {nombre}: Faltan {', '.join(faltantes)}")
        else:
            print(f"❌ {nombre}: Archivo no encontrado")
    
    print()
    print("=" * 70)
    
    # Guardar resultados en JSON
    output_json = Path(__file__).parent.parent / "test" / "output" / "glb" / "verificacion_avatares.json"
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Resultados guardados en: {output_json.name}")
    print()
    
    return resultados

if __name__ == "__main__":
    verificar_avatares()
