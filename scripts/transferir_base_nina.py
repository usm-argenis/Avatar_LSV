import bpy
import sys
from pathlib import Path

print("\n" + "="*80)
print("TRANSFERENCIA DE ANIMACIONES - MODELO BASE: NINA")
print("="*80)

# Rutas
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NINA_DIR = BASE_DIR / "Nina"
NINA_MODEL = NINA_DIR / "$RMPX0RX_default.glb"

# Avatar de destino (modificar según necesidad)
AVATAR_DESTINO = "Nancy"  # Cambiar a: Nancy, Remy, etc.
DESTINO_DIR = BASE_DIR / AVATAR_DESTINO

# Categorías a procesar (SIN alfabeto)
CATEGORIAS = ['saludos', 'pronombres', 'dias_semana', 'tiempo', 'cortesia', 'preguntas', 'expresiones']

print(f"✅ Modelo base Nina: {NINA_MODEL}")
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
    
    nina_cat_dir = NINA_DIR / categoria
    destino_cat_dir = DESTINO_DIR / categoria
    
    if not nina_cat_dir.exists():
        print(f"⚠️ No existe carpeta de Nina: {nina_cat_dir}")
        continue
    
    if not destino_cat_dir.exists():
        print(f"⚠️ No existe carpeta de {AVATAR_DESTINO}: {destino_cat_dir}")
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
        destino_file = destino_cat_dir / f"{AVATAR_DESTINO}_resultado_{sena}.glb"
        
        print(f"\n  🔄 Procesando: {sena}")
        print(f"     Nina (animación): {nina_file.name}")
        print(f"     {AVATAR_DESTINO} (destino):   {destino_file.name}")
        
        try:
            # PASO 1: Limpiar escena completamente
            bpy.ops.wm.read_factory_settings(use_empty=True)
            
            # PASO 2: Cargar SOLO modelo base Nina (para tener su malla y textura)
            print(f"     📦 Cargando modelo base Nina...")
            bpy.ops.import_scene.gltf(filepath=str(NINA_MODEL))
            
            nina_base_armature = None
            nina_base_meshes = []
            
            for obj in bpy.data.objects:
                if obj.type == 'ARMATURE':
                    nina_base_armature = obj
                elif obj.type == 'MESH':
                    nina_base_meshes.append(obj)
            
            if not nina_base_armature:
                print(f"     ❌ No se encontró armature de Nina base")
                total_fallidos += 1
                continue
            
            print(f"     ✅ Nina base: {len(nina_base_meshes)} mallas, armature: {nina_base_armature.name}")
            
            # Eliminar animación por defecto de Nina si existe
            if nina_base_armature.animation_data:
                nina_base_armature.animation_data_clear()
                print(f"     🗑️ Animación por defecto eliminada")
            
            # PASO 3: Cargar animación de Nina
            print(f"     🎬 Importando animación de Nina...")
            objetos_antes = set(bpy.data.objects)
            bpy.ops.import_scene.gltf(filepath=str(nina_file))
            objetos_nina_anim = set(bpy.data.objects) - objetos_antes
            
            nina_anim_armature = None
            for obj in objetos_nina_anim:
                if obj.type == 'ARMATURE':
                    nina_anim_armature = obj
                    break
            
            if not nina_anim_armature:
                print(f"     ❌ No se encontró armature de Nina con animación")
                total_fallidos += 1
                continue
            
            # PASO 4: Verificar animación de Nina
            if not nina_anim_armature.animation_data or not nina_anim_armature.animation_data.action:
                print(f"     ❌ No hay animación en Nina")
                total_fallidos += 1
                continue
            
            nina_action = nina_anim_armature.animation_data.action
            frame_start = nina_action.frame_range[0]
            frame_end = nina_action.frame_range[1]
            frames_total = frame_end - frame_start
            
            print(f"     📊 Animación Nina: {frames_total:.0f} frames ({frame_start:.0f} a {frame_end:.0f})")
            print(f"     📊 FCurves antes de filtrar: {len(nina_action.fcurves)}")
            
            # PASO 5: Verificar que los huesos coincidan
            print(f"     🦴 Verificando huesos...")
            bones_nina_base = set(nina_base_armature.data.bones.keys())
            bones_nina_anim = set(nina_anim_armature.data.bones.keys())
            bones_comunes = bones_nina_base & bones_nina_anim
            
            if len(bones_comunes) < 50:
                print(f"     ❌ Muy pocos huesos comunes: {len(bones_comunes)}")
                total_fallidos += 1
                continue
            
            print(f"     ✅ Huesos comunes: {len(bones_comunes)}")
            
            # PASO 6: Crear animation data en Nina base
            if not nina_base_armature.animation_data:
                nina_base_armature.animation_data_create()
            
            # PASO 7: Copiar action de Nina animación, ELIMINANDO PIERNAS
            print(f"     📋 Copiando animación (sin piernas)...")
            
            # Copiar la action completa
            nina_action_copy = nina_action.copy()
            nina_action_copy.name = f"{AVATAR_DESTINO}_{sena}"
            
            # ELIMINAR FCurves de piernas
            fcurves_a_eliminar = []
            for fc in nina_action_copy.fcurves:
                for hueso_pierna in HUESOS_PIERNAS:
                    if f'pose.bones["{hueso_pierna}"]' in fc.data_path:
                        fcurves_a_eliminar.append(fc)
                        break
            
            for fc in fcurves_a_eliminar:
                nina_action_copy.fcurves.remove(fc)
            
            print(f"     🗑️ Eliminadas {len(fcurves_a_eliminar)} FCurves de piernas")
            print(f"     📊 FCurves después de filtrar: {len(nina_action_copy.fcurves)}")
            
            # Asignar action a Nina base
            nina_base_armature.animation_data.action = nina_action_copy
            
            # Establecer frame range de la escena
            bpy.context.scene.frame_start = int(frame_start)
            bpy.context.scene.frame_end = int(frame_end)
            
            print(f"     ✅ Action copiada: {nina_action_copy.name}")
            
            # PASO 8: Eliminar TODOS los objetos de Nina con animación
            print(f"     🗑️ Eliminando objetos de Nina animación...")
            for obj in objetos_nina_anim:
                bpy.data.objects.remove(obj, do_unlink=True)
            
            # PASO 9: Verificar que solo queden objetos de Nina base
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
