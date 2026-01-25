"""
Script de Ejemplo: Animación Automática de Emociones
Compatible con Blender 4.5+

PROPÓSITO:
Demuestra cómo animar automáticamente las emociones faciales
creando keyframes en los controles maestros.

PREREQUISITO:
Debes ejecutar primero 'setup_facial_emotions_arkit.py' para
crear los controles de emociones.

INSTRUCCIONES:
1. Importar GLB en Blender
2. Ejecutar setup_facial_emotions_arkit.py
3. Ejecutar este script (Alt+P)
4. Presionar ESPACIO para ver la animación

El script crea una secuencia de 300 frames mostrando diferentes
emociones que se van interpolando suavemente.
"""

import bpy


class EmotionAnimator:
    """Crea animación automática de emociones"""
    
    def __init__(self):
        self.armature = None
        self.emotion_controls = [
            'EMOTION_SORPRESA',
            'EMOTION_IRA',
            'EMOTION_ALEGRIA',
            'EMOTION_ASCO',
            'EMOTION_TRISTEZA',
            'BLINK_CONTROL'
        ]
    
    def log(self, message: str):
        """Registra mensaje"""
        print(f"🎬 {message}")
    
    def find_armature(self) -> bool:
        """Encuentra el armature con controles de emociones"""
        armatures = [obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE']
        
        if not armatures:
            self.log("❌ No se encontró Armature")
            return False
        
        # Verificar que tenga los controles
        for arm in armatures:
            if 'EMOTION_ALEGRIA' in arm.keys():
                self.armature = arm
                self.log(f"✅ Armature encontrado: '{arm.name}'")
                return True
        
        self.log("❌ No se encontraron controles de emociones")
        self.log("   Ejecuta primero: setup_facial_emotions_arkit.py")
        return False
    
    def reset_emotions(self):
        """Resetea todas las emociones a 0"""
        for control in self.emotion_controls:
            if control in self.armature.keys():
                self.armature[control] = 0.0
    
    def set_emotion_keyframe(self, frame: int, emotion: str, value: float):
        """
        Crea un keyframe para una emoción
        
        Args:
            frame: Número de frame
            emotion: Nombre del control (ej: 'EMOTION_ALEGRIA')
            value: Valor del control (0.0 a 1.0)
        """
        if emotion not in self.armature.keys():
            return
        
        # Establecer valor
        self.armature[emotion] = value
        
        # Crear keyframe
        self.armature.keyframe_insert(data_path=f'["{emotion}"]', frame=frame)
    
    def create_demo_animation(self):
        """Crea una animación de demostración"""
        self.log("\n📊 Creando animación de demostración...")
        
        # Resetear todo
        self.reset_emotions()
        
        # Secuencia de emociones (frame, emoción, valor)
        keyframes = [
            # Inicio neutral
            (1, None, 0.0),
            
            # Sorpresa (frames 30-60)
            (30, 'EMOTION_SORPRESA', 1.0),
            (60, 'EMOTION_SORPRESA', 0.0),
            
            # Alegría (frames 70-100)
            (70, 'EMOTION_ALEGRIA', 1.0),
            (100, 'EMOTION_ALEGRIA', 0.0),
            
            # Tristeza (frames 110-140)
            (110, 'EMOTION_TRISTEZA', 0.8),
            (140, 'EMOTION_TRISTEZA', 0.0),
            
            # Ira (frames 150-180)
            (150, 'EMOTION_IRA', 0.9),
            (180, 'EMOTION_IRA', 0.0),
            
            # Asco (frames 190-220)
            (190, 'EMOTION_ASCO', 0.8),
            (220, 'EMOTION_ASCO', 0.0),
            
            # Combinación: Sorpresa + Alegría (frames 230-260)
            (230, 'EMOTION_SORPRESA', 0.5),
            (230, 'EMOTION_ALEGRIA', 0.7),
            (260, 'EMOTION_SORPRESA', 0.0),
            (260, 'EMOTION_ALEGRIA', 0.0),
            
            # Parpadeos durante todo (cada 30 frames)
            (20, 'BLINK_CONTROL', 1.0),
            (22, 'BLINK_CONTROL', 0.0),
            (80, 'BLINK_CONTROL', 1.0),
            (82, 'BLINK_CONTROL', 0.0),
            (130, 'BLINK_CONTROL', 1.0),
            (132, 'BLINK_CONTROL', 0.0),
            (170, 'BLINK_CONTROL', 1.0),
            (172, 'BLINK_CONTROL', 0.0),
            (210, 'BLINK_CONTROL', 1.0),
            (212, 'BLINK_CONTROL', 0.0),
            (250, 'BLINK_CONTROL', 1.0),
            (252, 'BLINK_CONTROL', 0.0),
            
            # Final neutral
            (280, None, 0.0),
        ]
        
        # Crear keyframes
        for frame, emotion, value in keyframes:
            if emotion:
                self.set_emotion_keyframe(frame, emotion, value)
                self.log(f"  Frame {frame:3d}: {emotion} = {value:.1f}")
            else:
                # Resetear todas las emociones
                for control in self.emotion_controls:
                    self.set_emotion_keyframe(frame, control, 0.0)
        
        # Configurar timeline
        bpy.context.scene.frame_start = 1
        bpy.context.scene.frame_end = 300
        bpy.context.scene.frame_current = 1
        
        self.log("\n✅ Animación creada: 300 frames")
        self.log("   Presiona ESPACIO para reproducir")
    
    def run(self):
        """Ejecuta el animator"""
        self.log("\n" + "="*60)
        self.log("ANIMATOR DE EMOCIONES - Demo Automática")
        self.log("="*60)
        
        if not self.find_armature():
            return False
        
        self.create_demo_animation()
        
        self.log("\n" + "="*60)
        self.log("TIMELINE DE EMOCIONES")
        self.log("="*60)
        self.log("Frames 30-60:   😮 Sorpresa")
        self.log("Frames 70-100:  😊 Alegría")
        self.log("Frames 110-140: 😢 Tristeza")
        self.log("Frames 150-180: 😠 Ira")
        self.log("Frames 190-220: 🤢 Asco")
        self.log("Frames 230-260: 😲 Sorpresa + Alegría")
        self.log("Cada ~30 frames: 😑 Parpadeo")
        self.log("="*60 + "\n")
        
        return True


def main():
    """Función principal"""
    animator = EmotionAnimator()
    animator.run()


if __name__ == "__main__":
    main()
