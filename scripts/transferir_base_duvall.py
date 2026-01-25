import bpy
import sys
from pathlib import Path

print("\n" + "="*80)
print("TRANSFERENCIA DE ANIMACIONES - MODELO BASE: DUVALL")
print("="*80)

# Rutas
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
DUVALL_DIR = BASE_DIR / "Duvall"
DUVALL_MODEL = DUVALL_DIR / "saludos" / "Duvall_resultado_hola_final.glb"  # Modelo corregido

# Avatar de destino (modificar según necesidad)
AVATAR_DESTINO = "Luis"  # Cambiar a: Luis, Carlos, etc.
DESTINO_DIR = BASE_DIR / AVATAR_DESTINO

# Categorías a procesar (SIN alfabeto)
CATEGORIAS = ['saludos', 'pronombres', 'dias_semana', 'tiempo', 'cortesia', 'preguntas', 'expresiones']

print(f"✅ Modelo base Duvall: {DUVALL_MODEL}")
print(f"🎯 Avatar destino: {AVATAR_DESTINO}")
print(f"📂 Procesando categorías: {', '.join(CATEGORIAS)}")
print()

# Huesos de piernas a eliminar
HUESOS_PIERNAS = [
    'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 'LeftToe_End',
    'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase', 'RightToe_End'
]

total_exitosos = 0
total_fallidos = 0

for categoria in CATEGORIAS:
    print(f"\n{'='*80}")
    print(f"📁 CATEGORÍA: {categoria.upper()}")
    print(f"{'='*80}")
    
    duvall_cat_dir = DUVALL_DIR / categoria
    destino_cat_dir = DESTINO_DIR / categoria
    
    if not duvall_cat_dir.exists():
        print(f"⚠️ No existe carpeta de Duvall: {duvall_cat_dir}")
        continue
    
    if not destino_cat_dir.exists():
        print(f"⚠️ No existe carpeta de {AVATAR_DESTINO}: {destino_cat_dir}")
        continue
    
    # Obtener archivos de Duvall
    duvall_files = list(duvall_cat_dir.glob("Duvall_resultado_*.glb"))
    
    if not duvall_files:
        print(f"⚠️ No hay archivos en {duvall_cat_dir}")
        continue
    
    print(f"📊 Encontrados {len(duvall_files)} archivos de Duvall")
    
    for duvall_file in duvall_files:
        # Extraer nombre de la seña
        sena = duvall_file.stem.replace("Duvall_resultado_", "")
        destino_file = destino_cat_dir / f"{AVATAR_DESTINO}_resultado_{sena}.glb"
        
        print(f"\n  🔄 Procesando: {sena}")
        print(f"     Duvall (animación): {duvall_file.name}")
        print(f"     {AVATAR_DESTINO} (destino):    {destino_file.name}")
        
        try:
            # PASO 1: Limpiar escena completamente
            bpy.ops.wm.read_factory_settings(use_empty=True)
            
            # PASO 2: Cargar SOLO modelo base Duvall (para tener su malla y textura)
            print(f"     📦 Cargando modelo base Duvall...")
            bpy.ops.import_scene.gltf(filepath=str(DUVALL_MODEL))
            
            duvall_base_armature = None
            duvall_base_meshes = []
            
            for obj in bpy.data.objects:
                if obj.type == 'ARMATURE':
                    duvall_base_armature = obj
                elif obj.type == 'MESH':
                    duvall_base_meshes.append(obj)
            
            if not duvall_base_armature:
                print(f"     ❌ No se encontró armature de Duvall base")
                total_fallidos += 1
                continue
            
            print(f"     ✅ Duvall base: {len(duvall_base_meshes)} mallas, armature: {duvall_base_armature.name}")
            
            # Eliminar animación por defecto de Duvall si existe
            if duvall_base_armature.animation_data:
                duvall_base_armature.animation_data_clear()
                print(f"     🗑️ Animación por defecto eliminada")
            
            # PASO 3: Cargar animación de Duvall
            print(f"     🎬 Importando animación de Duvall...")
            objetos_antes = set(bpy.data.objects)
            bpy.ops.import_scene.gltf(filepath=str(duvall_file))
            objetos_duvall_anim = set(bpy.data.objects) - objetos_antes
            
            duvall_anim_armature = None
            for obj in objetos_duvall_anim:
                if obj.type == 'ARMATURE':
                    duvall_anim_armature = obj
                    break
            
            if not duvall_anim_armature:
                print(f"     ❌ No se encontró armature de Duvall con animación")
                total_fallidos += 1
                continue
            
            # PASO 4: Verificar animación de Duvall
            if not duvall_anim_armature.animation_data or not duvall_anim_armature.animation_data.action:
                print(f"     ❌ No hay animación en Duvall")
                total_fallidos += 1
                continue
            
            duvall_action = duvall_anim_armature.animation_data.action
            frame_start = duvall_action.frame_range[0]
            frame_end = duvall_action.frame_range[1]
            frames_total = frame_end - frame_start
            
            print(f"     📊 Animación Duvall: {frames_total:.0f} frames ({frame_start:.0f} a {frame_end:.0f})")
            print(f"     📊 FCurves antes de filtrar: {len(duvall_action.fcurves)}")
            
            # PASO 5: Verificar que los huesos coincidan
            print(f"     🦴 Verificando huesos...")
            bones_duvall_base = set(duvall_base_armature.data.bones.keys())
            bones_duvall_anim = set(duvall_anim_armature.data.bones.keys())
            bones_comunes = bones_duvall_base & bones_duvall_anim
            
            if len(bones_comunes) < 50:
                print(f"     ❌ Muy pocos huesos comunes: {len(bones_comunes)}")
                total_fallidos += 1
                continue
            
            print(f"     ✅ Huesos comunes: {len(bones_comunes)}")
            
            # PASO 6: Crear animation data en Duvall base
            if not duvall_base_armature.animation_data:
                duvall_base_armature.animation_data_create()
            
            # PASO 7: Copiar action de Duvall animación, ELIMINANDO PIERNAS
            print(f"     📋 Copiando animación (sin piernas)...")
            
            # Copiar la action completa
            duvall_action_copy = duvall_action.copy()
            duvall_action_copy.name = f"{AVATAR_DESTINO}_{sena}"
            
            # ELIMINAR FCurves de piernas
            fcurves_a_eliminar = []
            for fc in duvall_action_copy.fcurves:
                for hueso_pierna in HUESOS_PIERNAS:
                    if f'pose.bones["{hueso_pierna}"]' in fc.data_path:
                        fcurves_a_eliminar.append(fc)
                        break
            
            for fc in fcurves_a_eliminar:
                duvall_action_copy.fcurves.remove(fc)
            
            print(f"     🗑️ Eliminadas {len(fcurves_a_eliminar)} FCurves de piernas")
            print(f"     📊 FCurves después de filtrar: {len(duvall_action_copy.fcurves)}")
            
            # Asignar action a Duvall base
            duvall_base_armature.animation_data.action = duvall_action_copy
            
            # Establecer frame range de la escena
            bpy.context.scene.frame_start = int(frame_start)
            bpy.context.scene.frame_end = int(frame_end)
            
            print(f"     ✅ Action copiada: {duvall_action_copy.name}")
            
            # PASO 8: Eliminar TODOS los objetos de Duvall con animación
            print(f"     🗑️ Eliminando objetos de Duvall animación...")
            for obj in objetos_duvall_anim:
                bpy.data.objects.remove(obj, do_unlink=True)
            
            # PASO 9: Verificar que solo queden objetos de Duvall base
            objetos_finales = list(bpy.data.objects)
            print(f"     ✅ Objetos restantes: {len(objetos_finales)}")
            
            # PASO 10: Verificar texturas
            texturas = len(bpy.data.images)
            materiales = len(bpy.data.materials)
            print(f"     🎨 Texturas: {texturas}, Materiales: {materiales}")
            
            # PASO 11: Exportar
            print(f"     💾 Exportando a GLB...")
            bpy.ops.export_scene.gltf(
                filepath=str(destino_file),
                export_format='GLB',
                export_animations=True,
                export_frame_range=True,
                export_current_frame=False,
                export_force_sampling=True,
                export_def_bones=False,
                export_optimize_animation_size=False,  # NO optimizar para mantener exactitud
                export_nla_strips=False,
                export_apply=True,
                export_textures=True,  # Mantener texturas
                export_materials='EXPORT'  # Exportar materiales
            )
            
            if destino_file.exists():
                size_mb = destino_file.stat().st_size / (1024 * 1024)
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
