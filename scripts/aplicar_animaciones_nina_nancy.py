import bpy
import os
import sys
from pathlib import Path

# Rutas
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NINA_DIR = BASE_DIR / "Nina"
NANCY_DIR = BASE_DIR / "Nancy"
# Usar el modelo que está en la carpeta Nancy
NANCY_MODEL = NANCY_DIR / "$RMPX0RX_default.glb"

# Categorías a procesar (SIN alfabeto)
CATEGORIAS = ['saludos', 'pronombres', 'dias_semana', 'tiempo', 'cortesia', 'preguntas', 'expresiones']

print("="*80)
print("APLICAR ANIMACIONES DE NINA A NANCY (SIN ALFABETO)")
print("="*80)

# Verificar modelo base
if not NANCY_MODEL.exists():
    print(f"❌ ERROR: No se encuentra Nancy.glb en: {NANCY_MODEL}")
    sys.exit(1)

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
            # Limpiar escena
            bpy.ops.wm.read_factory_settings(use_empty=True)
            
            # 1. Cargar archivo Nancy EXISTENTE (con su malla)
            print(f"     Cargando Nancy existente...")
            bpy.ops.import_scene.gltf(filepath=str(nancy_file))
            
            nancy_armature = None
            for obj in bpy.data.objects:
                if obj.type == 'ARMATURE':
                    nancy_armature = obj
                    break
            
            if not nancy_armature:
                print(f"     ❌ No se encontró armature de Nancy")
                total_fallidos += 1
                continue
            
            # 2. Importar Nina SOLO para extraer animación
            print(f"     Extrayendo animación de Nina...")
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
            
            # 3. Verificar animación de Nina
            if not nina_armature.animation_data or not nina_armature.animation_data.action:
                print(f"     ❌ No hay animación en Nina")
                total_fallidos += 1
                continue
            
            nina_action = nina_armature.animation_data.action
            frames = nina_action.frame_range[1] - nina_action.frame_range[0]
            print(f"     🎬 Animación Nina: {frames:.0f} frames")
            
            # 4. BORRAR animación vieja de Nancy si existe
            if nancy_armature.animation_data:
                nancy_armature.animation_data_clear()
            
            # 5. Crear nueva acción para Nancy
            nancy_armature.animation_data_create()
            nancy_action = bpy.data.actions.new(name=f"Nancy_{sena}")
            nancy_armature.animation_data.action = nancy_action
            
            # Establecer el rango de frames igual que Nina
            frame_start = nina_action.frame_range[0]
            frame_end = nina_action.frame_range[1]
            
            # 6. Copiar DIRECTAMENTE keyframes de Nina a Nancy
            print(f"     📋 Copiando keyframes...")
            keyframes_copiados = 0
            
            for fcurve in nina_action.fcurves:
                # Extraer nombre del hueso del data_path
                # Ejemplo: pose.bones["Spine1"].rotation_quaternion
                if "pose.bones[" in fcurve.data_path:
                    # Los huesos tienen nombres idénticos entre Nina y Nancy
                    # Copiar directamente el data_path
                    new_fcurve = nancy_action.fcurves.new(
                        data_path=fcurve.data_path,
                        index=fcurve.array_index
                    )
                    
                    # Copiar todos los keyframes
                    for keyframe in fcurve.keyframe_points:
                        new_fcurve.keyframe_points.insert(
                            keyframe.co[0],
                            keyframe.co[1],
                            options={'FAST'}
                        )
                        keyframes_copiados += 1
            
            print(f"     ✅ {keyframes_copiados} keyframes copiados")
            
            # Actualizar rango de frames de la acción
            nancy_action.frame_range = (frame_start, frame_end)
            
            # 7. Eliminar TODOS los objetos de Nina
            for obj in objetos_nina:
                bpy.data.objects.remove(obj, do_unlink=True)
            
            # 8. Exportar Nancy con nueva animación
            print(f"     💾 Exportando...")
            
            # Establecer frame range de la escena para exportar
            bpy.context.scene.frame_start = int(frame_start)
            bpy.context.scene.frame_end = int(frame_end)
            
            bpy.ops.export_scene.gltf(
                filepath=str(nancy_file),
                export_format='GLB',
                export_animations=True,
                export_frame_range=True,
                export_current_frame=False,
                export_force_sampling=True,
                export_def_bones=False,
                export_optimize_animation_size=True,
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
            total_fallidos += 1

# Resumen final
print("\n" + "="*80)
print("RESUMEN FINAL")
print("="*80)
print(f"✅ Exitosos: {total_exitosos}")
print(f"❌ Fallidos: {total_fallidos}")
print("="*80)
