"""
Script para aplicar animaciones de Remy a Ch12_nonPBR
Renombra los huesos de Ch12 para que coincidan con Mixamo estándar
"""
import bpy
import sys
from pathlib import Path

def limpiar_escena():
    """Limpiar toda la escena"""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    for block in bpy.data.meshes:
        if block.users == 0:
            bpy.data.meshes.remove(block)

def renombrar_huesos_ch12(armature):
    """Renombrar huesos de mixamorig4: a mixamorig:"""
    print("\n🔄 Renombrando huesos de Ch12...")
    
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='EDIT')
    
    renombrados = 0
    for bone in armature.data.edit_bones:
        if bone.name.startswith('mixamorig4:'):
            nuevo_nombre = bone.name.replace('mixamorig4:', 'mixamorig:')
            print(f"  {bone.name} → {nuevo_nombre}")
            bone.name = nuevo_nombre
            renombrados += 1
    
    bpy.ops.object.mode_set(mode='OBJECT')
    print(f"✅ {renombrados} huesos renombrados")
    
    return renombrados

def aplicar_animacion_a_ch12():
    """Aplicar animación de Remy a Ch12"""
    
    print("=" * 80)
    print("🎬 APLICACIÓN DE ANIMACIÓN: CH12 + REMY (CON RENOMBRADO)")
    print("=" * 80)
    
    # Rutas
    base_path = Path("C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb")
    ch12_path = base_path / "cc" / "Ch12_nonPBR (1).fbx"
    remy_animacion_path = base_path / "alfabeto" / "Remy_resultado_b.glb"
    output_path_fbx = base_path / "cc" / "Ch12_con_animacion_b_FINAL.fbx"
    output_path_glb = base_path / "cc" / "Ch12_con_animacion_b_FINAL.glb"
    
    limpiar_escena()
    
    # Cargar Ch12
    print(f"\n📥 Cargando Ch12: {ch12_path}")
    bpy.ops.import_scene.fbx(filepath=str(ch12_path))
    
    ch12_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            ch12_armature = obj
            break
    
    if not ch12_armature:
        print("❌ Error: No se encontró armature en Ch12")
        return
    
    print(f"✅ Armature: {ch12_armature.name}")
    
    # Renombrar huesos
    renombrados = renombrar_huesos_ch12(ch12_armature)
    
    if renombrados == 0:
        print("⚠️ No se renombró ningún hueso")
        return
    
    # Cargar animación
    print(f"\n📥 Cargando animación: {remy_animacion_path}")
    bpy.ops.import_scene.gltf(filepath=str(remy_animacion_path))
    
    # Buscar armature de Remy
    remy_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE' and obj != ch12_armature:
            remy_armature = obj
            break
    
    if not remy_armature:
        print("❌ Error: No se encontró animación de Remy")
        return
    
    print(f"✅ Animación: {remy_armature.name}")
    
    # Verificar animación
    if not remy_armature.animation_data or not remy_armature.animation_data.action:
        print("❌ Error: No se encontró action en Remy")
        return
    
    remy_action = remy_armature.animation_data.action
    print(f"✅ Action: {remy_action.name}")
    print(f"   Frames: {int(remy_action.frame_range[0])} → {int(remy_action.frame_range[1])}")
    
    # Obtener lista de huesos animados
    huesos_animados = set()
    for fcurve in remy_action.fcurves:
        data_path = fcurve.data_path
        if 'pose.bones[' in data_path:
            start = data_path.find('["') + 2
            end = data_path.find('"]', start)
            if start > 1 and end > start:
                nombre_hueso = data_path[start:end]
                huesos_animados.add(nombre_hueso)
    
    print(f"   Huesos animados: {len(huesos_animados)}")
    
    # Copiar animación a Ch12
    print(f"\n🔄 Copiando animación a Ch12...")
    
    if not ch12_armature.animation_data:
        ch12_armature.animation_data_create()
    
    # IMPORTANTE: Seleccionar ambos armatures para copiar constraints
    bpy.ops.object.select_all(action='DESELECT')
    remy_armature.select_set(True)
    ch12_armature.select_set(True)
    bpy.context.view_layer.objects.active = ch12_armature
    
    # Copiar pose de cada frame
    print(f"   Copiando {int(remy_action.frame_range[1] - remy_action.frame_range[0] + 1)} frames...")
    
    # Crear nueva acción para Ch12
    nueva_accion = bpy.data.actions.new(name="letra_b")
    ch12_armature.animation_data.action = nueva_accion
    
    # Configurar rango de frames
    frame_inicio = int(remy_action.frame_range[0])
    frame_fin = int(remy_action.frame_range[1])
    
    # Copiar keyframes para cada hueso
    for frame in range(frame_inicio, frame_fin + 1):
        bpy.context.scene.frame_set(frame)
        
        # Para cada hueso en Remy, copiar transformación a Ch12
        for bone_name in huesos_animados:
            if bone_name in remy_armature.pose.bones and bone_name in ch12_armature.pose.bones:
                remy_bone = remy_armature.pose.bones[bone_name]
                ch12_bone = ch12_armature.pose.bones[bone_name]
                
                # Copiar transformaciones
                ch12_bone.location = remy_bone.location.copy()
                ch12_bone.rotation_quaternion = remy_bone.rotation_quaternion.copy()
                ch12_bone.rotation_euler = remy_bone.rotation_euler.copy()
                ch12_bone.scale = remy_bone.scale.copy()
                
                # Insertar keyframes
                ch12_bone.keyframe_insert(data_path="location", frame=frame)
                ch12_bone.keyframe_insert(data_path="rotation_quaternion", frame=frame)
                ch12_bone.keyframe_insert(data_path="rotation_euler", frame=frame)
                ch12_bone.keyframe_insert(data_path="scale", frame=frame)
    
    print(f"✅ Animación copiada: {frame_fin - frame_inicio + 1} frames")
    print(f"   Action: {nueva_accion.name}")
    print(f"   FCurves: {len(nueva_accion.fcurves)}")
    
    # Eliminar modelo de Remy (solo dejar Ch12 con animación)
    print(f"\n🗑️  Eliminando modelo de Remy...")
    bpy.ops.object.select_all(action='DESELECT')
    
    objetos_a_eliminar = []
    for obj in bpy.data.objects:
        if obj.parent == remy_armature or obj == remy_armature:
            objetos_a_eliminar.append(obj)
    
    for obj in objetos_a_eliminar:
        bpy.data.objects.remove(obj, do_unlink=True)
    
    print(f"✅ {len(objetos_a_eliminar)} objetos eliminados")
    
    # Exportar resultado en GLB (mejor para animaciones)
    print(f"\n💾 Exportando GLB: {output_path_glb}")
    
    bpy.ops.object.select_all(action='DESELECT')
    ch12_armature.select_set(True)
    
    # Seleccionar meshes hijos
    for obj in bpy.data.objects:
        if obj.parent == ch12_armature:
            obj.select_set(True)
    
    bpy.ops.export_scene.gltf(
        filepath=str(output_path_glb),
        use_selection=True,
        export_animations=True,
        export_frame_range=True,
        export_current_frame=False,
        export_nla_strips=False,
        export_def_bones=False
    )
    
    print("✅ Exportación GLB completada!")
    
    # También exportar FBX
    print(f"\n💾 Exportando FBX: {output_path_fbx}")
    
    bpy.ops.export_scene.fbx(
        filepath=str(output_path_fbx),
        use_selection=True,
        bake_anim=True,
        bake_anim_use_all_bones=True,
        bake_anim_use_nla_strips=False,
        bake_anim_use_all_actions=False,
        bake_anim_force_startend_keying=True,
        bake_anim_step=1.0,
        bake_anim_simplify_factor=0.0,
        add_leaf_bones=False
    )
    
    print("✅ Exportación FBX completada!")
    
    print("\n" + "=" * 80)
    print("✅ PROCESO COMPLETADO EXITOSAMENTE")
    print("=" * 80)
    print(f"\n📁 Archivos generados:")
    print(f"   GLB: {output_path_glb}")
    print(f"   FBX: {output_path_fbx}")
    print(f"🎬 Animación aplicada: Letra B")
    print(f"📊 Frames: {frame_inicio} → {frame_fin} ({frame_fin - frame_inicio + 1} frames)")
    print(f"📈 FCurves: {len(nueva_accion.fcurves)}")

if __name__ == "__main__":
    aplicar_animacion_a_ch12()
