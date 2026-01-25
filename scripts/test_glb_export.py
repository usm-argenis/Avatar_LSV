"""
Script para probar y validar exportaciones GLB con animaciones
Verifica que el GLB exportado contenga todas las animaciones correctamente

Uso:
    python test_glb_export.py archivo.glb
"""

import json
import sys
from pathlib import Path
import struct

def analyze_glb_file(glb_path):
    """
    Analiza un archivo GLB y verifica su contenido
    """
    glb_path = Path(glb_path)
    
    if not glb_path.exists():
        print(f"❌ Archivo no encontrado: {glb_path}")
        return False
        
    print(f"🔍 Analizando: {glb_path.name}")
    print(f"📏 Tamaño: {glb_path.stat().st_size / 1024 / 1024:.2f} MB")
    
    try:
        with open(glb_path, 'rb') as f:
            # Leer header GLB
            magic = f.read(4)
            if magic != b'glTF':
                print("❌ No es un archivo GLB válido")
                return False
                
            version = struct.unpack('<I', f.read(4))[0]
            total_length = struct.unpack('<I', f.read(4))[0]
            
            print(f"✅ GLB válido")
            print(f"   Versión: {version}")
            print(f"   Tamaño declarado: {total_length} bytes")
            
            # Leer primer chunk (JSON)
            json_length = struct.unpack('<I', f.read(4))[0]
            json_type = f.read(4)
            
            if json_type != b'JSON':
                print("❌ Primer chunk no es JSON")
                return False
                
            # Leer datos JSON
            json_data = f.read(json_length).decode('utf-8')
            gltf_json = json.loads(json_data)
            
            # Analizar contenido
            analyze_gltf_content(gltf_json)
            
            return True
            
    except Exception as e:
        print(f"❌ Error al analizar archivo: {str(e)}")
        return False

def analyze_gltf_content(gltf_json):
    """
    Analiza el contenido JSON del glTF
    """
    print(f"\n📊 Contenido del GLB:")
    
    # Información básica
    asset = gltf_json.get('asset', {})
    print(f"   Generador: {asset.get('generator', 'N/A')}")
    print(f"   Versión glTF: {asset.get('version', 'N/A')}")
    
    # Escenas
    scenes = gltf_json.get('scenes', [])
    print(f"   🎬 Escenas: {len(scenes)}")
    
    # Nodos
    nodes = gltf_json.get('nodes', [])
    print(f"   🔗 Nodos: {len(nodes)}")
    
    # Mallas
    meshes = gltf_json.get('meshes', [])
    print(f"   🎭 Mallas: {len(meshes)}")
    
    # Materiales
    materials = gltf_json.get('materials', [])
    print(f"   🎨 Materiales: {len(materials)}")
    
    # Texturas
    textures = gltf_json.get('textures', [])
    images = gltf_json.get('images', [])
    print(f"   🖼️  Texturas: {len(textures)}")
    print(f"   📷 Imágenes: {len(images)}")
    
    # CRÍTICO: Animaciones
    animations = gltf_json.get('animations', [])
    print(f"   🎬 ANIMACIONES: {len(animations)}")
    
    if len(animations) == 0:
        print(f"   ❌ ¡NO HAY ANIMACIONES EN EL GLB!")
        print(f"      Esto indica que la exportación no preservó las animaciones")
        return False
    else:
        print(f"   ✅ Animaciones encontradas:")
        for i, anim in enumerate(animations):
            name = anim.get('name', f'Animation_{i}')
            channels = len(anim.get('channels', []))
            samplers = len(anim.get('samplers', []))
            print(f"      [{i}] {name}: {channels} canales, {samplers} samplers")
    
    # Skins (para animaciones de esqueletos)
    skins = gltf_json.get('skins', [])
    print(f"   🦴 Skins/Esqueletos: {len(skins)}")
    
    if len(skins) > 0:
        for i, skin in enumerate(skins):
            joints = len(skin.get('joints', []))
            print(f"      [{i}] {joints} joints")
    
    # Accesorios (datos de animación)
    accessors = gltf_json.get('accessors', [])
    print(f"   📊 Accessors: {len(accessors)}")
    
    return True

def test_glb_in_browser():
    """
    Genera una página HTML simple para probar el GLB en el navegador
    """
    html_content = '''<!DOCTYPE html>
<html>
<head>
    <title>Test GLB Animation</title>
    <style>
        body { margin: 0; overflow: hidden; background: #2a2a2a; }
        canvas { display: block; }
        #info { 
            position: absolute; top: 10px; left: 10px; color: white; 
            font-family: Arial; font-size: 14px; z-index: 100;
        }
        #controls { 
            position: absolute; bottom: 10px; left: 10px; color: white; 
            font-family: Arial; font-size: 12px; z-index: 100;
        }
    </style>
</head>
<body>
    <div id="info">
        <h3>Test GLB Animation</h3>
        <div id="status">Cargando...</div>
        <div id="animations"></div>
    </div>
    
    <div id="controls">
        <button onclick="toggleAnimation()">Play/Pause</button>
        <button onclick="resetAnimation()">Reset</button>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/0.160.0/three.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/0.160.0/examples/js/loaders/GLTFLoader.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/0.160.0/examples/js/controls/OrbitControls.js"></script>
    
    <script>
        let scene, camera, renderer, mixer, model;
        let animations = [];
        let clock = new THREE.Clock();
        
        init();
        animate();
        
        function init() {
            // Escena
            scene = new THREE.Scene();
            scene.background = new THREE.Color(0x404040);
            
            // Cámara
            camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(0, 1.5, 3);
            
            // Renderer
            renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.outputEncoding = THREE.sRGBEncoding;
            document.body.appendChild(renderer.domElement);
            
            // Controles
            const controls = new THREE.OrbitControls(camera, renderer.domElement);
            
            // Luces
            const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
            scene.add(ambientLight);
            const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
            directionalLight.position.set(10, 10, 5);
            scene.add(directionalLight);
            
            // Cargar GLB
            const loader = new THREE.GLTFLoader();
            const glbFile = prompt("Introduce el nombre del archivo GLB (debe estar en la misma carpeta):") || "archivo.glb";
            
            loader.load(glbFile, function(gltf) {
                model = gltf.scene;
                scene.add(model);
                
                // Configurar animaciones
                if (gltf.animations && gltf.animations.length > 0) {
                    mixer = new THREE.AnimationMixer(model);
                    animations = gltf.animations;
                    
                    document.getElementById('status').innerHTML = `✅ Modelo cargado con ${animations.length} animaciones`;
                    
                    let animInfo = '<h4>Animaciones encontradas:</h4>';
                    animations.forEach((anim, i) => {
                        animInfo += `<div>${i}: ${anim.name} (${anim.duration.toFixed(2)}s)</div>`;
                        
                        // Reproducir primera animación
                        if (i === 0) {
                            const action = mixer.clipAction(anim);
                            action.play();
                        }
                    });
                    document.getElementById('animations').innerHTML = animInfo;
                } else {
                    document.getElementById('status').innerHTML = '❌ No hay animaciones en el archivo';
                    document.getElementById('animations').innerHTML = '<div style="color: red;">El GLB no contiene animaciones</div>';
                }
                
                // Centrar modelo
                const box = new THREE.Box3().setFromObject(model);
                const center = box.getCenter(new THREE.Vector3());
                model.position.sub(center);
                
            }, undefined, function(error) {
                document.getElementById('status').innerHTML = '❌ Error cargando archivo: ' + error;
                console.error('Error:', error);
            });
        }
        
        function animate() {
            requestAnimationFrame(animate);
            
            if (mixer) mixer.update(clock.getDelta());
            renderer.render(scene, camera);
        }
        
        function toggleAnimation() {
            if (mixer && animations.length > 0) {
                mixer._actions.forEach(action => {
                    if (action.isRunning()) {
                        action.paused = !action.paused;
                    }
                });
            }
        }
        
        function resetAnimation() {
            if (mixer && animations.length > 0) {
                mixer._actions.forEach(action => {
                    action.reset().play();
                });
            }
        }
        
        // Redimensionar
        window.addEventListener('resize', function() {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });
    </script>
</body>
</html>'''
    
    test_html_path = Path("test_glb_animation.html")
    with open(test_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\n🌐 Archivo de prueba creado: {test_html_path}")
    print(f"   💡 Abre este archivo en un navegador para probar el GLB")
    print(f"   📁 Asegúrate de que el GLB esté en la misma carpeta")

def main():
    """
    Función principal
    """
    print("="*60)
    print("🔍 VALIDADOR DE ARCHIVOS GLB CON ANIMACIONES")
    print("="*60)
    
    if len(sys.argv) < 2:
        print("Uso: python test_glb_export.py archivo.glb")
        print("\nO ejecuta sin argumentos para crear archivo de prueba HTML")
        
        # Crear archivo de prueba HTML
        test_glb_in_browser()
        return
    
    glb_file = sys.argv[1]
    
    # Analizar archivo
    success = analyze_glb_file(glb_file)
    
    if success:
        print(f"\n🎉 Análisis completado")
        print(f"💡 Para probar la animación:")
        print(f"   1. Ejecuta: python test_glb_export.py")
        print(f"   2. Abre test_glb_animation.html en navegador")
        print(f"   3. Introduce el nombre del archivo GLB")
    else:
        print(f"\n💥 Hubo problemas con el archivo GLB")
        print(f"💡 Vuelve a exportar usando export_blend_to_glb.py")

if __name__ == "__main__":
    main()