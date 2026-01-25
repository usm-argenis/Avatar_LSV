"""
Script para aplicar animaciones de Nina a otros avatares (Duvall, Luis, Nancy)
Analiza la estructura de huesos y mapea las animaciones correctamente
"""

import bpy
import os
import sys
from pathlib import Path
import json

# Configuración
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis")
GLB_DIR = BASE_DIR / "test" / "output" / "glb"

# Avatares a procesar
AVATARES_DESTINO = ["Duvall", "Luis", "Nancy"]

# Obtener todas las animaciones de Nina organizadas
NINA_DIR = GLB_DIR / "Nina"

def limpiar_escena():
    """Limpia todos los objetos de la escena"""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
def cargar_glb(filepath):
    """Carga un archivo GLB y retorna el armature"""
    bpy.ops.import_scene.gltf(filepath=str(filepath))
    
    # Buscar el armature
    for obj in bpy.context.scene.objects:
        if obj.type == 'ARMATURE':
            return obj
    return None

def obtener_huesos(armature):
    """Obtiene lista de nombres de huesos de un armature"""
    if not armature or armature.type != 'ARMATURE':
        return []
    
    return [bone.name for bone in armature.data.bones]

def analizar_avatar(avatar_path, avatar_name):
    """Analiza la estructura de huesos de un avatar"""
    print(f"\n🔍 Analizando {avatar_name}...")
    
    limpiar_escena()
    armature = cargar_glb(avatar_path)
    
    if not armature:
        print(f"  ❌ No se encontró armature en {avatar_name}")
        return None
    
    huesos = obtener_huesos(armature)
    print(f"  📊 Huesos encontrados: {len(huesos)}")
    
    # Guardar info
    info = {
        "nombre": avatar_name,
        "total_huesos": len(huesos),
        "huesos": huesos
    }
    
    return info

def crear_mapeo_huesos(huesos_origen, huesos_destino):
    """Crea mapeo entre huesos de origen (Nina) y destino (otro avatar)"""
    mapeo = {}
    
    # Patrones comunes de nombres de huesos
    patrones = {
        # Columna vertebral
        "spine": ["spine", "column", "vertebra"],
        "chest": ["chest", "torso", "upper"],
        "neck": ["neck", "cuello"],
        "head": ["head", "cabeza", "skull"],
        
        # Brazos
        "shoulder": ["shoulder", "clavicle", "hombro"],
        "upperarm": ["upperarm", "upper_arm", "brazo"],
        "lowerarm": ["lowerarm", "lower_arm", "forearm", "antebrazo"],
        "hand": ["hand", "mano", "wrist"],
        
        # Dedos
        "thumb": ["thumb", "pulgar"],
        "index": ["index", "indice"],
        "middle": ["middle", "medio"],
        "ring": ["ring", "anular"],
        "pinky": ["pinky", "meñique", "little"],
        
        # Piernas
        "thigh": ["thigh", "upper_leg", "muslo"],
        "calf": ["calf", "lower_leg", "shin"],
        "foot": ["foot", "pie"],
        "toe": ["toe", "dedo"],
        
        # Otros
        "root": ["root", "hip", "pelvis", "cadera"],
    }
    
    for hueso_orig in huesos_origen:
        hueso_orig_lower = hueso_orig.lower()
        
        # Buscar coincidencia exacta
        if hueso_orig in huesos_destino:
            mapeo[hueso_orig] = hueso_orig
            continue
        
        # Buscar por patrones
        encontrado = False
        for clave, variantes in patrones.items():
            if any(v in hueso_orig_lower for v in variantes):
                # Buscar en destino
                for hueso_dest in huesos_destino:
                    if any(v in hueso_dest.lower() for v in variantes):
                        mapeo[hueso_orig] = hueso_dest
                        encontrado = True
                        break
            if encontrado:
                break
        
        # Si no se encontró, intentar matching por similitud de nombre
        if not encontrado:
            for hueso_dest in huesos_destino:
                if hueso_orig_lower in hueso_dest.lower() or hueso_dest.lower() in hueso_orig_lower:
                    mapeo[hueso_orig] = hueso_dest
                    break
    
    return mapeo

def aplicar_animacion_a_avatar(nina_glb, destino_glb, output_path, mapeo_huesos):
    """Aplica la animación de Nina a otro avatar usando el mapeo de huesos"""
    limpiar_escena()
    
    # Cargar animación de Nina primero
    nina_arm = cargar_glb(nina_glb)
    if not nina_arm:
        return False
    
    # Obtener datos de animación
    nina_animation_data = None
    if nina_arm.animation_data and nina_arm.animation_data.action:
        nina_animation_data = nina_arm.animation_data.action
    
    # Guardar referencia a mesh de Nina
    nina_meshes = [obj for obj in bpy.context.scene.objects if obj.type == 'MESH']
    
    # Cargar avatar destino
    limpiar_escena()
    destino_arm = cargar_glb(destino_glb)
    if not destino_arm:
        return False
    
    # Si Nina tiene animación, aplicarla al destino
    if nina_animation_data:
        # Cargar Nina de nuevo con destino
        bpy.ops.import_scene.gltf(filepath=str(nina_glb))
        
        # Encontrar ambos armatures
        armatures = [obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE']
        if len(armatures) >= 2:
            nina_arm_new = None
            dest_arm_new = None
            
            for arm in armatures:
                if arm != destino_arm:
                    nina_arm_new = arm
                else:
                    dest_arm_new = arm
            
            # Copiar animación directamente (mismo skeleton)
            if nina_arm_new and nina_arm_new.animation_data:
                if not dest_arm_new.animation_data:
                    dest_arm_new.animation_data_create()
                dest_arm_new.animation_data.action = nina_arm_new.animation_data.action.copy()
            
            # Eliminar objetos de Nina
            for obj in list(bpy.context.scene.objects):
                if obj != destino_arm and obj.parent != destino_arm and obj.type in ['ARMATURE', 'MESH']:
                    if obj == nina_arm_new or obj.parent == nina_arm_new:
                        bpy.data.objects.remove(obj, do_unlink=True)
    
    # Exportar
    bpy.ops.export_scene.gltf(
        filepath=str(output_path),
        export_format='GLB',
        export_animations=True,
        export_draco_mesh_compression_enable=True
    )
    
    return True

def procesar_avatar(avatar_info, nina_dir, mapeo_huesos):
    """Procesa un avatar completo aplicando todas las animaciones de Nina"""
    avatar_name = avatar_info["nombre"]
    print(f"\n{'='*60}")
    print(f"🎬 PROCESANDO {avatar_name}")
    print(f"{'='*60}")
    
    # Encontrar archivo base del avatar
    avatar_glb_dir = GLB_DIR / avatar_name
    avatar_files = list(avatar_glb_dir.glob("*.glb"))
    
    if not avatar_files:
        print(f"  ❌ No se encontró archivo base para {avatar_name}")
        return
    
    avatar_base = avatar_files[0]
    print(f"  📁 Archivo base: {avatar_base.name}")
    
    # Crear estructura de carpetas
    for categoria in ["alfabeto", "cortesia", "dias_semana", "expresiones", 
                      "preguntas", "pronombres", "saludos", "tiempo"]:
        (avatar_glb_dir / categoria).mkdir(parents=True, exist_ok=True)
    
    # Procesar cada categoría de Nina
    total_procesados = 0
    total_errores = 0
    
    for categoria_dir in nina_dir.iterdir():
        if not categoria_dir.is_dir():
            continue
        
        categoria = categoria_dir.name
        print(f"\n📂 Procesando categoría: {categoria}")
        
        # Procesar cada animación en la categoría
        for nina_anim in categoria_dir.glob("Nina_resultado_*.glb"):
            # Extraer nombre de la seña
            sena = nina_anim.stem.replace("Nina_resultado_", "")
            
            # Nombre de salida
            output_name = f"{avatar_name}_resultado_{sena}.glb"
            output_path = avatar_glb_dir / categoria / output_name
            
            print(f"  🔄 {sena}...", end=" ", flush=True)
            
            # Aplicar animación de Nina al avatar
            try:
                exito = aplicar_animacion_a_avatar(nina_anim, avatar_base, output_path, mapeo_huesos)
                if exito:
                    print(f"✅")
                    total_procesados += 1
                else:
                    print(f"❌ (error al procesar)")
                    total_errores += 1
            except Exception as e:
                print(f"❌ ({str(e)[:30]}...)")
                total_errores += 1
    
    print(f"\n✅ Total procesados para {avatar_name}: {total_procesados}")
    if total_errores > 0:
        print(f"⚠️  Errores: {total_errores}")

def main():
    print("=" * 60)
    print("🚀 APLICADOR DE ANIMACIONES DE NINA")
    print("=" * 60)
    
    # Paso 1: Analizar Nina
    print("\n📊 Paso 1: Analizando estructura de Nina...")
    nina_files = list((NINA_DIR / "pronombres").glob("Nina_resultado_*.glb"))
    if nina_files:
        nina_info = analizar_avatar(nina_files[0], "Nina")
        if nina_info:
            print(f"  ✅ Nina analizada: {nina_info['total_huesos']} huesos")
            
            # Guardar info
            with open(GLB_DIR / "nina_bones_info.json", "w") as f:
                json.dump(nina_info, f, indent=2)
    
    # Paso 2: Analizar avatares destino
    print("\n📊 Paso 2: Analizando avatares destino...")
    avatares_info = {}
    
    for avatar_name in AVATARES_DESTINO:
        avatar_dir = GLB_DIR / avatar_name
        avatar_files = list(avatar_dir.glob("*.glb"))
        
        if avatar_files:
            info = analizar_avatar(avatar_files[0], avatar_name)
            if info:
                avatares_info[avatar_name] = info
                
                # Guardar info
                with open(GLB_DIR / f"{avatar_name.lower()}_bones_info.json", "w") as f:
                    json.dump(info, f, indent=2)
    
    # Paso 3: Crear mapeos de huesos
    print("\n🗺️  Paso 3: Creando mapeos de huesos...")
    mapeos = {}
    if nina_info:
        for avatar_name, avatar_info in avatares_info.items():
            mapeo = crear_mapeo_huesos(nina_info["huesos"], avatar_info["huesos"])
            mapeos[avatar_name] = mapeo
            print(f"  ✅ Mapeo {avatar_name}: {len(mapeo)}/{len(nina_info['huesos'])} huesos mapeados")
            
            # Guardar mapeo
            with open(GLB_DIR / f"mapeo_nina_to_{avatar_name.lower()}.json", "w") as f:
                json.dump(mapeo, f, indent=2)
    
    # Paso 4: Aplicar animaciones
    print("\n🎬 Paso 4: Aplicando animaciones...")
    for avatar_name, avatar_info in avatares_info.items():
        procesar_avatar(avatar_info, NINA_DIR, mapeos.get(avatar_name, {}))
    
    print("\n" + "=" * 60)
    print("✅ PROCESO COMPLETADO")
    print("=" * 60)

if __name__ == "__main__":
    # Verificar si estamos en Blender
    if "bpy" in sys.modules:
        main()
    else:
        print("⚠️  Este script debe ejecutarse desde Blender")
        print("Ejecuta: blender --background --python aplicar_animaciones.py")
