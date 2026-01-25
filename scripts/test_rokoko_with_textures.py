"""
Script para transferir animaciones de Nina a Nancy usando Rokoko Studio
manteniendo las texturas de Nancy intactas.
"""

import bpy
from pathlib import Path

# Configuración
base_dir = Path(r"C:\Users\andre\OneDrive\Documentos\tesis")
nancy_base = base_dir / "test/output/glb/Nancy/Nancy.glb"

# Archivo de prueba
categoria = "saludos"
animacion = "hola"
archivo_nina = base_dir / f"test/output/glb/Nina/{categoria}/Nina_resultado_{animacion}.glb"
archivo_salida = base_dir / f"test/output/glb/Nancy/{categoria}/Nancy_resultado_{animacion}.glb"

print(f"\n{'='*80}")
print(f"PRUEBA: Rokoko Studio con texturas preservadas")
print(f"{'='*80}\n")

# Huesos de piernas a eliminar
huesos_piernas = [
    'Hips', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase',
    'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase'
]

try:
    # Limpiar escena
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
    # 1. Importar Nancy base (CON TEXTURAS)
    print(f"📥 Importando Nancy base con texturas...")
    bpy.ops.import_scene.gltf(filepath=str(nancy_base))
    
    nancy_objs = list(bpy.data.objects)
    nancy_armature = next((obj for obj in nancy_objs if obj.type == 'ARMATURE'), None)
    nancy_meshes = [obj for obj in nancy_objs if obj.type == 'MESH']
    
    if not nancy_armature:
        raise Exception("No se encontró armature de Nancy")
    
    texturas_nancy = len(bpy.data.images)
    print(f"   ✅ Nancy: {len(nancy_objs)} objetos, {texturas_nancy} texturas")
    print(f"   ✅ Meshes de Nancy: {[m.name for m in nancy_meshes]}")
    
    # 2. Importar Nina con animación
    print(f"\n📥 Importando Nina con animación...")
    bpy.ops.import_scene.gltf(filepath=str(archivo_nina))
    
    nina_objs = [obj for obj in bpy.data.objects if obj not in nancy_objs]
    nina_armature = next((obj for obj in nina_objs if obj.type == 'ARMATURE'), None)
    nina_meshes = [obj for obj in nina_objs if obj.type == 'MESH']
    
    if not nina_armature or not nina_armature.animation_data:
        raise Exception("Nina no tiene animación")
    
    action_nina = nina_armature.animation_data.action
    print(f"   ✅ Nina: animación '{action_nina.name}' con {len(action_nina.fcurves)} FCurves")
    
    # 3. Método de retarget con constraints + bake
    print(f"\n🎬 Aplicando retarget con constraints...")
    
    frame_start = int(action_nina.frame_range[0])
    frame_end = int(action_nina.frame_range[1])
    
    # Configurar timeline
    bpy.context.scene.frame_start = frame_start
    bpy.context.scene.frame_end = frame_end
    
    # Crear constraints Copy Transforms en cada hueso de Nancy
    print(f"   📌 Creando constraints...")
    bpy.context.view_layer.objects.active = nancy_armature
    
    constraints_creados = 0
    for nancy_bone in nancy_armature.pose.bones:
        if nancy_bone.name in nina_armature.pose.bones:
            constraint = nancy_bone.constraints.new('COPY_TRANSFORMS')
            constraint.target = nina_armature
            constraint.subtarget = nancy_bone.name
            constraints_creados += 1
    
    print(f"   ✅ {constraints_creados} constraints creados")
    
    # Bake la animación (esto copia la animación de Nina a Nancy)
    print(f"   🔥 Baking animación...")
    bpy.ops.object.select_all(action='DESELECT')
    nancy_armature.select_set(True)
    bpy.context.view_layer.objects.active = nancy_armature
    
    bpy.ops.nla.bake(
        frame_start=frame_start,
        frame_end=frame_end,
        step=1,
        only_selected=False,
        visual_keying=True,
        clear_constraints=True,  # Elimina los constraints después del bake
        clear_parents=False,
        use_current_action=False,
        clean_curves=False,
        bake_types={'POSE'}
    )
    
    print(f"   ✅ Bake completado")
    
    # 4. Verificar que Nancy tiene la animación
    if not nancy_armature.animation_data or not nancy_armature.animation_data.action:
        raise Exception("Nancy no tiene animación después del retarget")
    
    action_nancy = nancy_armature.animation_data.action
    print(f"   ✅ Nancy ahora tiene acción: {action_nancy.name} con {len(action_nancy.fcurves)} FCurves")
    
    # 5. Eliminar FCurves de piernas
    print(f"\n🔄 Eliminando animación de piernas...")
    fcurves_eliminadas = [fc for fc in action_nancy.fcurves if any(bone in fc.data_path for bone in huesos_piernas)]
    for fc in fcurves_eliminadas:
        action_nancy.fcurves.remove(fc)
    
    print(f"   ✅ Eliminadas {len(fcurves_eliminadas)} FCurves ({len(action_nancy.fcurves)} restantes)")
    
    # 6. Eliminar objetos de Nina (pero mantener todo de Nancy)
    print(f"\n🗑️ Eliminando objetos de Nina...")
    for obj in nina_objs:
        bpy.data.objects.remove(obj, do_unlink=True)
    
    # Verificar que las texturas de Nancy siguen ahí
    texturas_finales = len(bpy.data.images)
    print(f"   ✅ Texturas preservadas: {texturas_finales}")
    
    # 7. Limpiar acciones no usadas
    print(f"\n🗑️ Limpiando acciones...")
    acciones_a_eliminar = [act for act in bpy.data.actions if act != action_nancy]
    print(f"   Eliminando: {[act.name for act in acciones_a_eliminar]}")
    for act in acciones_a_eliminar:
        bpy.data.actions.remove(act)
    
    # 8. Verificar estructura final
    print(f"\n📊 VERIFICANDO ESTRUCTURA FINAL:")
    print(f"   Objetos: {len(bpy.data.objects)}")
    print(f"   Texturas: {len(bpy.data.images)}")
    print(f"   Acciones: {len(bpy.data.actions)} - {[act.name for act in bpy.data.actions]}")
    print(f"   FCurves en acción: {len(action_nancy.fcurves)}")
    print(f"   Acción activa en Nancy: {nancy_armature.animation_data.action.name if nancy_armature.animation_data.action else 'NINGUNA'}")
    
    # 9. CRÍTICO: Limpiar NLA tracks antes de exportar
    # Los NLA tracks exportados a GLB se importan como "muted" con influence=0
    print(f"\n🧹 Limpiando NLA tracks para exportación limpia...")
    if nancy_armature.animation_data:
        nla_count = len(nancy_armature.animation_data.nla_tracks)
        while len(nancy_armature.animation_data.nla_tracks) > 0:
            nancy_armature.animation_data.nla_tracks.remove(nancy_armature.animation_data.nla_tracks[0])
        print(f"   ✅ {nla_count} NLA tracks eliminados")
        print(f"   ✅ Use NLA: {nancy_armature.animation_data.use_nla}")
    
    # 10. Exportar a GLB con force_sampling
    print(f"\n💾 Exportando a GLB con force_sampling...")
    archivo_salida.parent.mkdir(parents=True, exist_ok=True)
    
    bpy.ops.export_scene.gltf(
        filepath=str(archivo_salida),
        export_format='GLB',
        export_animations=True,
        export_force_sampling=True,  # Exportar desde acción activa, ignorando NLA
        export_image_format='AUTO'
    )
    
    file_size = archivo_salida.stat().st_size / (1024*1024)
    print(f"   ✅ {file_size:.1f}MB exportado")
    
    print(f"\n{'='*80}")
    print(f"✅ EXPORTACIÓN EXITOSA")
    print(f"{'='*80}\n")
    
except Exception as e:
    print(f"\n{'='*80}")
    print(f"❌ ERROR: {e}")
    print(f"{'='*80}\n")
    import traceback
    traceback.print_exc()
