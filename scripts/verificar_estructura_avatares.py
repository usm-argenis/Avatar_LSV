"""
Script para verificar la nueva estructura de avatares
"""
from pathlib import Path
import json

def verificar_estructura():
    base_path = Path("test/output/glb")
    
    print("=" * 80)
    print("🔍 VERIFICACIÓN DE ESTRUCTURA DE AVATARES")
    print("=" * 80)
    
    avatares = {}
    
    # Buscar avatares
    for avatar_dir in base_path.iterdir():
        if avatar_dir.is_dir() and avatar_dir.name not in ['cc']:
            avatar_name = avatar_dir.name
            avatares[avatar_name] = {}
            
            print(f"\n📁 Avatar: {avatar_name}")
            print("-" * 80)
            
            total_archivos = 0
            
            # Buscar categorías
            for categoria_dir in sorted(avatar_dir.iterdir()):
                if categoria_dir.is_dir():
                    archivos = list(categoria_dir.glob(f"{avatar_name}_resultado_*.glb"))
                    avatares[avatar_name][categoria_dir.name] = len(archivos)
                    total_archivos += len(archivos)
                    
                    print(f"   📂 {categoria_dir.name:15} : {len(archivos):3} archivos")
            
            print("-" * 80)
            print(f"   ✅ TOTAL: {total_archivos} animaciones")
    
    print("\n" + "=" * 80)
    print("📊 RESUMEN")
    print("=" * 80)
    
    for avatar, categorias in avatares.items():
        total = sum(categorias.values())
        print(f"\n{avatar}: {total} animaciones")
        for cat, count in sorted(categorias.items()):
            print(f"  • {cat}: {count}")
    
    print("\n" + "=" * 80)
    print("✅ VERIFICACIÓN COMPLETADA")
    print("=" * 80)
    
    # Guardar resumen JSON
    with open("test/output/glb/estructura_avatares.json", "w", encoding="utf-8") as f:
        json.dump(avatares, f, indent=2, ensure_ascii=False)
    
    print("\n💾 Resumen guardado en: test/output/glb/estructura_avatares.json")

if __name__ == "__main__":
    verificar_estructura()
