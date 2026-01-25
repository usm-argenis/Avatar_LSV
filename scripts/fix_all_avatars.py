"""
Script FINAL para regenerar archivos de Nancy, Luis y Duvall con:
- Animaciones de Nina transferidas con constraints + bake
- Texturas preservadas del modelo base
- Sin animación de piernas (90 FCurves eliminados)
"""

import bpy
from pathlib import Path

# Configuración
base_dir = Path(r"C:\Users\andre\OneDrive\Documentos\tesis")
carpeta_entrada = base_dir / "test/output/glb/Nina"

# Configuración para cada avatar
avatares = [
    # Nancy ya procesado, comentado
    # {
    #     'nombre': 'Nancy',
    #     'base': base_dir / "test/output/glb/Nancy/Nancy.glb",
    #     'salida': base_dir / "test/output/glb/Nancy"
    # },
    {
        'nombre': 'Luis',
        'base': base_dir / "test/output/glb/Luis/Luis.glb",
        'salida': base_dir / "test/output/glb/Luis"
    },
    {
        'nombre': 'Duvall',
        'base': base_dir / "test/output/glb/Duvall/Duvall.glb",
        'salida': base_dir / "test/output/glb/Duvall"
    }
]

# Huesos de piernas a eliminar
huesos_piernas = [
    'Hips', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase',
    'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase'
]

# Buscar todos los archivos de Nina
archivos_nina = []
for categoria_path in carpeta_entrada.iterdir():
    if categoria_path.is_dir():
        for archivo in categoria_path.glob("Nina_resultado_*.glb"):
            archivos_nina.append((categoria_path.name, archivo))

print(f"\n{'='*80}")
print(f"REGENERACIÓN MASIVA: Nancy, Luis y Duvall")
print(f"Animaciones de Nina: {len(archivos_nina)}")
print(f"Total archivos a generar: {len(archivos_nina) * len(avatares)}")
print(f"{'='*80}\n")

# Procesar cada avatar
for avatar_config in avatares:
    avatar_nombre = avatar_config['nombre']
    avatar_base = avatar_config['base']
    carpeta_salida = avatar_config['salida']
    
    if not avatar_base.exists():
        print(f"\n⚠️ SALTANDO {avatar_nombre}: No se encontró archivo base {avatar_base.name}")
        continue
    
    print(f"\n{'='*80}")
    print(f"PROCESANDO: {avatar_nombre}")
    print(f"{'='*80}\n")
    
    total_procesados = 0
    total_fallidos = 0
    
    for categoria, archivo_nina in archivos_nina:
        animacion = archivo_nina.stem.replace("Nina_resultado_", "")
        
        carpeta_cat = carpeta_salida / categoria
        carpeta_cat.mkdir(parents=True, exist_ok=True)
        archivo_salida = carpeta_cat / f"{avatar_nombre}_resultado_{animacion}.glb"
        
        print(f"[{total_procesados+1}/{len(archivos_nina)}] {categoria}/{animacion}")
        
        try:
            # Limpiar escena
            bpy.ops.wm.read_factory_settings(use_empty=True)
            
            # 1. Importar avatar base (CON TEXTURAS)
            bpy.ops.import_scene.gltf(filepath=str(avatar_base))
            avatar_objs = list(bpy.data.objects)
            avatar_armature = next((obj for obj in avatar_objs if obj.type == 'ARMATURE'), None)
            
            if not avatar_armature:
                raise Exception(f"No se encontró armature de {avatar_nombre}")
            
            texturas_base = len(bpy.data.images)
            
            # 2. Importar Nina con animación
            bpy.ops.import_scene.gltf(filepath=str(archivo_nina))
            nina_objs = [obj for obj in bpy.data.objects if obj not in avatar_objs]
            nina_armature = next((obj for obj in nina_objs if obj.type == 'ARMATURE'), None)
            
            if not nina_armature or not nina_armature.animation_data or not nina_armature.animation_data.action:
                raise Exception("Nina no tiene animación")
            
            action_nina = nina_armature.animation_data.action
            frame_start = int(action_nina.frame_range[0])
            frame_end = int(action_nina.frame_range[1])
            
            # 3. Retarget con constraints + bake
            bpy.context.scene.frame_start = frame_start
            bpy.context.scene.frame_end = frame_end
            bpy.context.view_layer.objects.active = avatar_armature
            
            # Crear constraints Copy Transforms
            constraints_count = 0
            for avatar_bone in avatar_armature.pose.bones:
                if avatar_bone.name in nina_armature.pose.bones:
                    constraint = avatar_bone.constraints.new('COPY_TRANSFORMS')
                    constraint.target = nina_armature
                    constraint.subtarget = avatar_bone.name
                    constraints_count += 1
            
            # Bake la animación
            bpy.ops.object.select_all(action='DESELECT')
            avatar_armature.select_set(True)
            bpy.context.view_layer.objects.active = avatar_armature
            
            bpy.ops.nla.bake(
                frame_start=frame_start,
                frame_end=frame_end,
                step=1,
                only_selected=False,
                visual_keying=True,
                clear_constraints=True,
                clear_parents=False,
                use_current_action=False,
                clean_curves=False,
                bake_types={'POSE'}
            )
            
            # 4. Eliminar FCurves de piernas
            if not avatar_armature.animation_data or not avatar_armature.animation_data.action:
                raise Exception(f"{avatar_nombre} no tiene animación después del bake")
            
            action_avatar = avatar_armature.animation_data.action
            fcurves_antes = len(action_avatar.fcurves)
            fcurves_eliminadas = [fc for fc in action_avatar.fcurves if any(bone in fc.data_path for bone in huesos_piernas)]
            for fc in fcurves_eliminadas:
                action_avatar.fcurves.remove(fc)
            
            # 5. Eliminar objetos de Nina
            for obj in nina_objs:
                bpy.data.objects.remove(obj, do_unlink=True)
            
            # 6. Limpiar acciones no usadas
            acciones_a_eliminar = [act for act in bpy.data.actions if act != action_avatar]
            for act in acciones_a_eliminar:
                bpy.data.actions.remove(act)
            
            # 7. Limpiar NLA tracks
            if avatar_armature.animation_data:
                while len(avatar_armature.animation_data.nla_tracks) > 0:
                    avatar_armature.animation_data.nla_tracks.remove(avatar_armature.animation_data.nla_tracks[0])
            
            # 8. Exportar a GLB
            bpy.ops.export_scene.gltf(
                filepath=str(archivo_salida),
                export_format='GLB',
                export_animations=True,
                export_force_sampling=True,
                export_image_format='AUTO'
            )
            
            file_size = archivo_salida.stat().st_size / (1024*1024)
            texturas_finales = len(bpy.data.images)
            
            print(f"   ✅ {file_size:.1f}MB | {texturas_finales} texturas | {len(action_avatar.fcurves)} FCurves (-{len(fcurves_eliminadas)} piernas)")
            total_procesados += 1
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
            total_fallidos += 1
    
    print(f"\n{'='*40}")
    print(f"RESUMEN {avatar_nombre}")
    print(f"{'='*40}")
    print(f"✅ Procesados: {total_procesados}/{len(archivos_nina)}")
    print(f"❌ Fallidos: {total_fallidos}/{len(archivos_nina)}")
    print(f"{'='*40}\n")

print(f"\n{'='*80}")
print(f"PROCESO COMPLETO FINALIZADO")
print(f"{'='*80}\n")
