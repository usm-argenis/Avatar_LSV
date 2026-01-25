"""
Script de MotionBuilder para ajustar animación de manos basándose en video de referencia
Ejecutar en MotionBuilder 2026
"""

from pyfbsdk import *
from pyfbsdk_additions import *
import json
from pathlib import Path

# CONFIGURACIÓN
VIDEO_FPS = 30  # Redondeado de 29.47
VIDEO_DURACION = 2.75  # segundos
FRAMES_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\output\frames_r")
FRAMES_INFO = FRAMES_DIR / "frames_info.json"

# Convertir GLB a FBX primero (hacer manual en Blender)
FBX_INPUT = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\convertidor\animacion\Remy_resultado_r.fbx")
FBX_OUTPUT = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\output\Remy_resultado_r_ajustado.fbx")

def limpiar_escena():
    """Limpia la escena de MotionBuilder"""
    print("🧹 Limpiando escena...")
    
    # Crear nueva escena
    FBApplication().FileNew()
    
    print("✅ Escena limpiada")

def cargar_fbx():
    """Carga el archivo FBX"""
    print(f"\n📥 Cargando FBX: {FBX_INPUT}")
    
    if not FBX_INPUT.exists():
        print(f"❌ ERROR: No se encuentra el archivo: {FBX_INPUT}")
        print("💡 Primero debes convertir el GLB a FBX:")
        print("   1. Abre Blender")
        print("   2. Importa: test/output/glb/Remy_resultado_r.glb")
        print("   3. Exporta como FBX a: convertidor/animacion/Remy_resultado_r.fbx")
        return False
    
    # Cargar FBX
    FBApplication().FileMerge(str(FBX_INPUT))
    
    print("✅ FBX cargado")
    return True

def encontrar_character():
    """Encuentra el character en la escena"""
    print("\n🔍 Buscando character...")
    
    scene = FBSystem().Scene
    
    for comp in scene.Characters:
        print(f"   ✅ Character encontrado: {comp.Name}")
        return comp
    
    print("   ⚠️ No se encontró character, creando uno...")
    
    # Si no hay character, buscar el armature y crear uno
    armature = None
    for model in scene.RootModel.Children:
        if "armature" in model.Name.lower() or "skeleton" in model.Name.lower():
            armature = model
            break
    
    if not armature:
        # Buscar cualquier modelo que tenga hijos (probablemente el root del skeleton)
        for model in scene.RootModel.Children:
            if len(model.Children) > 5:  # Tiene muchos hijos, probablemente es el skeleton
                armature = model
                break
    
    if armature:
        print(f"   📍 Armature encontrado: {armature.Name}")
        character = FBCharacter("Remy_Ajustado")
        scene.Characters.append(character)
        return character
    
    print("   ❌ No se pudo encontrar ni crear character")
    return None

def listar_huesos_manos(character):
    """Lista los huesos de las manos"""
    print("\n🦴 Listando huesos de manos...")
    
    scene = FBSystem().Scene
    hand_bones = []
    
    # Buscar en todos los modelos
    for model in scene.RootModel.Children:
        for child in model.Children:
            if buscar_huesos_manos_recursivo(child, hand_bones):
                pass
    
    print(f"\n📊 Total huesos de manos encontrados: {len(hand_bones)}")
    for bone in hand_bones:
        print(f"   - {bone.Name}")
    
    return hand_bones

def buscar_huesos_manos_recursivo(model, hand_bones):
    """Busca huesos de manos recursivamente"""
    keywords = ['hand', 'finger', 'thumb', 'index', 'middle', 'ring', 'pinky']
    
    if isinstance(model, FBModelSkeleton):
        if any(keyword in model.Name.lower() for keyword in keywords):
            if model not in hand_bones:
                hand_bones.append(model)
    
    # Recursión en hijos
    for child in model.Children:
        buscar_huesos_manos_recursivo(child, hand_bones)
    
    return len(hand_bones) > 0

def ajustar_timeline():
    """Ajusta el timeline según el video"""
    print(f"\n⏱️ Ajustando timeline...")
    
    # Configurar FPS
    FBPlayerControl().SetTransportFps(FBTimeMode.kFBTimeMode30Frames)
    
    # Calcular frames totales
    total_frames = int(VIDEO_DURACION * VIDEO_FPS)
    
    # Configurar rango de reproducción
    time_span = FBTimeSpan()
    time_span.Set(FBTime(0, 0, 0, 0), FBTime(0, 0, 0, total_frames))
    FBSystem().CurrentTake.LocalTimeSpan = time_span
    
    print(f"   ✅ FPS: {VIDEO_FPS}")
    print(f"   ✅ Duración: {VIDEO_DURACION}s")
    print(f"   ✅ Total frames: {total_frames}")
    
    return total_frames

def cargar_referencias_frames():
    """Carga la información de los frames extraídos"""
    print(f"\n📊 Cargando referencias de frames...")
    
    if not FRAMES_INFO.exists():
        print(f"   ⚠️ No se encontró: {FRAMES_INFO}")
        return None
    
    with open(FRAMES_INFO, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"   ✅ Frames de referencia: {data['total_frames']}")
    print(f"   ✅ FPS video: {data['fps']}")
    print(f"   ✅ Duración: {data['duracion']}s")
    
    return data

def crear_story_con_referencias(frames_data):
    """Crea un Story con las imágenes de referencia"""
    print(f"\n🎬 Configurando Story para referencias visuales...")
    
    # El Story en MotionBuilder permite ver imágenes de referencia
    # mientras editas la animación
    
    print("   💡 Para ver las referencias:")
    print("   1. Ve a la pestaña 'Story' en MotionBuilder")
    print("   2. Arrastra las imágenes de output/frames_r/ al Story")
    print("   3. Coloca cada imagen en el frame correspondiente")
    print("   4. Usa las imágenes como guía visual para ajustar las manos")
    
    return True

def guardar_fbx_ajustado():
    """Guarda el FBX ajustado"""
    print(f"\n💾 Guardando FBX ajustado...")
    
    # Crear directorio de salida
    FBX_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    
    # Guardar
    FBApplication().FileSave(str(FBX_OUTPUT))
    
    print(f"✅ FBX guardado: {FBX_OUTPUT}")
    
    # Verificar tamaño
    if FBX_OUTPUT.exists():
        tamaño_mb = FBX_OUTPUT.stat().st_size / (1024 * 1024)
        print(f"📊 Tamaño: {tamaño_mb:.2f} MB")
    
    return FBX_OUTPUT

def main():
    print("=" * 70)
    print("🔧 AJUSTE DE ANIMACIÓN DE MANOS - MOTIONBUILDER")
    print("=" * 70)
    
    # 1. Limpiar escena
    limpiar_escena()
    
    # 2. Cargar FBX
    if not cargar_fbx():
        return
    
    # 3. Encontrar character
    character = encontrar_character()
    
    # 4. Listar huesos de manos
    hand_bones = listar_huesos_manos(character)
    
    # 5. Ajustar timeline
    total_frames = ajustar_timeline()
    
    # 6. Cargar referencias
    frames_data = cargar_referencias_frames()
    
    # 7. Configurar Story
    crear_story_con_referencias(frames_data)
    
    print("\n" + "=" * 70)
    print("✅ CONFIGURACIÓN COMPLETADA")
    print("=" * 70)
    print("\n📋 SIGUIENTE PASO - AJUSTE MANUAL:")
    print("   1. Ve a Story window (Window > Story)")
    print("   2. Arrastra imágenes de output/frames_r/ al Story")
    print("   3. Coloca cada imagen en su timestamp correspondiente")
    print("   4. Usa modo 'Key Controls' (K) para crear keyframes")
    print("   5. Selecciona los huesos de las manos y ajusta según la referencia")
    print("   6. Cuando termines, ejecuta: guardar_fbx_ajustado()")
    print(f"\n💾 El archivo se guardará en: {FBX_OUTPUT}")
    print("\n💡 TIP: Usa 'Auto Key' (A) para crear keyframes automáticamente")
    print("         mientras mueves los huesos de las manos")

if __name__ == "__main__":
    main()
