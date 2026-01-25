"""
Script de MotionBuilder para crear la animación de la seña "R" desde cero
basándose en el análisis del video r.mp4
"""

from pyfbsdk import *
from pyfbsdk_additions import *

# CONFIGURACIÓN
VIDEO_FPS = 30
VIDEO_DURACION = 2.75
TOTAL_FRAMES = int(VIDEO_DURACION * VIDEO_FPS)  # ~82 frames

# SECUENCIA DE LA SEÑA "R" (basado en descripción)
# Frame 0-20: Pose inicial - manos juntas
# Frame 21-40: Transición - mano derecha sube
# Frame 41-82: Seña R - índice y medio extendidos y entrelazados, demás dedos cerrados

def limpiar_escena():
    """Limpia la escena"""
    print("🧹 Limpiando escena...")
    FBApplication().FileNew()
    print("✅ Escena limpiada")

def cargar_modelo():
    """Carga el modelo base"""
    print("\n📥 Cargando modelo...")
    
    # Intentar cargar diferentes modelos disponibles
    modelos_posibles = [
        r"C:\Users\andre\OneDrive\Documentos\tesis\convertidor\avatar\Remy_base.fbx",
        r"C:\Users\andre\OneDrive\Documentos\tesis\convertidor\avatar\Leonard.fbx",
        r"C:\Users\andre\OneDrive\Documentos\tesis\convertidor\animacion\Remy_resultado_r.fbx",
        r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Remy_resultado_r.glb"
    ]
    
    from pathlib import Path
    
    for modelo in modelos_posibles:
        if Path(modelo).exists():
            print(f"   ✅ Cargando: {modelo}")
            
            if modelo.endswith('.glb'):
                # Para GLB, primero convertir a FBX usando Blender
                print("   ⚠️ Archivo GLB detectado")
                print("   💡 Debes convertirlo a FBX primero en Blender")
                print("      1. Abre Blender")
                print("      2. Import glTF 2.0 > " + modelo)
                print("      3. Export FBX > convertidor/avatar/Remy_base.fbx")
                return False
            else:
                FBApplication().FileMerge(modelo)
                print("   ✅ Modelo cargado")
                return True
    
    print("   ❌ No se encontró ningún modelo")
    print("   💡 Coloca un archivo FBX en: convertidor/avatar/Remy_base.fbx")
    return False

def encontrar_huesos_manos():
    """Encuentra los huesos de las manos"""
    print("\n🦴 Buscando huesos de manos...")
    
    scene = FBSystem().Scene
    huesos = {
        # Mano izquierda
        'left_hand': None,
        'left_thumb1': None,
        'left_thumb2': None,
        'left_thumb3': None,
        'left_index1': None,
        'left_index2': None,
        'left_index3': None,
        'left_middle1': None,
        'left_middle2': None,
        'left_middle3': None,
        'left_ring1': None,
        'left_ring2': None,
        'left_ring3': None,
        'left_pinky1': None,
        'left_pinky2': None,
        'left_pinky3': None,
        
        # Mano derecha
        'right_hand': None,
        'right_thumb1': None,
        'right_thumb2': None,
        'right_thumb3': None,
        'right_index1': None,
        'right_index2': None,
        'right_index3': None,
        'right_middle1': None,
        'right_middle2': None,
        'right_middle3': None,
        'right_ring1': None,
        'right_ring2': None,
        'right_ring3': None,
        'right_pinky1': None,
        'right_pinky2': None,
        'right_pinky3': None,
    }
    
    def buscar_recursivo(model):
        """Busca huesos recursivamente"""
        if isinstance(model, FBModelSkeleton):
            name_lower = model.Name.lower()
            
            # Mapeo de nombres (ajustar según tu modelo)
            mapeo = {
                'lefthand': 'left_hand',
                'left_hand': 'left_hand',
                'lefthandthumb1': 'left_thumb1',
                'left_hand_thumb_1': 'left_thumb1',
                'lefthandthumb2': 'left_thumb2',
                'lefthandthumb3': 'left_thumb3',
                'lefthandindex1': 'left_index1',
                'left_hand_index_1': 'left_index1',
                'lefthandindex2': 'left_index2',
                'lefthandindex3': 'left_index3',
                'lefthandmiddle1': 'left_middle1',
                'left_hand_middle_1': 'left_middle1',
                'lefthandmiddle2': 'left_middle2',
                'lefthandmiddle3': 'left_middle3',
                'lefthandring1': 'left_ring1',
                'left_hand_ring_1': 'left_ring1',
                'lefthandring2': 'left_ring2',
                'lefthandring3': 'left_ring3',
                'lefthandpinky1': 'left_pinky1',
                'left_hand_pinky_1': 'left_pinky1',
                'lefthandpinky2': 'left_pinky2',
                'lefthandpinky3': 'left_pinky3',
                
                # Mano derecha
                'righthand': 'right_hand',
                'right_hand': 'right_hand',
                'righthandthumb1': 'right_thumb1',
                'right_hand_thumb_1': 'right_thumb1',
                'righthandthumb2': 'right_thumb2',
                'righthandthumb3': 'right_thumb3',
                'righthandindex1': 'right_index1',
                'right_hand_index_1': 'right_index1',
                'righthandindex2': 'right_index2',
                'righthandindex3': 'right_index3',
                'righthandmiddle1': 'right_middle1',
                'right_hand_middle_1': 'right_middle1',
                'righthandmiddle2': 'right_middle2',
                'righthandmiddle3': 'right_middle3',
                'righthandring1': 'right_ring1',
                'right_hand_ring_1': 'right_ring1',
                'righthandring2': 'right_ring2',
                'righthandring3': 'right_ring3',
                'righthandpinky1': 'right_pinky1',
                'right_hand_pinky_1': 'right_pinky1',
                'righthandpinky2': 'right_pinky2',
                'righthandpinky3': 'right_pinky3',
            }
            
            for patron, key in mapeo.items():
                if patron in name_lower:
                    huesos[key] = model
                    print(f"   ✅ {key}: {model.Name}")
                    break
        
        for child in model.Children:
            buscar_recursivo(child)
    
    for model in scene.RootModel.Children:
        buscar_recursivo(model)
    
    # Contar cuántos encontramos
    encontrados = sum(1 for v in huesos.values() if v is not None)
    print(f"\n📊 Huesos encontrados: {encontrados}/32")
    
    return huesos

def crear_pose_inicial(huesos, frame=0):
    """Frame 0-20: Manos juntas (pose inicial)"""
    print(f"\n🎬 Creando pose inicial (frame {frame})...")
    
    # Ir al frame
    FBPlayerControl().Goto(FBTime(0, 0, 0, frame))
    
    # TODO: Configurar rotaciones para manos juntas
    # Esto requiere valores específicos según tu modelo
    print("   💡 Posiciona las manos juntas manualmente y presiona K para keyframe")
    
    return True

def crear_transicion_subida(huesos, frame_inicio=21, frame_fin=40):
    """Frame 21-40: Mano derecha sube"""
    print(f"\n🎬 Creando transición - mano sube (frames {frame_inicio}-{frame_fin})...")
    
    # Frame inicio transición
    FBPlayerControl().Goto(FBTime(0, 0, 0, frame_inicio))
    print("   💡 Posiciona la mano derecha comenzando a subir y presiona K")
    
    # Frame fin transición
    FBPlayerControl().Goto(FBTime(0, 0, 0, frame_fin))
    print("   💡 Posiciona la mano derecha arriba y presiona K")
    
    return True

def crear_sena_r(huesos, frame_inicio=41):
    """Frame 41-82: Seña R - índice y medio extendidos y entrelazados"""
    print(f"\n🎬 Creando seña R (frame {frame_inicio} en adelante)...")
    
    # Ir al frame
    FBPlayerControl().Goto(FBTime(0, 0, 0, frame_inicio))
    
    print("   💡 Configura la mano derecha:")
    print("      - Índice extendido")
    print("      - Medio extendido")
    print("      - Índice y medio entrelazados (cruzados)")
    print("      - Pulgar, anular y meñique doblados hacia abajo")
    print("   💡 Presiona K para crear keyframe")
    
    return True

def configurar_timeline():
    """Configura el timeline"""
    print(f"\n⏱️ Configurando timeline...")
    
    # FPS
    FBPlayerControl().SetTransportFps(FBTimeMode.kFBTimeMode30Frames)
    
    # Rango
    time_span = FBTimeSpan()
    time_span.Set(FBTime(0, 0, 0, 0), FBTime(0, 0, 0, TOTAL_FRAMES))
    FBSystem().CurrentTake.LocalTimeSpan = time_span
    
    print(f"   ✅ FPS: {VIDEO_FPS}")
    print(f"   ✅ Total frames: {TOTAL_FRAMES}")
    print(f"   ✅ Duración: {VIDEO_DURACION}s")
    
    return True

def activar_auto_key():
    """Activa el modo Auto Key"""
    print("\n🔑 Activando Auto Key...")
    print("   💡 Presiona 'A' en MotionBuilder para activar Auto Key")
    print("   💡 Con Auto Key activo, cualquier cambio crea keyframes automáticamente")
    
    return True

def guardar_animacion():
    """Guarda la animación"""
    output = r"C:\Users\andre\OneDrive\Documentos\tesis\output\Remy_sena_r.fbx"
    print(f"\n💾 Guardando animación en: {output}")
    
    FBApplication().FileSave(output)
    print("✅ Animación guardada")
    
    return output

def main():
    print("=" * 70)
    print("🎯 CREAR ANIMACIÓN SEÑA 'R' - PASO A PASO")
    print("=" * 70)
    
    print("\n📋 SECUENCIA:")
    print("   Frame 0-20:  Pose inicial - manos juntas")
    print("   Frame 21-40: Transición - mano derecha sube")
    print("   Frame 41-82: Seña R - índice y medio extendidos y entrelazados")
    
    # 1. Limpiar escena
    limpiar_escena()
    
    # 2. Cargar modelo
    if not cargar_modelo():
        print("\n❌ No se pudo cargar el modelo. Proceso detenido.")
        return
    
    # 3. Configurar timeline
    configurar_timeline()
    
    # 4. Encontrar huesos
    huesos = encontrar_huesos_manos()
    
    # 5. Activar Auto Key
    activar_auto_key()
    
    print("\n" + "=" * 70)
    print("✅ CONFIGURACIÓN COMPLETADA")
    print("=" * 70)
    
    print("\n📋 AHORA CREA LA ANIMACIÓN MANUALMENTE:")
    print("\n1️⃣ FRAME 0-20: Pose Inicial")
    print("   - Ve al frame 0: FBPlayerControl().Goto(FBTime(0,0,0,0))")
    print("   - Presiona 'A' para activar Auto Key (luz roja)")
    print("   - Selecciona huesos de ambas manos")
    print("   - Posiciona las manos juntas frente al pecho")
    print("   - Los keyframes se crearán automáticamente")
    
    print("\n2️⃣ FRAME 21-40: Transición")
    print("   - Ve al frame 21: FBPlayerControl().Goto(FBTime(0,0,0,21))")
    print("   - Mueve mano derecha comenzando a subir")
    print("   - Ve al frame 40: FBPlayerControl().Goto(FBTime(0,0,0,40))")
    print("   - Mano derecha arriba (altura de la cabeza)")
    
    print("\n3️⃣ FRAME 41-82: Seña R")
    print("   - Ve al frame 41: FBPlayerControl().Goto(FBTime(0,0,0,41))")
    print("   - Configura la mano derecha:")
    print("     * RightHandIndex1-3: Extendidos")
    print("     * RightHandMiddle1-3: Extendidos")
    print("     * Rota índice y medio para entrelazarlos (cruzar)")
    print("     * RightHandThumb1-3: Doblados hacia abajo")
    print("     * RightHandRing1-3: Doblados hacia abajo")
    print("     * RightHandPinky1-3: Doblados hacia abajo")
    
    print("\n4️⃣ GUARDAR")
    print("   - Cuando termines, ejecuta: guardar_animacion()")
    
    print("\n💡 TIPS:")
    print("   - Usa el Gimbal rotate para rotar huesos")
    print("   - Presiona 'R' para activar rotation tool")
    print("   - Usa las vistas Front (F1), Top (F2), Right (F3)")
    print("   - Reproduce la animación con Space para verificar")

if __name__ == "__main__":
    main()
