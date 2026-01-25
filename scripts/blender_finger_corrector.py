"""
Sistema de Corrección Automática de Dedos en Blender
Aplica correcciones basadas en análisis MediaPipe al avatar Nancy.glb

Uso en Blender:
1. Abrir Blender
2. Cargar Nancy.glb y la animación a corregir
3. Ejecutar este script en Scripting tab
4. Las correcciones se aplicarán automáticamente

Autor: Sistema LSV
Fecha: 2025
"""

import bpy
import json
import math
from pathlib import Path
from mathutils import Euler, Quaternion, Vector


class BlenderFingerCorrector:
    """Aplica correcciones de dedos en Blender usando datos de MediaPipe"""
    
    # Mapeo de nombres de huesos Nancy -> Estructura estándar
    BONE_MAPPING = {
        # Pulgar derecho
        'thumb_01_r': 'thumb_mcp',
        'thumb_02_r': 'thumb_pip',
        'thumb_03_r': 'thumb_dip',
        
        # Índice derecho
        'f_index.01_r': 'index_mcp',
        'f_index.02_r': 'index_pip',
        'f_index.03_r': 'index_dip',
        
        # Medio derecho
        'f_middle.01_r': 'middle_mcp',
        'f_middle.02_r': 'middle_pip',
        'f_middle.03_r': 'middle_dip',
        
        # Anular derecho
        'f_ring.01_r': 'ring_mcp',
        'f_ring.02_r': 'ring_pip',
        'f_ring.03_r': 'ring_dip',
        
        # Meñique derecho
        'f_pinky.01_r': 'pinky_mcp',
        'f_pinky.02_r': 'pinky_pip',
        'f_pinky.03_r': 'pinky_dip',
    }
    
    def __init__(self, armature_name: str = "Armature"):
        """Inicializa el corrector"""
        self.armature = bpy.data.objects.get(armature_name)
        if not self.armature:
            raise ValueError(f"Armature '{armature_name}' no encontrado")
        
        self.pose_bones = self.armature.pose.bones
        print(f"✅ Armature cargado: {armature_name}")
        print(f"   Total huesos: {len(self.pose_bones)}")
    
    def load_corrections(self, json_path: str) -> dict:
        """Carga el archivo JSON con correcciones"""
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"📄 Correcciones cargadas: {json_path}")
        print(f"   Frames a corregir: {len(data.get('frames', []))}")
        return data
    
    def apply_angle_to_bone(self, bone_name: str, angle_degrees: float, axis: str = 'Z'):
        """Aplica un ángulo a un hueso específico"""
        bone = self.pose_bones.get(bone_name)
        if not bone:
            print(f"⚠️ Hueso no encontrado: {bone_name}")
            return
        
        # Convertir ángulo a radianes
        angle_rad = math.radians(angle_degrees)
        
        # Crear rotación según el eje
        if axis == 'X':
            rotation = Euler((angle_rad, 0, 0), 'XYZ')
        elif axis == 'Y':
            rotation = Euler((0, angle_rad, 0), 'XYZ')
        else:  # Z
            rotation = Euler((0, 0, angle_rad), 'XYZ')
        
        # Aplicar rotación
        bone.rotation_euler = rotation
        bpy.context.view_layer.update()
    
    def apply_corrections_to_frame(self, frame_data: dict, frame_number: int):
        """Aplica correcciones a un frame específico"""
        bpy.context.scene.frame_set(frame_number)
        
        differences = frame_data.get('differences', {})
        
        # Aplicar corrección a cada articulación
        for joint_name, difference in differences.items():
            # Buscar el hueso correspondiente
            for blender_bone, standard_name in self.BONE_MAPPING.items():
                if standard_name == joint_name:
                    # Obtener ángulo actual
                    bone = self.pose_bones.get(blender_bone)
                    if bone:
                        # Aplicar corrección
                        current_angle = math.degrees(bone.rotation_euler.z)
                        corrected_angle = current_angle + difference
                        
                        self.apply_angle_to_bone(blender_bone, corrected_angle, 'Z')
                        
                        # Insertar keyframe
                        bone.keyframe_insert(data_path="rotation_euler", frame=frame_number)
                    break
        
        print(f"✅ Frame {frame_number} corregido")
    
    def apply_all_corrections(self, corrections_data: dict, smooth: bool = True):
        """Aplica todas las correcciones del JSON"""
        frames = corrections_data.get('frames', [])
        
        print(f"\n🔧 Aplicando correcciones a {len(frames)} frames...")
        
        for frame_data in frames:
            frame_number = frame_data['frame']
            self.apply_corrections_to_frame(frame_data, frame_number)
        
        if smooth:
            self.smooth_corrections()
        
        print("\n✅ Todas las correcciones aplicadas!")
    
    def smooth_corrections(self):
        """Suaviza las correcciones con interpolación"""
        print("🔄 Suavizando correcciones...")
        
        # Seleccionar todos los huesos de dedos
        for bone_name in self.BONE_MAPPING.keys():
            bone = self.pose_bones.get(bone_name)
            if bone:
                bone.bone.select = True
        
        # Aplicar suavizado de curvas F
        bpy.ops.graph.smooth()
        
        print("✅ Suavizado completado")
    
    def export_corrected_animation(self, output_path: str):
        """Exporta la animación corregida como GLB"""
        bpy.ops.export_scene.gltf(
            filepath=output_path,
            export_format='GLB',
            export_animations=True,
            export_frame_range=True
        )
        print(f"💾 Animación exportada: {output_path}")
    
    def list_available_bones(self):
        """Lista todos los huesos disponibles en el armature"""
        print("\n📋 HUESOS DISPONIBLES:")
        print("="*60)
        
        finger_bones = []
        for bone in self.pose_bones:
            name = bone.name.lower()
            # Filtrar solo huesos de dedos
            if any(keyword in name for keyword in ['thumb', 'index', 'middle', 'ring', 'pinky', 'pulgar', 'indice', 'medio', 'anular']):
                finger_bones.append(bone.name)
        
        for bone_name in sorted(finger_bones):
            print(f"   - {bone_name}")
        
        print("="*60)
        return finger_bones


def main():
    """Función principal para ejecutar en Blender"""
    print("\n" + "="*60)
    print("🎨 CORRECTOR DE DEDOS PARA BLENDER")
    print("="*60)
    
    # Ruta al archivo de correcciones
    corrections_path = r"c:\Users\andre\OneDrive\Documentos\tesis\test\output\comparisons\gracias_comparison_report.json"
    
    # Ruta de salida para la animación corregida
    output_path = r"c:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy\cortesia\Nancy_resultado_gracias_CORREGIDO.glb"
    
    try:
        # Crear corrector
        corrector = BlenderFingerCorrector("Armature")
        
        # Listar huesos disponibles (útil para debugging)
        corrector.list_available_bones()
        
        # Cargar correcciones
        corrections = corrector.load_corrections(corrections_path)
        
        # Aplicar correcciones
        corrector.apply_all_corrections(corrections, smooth=True)
        
        # Exportar animación corregida
        corrector.export_corrected_animation(output_path)
        
        print("\n✅ ¡PROCESO COMPLETADO!")
        print(f"📁 Animación corregida guardada en:")
        print(f"   {output_path}")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()


# Si se ejecuta directamente en Blender
if __name__ == "__main__":
    main()


# ==============================================================================
# GUÍA DE USO RÁPIDO
# ==============================================================================
"""
PASO 1: Analizar video y generar comparación
---------------------------------------------
cd c:\\Users\\andre\\OneDrive\\Documentos\\tesis
python scripts/video_to_glb_comparator.py

Esto genera:
- gracias_comparison_report.json (correcciones)
- gracias_comparison_viz.png (visualización)


PASO 2: Abrir Blender
----------------------
1. Abrir Blender
2. File > Import > glTF 2.0 (.glb/.gltf)
3. Cargar: Nancy.glb
4. Cargar: Nancy_resultado_gracias.glb


PASO 3: Ejecutar correcciones
------------------------------
1. Ir a Scripting tab
2. Abrir este script (blender_finger_corrector.py)
3. Presionar "Run Script"
4. Esperar a que termine


PASO 4: Verificar y exportar
-----------------------------
1. Revisar animación en Timeline
2. Si se ve bien: File > Export > glTF 2.0 (.glb)
3. Guardar como: Nancy_resultado_gracias_CORREGIDO.glb


PASO 5: Usar en el sistema
---------------------------
1. Copiar archivo corregido a:
   test/output/glb/Nancy/cortesia/Nancy_resultado_gracias.glb
2. Probar en: http://localhost:8000/animation.html
3. Escribir: "gracias"
4. Verificar que los dedos se vean correctos


NOTAS IMPORTANTES:
------------------
- El script mantiene intacta la animación corporal de DeepMotion
- Solo modifica las rotaciones de los dedos
- Aplica suavizado automático para fluidez
- Compatible con exportación GLB
- Funciona con React Native


TROUBLESHOOTING:
----------------
Si los huesos no se encuentran:
1. Ejecutar: corrector.list_available_bones()
2. Actualizar BONE_MAPPING con los nombres correctos
3. Volver a ejecutar

Si la corrección es demasiado fuerte:
1. Modificar threshold en video_to_glb_comparator.py
2. Re-generar el comparison_report.json
3. Volver a aplicar correcciones
"""
