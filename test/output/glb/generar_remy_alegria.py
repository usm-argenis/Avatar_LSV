"""
GENERADOR AUTOMÁTICO - REMY CON ALEGRÍA
Script completo que:
1. Limpia la escena
2. Carga Remy_resultado_b.glb
3. Configura controles de emociones
4. Aplica ALEGRÍA
5. Exporta como Remy_ALEGRIA.glb

NO REQUIERE PASOS MANUALES - Solo ejecutar
"""

import bpy
import os
from pathlib import Path


# ============================================================================
# CONFIGURACIÓN
# ============================================================================

RUTA_GLB_ORIGINAL = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Mujer\Nancy.glb"
RUTA_SALIDA = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy_ALEGRIA.glb"
INTENSIDAD_ALEGRIA = 0.9  # 0.0 a 1.0


# ============================================================================
# CLASE PARA SETUP DE EMOCIONES
# ============================================================================

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
    
    def log(self, msg, symbol='OK'):
        """Log con marcas simples"""
        prefix = {'OK': '  [OK]', 'ERROR': '  [ERROR]', 'WARN': '  [WARN]'}
        print(f"{prefix.get(symbol, '  [INFO]')} {msg}")
    
    def find_armature(self):
        """Encuentra el armature"""
        try:
            armatures = [obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE']
            if armatures:
                self.armature = armatures[0]
                self.log(f"Armature encontrado: {self.armature.name}")
                return True
            self.log("No se encontro Armature", 'ERROR')
            return False
        except Exception as e:
            self.log(f"Error buscando Armature: {e}", 'ERROR')
            return False
    
    def find_face_mesh(self):
        """Encuentra el mesh con shape keys"""
        try:
            for obj in bpy.data.objects:
                if obj.type == 'MESH' and obj.data.shape_keys:
                    self.face_mesh = obj
                    num_shapes = len(obj.data.shape_keys.key_blocks)
                    self.log(f"Mesh encontrado: {obj.name} ({num_shapes} shape keys)")
                    return True
            self.log("No se encontro mesh con shape keys", 'ERROR')
            return False
        except Exception as e:
            self.log(f"Error buscando mesh: {e}", 'ERROR')
            return False
    
    def create_custom_properties(self):
        """Crea las propiedades personalizadas en el Armature"""
        if not self.armature:
            return False
        
        for prop_name in self.EMOTION_MAPPINGS.keys():
            self.armature[prop_name] = 0.0
            
            # Configurar UI
            id_props = self.armature.id_properties_ui(prop_name)
            id_props.update(
                min=0.0,
                max=1.0,
                soft_min=0.0,
                soft_max=1.0,
                default=0.0
            )
        
        self.log(f"Propiedades creadas: {len(self.EMOTION_MAPPINGS)}")
        return True
    
    def create_driver(self, shape_key_name, property_name):
        """Crea un driver conectando propiedad a shape key"""
        try:
            if not self.face_mesh or not self.face_mesh.data.shape_keys:
                return False
            
            key_blocks = self.face_mesh.data.shape_keys.key_blocks
            
            # Buscar shape key
            shape_key = None
            for kb in key_blocks:
                if kb.name == shape_key_name:
                    shape_key = kb
                    break
            
            if not shape_key:
                # No mostrar warning, es normal que falten algunos
                return False
            
            # Limpiar drivers existentes
            try:
                shape_key.driver_remove('value')
            except:
                pass
            
            # Crear driver
            driver = shape_key.driver_add('value').driver
            driver.type = 'AVERAGE'
            
            # Variable que apunta a la propiedad
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
            
        except Exception as e:
            # Solo reportar errores críticos
            return False
    
    def setup_all_drivers(self):
        """Configura todos los drivers"""
        self.log("\nConfigurando drivers...")
        
        for prop_name, config in self.EMOTION_MAPPINGS.items():
            successful = 0
            for shape_key_name in config['blendshapes']:
                if self.create_driver(shape_key_name, prop_name):
                    successful += 1
            
            self.log(f"  {prop_name}: {successful}/{len(config['blendshapes'])} conectados")
        
        return True
    
    def run(self):
        """Ejecuta el setup completo"""
        self.log("\n" + "="*60)
        self.log("CONFIGURANDO EMOCIONES FACIALES")
        self.log("="*60)
        
        if not self.find_armature():
            return False
        
        if not self.find_face_mesh():
            return False
        
        if not self.create_custom_properties():
            return False
        
        if not self.setup_all_drivers():
            return False
        
        self.log(f"\n✅ Setup completado - {self.drivers_created} drivers creados")
        return True


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def generar_remy_alegria():
    """Genera Remy con expresión de alegría"""
    
    print("\n" + "="*70)
    print("GENERADOR AUTOMATICO - REMY CON ALEGRIA")
    print("="*70)
    
    # PASO 1: Limpiar escena
    print("\nPASO 1: Limpiando escena...")
    try:
        # Deseleccionar todo primero
        bpy.ops.object.select_all(action='DESELECT')
        
        # Seleccionar y eliminar todo
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        
        # Limpiar data blocks huérfanos
        for mesh in bpy.data.meshes:
            if mesh.users == 0:
                bpy.data.meshes.remove(mesh)
        
        for armature in bpy.data.armatures:
            if armature.users == 0:
                bpy.data.armatures.remove(armature)
        
        print("   OK - Escena limpiada")
    except Exception as e:
        print(f"   ADVERTENCIA al limpiar: {e}")
    
    # PASO 2: Verificar archivo existe
    print("\nPASO 2: Verificando archivo GLB...")
    if not os.path.exists(RUTA_GLB_ORIGINAL):
        print(f"   ERROR: No se encuentra el archivo:")
        print(f"      {RUTA_GLB_ORIGINAL}")
        return False
    
    print(f"   OK - Archivo encontrado: Remy_resultado_b.glb")
    
    # PASO 3: Importar GLB
    print("\nPASO 3: Importando GLB...")
    try:
        result = bpy.ops.import_scene.gltf(filepath=RUTA_GLB_ORIGINAL)
        print(f"   Resultado importacion: {result}")
        print("   OK - GLB importado correctamente")
    except Exception as e:
        print(f"   ERROR al importar: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # PASO 4: Configurar emociones
    print("\nPASO 4: Configurando sistema de emociones...")
    try:
        setup = FacialEmotionSetup()
        if not setup.run():
            print("   ERROR en configuracion")
            return False
    except Exception as e:
        print(f"   ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # PASO 5: Aplicar ALEGRÍA
    print("\nPASO 5: Aplicando emocion ALEGRIA...")
    
    try:
        armature = setup.armature
        
        # Resetear todas las emociones
        for emotion in setup.EMOTION_MAPPINGS.keys():
            armature[emotion] = 0.0
        
        # Aplicar alegría
        armature['EMOTION_ALEGRIA'] = INTENSIDAD_ALEGRIA
        
        print(f"   OK - EMOTION_ALEGRIA = {INTENSIDAD_ALEGRIA}")
        
        # Forzar actualización
        bpy.context.view_layer.update()
        bpy.context.evaluated_depsgraph_get().update()
        
        # Verificar que cambió
        mesh = setup.face_mesh
        if mesh and mesh.data.shape_keys:
            shape_keys = mesh.data.shape_keys.key_blocks
            print("\n   Verificando cambios en shape keys:")
            
            for bs_name in ['MouthSmileLeft', 'MouthSmileRight', 'CheekPuff']:
                if bs_name in shape_keys:
                    valor = shape_keys[bs_name].value
                    if valor > 0.01:
                        print(f"      OK - {bs_name}: {valor:.3f}")
                    else:
                        print(f"      ADVERTENCIA - {bs_name}: {valor:.3f} (no cambio)")
        else:
            print("   ADVERTENCIA: No se pudo verificar shape keys")
    
    except Exception as e:
        print(f"   ERROR al aplicar emocion: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # PASO 6: Exportar
    print(f"\nPASO 6: Exportando a {os.path.basename(RUTA_SALIDA)}...")
    
    try:
        result = bpy.ops.export_scene.gltf(
            filepath=RUTA_SALIDA,
            export_format='GLB',
            export_animations=True,
            export_morph=True,
            export_current_frame=True
        )
        print(f"   Resultado exportacion: {result}")
        
        # Verificar que el archivo se creó
        if os.path.exists(RUTA_SALIDA):
            tamano = os.path.getsize(RUTA_SALIDA)
            print(f"   OK - Exportado exitosamente:")
            print(f"      Archivo: {RUTA_SALIDA}")
            print(f"      Tamano: {tamano / 1024 / 1024:.2f} MB")
        else:
            print(f"   ERROR: El archivo no se creo")
            return False
            
    except Exception as e:
        print(f"   ERROR al exportar: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # RESUMEN FINAL
    print("\n" + "="*70)
    print("PROCESO COMPLETADO CON EXITO")
    print("="*70)
    print(f"\nRESUMEN:")
    print(f"   Archivo original:  Remy_resultado_b.glb")
    print(f"   Archivo generado:  Remy_ALEGRIA.glb")
    print(f"   Emocion aplicada:  ALEGRIA (intensidad: {INTENSIDAD_ALEGRIA})")
    print(f"   Drivers creados:   {setup.drivers_created}")
    print(f"   Ubicacion:         {os.path.dirname(RUTA_SALIDA)}")
    print("\nListo! Ahora tienes a Remy con expresion de alegria")
    print("="*70 + "\n")
    
    return True


# ============================================================================
# EJECUTAR
# ============================================================================

if __name__ == "__main__":
    try:
        print("\n\n" + "#"*70)
        print("# INICIANDO GENERADOR DE REMY CON ALEGRIA")
        print("#"*70 + "\n")
        
        resultado = generar_remy_alegria()
        
        if not resultado:
            print("\n" + "="*70)
            print("ERROR: EL PROCESO FALLO")
            print("="*70)
            print("\nRevisa los errores arriba para ver que salio mal.")
            print("="*70 + "\n")
        else:
            print("\n" + "#"*70)
            print("# GENERACION EXITOSA!")
            print("#"*70 + "\n")
            
    except Exception as e:
        print("\n" + "="*70)
        print("ERROR CRITICO EN LA EJECUCION")
        print("="*70)
        print(f"\nError: {e}")
        print("\nStack trace completo:")
        import traceback
        traceback.print_exc()
        print("="*70 + "\n")
