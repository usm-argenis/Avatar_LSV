"""
Script para preparar y desplegar el visualizador en GitHub Pages
"""

import shutil
from pathlib import Path
import json

# Rutas
BASE_PATH = Path(__file__).resolve().parents[1]
TEST_DIR = BASE_PATH / "test"
DEPLOY_DIR = BASE_PATH / "deploy-viewer-temp"
OUTPUT_DIR = BASE_PATH / "output"

def limpiar_deploy():
    """Limpia el directorio de despliegue"""
    print("🧹 Limpiando directorio de despliegue...")
    
    if DEPLOY_DIR.exists():
        # Mantener .git si existe
        git_dir = DEPLOY_DIR / ".git"
        if git_dir.exists():
            print("   ℹ️ Manteniendo directorio .git")
        
        # Limpiar archivos
        for item in DEPLOY_DIR.iterdir():
            if item.name != ".git":
                if item.is_file():
                    item.unlink()
                elif item.is_dir():
                    shutil.rmtree(item)
    else:
        DEPLOY_DIR.mkdir(parents=True)
    
    print("✅ Directorio limpiado")

def copiar_html():
    """Copia el archivo HTML principal"""
    print("\n📄 Copiando archivos HTML...")
    
    # Buscar el visualizador principal
    html_files = [
        TEST_DIR / "visualizador_senas.html",
        TEST_DIR / "viewer_senas_v3.html",
        TEST_DIR / "index.html"
    ]
    
    for html_file in html_files:
        if html_file.exists():
            # Copiar como index.html
            shutil.copy2(html_file, DEPLOY_DIR / "index.html")
            print(f"   ✅ Copiado: {html_file.name} → index.html")
            break
    else:
        print("   ❌ No se encontró archivo HTML principal")
        return False
    
    return True

def copiar_assets():
    """Copia assets (CSS, JS, imágenes)"""
    print("\n📦 Copiando assets...")
    
    # Copiar directorio test completo (contiene viewer.js, etc.)
    test_dest = DEPLOY_DIR / "test"
    if not test_dest.exists():
        test_dest.mkdir()
    
    # Copiar archivos JavaScript
    js_files = ['viewer.js', 'viewer_senas.js', 'viewer_senas_v2.js']
    for js_file in js_files:
        src = TEST_DIR / js_file
        if src.exists():
            shutil.copy2(src, test_dest / js_file)
            print(f"   ✅ {js_file}")
    
    # Copiar subdirectorios importantes
    subdirs = ['output', 'data', 'scripts']
    for subdir in subdirs:
        src_dir = TEST_DIR / subdir
        if src_dir.exists():
            dest_dir = test_dest / subdir
            if dest_dir.exists():
                shutil.rmtree(dest_dir)
            shutil.copytree(src_dir, dest_dir)
            print(f"   ✅ {subdir}/")

def copiar_glb_files():
    """Copia archivos GLB de animaciones"""
    print("\n🎬 Copiando animaciones GLB...")
    
    # Crear directorio output/glb en deploy
    glb_dest = DEPLOY_DIR / "test" / "output" / "glb"
    glb_dest.mkdir(parents=True, exist_ok=True)
    
    # Copiar GLBs desde test/output/glb
    glb_src = TEST_DIR / "output" / "glb"
    if glb_src.exists():
        count = 0
        for glb_file in glb_src.glob("*.glb"):
            shutil.copy2(glb_file, glb_dest / glb_file.name)
            count += 1
        print(f"   ✅ {count} archivos GLB copiados")
    
    # Copiar GLBs adicionales desde output/
    if OUTPUT_DIR.exists():
        for glb_file in OUTPUT_DIR.glob("*.glb"):
            shutil.copy2(glb_file, glb_dest / glb_file.name)
            print(f"   ✅ {glb_file.name}")

def crear_readme():
    """Crea README para GitHub Pages"""
    print("\n📝 Creando README...")
    
    readme_content = """# Visualizador de Lengua de Señas Venezolana (LSV)

## 🎯 Acceso Directo

**URL:** https://usm-argenis.github.io/STT_LSV/

## 📖 Uso

### Parámetros de URL

```
?word=SEÑA&avatar=AVATAR&autoload=true
```

**Parámetros:**
- `word`: Nombre de la seña a mostrar (ej: `hola`, `gracias`, `a`, `b`)
- `avatar`: Avatar a usar (`Remy`, `Leonard`, `JH`)
- `autoload`: Cargar automáticamente (`true` o `false`)

### Ejemplos

**Letra "R":**
```
https://usm-argenis.github.io/STT_LSV/?word=r&avatar=Remy&autoload=true
```

**Palabra "Hola":**
```
https://usm-argenis.github.io/STT_LSV/?word=hola&avatar=Leonard&autoload=true
```

**Alfabeto completo:**
```
https://usm-argenis.github.io/STT_LSV/?word=a&avatar=Remy
```

## 🎮 Controles

- **Reproducir/Pausar**: Barra espaciadora
- **Reiniciar**: Botón "Restart"
- **Cambiar Avatar**: Selector dropdown
- **Cargar Seña**: Input + botón "Load"

## 📚 Señas Disponibles

### Alfabeto
A-Z, Ñ

### Números
0-9

### Palabras Comunes
- Saludos: hola, adiós, buenos días
- Cortesía: gracias, por favor, perdón
- Familia: papá, mamá, hermano
- Lugares: casa, escuela, trabajo

## 🔧 Tecnologías

- **Three.js**: Renderizado 3D
- **GLTFLoader**: Carga de modelos 3D
- **Vanilla JS**: Sin frameworks

## 📱 Integración con App Móvil

Esta página se integra con la app móvil React Native de LSV.

---

*Última actualización: Noviembre 2025*
"""
    
    with open(DEPLOY_DIR / "README.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("✅ README creado")

def crear_configuracion_github():
    """Crea archivos de configuración de GitHub Pages"""
    print("\n⚙️ Creando configuración de GitHub Pages...")
    
    # Crear .nojekyll para evitar procesamiento de Jekyll
    (DEPLOY_DIR / ".nojekyll").touch()
    print("   ✅ .nojekyll creado")
    
    # Crear CNAME si tienes dominio personalizado
    # (DEPLOY_DIR / "CNAME").write_text("tu-dominio.com")

def generar_indice_senas():
    """Genera un índice JSON de todas las señas disponibles"""
    print("\n📊 Generando índice de señas...")
    
    glb_dir = DEPLOY_DIR / "test" / "output" / "glb"
    if not glb_dir.exists():
        print("   ⚠️ No se encontró directorio de GLB")
        return
    
    senas = []
    for glb_file in glb_dir.glob("*.glb"):
        # Formato esperado: Avatar_resultado_SEÑA.glb
        name = glb_file.stem
        parts = name.split('_')
        
        if len(parts) >= 3:
            avatar = parts[0]
            sena = parts[-1]
            
            senas.append({
                'seña': sena,
                'avatar': avatar,
                'archivo': glb_file.name,
                'tamaño_mb': round(glb_file.stat().st_size / (1024 * 1024), 2)
            })
    
    # Guardar índice
    indice_path = DEPLOY_DIR / "test" / "output" / "indice_senas.json"
    with open(indice_path, 'w', encoding='utf-8') as f:
        json.dump({
            'total': len(senas),
            'senas': senas
        }, f, indent=2, ensure_ascii=False)
    
    print(f"   ✅ Índice generado: {len(senas)} señas")

def main():
    print("=" * 70)
    print("🚀 PREPARACIÓN PARA GITHUB PAGES")
    print("=" * 70)
    
    # 1. Limpiar
    limpiar_deploy()
    
    # 2. Copiar HTML
    if not copiar_html():
        print("\n❌ Error al copiar HTML. Proceso detenido.")
        return
    
    # 3. Copiar assets
    copiar_assets()
    
    # 4. Copiar GLB
    copiar_glb_files()
    
    # 5. Crear README
    crear_readme()
    
    # 6. Configuración GitHub
    crear_configuracion_github()
    
    # 7. Generar índice
    generar_indice_senas()
    
    print("\n" + "=" * 70)
    print("✅ PREPARACIÓN COMPLETADA")
    print("=" * 70)
    print(f"\n📁 Archivos listos en: {DEPLOY_DIR}")
    print("\n📋 SIGUIENTE PASO - DESPLEGAR A GITHUB:")
    print("   1. cd deploy-viewer-temp")
    print("   2. git add .")
    print("   3. git commit -m 'Update viewer'")
    print("   4. git push origin gh-pages")
    print("\n🌐 URL después de desplegar:")
    print("   https://usm-argenis.github.io/STT_LSV/")

if __name__ == "__main__":
    main()
