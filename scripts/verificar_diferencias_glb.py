"""
Verificador de diferencias entre GLBs
Compara quaternions de animación para confirmar que se aplicaron cambios
"""

import numpy as np
from pathlib import Path
from pygltflib import GLTF2, BufferFormat
import struct

def leer_quaternions_hueso(gltf, nombre_hueso):
    """Lee los quaternions de un hueso específico"""
    # Encontrar nodo
    node_idx = None
    for i, node in enumerate(gltf.nodes):
        if node.name == nombre_hueso:
            node_idx = i
            break
    
    if node_idx is None:
        return None
    
    # Encontrar canal de rotación
    if not gltf.animations:
        return None
        
    anim = gltf.animations[0]
    for channel in anim.channels:
        if channel.target.node == node_idx and channel.target.path == 'rotation':
            sampler = anim.samplers[channel.sampler]
            
            # Leer accessor
            accessor = gltf.accessors[sampler.output]
            buffer_view = gltf.bufferViews[accessor.bufferView]
            buffer = gltf.buffers[buffer_view.buffer]
            
            data = gltf.get_data_from_buffer_uri(buffer.uri)
            offset = buffer_view.byteOffset + (accessor.byteOffset if accessor.byteOffset else 0)
            
            # Leer quaternions (4 floats cada uno)
            count = accessor.count
            quaternions = []
            for i in range(count):
                quat_offset = offset + i * 16  # 4 floats * 4 bytes
                quat = struct.unpack_from('ffff', data, quat_offset)
                quaternions.append(quat)
            
            return np.array(quaternions)
    
    return None

def comparar_glbs():
    """Compara original vs corregido"""
    BASE_DIR = Path(__file__).parent.parent
    GLB_ORIGINAL = BASE_DIR / "test" / "output" / "glb" / "Nancy" / "pronombres" / "Nancy_resultado_yo.glb"
    GLB_CORREGIDO = BASE_DIR / "test" / "output" / "glb" / "Nancy" / "pronombres" / "Nancy_resultado_yo_AUTOCORREGIDO.glb"
    
    print("Cargando GLBs...")
    gltf_orig = GLTF2().load(str(GLB_ORIGINAL))
    gltf_orig.convert_buffers(BufferFormat.DATAURI)
    
    gltf_corr = GLTF2().load(str(GLB_CORREGIDO))
    gltf_corr.convert_buffers(BufferFormat.DATAURI)
    
    huesos = [
        'RightHandIndex1',
        'RightHandMiddle1',
        'RightHandRing1',
        'RightHandPinky1',
        'RightHandThumb1'
    ]
    
    print("\nComparando quaternions de rotación:\n")
    
    diferencias_encontradas = 0
    
    for hueso in huesos:
        quats_orig = leer_quaternions_hueso(gltf_orig, hueso)
        quats_corr = leer_quaternions_hueso(gltf_corr, hueso)
        
        if quats_orig is not None and quats_corr is not None:
            # Calcular diferencia promedio
            diff = np.abs(quats_orig - quats_corr).mean()
            max_diff = np.abs(quats_orig - quats_corr).max()
            
            if diff > 0.0001:  # Umbral de diferencia significativa
                diferencias_encontradas += 1
                print(f"✅ {hueso}")
                print(f"   Diferencia promedio: {diff:.6f}")
                print(f"   Diferencia máxima: {max_diff:.6f}")
                print(f"   Frames: {len(quats_orig)}")
            else:
                print(f"⚠️  {hueso} - Sin cambios detectados")
        else:
            print(f"❌ {hueso} - No se pudo leer")
    
    print(f"\n{'='*50}")
    if diferencias_encontradas == 5:
        print("✅ VERIFICACIÓN EXITOSA")
        print(f"   5/5 huesos modificados correctamente")
        print(f"   Las animaciones son DIFERENTES")
    elif diferencias_encontradas > 0:
        print(f"⚠️  VERIFICACIÓN PARCIAL")
        print(f"   {diferencias_encontradas}/5 huesos modificados")
    else:
        print("❌ ERROR: No se detectaron cambios")
        print("   Los archivos son idénticos")
    
    return diferencias_encontradas

if __name__ == "__main__":
    comparar_glbs()
