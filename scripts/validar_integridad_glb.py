"""
Prueba visual del GLB corregido
Valida que el avatar no esté deformado
"""

from pathlib import Path
from pygltflib import GLTF2
import json

def validar_integridad_glb():
    """Valida que el GLB no tenga deformaciones"""
    BASE_DIR = Path(__file__).parent.parent
    GLB_CORREGIDO = BASE_DIR / "test" / "output" / "glb" / "Nancy" / "pronombres" / "Nancy_resultado_yo_AUTOCORREGIDO.glb"
    
    print("Validando integridad del GLB...\n")
    
    gltf = GLTF2().load(str(GLB_CORREGIDO))
    
    # 1. Verificar número de nodos (no debe cambiar)
    assert len(gltf.nodes) == 85, f"ERROR: Nodos incorrectos {len(gltf.nodes)}"
    print(f"✅ Nodos: {len(gltf.nodes)} (correcto)")
    
    # 2. Verificar meshes (no deben cambiar)
    num_meshes = len(gltf.meshes) if gltf.meshes else 0
    assert num_meshes == 9, f"ERROR: Meshes incorrectos {num_meshes}"
    print(f"✅ Meshes: {num_meshes} (correcto)")
    
    # 3. Verificar animación
    assert gltf.animations and len(gltf.animations) > 0, "ERROR: Sin animación"
    anim = gltf.animations[0]
    assert len(anim.channels) == 201, f"ERROR: Canales incorrectos {len(anim.channels)}"
    print(f"✅ Animación: {len(anim.channels)} canales (correcto)")
    
    # 4. Verificar que los huesos de dedos tengan rotación
    dedos_con_rotacion = 0
    huesos_dedos = [
        'RightHandIndex1', 'RightHandMiddle1', 'RightHandRing1',
        'RightHandPinky1', 'RightHandThumb1'
    ]
    
    node_indices = {}
    for i, node in enumerate(gltf.nodes):
        if node.name in huesos_dedos:
            node_indices[node.name] = i
    
    for channel in anim.channels:
        if channel.target.node in node_indices.values() and channel.target.path == 'rotation':
            dedos_con_rotacion += 1
    
    assert dedos_con_rotacion == 5, f"ERROR: Solo {dedos_con_rotacion}/5 dedos con animación"
    print(f"✅ Dedos animados: {dedos_con_rotacion}/5 (correcto)")
    
    # 5. Verificar que NO hay escalado extraño
    for node in gltf.nodes:
        if node.scale:
            # Escala debe estar cerca de [1, 1, 1]
            for s in node.scale:
                assert 0.1 < s < 10.0, f"ERROR: Escala anormal en {node.name}: {node.scale}"
    print(f"✅ Sin escalados anormales")
    
    # 6. Verificar tamaño del archivo
    size_mb = GLB_CORREGIDO.stat().st_size / (1024 * 1024)
    assert 2.0 < size_mb < 4.0, f"ERROR: Tamaño anormal {size_mb:.2f} MB"
    print(f"✅ Tamaño: {size_mb:.2f} MB (normal)")
    
    print(f"\n{'='*50}")
    print("✅ VALIDACIÓN COMPLETA EXITOSA")
    print("   El GLB está íntegro y sin deformaciones")
    print("   Listo para usar en el comparador")
    
    return True

if __name__ == "__main__":
    try:
        validar_integridad_glb()
    except AssertionError as e:
        print(f"\n❌ VALIDACIÓN FALLIDA: {e}")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
