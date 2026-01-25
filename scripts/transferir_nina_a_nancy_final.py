import bpy
import sys
from pathlib import Path

print("\n" + "="*80)
print("TRANSFERENCIA DE ANIMACIONES NINA → NANCY")
print("="*80)

# Rutas
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NINA_DIR = BASE_DIR / "Nina"
NANCY_DIR = BASE_DIR / "Nancy"
NANCY_MODEL = NANCY_DIR / "$RMPX0RX_default.glb"

# Categorías a procesar (SIN alfabeto)
CATEGORIAS = ['saludos', 'pronombres', 'dias_semana', 'tiempo', 'cortesia', 'preguntas', 'expresiones']

print(f"✅ Modelo base Nancy: {NANCY_MODEL}")
print(f"📂 Procesando categorías: {', '.join(CATEGORIAS)}")
print()

total_exitosos = 0
total_fallidos = 0

for categoria in CATEGORIAS:
    print(f"\n{'='*80}")
    print(f"📁 CATEGORÍA: {categoria.upper()}")
    print(f"{'='*80}")
    
    nina_cat_dir = NINA_DIR / categoria
    nancy_cat_dir = NANCY_DIR / categoria
    
    if not nina_cat_dir.exists():
        print(f"⚠️ No existe carpeta de Nina: {nina_cat_dir}")
        continue
    
    if not nancy_cat_dir.exists():
        print(f"⚠️ No existe carpeta de Nancy: {nancy_cat_dir}")
        continue
    
    # Obtener archivos de Nina
    nina_files = list(nina_cat_dir.glob("Nina_resultado_*.glb"))
    
    if not nina_files:
        print(f"⚠️ No hay archivos en {nina_cat_dir}")
        continue
    
    print(f"📊 Encontrados {len(nina_files)} archivos de Nina")
    
    for nina_file in nina_files:
        # Extraer nombre de la seña
        sena = nina_file.stem.replace("Nina_resultado_", "")
        nancy_file = nancy_cat_dir / f"Nancy_resultado_{sena}.glb"
        
        print(f"\n  🔄 Procesando: {sena}")
        print(f"     Nina:  {nina_file.name}")
        print(f"     Nancy: {nancy_file.name}")
        
        try:
            # PASO 1: Limpiar escena completamente
            bpy.ops.wm.read_factory_settings(use_empty=True)
            
            # PASO 2: Cargar SOLO modelo base Nancy (para tener su malla)
            print(f"     📦 Cargando modelo base Nancy...")
            bpy.ops.import_scene.gltf(filepath=str(NANCY_MODEL))
            
            nancy_armature = None
            nancy_meshes = []
            
            for obj in bpy.data.objects:
                if obj.type == 'ARMATURE':
                    nancy_armature = obj
                elif obj.type == 'MESH':
                    nancy_meshes.append(obj)
            
            if not nancy_armature:
                print(f"     ❌ No se encontró armature de Nancy")
                total_fallidos += 1
                continue
            
            print(f"     ✅ Nancy: {len(nancy_meshes)} mallas, armature: {nancy_armature.name}")
            
            # Eliminar animación por defecto de Nancy si existe
            if nancy_armature.animation_data:
                nancy_armature.animation_data_clear()
                print(f"     🗑️ Animación por defecto eliminada")
            
            # PASO 3: Cargar animación de Nina
            print(f"     🎬 Importando animación de Nina...")
            objetos_antes = set(bpy.data.objects)
            bpy.ops.import_scene.gltf(filepath=str(nina_file))
            objetos_nina = set(bpy.data.objects) - objetos_antes
            
            nina_armature = None
            for obj in objetos_nina:
                if obj.type == 'ARMATURE':
                    nina_armature = obj
                    break
            
            if not nina_armature:
                print(f"     ❌ No se encontró armature de Nina")
                total_fallidos += 1
                continue
            
            # PASO 4: Verificar animación de Nina
            if not nina_armature.animation_data or not nina_armature.animation_data.action:
                print(f"     ❌ No hay animación en Nina")
                total_fallidos += 1
                continue
            
            nina_action = nina_armature.animation_data.action
            frame_start = nina_action.frame_range[0]
            frame_end = nina_action.frame_range[1]
            frames_total = frame_end - frame_start
            
            print(f"     📊 Animación Nina: {frames_total:.0f} frames ({frame_start:.0f} a {frame_end:.0f})")
            
            # PASO 5: Verificar que los huesos coincidan
            print(f"     🦴 Verificando huesos...")
            bones_nancy = set(nancy_armature.data.bones.keys())
            bones_nina = set(nina_armature.data.bones.keys())
            bones_comunes = bones_nancy & bones_nina
            
            if len(bones_comunes) < 50:
                print(f"     ❌ Muy pocos huesos comunes: {len(bones_comunes)}")
                total_fallidos += 1
                continue
            
            print(f"     ✅ Huesos comunes: {len(bones_comunes)}")
            
            # PASO 6: Crear animation data en Nancy
            if not nancy_armature.animation_data:
                nancy_armature.animation_data_create()
            
            # PASO 7: Copiar action COMPLETA de Nina a Nancy
            print(f"     📋 Copiando animación...")
            
            # Copiar la action completa
            nancy_action = nina_action.copy()
            nancy_action.name = f"Nancy_{sena}"
            nancy_armature.animation_data.action = nancy_action
            
            # Establecer frame range de la escena
            bpy.context.scene.frame_start = int(frame_start)
            bpy.context.scene.frame_end = int(frame_end)
            
            print(f"     ✅ Action copiada: {nancy_action.name}")
            print(f"     📊 FCurves: {len(nancy_action.fcurves)}")
            
            # PASO 8: Eliminar TODOS los objetos de Nina
            print(f"     🗑️ Eliminando objetos de Nina...")
            for obj in objetos_nina:
                bpy.data.objects.remove(obj, do_unlink=True)
            
            # PASO 9: Verificar que solo queden objetos de Nancy
            objetos_finales = list(bpy.data.objects)
            print(f"     ✅ Objetos restantes: {len(objetos_finales)}")
            
            # PASO 10: Exportar
            print(f"     💾 Exportando a GLB...")
            bpy.ops.export_scene.gltf(
                filepath=str(nancy_file),
                export_format='GLB',
                export_animations=True,
                export_frame_range=True,
                export_current_frame=False,
                export_force_sampling=True,
                export_def_bones=False,
                export_optimize_animation_size=False,  # NO optimizar para mantener exactitud
                export_nla_strips=False,
                export_apply=True
            )
            
            if nancy_file.exists():
                size_mb = nancy_file.stat().st_size / (1024 * 1024)
                print(f"     ✅ ÉXITO ({size_mb:.1f} MB)")
                total_exitosos += 1
            else:
                print(f"     ❌ No se generó archivo")
                total_fallidos += 1
                
        except Exception as e:
            print(f"     ❌ ERROR: {str(e)}")
            import traceback
            traceback.print_exc()
            total_fallidos += 1

# Resumen final
print("\n" + "="*80)
print("RESUMEN FINAL")
print("="*80)
print(f"✅ Exitosos: {total_exitosos}")
print(f"❌ Fallidos: {total_fallidos}")
print("="*80)
