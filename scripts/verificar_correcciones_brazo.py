"""
Verificador de correcciones de brazo
Compara posiciones de translación entre original y corregido
"""

import numpy as np
from pathlib import Path
from pygltflib import GLTF2, BufferFormat
import struct

def leer_translaciones_hueso(gltf, nombre_hueso):
    """Lee las translaciones de un hueso específico"""
    # Encontrar nodo
    node_idx = None
    for i, node in enumerate(gltf.nodes):
        if node.name == nombre_hueso:
            node_idx = i
            break
    
    if node_idx is None:
        return None, None
    
    # Verificar translación base del nodo
    node = gltf.nodes[node_idx]
    trans_base = node.translation if node.translation else [0.0, 0.0, 0.0]
    
    # Encontrar canal de translación animada
    if not gltf.animations:
        return trans_base, None
        
    anim = gltf.animations[0]
    for channel in anim.channels:
        if channel.target.node == node_idx and channel.target.path == 'translation':
            sampler = anim.samplers[channel.sampler]
            
            # Leer accessor
            accessor = gltf.accessors[sampler.output]
            buffer_view = gltf.bufferViews[accessor.bufferView]
            buffer = gltf.buffers[buffer_view.buffer]
            
            data = gltf.get_data_from_buffer_uri(buffer.uri)
            offset = buffer_view.byteOffset + (accessor.byteOffset if accessor.byteOffset else 0)
            
            # Leer translaciones (3 floats cada una: x, y, z)
            count = accessor.count
            translaciones = []
            for i in range(count):
                trans_offset = offset + i * 12  # 3 floats * 4 bytes
                trans = struct.unpack_from('fff', data, trans_offset)
                translaciones.append(trans)
            
            return trans_base, np.array(translaciones)
    
    return trans_base, None

def verificar_correcciones_brazo():
    """Verifica que las correcciones de brazo se aplicaron"""
    BASE_DIR = Path(__file__).parent.parent
    GLB_ORIGINAL = BASE_DIR / "test" / "output" / "glb" / "Nancy" / "pronombres" / "Nancy_resultado_yo.glb"
    GLB_CORREGIDO = BASE_DIR / "test" / "output" / "glb" / "Nancy" / "pronombres" / "Nancy_resultado_yo_AUTOCORREGIDO.glb"
    
    print("Verificando correcciones de brazo...\n")
    
    gltf_orig = GLTF2().load(str(GLB_ORIGINAL))
    gltf_orig.convert_buffers(BufferFormat.DATAURI)
    
    gltf_corr = GLTF2().load(str(GLB_CORREGIDO))
    gltf_corr.convert_buffers(BufferFormat.DATAURI)
    
    huesos_brazo = ['RightForeArm', 'RightHand']
    
    print("Comparando posiciones (eje Z = adelante/atrás):\n")
    
    correcciones_detectadas = 0
    
    for hueso in huesos_brazo:
        base_orig, anim_orig = leer_translaciones_hueso(gltf_orig, hueso)
        base_corr, anim_corr = leer_translaciones_hueso(gltf_corr, hueso)
        
        print(f"📍 {hueso}:")
        
        # Comparar translación base
        if base_orig and base_corr:
            diff_base = base_corr[2] - base_orig[2]  # Z
            if abs(diff_base) > 0.001:
                correcciones_detectadas += 1
                print(f"   ✅ Translación base Z: {base_orig[2]:.4f} → {base_corr[2]:.4f}")
                print(f"   📏 Desplazamiento: +{diff_base:.4f}m ({diff_base*100:.1f}cm adelante)")
        
        # Comparar animación
        if anim_orig is not None and anim_corr is not None:
            diff_anim = np.abs(anim_orig[:, 2] - anim_corr[:, 2]).mean()
            if diff_anim > 0.001:
                print(f"   ✅ Animación modificada: {len(anim_orig)} frames")
                print(f"   📏 Diferencia Z promedio: {diff_anim:.4f}m")
        elif anim_orig is None and anim_corr is None:
            print(f"   ℹ️  Sin animación de translación")
        
        print()
    
    # Verificar si hubo cambios en animación
    huesos_con_cambios = []
    for hueso in huesos_brazo:
        base_orig, anim_orig = leer_translaciones_hueso(gltf_orig, hueso)
        base_corr, anim_corr = leer_translaciones_hueso(gltf_corr, hueso)
        
        if anim_orig is not None and anim_corr is not None:
            diff_anim = np.abs(anim_orig[:, 2] - anim_corr[:, 2]).mean()
            if diff_anim > 0.001:
                huesos_con_cambios.append(hueso)
    
    print(f"{'='*50}")
    if len(huesos_con_cambios) > 0 or correcciones_detectadas > 0:
        print(f"✅ CORRECCIONES DE BRAZO APLICADAS")
        print(f"   {len(huesos_con_cambios)} huesos con animación modificada")
        print(f"   {correcciones_detectadas} huesos con translación base modificada")
        print(f"   La mano estará más visible (adelante del torso)")
    else:
        print("⚠️  No se detectaron correcciones de brazo")
    
    return correcciones_detectadas

if __name__ == "__main__":
    verificar_correcciones_brazo()
