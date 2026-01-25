import bpy
import os
import sys
from pathlib import Path

# Rutas
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis")
ANIMATIONS_DIR = BASE_DIR / "animations_library" / "alphabet"
NANCY_MODEL = BASE_DIR / "test" / "output" / "glb" / "Nancy.glb"
OUTPUT_DIR = BASE_DIR / "test" / "output" / "glb" / "Nancy" / "alfabeto"

# Crear carpeta de salida
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Alfabeto completo LSV
ALFABETO = ['a', 'b', 'c', 'ch', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'll', 
            'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 'rr', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("="*80)
print("APLICAR ANIMACIONES DE ALFABETO DE NINA A NANCY")
print("="*80)

# Verificar que existe el modelo de Nancy
if not NANCY_MODEL.exists():
    print(f"❌ ERROR: No se encuentra el modelo de Nancy en: {NANCY_MODEL}")
    sys.exit(1)

print(f"✅ Modelo de Nancy encontrado: {NANCY_MODEL}")
print(f"📁 Buscando animaciones en: {ANIMATIONS_DIR}")
print(f"💾 Salida: {OUTPUT_DIR}")
print()

# Contador de éxitos
exitosos = 0
fallidos = 0

for letra in ALFABETO:
    print(f"\n{'='*60}")
    print(f"Procesando letra: {letra.upper()}")
    print(f"{'='*60}")
    
    # Buscar el archivo FBX de animación de Nina para esta letra
    # Los archivos están como: b_deepmotion.fbx, c_deepmotion.fbx, etc.
    anim_file = ANIMATIONS_DIR / f"{letra}_deepmotion.fbx"
    
    if not anim_file.exists():
        # Intentar otros patrones
        alternativas = [
            ANIMATIONS_DIR / f"{letra}.fbx",
            ANIMATIONS_DIR / f"Nina_{letra}.fbx",
            ANIMATIONS_DIR / f"{letra}_Nina.fbx"
        ]
        
        encontrado = False
        for alt in alternativas:
            if alt.exists():
                anim_file = alt
                encontrado = True
                break
        
        if not encontrado:
            print(f"⚠️ No se encontró animación para '{letra}'")
            fallidos += 1
            continue
    
    print(f"📂 Animación encontrada: {anim_file.name}")
    
    try:
        # Limpiar escena
        bpy.ops.wm.read_factory_settings(use_empty=True)
        
        # 1. Importar modelo de Nancy
        print("   Importando modelo Nancy...")
        bpy.ops.import_scene.gltf(filepath=str(NANCY_MODEL))
        
        # Encontrar armature de Nancy
        nancy_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                nancy_armature = obj
                break
        
        if not nancy_armature:
            print(f"   ❌ ERROR: No se encontró armature en el modelo de Nancy")
            fallidos += 1
            continue
        
        print(f"   ✅ Armature de Nancy: {nancy_armature.name}")
        print(f"   🦴 Huesos: {len(nancy_armature.data.bones)}")
        
        # 2. Importar animación de Nina
        print(f"   Importando animación de Nina...")
        bpy.ops.import_scene.fbx(filepath=str(anim_file))
        
        # Encontrar armature de Nina
        nina_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE' and obj != nancy_armature:
                nina_armature = obj
                break
        
        if not nina_armature:
            print(f"   ❌ ERROR: No se encontró animación de Nina")
            fallidos += 1
            continue
        
        print(f"   ✅ Armature de Nina: {nina_armature.name}")
        
        # 3. Copiar animación de Nina a Nancy
        if nina_armature.animation_data and nina_armature.animation_data.action:
            nina_action = nina_armature.animation_data.action
            print(f"   🎬 Acción encontrada: {nina_action.name}")
            print(f"   ⏱️  Duración: {nina_action.frame_range[1] - nina_action.frame_range[0]} frames")
            
            # Crear una copia de la acción para Nancy
            nancy_action = nina_action.copy()
            nancy_action.name = f"Nancy_{letra}"
            
            # Asignar la acción a Nancy
            if not nancy_armature.animation_data:
                nancy_armature.animation_data_create()
            
            nancy_armature.animation_data.action = nancy_action
            
            # Eliminar el armature de Nina
            bpy.data.objects.remove(nina_armature, do_unlink=True)
            
            print(f"   ✅ Animación aplicada a Nancy")
        else:
            print(f"   ❌ ERROR: No se encontró acción de animación en Nina")
            fallidos += 1
            continue
        
        # 4. Exportar como GLB
        output_file = OUTPUT_DIR / f"Nancy_resultado_{letra}.glb"
        print(f"   💾 Exportando: {output_file.name}")
        
        bpy.ops.export_scene.gltf(
            filepath=str(output_file),
            export_format='GLB',
            export_animations=True,
            export_frame_range=True,
            export_force_sampling=True,
            export_def_bones=False,
            export_optimize_animation_size=True,
            export_nla_strips=False,
            export_apply=True
        )
        
        # Verificar que se creó el archivo
        if output_file.exists():
            size_mb = output_file.stat().st_size / (1024 * 1024)
            print(f"   ✅ ÉXITO: {output_file.name} ({size_mb:.1f} MB)")
            exitosos += 1
        else:
            print(f"   ❌ ERROR: No se generó el archivo")
            fallidos += 1
            
    except Exception as e:
        print(f"   ❌ ERROR: {str(e)}")
        fallidos += 1
        continue

# Resumen final
print("\n" + "="*80)
print("RESUMEN FINAL")
print("="*80)
print(f"✅ Exitosos: {exitosos}/{len(ALFABETO)}")
print(f"❌ Fallidos: {fallidos}/{len(ALFABETO)}")
print(f"📁 Archivos generados en: {OUTPUT_DIR}")
print("="*80)
