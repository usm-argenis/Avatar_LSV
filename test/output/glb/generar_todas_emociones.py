"""
GENERADOR DE TODAS LAS EMOCIONES
Crea 6 archivos GLB con diferentes expresiones
"""

import bpy
import os


RUTA_GLB_ORIGINAL = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Mujer\Nancy.glb"
DIRECTORIO_SALIDA = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb"


class FacialEmotionSetup:
    """Configura controles de emociones faciales"""
    
    EMOTION_MAPPINGS = {
        'EMOTION_SORPRESA': {
            'blendshapes': ['BrowInnerUp', 'BrowOuterUpLeft', 'BrowOuterUpRight', 
                           'EyeWideLeft', 'EyeWideRight']
        },
        'EMOTION_IRA': {
            'blendshapes': ['BrowDownLeft', 'BrowDownRight', 'MouthFrownLeft', 'MouthFrownRight']
        },
        'EMOTION_ALEGRIA': {
            'blendshapes': ['MouthSmileLeft', 'MouthSmileRight', 'CheekPuff']
        },
        'EMOTION_ASCO': {
            'blendshapes': ['NoseSneerLeft', 'NoseSneerRight', 'MouthUpperUpLeft', 'MouthUpperUpRight']
        },
        'EMOTION_TRISTEZA': {
            'blendshapes': ['MouthDimpleLeft', 'MouthDimpleRight', 'MouthLowerDownLeft', 'MouthLowerDownRight']
        },
        'BLINK_CONTROL': {
            'blendshapes': ['EyeBlinkLeft', 'EyeBlinkRight']
        }
    }
    
    def __init__(self):
        self.armature = None
        self.face_mesh = None
        self.drivers_created = 0
    
    def log(self, msg, symbol='✅'):
        print(f"{symbol} {msg}")
    
    def find_armature(self):
        armatures = [obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE']
        if armatures:
            self.armature = armatures[0]
            return True
        return False
    
    def find_face_mesh(self):
        for obj in bpy.data.objects:
            if obj.type == 'MESH' and obj.data.shape_keys:
                self.face_mesh = obj
                return True
        return False
    
    def create_custom_properties(self):
        if not self.armature:
            return False
        for prop_name in self.EMOTION_MAPPINGS.keys():
            self.armature[prop_name] = 0.0
            id_props = self.armature.id_properties_ui(prop_name)
            id_props.update(min=0.0, max=1.0, soft_min=0.0, soft_max=1.0, default=0.0)
        return True
    
    def create_driver(self, shape_key_name, property_name):
        if not self.face_mesh or not self.face_mesh.data.shape_keys:
            return False
        
        key_blocks = self.face_mesh.data.shape_keys.key_blocks
        shape_key = None
        for kb in key_blocks:
            if kb.name == shape_key_name:
                shape_key = kb
                break
        
        if not shape_key:
            return False
        
        try:
            shape_key.driver_remove('value')
        except:
            pass
        
        driver = shape_key.driver_add('value').driver
        driver.type = 'AVERAGE'
        
        var = driver.variables.new()
        var.name = 'emotion_value'
        var.type = 'SINGLE_PROP'
        
        target = var.targets[0]
        target.id_type = 'OBJECT'
        target.id = self.armature
        target.data_path = f'["{property_name}"]'
        driver.expression = 'emotion_value'
        
        self.drivers_created += 1
        return True
    
    def setup_all_drivers(self):
        for prop_name, config in self.EMOTION_MAPPINGS.items():
            for shape_key_name in config['blendshapes']:
                self.create_driver(shape_key_name, prop_name)
        return True
    
    def run(self):
        if not self.find_armature():
            return False
        if not self.find_face_mesh():
            return False
        if not self.create_custom_properties():
            return False
        if not self.setup_all_drivers():
            return False
        return True


def limpiar_escena():
    """Limpia la escena completamente"""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    for mesh in bpy.data.meshes:
        if mesh.users == 0:
            bpy.data.meshes.remove(mesh)
    for armature in bpy.data.armatures:
        if armature.users == 0:
            bpy.data.armatures.remove(armature)


def generar_emocion(nombre_emocion, propiedad, intensidad, emoji):
    """Genera un GLB con una emoción específica"""
    
    print(f"\n{'='*70}")
    print(f"{emoji} GENERANDO: {nombre_emocion}")
    print(f"{'='*70}")
    
    # Limpiar
    limpiar_escena()
    
    # Importar
    print("📥 Importando GLB...")
    bpy.ops.import_scene.gltf(filepath=RUTA_GLB_ORIGINAL)
    
    # Setup
    print("⚙️  Configurando emociones...")
    setup = FacialEmotionSetup()
    if not setup.run():
        print("❌ Error en setup")
        return False
    
    # Aplicar emoción
    print(f"🎭 Aplicando {nombre_emocion} ({intensidad})...")
    armature = setup.armature
    
    # Resetear
    for emotion in setup.EMOTION_MAPPINGS.keys():
        armature[emotion] = 0.0
    
    # Aplicar
    armature[propiedad] = intensidad
    
    # Actualizar
    bpy.context.view_layer.update()
    bpy.context.evaluated_depsgraph_get().update()
    
    # Exportar
    ruta_salida = os.path.join(DIRECTORIO_SALIDA, f"Nancy_{nombre_emocion}.glb")
    print(f"💾 Exportando...")
    
    bpy.ops.export_scene.gltf(
        filepath=ruta_salida,
        export_format='GLB',
        export_animations=True,
        export_morph=True,
        export_current_frame=True
    )
    
    print(f"✅ {nombre_emocion} generado: {os.path.basename(ruta_salida)}")
    return True


def generar_todas():
    """Genera todas las emociones"""
    
    print("\n" + "="*70)
    print("🎭 GENERADOR DE TODAS LAS EMOCIONES")
    print("="*70)
    
    # Verificar archivo
    if not os.path.exists(RUTA_GLB_ORIGINAL):
        print(f"❌ No se encuentra: Nancy.glb en carpeta Mujer/")
        return
    
    emociones = [
        ('NEUTRAL', 'EMOTION_ALEGRIA', 0.0, '😐'),
        ('ALEGRIA', 'EMOTION_ALEGRIA', 0.9, '😄'),
        ('SORPRESA', 'EMOTION_SORPRESA', 1.0, '😮'),
        ('IRA', 'EMOTION_IRA', 0.8, '😠'),
        ('ASCO', 'EMOTION_ASCO', 0.8, '🤢'),
        ('TRISTEZA', 'EMOTION_TRISTEZA', 0.8, '😢'),
    ]
    
    exitosos = 0
    
    for nombre, propiedad, intensidad, emoji in emociones:
        try:
            if generar_emocion(nombre, propiedad, intensidad, emoji):
                exitosos += 1
        except Exception as e:
            print(f"❌ Error en {nombre}: {e}")
    
    # Resumen
    print("\n" + "="*70)
    print("📊 RESUMEN FINAL")
    print("="*70)
    print(f"\n✅ Generados exitosamente: {exitosos}/{len(emociones)}")
    print(f"\n📁 Archivos creados:")
    
    for nombre, _, _, emoji in emociones[:exitosos]:
        print(f"   {emoji} Nancy_{nombre}.glb")
    
    print(f"\n📍 Ubicación: {DIRECTORIO_SALIDA}")
    print("\n🎉 ¡Proceso completado!")
    print("="*70 + "\n")


if __name__ == "__main__":
    generar_todas()
