"""
Script para crear animaciones de Carlos copiando las de Remy
"""
import os
import shutil
from pathlib import Path

def crear_animaciones_carlos():
    base_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
    remy_path = base_path / "Remy"
    carlos_path = base_path / "Carlos"
    
    categorias = ['alfabeto', 'dias_semana', 'tiempo', 'pronombres', 
                  'saludos', 'cortesia', 'preguntas', 'expresiones']
    
    total_copiados = 0
    
    print("=" * 80)
    print("📋 CREANDO ANIMACIONES PARA CARLOS")
    print("=" * 80)
    
    for categoria in categorias:
        remy_cat_path = remy_path / categoria
        carlos_cat_path = carlos_path / categoria
        
        if not remy_cat_path.exists():
            print(f"⚠️ No existe: {remy_cat_path}")
            continue
        
        archivos_remy = list(remy_cat_path.glob("Remy_resultado_*.glb"))
        
        print(f"\n📁 {categoria.upper()}: {len(archivos_remy)} archivos")
        
        for archivo_remy in archivos_remy:
            # Crear nombre para Carlos
            nombre_carlos = archivo_remy.name.replace("Remy_resultado_", "Carlos_resultado_")
            archivo_carlos = carlos_cat_path / nombre_carlos
            
            # Copiar archivo
            shutil.copy2(archivo_remy, archivo_carlos)
            print(f"   ✅ {archivo_remy.name} → {nombre_carlos}")
            total_copiados += 1
    
    print("\n" + "=" * 80)
    print(f"✅ COMPLETADO: {total_copiados} archivos copiados para Carlos")
    print("=" * 80)

if __name__ == "__main__":
    crear_animaciones_carlos()
