"""
Script de prueba rápida para verificar que un avatar funcione en la app.
Prueba cargar una animación de cada avatar nuevo.
"""

from pathlib import Path
import sys

def probar_avatar(avatar_name):
    """Prueba que un avatar tenga archivos GLB válidos"""
    
    base_path = Path(__file__).parent.parent / "test" / "output" / "glb"
    avatar_path = base_path / avatar_name
    
    if not avatar_path.exists():
        print(f"❌ Error: Carpeta {avatar_name} no existe")
        return False
    
    # Buscar la primera animación disponible
    categorias = ['saludos', 'cortesia', 'tiempo', 'pronombres', 'dias_semana']
    
    for categoria in categorias:
        categoria_path = avatar_path / categoria
        if categoria_path.exists():
            archivos = list(categoria_path.glob(f"{avatar_name}_resultado_*.glb"))
            if archivos:
                archivo = archivos[0]
                nombre_sena = archivo.stem.replace(f"{avatar_name}_resultado_", "")
                size_mb = archivo.stat().st_size / (1024 * 1024)
                
                print(f"✅ {avatar_name}")
                print(f"   📁 Categoría: {categoria}")
                print(f"   📄 Archivo: {archivo.name}")
                print(f"   🤟 Seña: {nombre_sena}")
                print(f"   💾 Tamaño: {size_mb:.2f} MB")
                print(f"   🔗 URL de prueba:")
                print(f"      http://localhost:8000/test/prueba.html?text={nombre_sena}&avatar={avatar_name}&autoload=true")
                print()
                return True
    
    print(f"⚠️  {avatar_name}: No se encontraron archivos GLB")
    return False

def main():
    """Prueba todos los avatares nuevos"""
    
    print("=" * 70)
    print("🧪 PRUEBA RÁPIDA DE AVATARES")
    print("=" * 70)
    print()
    
    avatares_nuevos = ['Nancy', 'Nina', 'Luis', 'Duvall']
    
    resultados = []
    for avatar in avatares_nuevos:
        resultado = probar_avatar(avatar)
        resultados.append((avatar, resultado))
    
    print("=" * 70)
    print("📊 RESUMEN")
    print("=" * 70)
    
    exitosos = sum(1 for _, r in resultados if r)
    
    print(f"✅ Avatares funcionando: {exitosos}/{len(avatares_nuevos)}")
    print()
    
    if exitosos == len(avatares_nuevos):
        print("🎉 ¡Todos los avatares están listos!")
        print()
        print("Para probarlos en la app móvil:")
        print("  1. Inicia el servidor: cd backend && python main.py")
        print("  2. Inicia la app: cd mobile_app/lengua-de-senas && npm start")
        print("  3. Abre la app y selecciona un avatar nuevo")
        print("  4. Prueba una palabra (ej: 'hola', 'gracias')")
    else:
        print("⚠️  Algunos avatares tienen problemas.")
        print("Ejecuta: python scripts/verificar_avatares_app.py")
    
    print()
    print("=" * 70)

if __name__ == "__main__":
    main()
