"""
Script de Blender para Inspeccionar Shape Keys ARKit
Compatible con Blender 4.5+

PROPÓSITO:
Este script analiza un modelo importado desde DeepMotion y muestra
todos los Shape Keys (Blendshapes) disponibles, ayudando a verificar
cuáles están presentes antes de configurar las emociones.

INSTRUCCIONES:
1. Importar modelo GLB en Blender
2. Abrir pestaña "Scripting"
3. Cargar este script
4. Ejecutar (Alt+P o "Run Script")
5. Ver reporte en la consola

El script mostrará:
- Todos los Shape Keys encontrados
- Cuáles están presentes del estándar ARKit
- Cuáles faltan para configurar emociones
"""

import bpy
from typing import Dict, List, Set


class ARKitShapeKeyInspector:
    """Inspecciona Shape Keys ARKit en modelos de DeepMotion"""
    
    # Shape Keys ARKit estándar para emociones
    ARKIT_FACE_SHAPES = {
        # Cejas
        'BrowDownLeft', 'BrowDownRight', 'BrowInnerUp',
        'BrowOuterUpLeft', 'BrowOuterUpRight',
        
        # Mejillas
        'CheekPuff', 'CheekSquintLeft', 'CheekSquintRight',
        
        # Ojos
        'EyeBlinkLeft', 'EyeBlinkRight',
        'EyeLookDownLeft', 'EyeLookDownRight',
        'EyeLookInLeft', 'EyeLookInRight',
        'EyeLookOutLeft', 'EyeLookOutRight',
        'EyeLookUpLeft', 'EyeLookUpRight',
        'EyeSquintLeft', 'EyeSquintRight',
        'EyeWideLeft', 'EyeWideRight',
        
        # Mandíbula
        'JawForward', 'JawLeft', 'JawRight', 'JawOpen',
        
        # Boca
        'MouthClose', 'MouthFunnel', 'MouthPucker',
        'MouthLeft', 'MouthRight',
        'MouthSmileLeft', 'MouthSmileRight',
        'MouthFrownLeft', 'MouthFrownRight',
        'MouthDimpleLeft', 'MouthDimpleRight',
        'MouthStretchLeft', 'MouthStretchRight',
        'MouthRollLower', 'MouthRollUpper',
        'MouthShrugLower', 'MouthShrugUpper',
        'MouthPressLeft', 'MouthPressRight',
        'MouthLowerDownLeft', 'MouthLowerDownRight',
        'MouthUpperUpLeft', 'MouthUpperUpRight',
        
        # Nariz
        'NoseSneerLeft', 'NoseSneerRight',
        
        # Lengua
        'TongueOut'
    }
    
    # Shape Keys necesarios para cada emoción
    EMOTION_REQUIREMENTS = {
        'EMOTION_SORPRESA': ['BrowInnerUp', 'BrowOuterUpLeft', 'BrowOuterUpRight', 
                            'EyeWideLeft', 'EyeWideRight'],
        'EMOTION_IRA': ['BrowDownLeft', 'BrowDownRight', 'MouthFrownLeft', 'MouthFrownRight'],
        'EMOTION_ALEGRIA': ['MouthSmileLeft', 'MouthSmileRight', 'CheekPuff'],
        'EMOTION_ASCO': ['NoseSneerLeft', 'NoseSneerRight', 'MouthUpperUpLeft', 'MouthUpperUpRight'],
        'EMOTION_TRISTEZA': ['MouthDimpleLeft', 'MouthDimpleRight', 'MouthLowerDownLeft', 'MouthLowerDownRight'],
        'BLINK_CONTROL': ['EyeBlinkLeft', 'EyeBlinkRight']
    }
    
    def __init__(self):
        self.face_mesh = None
        self.shape_keys_found = []
        self.arkit_shapes_present = set()
        self.arkit_shapes_missing = set()
    
    def log(self, message: str, level: str = 'INFO'):
        """Registra mensajes con formato"""
        prefix = {
            'INFO': 'ℹ️',
            'SUCCESS': '✅',
            'WARNING': '⚠️',
            'ERROR': '❌',
            'HEADER': '📊'
        }.get(level, '  ')
        
        print(f"{prefix} {message}")
    
    def find_face_mesh(self) -> bool:
        """Encuentra la malla con Shape Keys"""
        self.log("\n🔍 Buscando malla con Shape Keys...")
        
        # Buscar meshes con Shape Keys
        candidates = []
        for obj in bpy.context.scene.objects:
            if obj.type == 'MESH' and obj.data.shape_keys:
                candidates.append(obj)
        
        if not candidates:
            self.log("No se encontró ninguna malla con Shape Keys", 'ERROR')
            return False
        
        # Priorizar meshes con 'Face' o 'Head' en el nombre
        for obj in candidates:
            name_lower = obj.name.lower()
            if 'face' in name_lower or 'head' in name_lower:
                self.face_mesh = obj
                break
        
        # Si no se encontró, tomar el primero
        if not self.face_mesh:
            self.face_mesh = candidates[0]
        
        self.log(f"Malla encontrada: '{self.face_mesh.name}'", 'SUCCESS')
        return True
    
    def analyze_shape_keys(self):
        """Analiza los Shape Keys disponibles"""
        if not self.face_mesh or not self.face_mesh.data.shape_keys:
            return
        
        key_blocks = self.face_mesh.data.shape_keys.key_blocks
        
        # Recopilar todos los shape keys (excepto Basis)
        for kb in key_blocks:
            if kb.name != 'Basis':
                self.shape_keys_found.append(kb.name)
                
                # Verificar si es ARKit
                if kb.name in self.ARKIT_FACE_SHAPES:
                    self.arkit_shapes_present.add(kb.name)
        
        # Calcular faltantes
        self.arkit_shapes_missing = self.ARKIT_FACE_SHAPES - self.arkit_shapes_present
    
    def print_shape_keys_list(self):
        """Imprime lista completa de Shape Keys"""
        self.log("\n" + "="*60)
        self.log("SHAPE KEYS ENCONTRADOS", 'HEADER')
        self.log("="*60)
        
        if not self.shape_keys_found:
            self.log("Ningún Shape Key encontrado", 'WARNING')
            return
        
        self.log(f"Total: {len(self.shape_keys_found)} Shape Keys\n")
        
        # Agrupar por categoría si es ARKit
        arkit_found = []
        other_found = []
        
        for sk in sorted(self.shape_keys_found):
            if sk in self.ARKIT_FACE_SHAPES:
                arkit_found.append(sk)
            else:
                other_found.append(sk)
        
        if arkit_found:
            self.log(f"ARKit Shape Keys ({len(arkit_found)}):", 'SUCCESS')
            for i, sk in enumerate(arkit_found, 1):
                print(f"  {i:2d}. {sk}")
        
        if other_found:
            self.log(f"\nOtros Shape Keys ({len(other_found)}):", 'INFO')
            for i, sk in enumerate(other_found, 1):
                print(f"  {i:2d}. {sk}")
    
    def print_arkit_coverage(self):
        """Imprime cobertura de ARKit"""
        self.log("\n" + "="*60)
        self.log("COBERTURA ARKit", 'HEADER')
        self.log("="*60)
        
        total_arkit = len(self.ARKIT_FACE_SHAPES)
        present = len(self.arkit_shapes_present)
        missing = len(self.arkit_shapes_missing)
        
        percentage = (present / total_arkit * 100) if total_arkit > 0 else 0
        
        self.log(f"Presentes: {present}/{total_arkit} ({percentage:.1f}%)")
        
        if missing > 0:
            self.log(f"Faltantes: {missing}", 'WARNING')
            
            if missing <= 10:
                self.log("\nShape Keys ARKit faltantes:")
                for sk in sorted(self.arkit_shapes_missing):
                    print(f"  - {sk}")
    
    def check_emotion_coverage(self):
        """Verifica si se pueden configurar las emociones"""
        self.log("\n" + "="*60)
        self.log("VERIFICACIÓN DE EMOCIONES", 'HEADER')
        self.log("="*60)
        
        for emotion, required_shapes in self.EMOTION_REQUIREMENTS.items():
            present_shapes = [sk for sk in required_shapes if sk in self.arkit_shapes_present]
            missing_shapes = [sk for sk in required_shapes if sk not in self.arkit_shapes_present]
            
            coverage = len(present_shapes) / len(required_shapes) * 100
            
            if coverage == 100:
                status = '✅ COMPLETO'
            elif coverage >= 50:
                status = '⚠️  PARCIAL'
            else:
                status = '❌ INSUFICIENTE'
            
            self.log(f"\n{emotion}:")
            self.log(f"  Estado: {status} ({coverage:.0f}%)")
            self.log(f"  Presentes: {len(present_shapes)}/{len(required_shapes)}")
            
            if missing_shapes:
                self.log(f"  Faltantes: {', '.join(missing_shapes)}", 'WARNING')
    
    def print_recommendations(self):
        """Imprime recomendaciones"""
        self.log("\n" + "="*60)
        self.log("RECOMENDACIONES", 'HEADER')
        self.log("="*60)
        
        arkit_coverage = len(self.arkit_shapes_present) / len(self.ARKIT_FACE_SHAPES) * 100
        
        if arkit_coverage >= 80:
            self.log("✅ Este modelo tiene buena cobertura de ARKit Blendshapes", 'SUCCESS')
            self.log("   Puedes ejecutar 'setup_facial_emotions_arkit.py' para configurar emociones")
        elif arkit_coverage >= 50:
            self.log("⚠️  Este modelo tiene cobertura parcial de ARKit", 'WARNING')
            self.log("   Algunas emociones podrían no funcionar completamente")
            self.log("   Revisa la sección 'VERIFICACIÓN DE EMOCIONES' arriba")
        else:
            self.log("❌ Este modelo tiene baja cobertura de ARKit", 'ERROR')
            self.log("   Es posible que no sea compatible con el sistema de emociones")
            self.log("   Verifica que el modelo sea exportado desde DeepMotion con ARKit enabled")
    
    def run(self):
        """Ejecuta el inspector completo"""
        self.log("\n" + "="*70)
        self.log("🔍 INSPECTOR DE SHAPE KEYS ARKit - DeepMotion GLB", 'HEADER')
        self.log("="*70)
        
        # 1. Encontrar malla
        if not self.find_face_mesh():
            return False
        
        # 2. Analizar Shape Keys
        self.analyze_shape_keys()
        
        # 3. Reportes
        self.print_shape_keys_list()
        self.print_arkit_coverage()
        self.check_emotion_coverage()
        self.print_recommendations()
        
        self.log("\n" + "="*70)
        self.log("INSPECCIÓN COMPLETADA", 'SUCCESS')
        self.log("="*70 + "\n")
        
        return True


def main():
    """Función principal"""
    inspector = ARKitShapeKeyInspector()
    inspector.run()


if __name__ == "__main__":
    main()
