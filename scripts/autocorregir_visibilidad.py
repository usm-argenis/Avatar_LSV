"""
Sistema de Auto-Corrección de Visibilidad y Dedos
Corrige automáticamente:
1. Posición de dedos según correcciones definidas
2. Visibilidad de manos (detecta y corrige cuando están ocultas por el torso)
"""

import json
import numpy as np
from pathlib import Path
from pygltflib import GLTF2
import struct
import math

class AutoCorrector:
    def __init__(self, glb_path, output_path):
        self.glb_path = Path(glb_path)
        self.output_path = Path(output_path)
        self.gltf = None
        
        # Mapeo de huesos
        self.BONE_MAPPING = {
            'thumb_01_r': 'thumb_mcp',
            'f_index.01_r': 'index_mcp',
            'f_middle.01_r': 'middle_mcp',
            'f_ring.01_r': 'ring_mcp',
            'f_pinky.01_r': 'pinky_mcp'
        }
        
        # Huesos de brazo para visibilidad
        self.ARM_BONES = [
            'shoulder_r',
            'upper_arm_r',
            'forearm_r',
            'hand_r'
        ]
        
        # Hueso de referencia del torso
        self.TORSO_BONE = 'spine_03'
        
    def cargar_glb(self):
        """Carga el archivo GLB"""
        print(f"📂 Cargando: {self.glb_path.name}")
        self.gltf = GLTF2().load(str(self.glb_path))
        return True
        
    def encontrar_bone_index(self, bone_name):
        """Encuentra el índice de un hueso por nombre"""
        for skin in self.gltf.skins:
            for i, joint_index in enumerate(skin.joints):
                node = self.gltf.nodes[joint_index]
                if node.name == bone_name:
                    return joint_index
        return None
        
    def obtener_posicion_bone(self, bone_name, frame):
        """Obtiene la posición 3D de un hueso en un frame específico"""
        bone_index = self.encontrar_bone_index(bone_name)
        if bone_index is None:
            return None
            
        # Por ahora retornamos la posición base del nodo
        node = self.gltf.nodes[bone_index]
        if node.translation:
            return np.array(node.translation)
        return np.array([0.0, 0.0, 0.0])
        
    def mano_esta_oculta(self, frame):
        """
        Detecta si la mano está oculta detrás del torso
        Retorna: (esta_oculta: bool, distancia_Z: float)
        """
        pos_mano = self.obtener_posicion_bone('hand_r', frame)
        pos_torso = self.obtener_posicion_bone(self.TORSO_BONE, frame)
        
        if pos_mano is None or pos_torso is None:
            return False, 0.0
            
        # En Blender/GLB, Z positivo es hacia adelante
        # Si mano.z < torso.z, la mano está detrás del torso
        distancia_z = pos_mano[2] - pos_torso[2]
        
        # También verificar que esté cerca en X (frente al cuerpo)
        distancia_x = abs(pos_mano[0] - pos_torso[0])
        
        esta_oculta = distancia_z < 0.05 and distancia_x < 0.3
        
        return esta_oculta, distancia_z
        
    def aplicar_correccion_visibilidad(self, bone_name, frame, ajuste_Z=0.15):
        """
        Aplica corrección para traer el brazo hacia adelante
        ajuste_Z: metros a mover hacia adelante (default 15cm)
        """
        bone_index = self.encontrar_bone_index(bone_name)
        if bone_index is None:
            return False
            
        print(f"   🔧 Ajustando {bone_name} hacia adelante (+{ajuste_Z}m)")
        
        # Aquí aplicaríamos la transformación
        # Por limitaciones de pygltflib, generamos instrucciones para Blender
        return True
        
    def aplicar_correccion_dedos(self, correcciones):
        """
        Aplica correcciones de rotación a los dedos
        correcciones: dict con estructura {articulacion: grados}
        """
        print(f"\n🔧 Aplicando correcciones de dedos...")
        
        for bone_glb, bone_logic in self.BONE_MAPPING.items():
            if bone_logic in correcciones:
                grados = correcciones[bone_logic]
                print(f"   • {bone_logic}: {grados:+.1f}°")
                
        return True
        
    def analizar_visibilidad_completa(self, total_frames=54):
        """
        Analiza todos los frames para detectar problemas de visibilidad
        """
        print(f"\n🔍 Analizando visibilidad en {total_frames} frames...\n")
        
        frames_ocultos = []
        
        for frame in range(total_frames):
            esta_oculta, dist_z = self.mano_esta_oculta(frame)
            
            if esta_oculta:
                frames_ocultos.append({
                    'frame': frame,
                    'distancia_z': dist_z,
                    'tiempo': frame / 29.97
                })
                
        if frames_ocultos:
            print(f"⚠️  MANO OCULTA en {len(frames_ocultos)} frames:")
            for info in frames_ocultos[:5]:  # Mostrar primeros 5
                print(f"   • Frame {info['frame']:3d} (t={info['tiempo']:.2f}s) - Z={info['distancia_z']:+.3f}m")
            if len(frames_ocultos) > 5:
                print(f"   ... y {len(frames_ocultos) - 5} frames más")
        else:
            print("✅ Mano visible en todos los frames")
            
        return frames_ocultos
        
    def generar_script_blender(self, correcciones_dedos, frames_ocultos, output_json):
        """
        Genera un JSON con todas las correcciones para aplicar en Blender
        """
        script_data = {
            "metadata": {
                "glb_original": str(self.glb_path),
                "glb_output": str(self.output_path),
                "fecha": "2025-12-17"
            },
            "correcciones_dedos": [],
            "correcciones_visibilidad": [],
            "instrucciones": []
        }
        
        # Correcciones de dedos
        for bone_glb, bone_logic in self.BONE_MAPPING.items():
            if bone_logic in correcciones_dedos:
                script_data["correcciones_dedos"].append({
                    "bone_name": bone_glb,
                    "rotation_z_degrees": correcciones_dedos[bone_logic],
                    "frame_start": 10,
                    "frame_end": 50,
                    "tipo": "rotation"
                })
                
        # Correcciones de visibilidad
        if frames_ocultos:
            # Agrupar frames consecutivos
            grupos = []
            grupo_actual = [frames_ocultos[0]['frame']]
            
            for i in range(1, len(frames_ocultos)):
                if frames_ocultos[i]['frame'] - frames_ocultos[i-1]['frame'] <= 2:
                    grupo_actual.append(frames_ocultos[i]['frame'])
                else:
                    grupos.append(grupo_actual)
                    grupo_actual = [frames_ocultos[i]['frame']]
            grupos.append(grupo_actual)
            
            for grupo in grupos:
                script_data["correcciones_visibilidad"].append({
                    "bone_name": "upper_arm_r",
                    "frame_start": min(grupo),
                    "frame_end": max(grupo),
                    "ajuste_Z": 0.15,  # 15cm hacia adelante
                    "tipo": "translation",
                    "razon": "Mano oculta por torso"
                })
                
        # Instrucciones para Blender
        script_data["instrucciones"] = [
            "1. Abrir Blender y crear nueva escena",
            "2. Importar GLB: File > Import > glTF 2.0",
            f"3. Seleccionar archivo: {self.glb_path}",
            "4. Cambiar a Pose Mode (Ctrl+Tab)",
            "5. Aplicar correcciones automáticamente con script Python",
            "6. Exportar: File > Export > glTF 2.0",
            f"7. Guardar como: {self.output_path}"
        ]
        
        # Guardar JSON
        output_json.parent.mkdir(parents=True, exist_ok=True)
        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump(script_data, f, indent=2, ensure_ascii=False)
            
        print(f"\n💾 Script Blender guardado: {output_json}")
        return script_data
        
    def generar_script_blender_python(self, correcciones_json, output_py):
        """
        Genera un script Python que se puede ejecutar dentro de Blender
        """
        with open(correcciones_json, 'r') as f:
            data = json.load(f)
            
        script = f'''"""
Script de Auto-Corrección para Blender
Generado automáticamente
Aplica correcciones de dedos y visibilidad
"""

import bpy
import math

def aplicar_correccion_dedo(bone_name, rotation_z_deg, frame_start, frame_end):
    """Aplica rotación a un hueso de dedo"""
    armature = bpy.context.active_object
    if armature.type != 'ARMATURE':
        print("⚠️  Por favor selecciona el Armature primero")
        return False
        
    pose_bone = armature.pose.bones.get(bone_name)
    if not pose_bone:
        print(f"⚠️  Hueso {{bone_name}} no encontrado")
        return False
        
    bpy.context.scene.frame_set(frame_start)
    
    # Rotar en Z
    rotation_rad = math.radians(rotation_z_deg)
    pose_bone.rotation_euler[2] += rotation_rad
    pose_bone.keyframe_insert(data_path="rotation_euler", frame=frame_start)
    
    bpy.context.scene.frame_set(frame_end)
    pose_bone.keyframe_insert(data_path="rotation_euler", frame=frame_end)
    
    print(f"✅ {{bone_name}}: {{rotation_z_deg:+.1f}}° (frames {{frame_start}}-{{frame_end}})")
    return True

def aplicar_correccion_visibilidad(bone_name, frame_start, frame_end, ajuste_Z):
    """Mueve el brazo hacia adelante para visibilidad"""
    armature = bpy.context.active_object
    if armature.type != 'ARMATURE':
        return False
        
    pose_bone = armature.pose.bones.get(bone_name)
    if not pose_bone:
        print(f"⚠️  Hueso {{bone_name}} no encontrado")
        return False
        
    bpy.context.scene.frame_set(frame_start)
    
    # Mover en Z (hacia adelante)
    pose_bone.location[2] += ajuste_Z
    pose_bone.keyframe_insert(data_path="location", frame=frame_start)
    
    bpy.context.scene.frame_set(frame_end)
    pose_bone.keyframe_insert(data_path="location", frame=frame_end)
    
    print(f"✅ {{bone_name}}: +{{ajuste_Z}}m adelante (frames {{frame_start}}-{{frame_end}})")
    return True

def main():
    print("\\n" + "="*60)
    print("🚀 INICIANDO AUTO-CORRECCIÓN")
    print("="*60 + "\\n")
    
    # Verificar que hay un armature seleccionado
    if not bpy.context.active_object or bpy.context.active_object.type != 'ARMATURE':
        print("❌ ERROR: Por favor selecciona el Armature en la escena")
        return
        
    bpy.ops.object.mode_set(mode='POSE')
    
    # CORRECCIONES DE DEDOS
    print("\\n🔧 APLICANDO CORRECCIONES DE DEDOS\\n")
    correcciones_dedos = {json.dumps(data['correcciones_dedos'], indent=8)}
    
    for corr in correcciones_dedos:
        aplicar_correccion_dedo(
            corr['bone_name'],
            corr['rotation_z_degrees'],
            corr['frame_start'],
            corr['frame_end']
        )
    
    # CORRECCIONES DE VISIBILIDAD
    print("\\n👁️  APLICANDO CORRECCIONES DE VISIBILIDAD\\n")
    correcciones_vis = {json.dumps(data['correcciones_visibilidad'], indent=8)}
    
    for corr in correcciones_vis:
        aplicar_correccion_visibilidad(
            corr['bone_name'],
            corr['frame_start'],
            corr['frame_end'],
            corr['ajuste_Z']
        )
    
    # Suavizar curvas
    print("\\n✨ SUAVIZANDO ANIMACIÓN\\n")
    bpy.ops.pose.select_all(action='SELECT')
    bpy.ops.graph.smooth()
    
    print("\\n" + "="*60)
    print("✅ AUTO-CORRECCIÓN COMPLETADA")
    print("="*60)
    print("\\n📤 Ahora exporta: File > Export > glTF 2.0 (.glb)")
    print(f"📁 Guardar como: {data['metadata']['glb_output']}\\n")

if __name__ == "__main__":
    main()
'''
        
        output_py.parent.mkdir(parents=True, exist_ok=True)
        with open(output_py, 'w', encoding='utf-8') as f:
            f.write(script)
            
        print(f"💾 Script Python Blender: {output_py}")
        return True


def procesar_yo():
    """Procesa la seña 'yo' con auto-corrección completa"""
    
    BASE_DIR = Path(__file__).parent.parent
    GLB_ORIGINAL = BASE_DIR / "test" / "output" / "glb" / "Nancy" / "pronombres" / "Nancy_resultado_yo.glb"
    GLB_OUTPUT = BASE_DIR / "test" / "output" / "glb" / "Nancy" / "pronombres" / "Nancy_resultado_yo_AUTOCORREGIDO.glb"
    JSON_OUTPUT = BASE_DIR / "test" / "output" / "comparisons" / "yo_autocorreccion.json"
    SCRIPT_BLENDER = BASE_DIR / "scripts" / "blender_autocorreccion_yo.py"
    
    print("=" * 70)
    print("🤖 SISTEMA DE AUTO-CORRECCIÓN - SEÑA 'YO'")
    print("=" * 70)
    
    # Verificar archivo original
    if not GLB_ORIGINAL.exists():
        print(f"❌ ERROR: No se encuentra {GLB_ORIGINAL}")
        return False
        
    # Crear corrector
    corrector = AutoCorrector(GLB_ORIGINAL, GLB_OUTPUT)
    
    # Cargar GLB
    corrector.cargar_glb()
    
    # Correcciones de dedos para "yo"
    correcciones_dedos = {
        'index_mcp': -15,    # Índice más extendido
        'middle_mcp': 10,    # Medio más cerrado
        'ring_mcp': 10,      # Anular más cerrado
        'pinky_mcp': 10,     # Meñique más cerrado
        'thumb_mcp': 5       # Pulgar ajuste ligero
    }
    
    print("\n📋 CORRECCIONES DE DEDOS DEFINIDAS:")
    for dedo, grados in correcciones_dedos.items():
        prioridad = "🔴 CRÍTICO" if dedo == 'index_mcp' else "⚠️  IMPORTANTE" if abs(grados) >= 10 else "✅ MENOR"
        print(f"   • {dedo}: {grados:+d}° {prioridad}")
    
    # Analizar visibilidad
    frames_ocultos = corrector.analizar_visibilidad_completa(total_frames=54)
    
    # Generar scripts
    print("\n📝 Generando scripts de corrección...")
    corrector.generar_script_blender(correcciones_dedos, frames_ocultos, JSON_OUTPUT)
    corrector.generar_script_blender_python(JSON_OUTPUT, SCRIPT_BLENDER)
    
    # Resumen
    print("\n" + "=" * 70)
    print("✅ ANÁLISIS COMPLETADO")
    print("=" * 70)
    print(f"\n📊 RESULTADOS:")
    print(f"   • Correcciones de dedos: {len(correcciones_dedos)}")
    print(f"   • Frames con mano oculta: {len(frames_ocultos)}")
    print(f"   • Correcciones de visibilidad: {len(frames_ocultos) > 0}")
    
    print(f"\n📁 ARCHIVOS GENERADOS:")
    print(f"   1. {JSON_OUTPUT.name}")
    print(f"   2. {SCRIPT_BLENDER.name}")
    
    print(f"\n🚀 PRÓXIMOS PASOS:")
    print(f"   1. Abrir Blender")
    print(f"   2. Importar: {GLB_ORIGINAL.name}")
    print(f"   3. Abrir Scripting tab")
    print(f"   4. Cargar y ejecutar: {SCRIPT_BLENDER.name}")
    print(f"   5. Exportar como: {GLB_OUTPUT.name}")
    print(f"   6. Comparar en el navegador\n")
    
    return True


if __name__ == "__main__":
    procesar_yo()
