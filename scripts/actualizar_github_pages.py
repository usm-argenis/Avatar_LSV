"""
Script para actualizar GitHub Pages con animation_mobile.html y todos los archivos GLB
Copia archivos desde test/output/glb hacia gh-pages-worktree
"""

import os
import shutil
from pathlib import Path
import json

def main():
    print("=" * 60)
    print("🚀 ACTUALIZAR GITHUB PAGES - LSV")
    print("=" * 60)
    print()
    
    # Directorios base
    base_dir = Path(__file__).parent.parent
    source_glb = base_dir / "test" / "output" / "glb"
    source_html = base_dir / "test" / "animation_mobile.html"
    dest_dir = base_dir / "gh-pages-worktree"
    dest_test = dest_dir / "test"
    dest_glb = dest_test / "output" / "glb"
    
    # Verificar que existen los directorios
    if not source_glb.exists():
        print(f"❌ Error: No se encontró el directorio {source_glb}")
        return False
        
    if not source_html.exists():
        print(f"❌ Error: No se encontró {source_html}")
        return False
        
    if not dest_dir.exists():
        print(f"❌ Error: No se encontró el directorio gh-pages-worktree")
        print("   Debes tener configurado GitHub Pages primero")
        return False
    
    # Crear directorios de destino si no existen
    dest_test.mkdir(exist_ok=True)
    dest_glb.mkdir(parents=True, exist_ok=True)
    
    print("✅ Directorios verificados")
    print()
    
    # 1. Copiar animation_mobile.html
    print("📄 Copiando animation_mobile.html...")
    shutil.copy2(source_html, dest_test / "animation_mobile.html")
    print(f"   ✓ Copiado a {dest_test / 'animation_mobile.html'}")
    print()
    
    # 2. Copiar todos los archivos GLB organizados por avatar y categoría
    print("📦 Copiando archivos GLB...")
    total_files = 0
    avatares = {}
    
    # Recorrer todos los avatares
    for avatar_dir in source_glb.iterdir():
        if not avatar_dir.is_dir():
            continue
            
        avatar_name = avatar_dir.name
        avatares[avatar_name] = {"categorias": {}, "total": 0}
        
        print(f"\n👤 Avatar: {avatar_name}")
        
        # Crear directorio del avatar en destino
        dest_avatar = dest_glb / avatar_name
        dest_avatar.mkdir(exist_ok=True)
        
        # Copiar el archivo base del avatar (si existe)
        avatar_base = avatar_dir / f"{avatar_name}.glb"
        if avatar_base.exists():
            shutil.copy2(avatar_base, dest_avatar / f"{avatar_name}.glb")
            print(f"   ✓ {avatar_name}.glb (modelo base)")
            total_files += 1
            avatares[avatar_name]["total"] += 1
        
        # Recorrer categorías
        for categoria_dir in avatar_dir.iterdir():
            if not categoria_dir.is_dir():
                continue
                
            categoria_name = categoria_dir.name
            
            # Crear directorio de categoría
            dest_categoria = dest_avatar / categoria_name
            dest_categoria.mkdir(exist_ok=True)
            
            # Contar archivos en la categoría
            glb_files = list(categoria_dir.glob("*.glb"))
            if glb_files:
                avatares[avatar_name]["categorias"][categoria_name] = len(glb_files)
                avatares[avatar_name]["total"] += len(glb_files)
                
                print(f"   📁 {categoria_name}: {len(glb_files)} archivos")
                
                # Copiar todos los GLB de la categoría
                for glb_file in glb_files:
                    dest_file = dest_categoria / glb_file.name
                    shutil.copy2(glb_file, dest_file)
                    total_files += 1
    
    print()
    print("=" * 60)
    print(f"✅ ACTUALIZACIÓN COMPLETADA")
    print("=" * 60)
    print()
    print(f"📊 Resumen:")
    print(f"   • Total de archivos GLB copiados: {total_files}")
    print(f"   • Avatares procesados: {len(avatares)}")
    print()
    
    # Mostrar detalle por avatar
    for avatar, data in avatares.items():
        print(f"   👤 {avatar}: {data['total']} archivos")
        for cat, count in data['categorias'].items():
            print(f"      - {cat}: {count}")
    
    print()
    print("📍 Archivos copiados a:")
    print(f"   {dest_test / 'animation_mobile.html'}")
    print(f"   {dest_glb}")
    print()
    
    # 3. Crear un archivo JSON con el inventario
    print("📝 Creando inventario de animaciones...")
    inventory_file = dest_test / "animations_inventory.json"
    inventory = {
        "last_updated": str(Path.cwd()),
        "total_files": total_files,
        "avatares": avatares
    }
    
    with open(inventory_file, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, indent=2, ensure_ascii=False)
    
    print(f"   ✓ Inventario guardado en {inventory_file}")
    print()
    
    # 4. Instrucciones finales
    print("=" * 60)
    print("📋 PRÓXIMOS PASOS:")
    print("=" * 60)
    print()
    print("1. Actualizar index.html para agregar link a animation_mobile.html")
    print("2. Hacer commit y push a la rama gh-pages:")
    print()
    print("   cd gh-pages-worktree")
    print("   git add .")
    print('   git commit -m "Actualizar animaciones y archivos GLB"')
    print("   git push origin gh-pages")
    print()
    print("3. Tu GitHub Pages se actualizará automáticamente")
    print()
    
    return True

if __name__ == "__main__":
    success = main()
    if success:
        print("🎉 ¡Todo listo!")
    else:
        print("❌ Hubo errores en la actualización")
    
    input("\nPresiona Enter para salir...")
