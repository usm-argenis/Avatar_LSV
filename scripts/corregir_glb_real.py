"""
Corrector REAL de GLB - Aplica modificaciones directas a la animación
Modifica los quaternions de rotación en los buffers binarios
"""

import struct
import numpy as np
from pathlib import Path
from pygltflib import GLTF2, BufferFormat
import json
from scipy.spatial.transform import Rotation

class GLBRealCorrector:
    def __init__(self, glb_path, output_path):
        self.glb_path = Path(glb_path)
        self.output_path = Path(output_path)
        self.gltf = None
        self.modificaciones_aplicadas = []
        
    def cargar(self):
        """Carga el GLB"""
        self.gltf = GLTF2().load(str(self.glb_path))
        self.gltf.convert_buffers(BufferFormat.DATAURI)
        return True
        
    def encontrar_node_index(self, nombre_hueso):
        """Encuentra el índice del nodo por nombre"""
        for i, node in enumerate(self.gltf.nodes):
            if node.name == nombre_hueso:
                return i
        return None
        
    def encontrar_animation_channel(self, node_index, path='rotation'):
        """Encuentra el canal de animación para un nodo específico"""
        if not self.gltf.animations:
            return None, None
            
        anim = self.gltf.animations[0]
        
        for channel_idx, channel in enumerate(anim.channels):
            if channel.target.node == node_index and channel.target.path == path:
                sampler_idx = channel.sampler
                return channel_idx, anim.samplers[sampler_idx]
        
        return None, None
        
    def leer_accessor_data(self, accessor_idx):
        """Lee datos de un accessor"""
        accessor = self.gltf.accessors[accessor_idx]
        buffer_view = self.gltf.bufferViews[accessor.bufferView]
        buffer = self.gltf.buffers[buffer_view.buffer]
        
        # Obtener datos binarios
        data = self.gltf.get_data_from_buffer_uri(buffer.uri)
        
        offset = buffer_view.byteOffset + (accessor.byteOffset if accessor.byteOffset else 0)
        
        # Determinar tipo y tamaño
        component_type = accessor.componentType
        type_map = {
            5120: ('b', 1),  # BYTE
            5121: ('B', 1),  # UNSIGNED_BYTE
            5122: ('h', 2),  # SHORT
            5123: ('H', 2),  # UNSIGNED_SHORT
            5125: ('I', 4),  # UNSIGNED_INT
            5126: ('f', 4),  # FLOAT
        }
        
        fmt, size = type_map.get(component_type, ('f', 4))
        
        # Número de componentes por elemento
        type_sizes = {'SCALAR': 1, 'VEC2': 2, 'VEC3': 3, 'VEC4': 4, 'MAT4': 16}
        num_components = type_sizes.get(accessor.type, 1)
        
        # Leer datos
        count = accessor.count
        element_size = size * num_components
        
        result = []
        for i in range(count):
            element_offset = offset + i * element_size
            element_data = struct.unpack_from(fmt * num_components, data, element_offset)
            result.append(list(element_data))
        
        return np.array(result)
        
    def escribir_accessor_data(self, accessor_idx, new_data):
        """Escribe datos modificados a un accessor"""
        accessor = self.gltf.accessors[accessor_idx]
        buffer_view = self.gltf.bufferViews[accessor.bufferView]
        
        # Como convertimos a DATAURI, necesitamos trabajar con el buffer view directamente
        # El buffer está en formato data URI después de convert_buffers
        
        # Reconstruir los datos del buffer
        binary_blob = self.gltf.binary_blob()
        if binary_blob:
            data = bytearray(binary_blob)
        else:
            # Si no hay binary blob, trabajar con el buffer URI
            buffer = self.gltf.buffers[buffer_view.buffer]
            data = bytearray(self.gltf.get_data_from_buffer_uri(buffer.uri))
        
        offset = buffer_view.byteOffset + (accessor.byteOffset if accessor.byteOffset else 0)
        
        component_type = accessor.componentType
        type_map = {5126: ('f', 4)}  # FLOAT
        fmt, size = type_map.get(component_type, ('f', 4))
        
        type_sizes = {'SCALAR': 1, 'VEC2': 2, 'VEC3': 3, 'VEC4': 4}
        num_components = type_sizes.get(accessor.type, 1)
        
        element_size = size * num_components
        
        for i, element in enumerate(new_data):
            element_offset = offset + i * element_size
            struct.pack_into(fmt * num_components, data, element_offset, *element)
        
        # Actualizar el buffer completo
        # Necesitamos actualizar el data URI del buffer
        import base64
        buffer = self.gltf.buffers[buffer_view.buffer]
        buffer.uri = f"data:application/octet-stream;base64,{base64.b64encode(bytes(data)).decode('ascii')}"
        
    def aplicar_rotacion_euler_a_quaternion(self, quaternions, euler_degrees, eje='z'):
        """
        Aplica una rotación euler adicional a quaternions existentes
        quaternions: array de quaternions [x, y, z, w]
        euler_degrees: grados a rotar
        eje: 'x', 'y', o 'z'
        """
        # Convertir euler a quaternion
        euler_rad = np.radians(euler_degrees)
        
        if eje == 'x':
            rot_euler = [euler_rad, 0, 0]
        elif eje == 'y':
            rot_euler = [0, euler_rad, 0]
        else:  # z
            rot_euler = [0, 0, euler_rad]
        
        rot_adicional = Rotation.from_euler('xyz', rot_euler)
        quat_adicional = rot_adicional.as_quat()  # [x, y, z, w]
        
        # Aplicar a cada quaternion
        result = []
        for quat in quaternions:
            # Convertir quaternion existente
            rot_existente = Rotation.from_quat(quat)
            
            # Componer rotaciones
            rot_nueva = rot_existente * rot_adicional
            
            result.append(rot_nueva.as_quat())
        
        return np.array(result)
        
    def corregir_dedo(self, nombre_hueso, rotacion_grados, eje='z'):
        """Aplica corrección de rotación a un hueso específico"""
        # Encontrar nodo
        node_idx = self.encontrar_node_index(nombre_hueso)
        if node_idx is None:
            return False
            
        # Encontrar canal de animación
        channel_idx, sampler = self.encontrar_animation_channel(node_idx, 'rotation')
        if sampler is None:
            return False
            
        # Leer quaternions actuales
        output_accessor_idx = sampler.output
        quaternions = self.leer_accessor_data(output_accessor_idx)
        
        # Aplicar rotación
        quaternions_nuevos = self.aplicar_rotacion_euler_a_quaternion(
            quaternions, 
            rotacion_grados, 
            eje
        )
        
        # Escribir de vuelta
        self.escribir_accessor_data(output_accessor_idx, quaternions_nuevos)
        
        self.modificaciones_aplicadas.append({
            'hueso': nombre_hueso,
            'tipo': 'rotacion',
            'rotacion': rotacion_grados,
            'eje': eje,
            'frames_modificados': len(quaternions)
        })
        
        return True
    
    def mover_hueso_adelante(self, nombre_hueso, distancia_metros):
        """Mueve un hueso hacia adelante (eje Z positivo)"""
        # Encontrar nodo
        node_idx = self.encontrar_node_index(nombre_hueso)
        if node_idx is None:
            return False
            
        # Encontrar canal de translación
        channel_idx, sampler = self.encontrar_animation_channel(node_idx, 'translation')
        if sampler is None:
            # Si no hay animación de translación, modificar la posición base del nodo
            node = self.gltf.nodes[node_idx]
            if node.translation:
                node.translation[2] += distancia_metros
            else:
                node.translation = [0.0, 0.0, distancia_metros]
            
            self.modificaciones_aplicadas.append({
                'hueso': nombre_hueso,
                'tipo': 'translacion_base',
                'desplazamiento_Z': distancia_metros,
                'frames_modificados': 0
            })
            return True
            
        # Leer posiciones actuales
        output_accessor_idx = sampler.output
        posiciones = self.leer_accessor_data(output_accessor_idx)
        
        # Aplicar desplazamiento en Z
        posiciones_nuevas = posiciones.copy()
        posiciones_nuevas[:, 2] += distancia_metros  # Z es el índice 2
        
        # Escribir de vuelta
        self.escribir_accessor_data(output_accessor_idx, posiciones_nuevas)
        
        self.modificaciones_aplicadas.append({
            'hueso': nombre_hueso,
            'tipo': 'translacion',
            'desplazamiento_Z': distancia_metros,
            'frames_modificados': len(posiciones)
        })
        
        return True
        
    def guardar(self):
        """Guarda el GLB modificado"""
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.gltf.save(str(self.output_path))
        
        # Verificar tamaño
        size_mb = self.output_path.stat().st_size / (1024 * 1024)
        return size_mb


def aplicar_correcciones_yo():
    """Aplica correcciones específicas para la seña YO"""
    BASE_DIR = Path(__file__).parent.parent
    GLB_ORIGINAL = BASE_DIR / "test" / "output" / "glb" / "Nancy" / "pronombres" / "Nancy_resultado_yo.glb"
    GLB_OUTPUT = BASE_DIR / "test" / "output" / "glb" / "Nancy" / "pronombres" / "Nancy_resultado_yo_AUTOCORREGIDO.glb"
    
    if not GLB_ORIGINAL.exists():
        print(f"ERROR: {GLB_ORIGINAL} no existe")
        return False
    
    # Crear corrector
    corrector = GLBRealCorrector(GLB_ORIGINAL, GLB_OUTPUT)
    
    # Cargar
    print("Cargando GLB...")
    corrector.cargar()
    
    # Aplicar correcciones de dedos
    print("Aplicando correcciones de dedos...")
    
    correcciones_dedos = {
        'RightHandIndex1': -15,   # Índice más extendido
        'RightHandMiddle1': 10,   # Medio más cerrado
        'RightHandRing1': 10,     # Anular más cerrado
        'RightHandPinky1': 10,    # Meñique más cerrado
        'RightHandThumb1': 5      # Pulgar ajuste ligero
    }
    
    exitosas_dedos = 0
    for hueso, grados in correcciones_dedos.items():
        if corrector.corregir_dedo(hueso, grados, 'z'):
            exitosas_dedos += 1
    
    # Aplicar correcciones de brazo (mover hacia adelante)
    print("Aplicando correcciones de visibilidad (codo adelante)...")
    
    correcciones_brazo = {
        'RightForeArm': 0.08,     # Antebrazo 8cm adelante
        'RightHand': 0.05         # Mano 5cm adelante adicional
    }
    
    exitosas_brazo = 0
    for hueso, distancia in correcciones_brazo.items():
        if corrector.mover_hueso_adelante(hueso, distancia):
            exitosas_brazo += 1
    
    total_exitosas = exitosas_dedos + exitosas_brazo
    
    if total_exitosas == 0:
        print("ERROR: No se aplicó ninguna corrección")
        return False
    
    # Guardar
    print("Guardando GLB modificado...")
    size_mb = corrector.guardar()
    
    print(f"\nÉXITO:")
    print(f"  - Correcciones de dedos: {exitosas_dedos}/5")
    print(f"  - Correcciones de brazo: {exitosas_brazo}/2")
    print(f"  - Total: {total_exitosas}/7")
    print(f"  - Archivo: {GLB_OUTPUT.name}")
    print(f"  - Tamaño: {size_mb:.2f} MB")
    
    # Guardar reporte
    reporte_path = BASE_DIR / "test" / "output" / "comparisons" / "yo_correcciones_reales.json"
    reporte_path.parent.mkdir(parents=True, exist_ok=True)
    with open(reporte_path, 'w') as f:
        json.dump({
            'archivo_original': str(GLB_ORIGINAL),
            'archivo_corregido': str(GLB_OUTPUT),
            'modificaciones': corrector.modificaciones_aplicadas,
            'correcciones_dedos': exitosas_dedos,
            'correcciones_brazo': exitosas_brazo,
            'total_exitosas': total_exitosas
        }, f, indent=2)
    
    return True


if __name__ == "__main__":
    try:
        aplicar_correcciones_yo()
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
