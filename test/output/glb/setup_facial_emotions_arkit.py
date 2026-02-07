"""
Script de Blender para Animación Facial con ARKit Blendshapes
Compatible con Blender 4.5+

INSTRUCCIONES:
1. Importar modelo GLB desde DeepMotion en Blender
2. Abrir pestaña "Scripting"
3. Cargar este script
4. Ejecutar (Alt+P o "Run Script")
5. Los controles maestros aparecerán en el Armature
6. Ajustar los sliders para controlar las emociones

CONTROLES MAESTROS:
- EMOTION_SORPRESA (0-1): Pregunta/Asombro
- EMOTION_IRA (0-1): Enojo/Tensión
- EMOTION_ALEGRIA (0-1): Sonrisa/Risa
- EMOTION_ASCO (0-1): Desaprobación
- EMOTION_TRISTEZA (0-1): Pena/Preocupación
- BLINK_CONTROL (0-1): Parpadeo

Autor: Sistema LSV
Fecha: Noviembre 2025
Versión: 1.0
"""

import bpy
from typing import Optional, List, Dict


class FacialEmotionSetup:
    """Configura controles de emociones faciales para personajes con ARKit Blendshapes"""
    
    # Definición de controles maestros y sus blendshapes asociados
    EMOTION_MAPPINGS = {
        'EMOTION_SORPRESA': {
            'description': 'Pregunta/Asombro',
            'blendshapes': [
                'browInnerUp',
                'browOuterUp_L',
                'browOuterUp_R',
                'eyeWide_L',
                'eyeWide_R'
            ]
        },
        'EMOTION_IRA': {
            'description': 'Enojo/Tensión',
            'blendshapes': [
                'browDown_L',
                'browDown_R',
                'mouthFrown_L',
                'mouthFrown_R'
            ]
        },
        'EMOTION_ALEGRIA': {
            'description': 'Sonrisa/Risa',
            'blendshapes': [
                'mouthSmile_L',
                'mouthSmile_R',
                'cheekPuff'
            ]
        },
        'EMOTION_ASCO': {
            'description': 'Desaprobación',
            'blendshapes': [
                'noseSneer_L',
                'noseSneer_R',
                'mouthUpperUp_L',
                'mouthUpperUp_R'
            ]
        },
        'EMOTION_TRISTEZA': {
            'description': 'Pena/Preocupación',
            'blendshapes': [
                'mouthDimple_L',
                'mouthDimple_R',
                'mouthLowerDown_L',
                'mouthLowerDown_R'
            ]
        },
        'BLINK_CONTROL': {
            'description': 'Parpadeo',
            'blendshapes': [
                'eyeBlink_L',
                'eyeBlink_R'
            ]
        }
    }
    
    def __init__(self):
        self.armature = None
        self.face_mesh = None
        self.drivers_created = 0
        self.errors = []
    
    def log(self, message: str, level: str = 'INFO'):
        """Registra mensajes con formato"""
        prefix = {
            'INFO': '✅',
            'WARNING': '⚠️',
            'ERROR': '❌',
            'SUCCESS': '🎉'
        }.get(level, 'ℹ️')
        
        print(f"{prefix} {message}")
    
    def find_armature(self) -> Optional[bpy.types.Object]:
        """Encuentra el armature principal en la escena"""
        self.log("Buscando Armature en la escena...")
        
        armatures = [obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE']
        
        if not armatures:
            self.log("No se encontró ningún Armature en la escena", 'ERROR')
            return None
        
        # Si hay múltiples, tomar el primero
        armature = armatures[0]
        self.log(f"Armature encontrado: '{armature.name}'", 'SUCCESS')
        return armature
    
    def find_face_mesh(self) -> Optional[bpy.types.Object]:
        """Encuentra la malla facial (busca nombres con 'Face' o 'Head')"""
        self.log("Buscando malla facial...")
        
        # Buscar meshes con nombres que contengan Face o Head
        candidates = []
        for obj in bpy.context.scene.objects:
            if obj.type == 'MESH':
                name_lower = obj.name.lower()
                if 'face' in name_lower or 'head' in name_lower:
                    candidates.append(obj)
        
        if not candidates:
            # Si no hay candidatos, buscar cualquier mesh con shape keys
            self.log("No se encontró mesh con 'Face' o 'Head', buscando cualquier mesh con Shape Keys...")
            candidates = [obj for obj in bpy.context.scene.objects 
                         if obj.type == 'MESH' and obj.data.shape_keys]
        
        if not candidates:
            self.log("No se encontró ninguna malla facial", 'ERROR')
            return None
        
        # Tomar el primero
        face_mesh = candidates[0]
        
        # Verificar que tenga shape keys
        if not face_mesh.data.shape_keys:
            self.log(f"La malla '{face_mesh.name}' no tiene Shape Keys", 'ERROR')
            return None
        
        self.log(f"Malla facial encontrada: '{face_mesh.name}'", 'SUCCESS')
        
        # Listar shape keys disponibles
        shape_keys = face_mesh.data.shape_keys.key_blocks
        self.log(f"Shape Keys encontrados: {len(shape_keys)}")
        
        return face_mesh
    
    def create_custom_properties(self):
        """Crea las propiedades personalizadas en el Armature"""
        self.log("\n📝 Creando propiedades personalizadas...")
        
        if not self.armature:
            self.log("No hay Armature para crear propiedades", 'ERROR')
            return False
        
        for prop_name, config in self.EMOTION_MAPPINGS.items():
            # Crear propiedad con rango 0.0 a 1.0
            self.armature[prop_name] = 0.0
            
            # Configurar límites y UI
            id_props = self.armature.id_properties_ui(prop_name)
            id_props.update(
                min=0.0,
                max=1.0,
                soft_min=0.0,
                soft_max=1.0,
                default=0.0,
                description=config['description']
            )
            
            self.log(f"  ✓ Creada: {prop_name} ({config['description']})")
        
        self.log(f"Propiedades personalizadas creadas: {len(self.EMOTION_MAPPINGS)}", 'SUCCESS')
        return True
    
    def get_shape_key_index(self, shape_key_name: str) -> Optional[int]:
        """Obtiene el índice de un shape key por nombre"""
        if not self.face_mesh or not self.face_mesh.data.shape_keys:
            return None
        
        key_blocks = self.face_mesh.data.shape_keys.key_blocks
        for i, key_block in enumerate(key_blocks):
            if key_block.name == shape_key_name:
                return i
        
        return None
    
    def create_driver(self, shape_key_name: str, property_name: str) -> bool:
        """
        Crea un driver que conecta una propiedad del Armature a un Shape Key
        
        Args:
            shape_key_name: Nombre del Shape Key a controlar
            property_name: Nombre de la propiedad personalizada del Armature
        
        Returns:
            True si el driver se creó exitosamente
        """
        # Verificar que el shape key existe
        if not self.face_mesh or not self.face_mesh.data.shape_keys:
            return False
        
        key_blocks = self.face_mesh.data.shape_keys.key_blocks
        
        # Buscar el shape key
        shape_key = None
        for kb in key_blocks:
            if kb.name == shape_key_name:
                shape_key = kb
                break
        
        if not shape_key:
            self.log(f"Shape Key '{shape_key_name}' no encontrado", 'WARNING')
            self.errors.append(f"Shape Key faltante: {shape_key_name}")
            return False
        
        # Limpiar drivers existentes
        shape_key.driver_remove('value')
        
        # Crear nuevo driver
        driver = shape_key.driver_add('value').driver
        driver.type = 'AVERAGE'
        
        # Agregar variable que apunta a la propiedad del Armature
        var = driver.variables.new()
        var.name = 'emotion_value'
        var.type = 'SINGLE_PROP'
        
        # Configurar target
        target = var.targets[0]
        target.id_type = 'OBJECT'
        target.id = self.armature
        target.data_path = f'["{property_name}"]'
        
        # Configurar expresión simple (1:1 mapping)
        driver.expression = 'emotion_value'
        
        self.drivers_created += 1
        return True
    
    def setup_all_drivers(self):
        """Configura todos los drivers para las emociones"""
        self.log("\n🔗 Configurando drivers...")
        
        if not self.armature or not self.face_mesh:
            self.log("Faltan componentes para crear drivers", 'ERROR')
            return False
        
        for prop_name, config in self.EMOTION_MAPPINGS.items():
            self.log(f"\n  Control: {prop_name}")
            
            successful = 0
            failed = 0
            
            for shape_key_name in config['blendshapes']:
                if self.create_driver(shape_key_name, prop_name):
                    self.log(f"    ✓ {shape_key_name}")
                    successful += 1
                else:
                    self.log(f"    ✗ {shape_key_name} (no encontrado)", 'WARNING')
                    failed += 1
            
            if successful > 0:
                self.log(f"  Conectados: {successful}/{len(config['blendshapes'])}")
        
        return True
    
    def run(self):
        """Ejecuta el setup completo"""
        self.log("\n" + "="*60)
        self.log("🎭 SETUP DE EMOCIONES FACIALES - ARKit Blendshapes")
        self.log("="*60)
        
        # 1. Encontrar Armature
        self.armature = self.find_armature()
        if not self.armature:
            return False
        
        # 2. Encontrar malla facial
        self.face_mesh = self.find_face_mesh()
        if not self.face_mesh:
            return False
        
        # 3. Crear propiedades personalizadas
        if not self.create_custom_properties():
            return False
        
        # 4. Configurar drivers
        if not self.setup_all_drivers():
            return False
        
        # Resumen final
        self.log("\n" + "="*60)
        self.log("RESUMEN DEL SETUP", 'SUCCESS')
        self.log("="*60)
        self.log(f"Armature: {self.armature.name}")
        self.log(f"Malla Facial: {self.face_mesh.name}")
        self.log(f"Propiedades creadas: {len(self.EMOTION_MAPPINGS)}")
        self.log(f"Drivers creados: {self.drivers_created}")
        
        if self.errors:
            self.log(f"\n⚠️  Advertencias: {len(self.errors)}")
            for error in self.errors[:5]:  # Mostrar solo las primeras 5
                self.log(f"  - {error}", 'WARNING')
        
        self.log("\n✅ SETUP COMPLETADO")
        self.log("\n💡 CÓMO USAR:")
        self.log("1. Seleccionar el Armature en el Outliner")
        self.log("2. Ver panel 'Object Properties' (ícono de cubo naranja)")
        self.log("3. Scroll down a 'Custom Properties'")
        self.log("4. Ajustar los sliders de emociones (0.0 a 1.0)")
        self.log("5. Ver cambios en tiempo real en la cara del personaje")
        self.log("\n🎬 Puedes animar estos sliders con keyframes!")
        self.log("="*60 + "\n")
        
        return True


def main():
    """Función principal para ejecutar el script"""
    setup = FacialEmotionSetup()
    setup.run()


if __name__ == "__main__":
    # Ejecutar setup
    main()
