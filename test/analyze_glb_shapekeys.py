"""
Script para analizar shape keys en archivos GLB usando pygltflib
"""
import json
from pathlib import Path

try:
    from pygltflib import GLTF2
except ImportError:
    print("Instalando pygltflib...")
    import subprocess
    subprocess.check_call(['pip', 'install', 'pygltflib'])
    from pygltflib import GLTF2

def analyze_glb_shapekeys(glb_path):
    """Analiza los shape keys (morph targets) de un archivo GLB"""
    
    glb_file = Path(glb_path)
    if not glb_file.exists():
        print(f"❌ Archivo no encontrado: {glb_path}")
        return None
    
    print(f"\n{'='*70}")
    print(f"🔍 ANALIZANDO: {glb_file.name}")
    print(f"{'='*70}\n")
    
    # Cargar GLB
    gltf = GLTF2().load(glb_path)
    
    results = {
        'file': str(glb_path),
        'meshes': [],
        'total_shape_keys': 0
    }
    
    # Analizar cada mesh
    for mesh_idx, mesh in enumerate(gltf.meshes):
        mesh_info = {
            'mesh_index': mesh_idx,
            'mesh_name': mesh.name if mesh.name else f'Mesh_{mesh_idx}',
            'primitives': []
        }
        
        # Analizar primitivas del mesh
        for prim_idx, primitive in enumerate(mesh.primitives):
            prim_info = {
                'primitive_index': prim_idx,
                'shape_keys': []
            }
            
            # Verificar si tiene targets (shape keys/morph targets)
            if hasattr(primitive, 'targets') and primitive.targets:
                print(f"\n📦 Mesh: {mesh_info['mesh_name']} (Primitiva {prim_idx})")
                print(f"   ✅ Encontrados {len(primitive.targets)} shape keys")
                
                # Intentar obtener los nombres de los shape keys
                if mesh.extras:
                    try:
                        extras = json.loads(json.dumps(mesh.extras))
                        if 'targetNames' in extras:
                            target_names = extras['targetNames']
                            print(f"   📝 Nombres disponibles: {target_names}")
                            
                            for i, name in enumerate(target_names):
                                if i < len(primitive.targets):
                                    shape_key_info = {
                                        'index': i,
                                        'name': name,
                                        'attributes': list(primitive.targets[i].keys())
                                    }
                                    prim_info['shape_keys'].append(shape_key_info)
                                    print(f"      {i}: {name} - Atributos: {list(primitive.targets[i].keys())}")
                    except Exception as e:
                        print(f"   ⚠️ No se pudieron obtener nombres: {e}")
                
                # Si no hay nombres, listar por índice
                if not prim_info['shape_keys']:
                    for i, target in enumerate(primitive.targets):
                        shape_key_info = {
                            'index': i,
                            'name': f'Target_{i}',
                            'attributes': list(target.keys())
                        }
                        prim_info['shape_keys'].append(shape_key_info)
                        print(f"      {i}: Target_{i} - Atributos: {list(target.keys())}")
                
                results['total_shape_keys'] += len(primitive.targets)
            
            if prim_info['shape_keys']:
                mesh_info['primitives'].append(prim_info)
        
        if mesh_info['primitives']:
            results['meshes'].append(mesh_info)
    
    # Resumen
    print(f"\n{'='*70}")
    print(f"📊 RESUMEN:")
    print(f"{'='*70}")
    print(f"Total de meshes con shape keys: {len(results['meshes'])}")
    print(f"Total de shape keys encontrados: {results['total_shape_keys']}")
    
    # Guardar resultados
    output_file = glb_file.parent / f"{glb_file.stem}_shapekeys_analysis.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Análisis guardado en: {output_file}")
    print(f"{'='*70}\n")
    
    return results

if __name__ == "__main__":
    # Analizar Luis.glb
    glb_path = r"output\glb\Luis\Luis.glb"
    results = analyze_glb_shapekeys(glb_path)
    
    if results:
        print("\n✅ Análisis completado exitosamente")
        print(f"\nPara usar estos shape keys en Three.js:")
        print("1. Acceder al mesh con shape keys: mesh.morphTargetInfluences")
        print("2. Los índices corresponden a los shape keys listados arriba")
        print("3. Los valores van de 0.0 (sin efecto) a 1.0 (efecto completo)")
        print("\nEjemplo en Three.js:")
        print("  mesh.morphTargetInfluences[0] = 0.5; // 50% del primer shape key")
    else:
        print("\n❌ No se pudo completar el análisis")
