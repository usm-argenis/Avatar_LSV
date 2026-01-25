"""
Script para generar todas las animaciones de Carlos usando Ch12_nonPBR
Aplica cada animación de Remy al modelo Ch12 y exporta como Carlos
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
    
    for block in bpy.data.armatures:
        if block.users == 0:
            bpy.data.armatures.remove(block)
    
    for block in bpy.data.actions:
        if block.users == 0:
            bpy.data.actions.remove(block)

def renombrar_huesos_ch12(armature):
    """Renombrar huesos de mixamorig4: a mixamorig:"""
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='EDIT')
    
    renombrados = 0
    for bone in armature.data.edit_bones:
        if bone.name.startswith('mixamorig4:'):
            nuevo_nombre = bone.name.replace('mixamorig4:', 'mixamorig:')
            bone.name = nuevo_nombre
            renombrados += 1
    
    bpy.ops.object.mode_set(mode='OBJECT')
    return renombrados

def aplicar_animacion_a_ch12(remy_animacion_path, output_path, nombre_animacion):
    """Aplicar una animación de Remy a Ch12"""
    
    ch12_path = Path("C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/cc/Ch12_nonPBR (1).fbx")
    
    limpiar_escena()
    
    # Cargar Ch12
    bpy.ops.import_scene.fbx(filepath=str(ch12_path))
    
    ch12_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            ch12_armature = obj
            break
    
    if not ch12_armature:
        print(f"❌ Error: No se encontró armature en Ch12")
        return False
    
    # Renombrar huesos
    renombrados = renombrar_huesos_ch12(ch12_armature)
    
    if renombrados == 0:
        print(f"⚠️ No se renombró ningún hueso")
        return False
    
    # Cargar animación de Remy
    bpy.ops.import_scene.gltf(filepath=str(remy_animacion_path))
    
    # Buscar armature de Remy
    remy_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE' and obj != ch12_armature:
            remy_armature = obj
            break
    
    if not remy_armature:
        print(f"❌ Error: No se encontró animación de Remy en {remy_animacion_path}")
        return False
    
    # Verificar animación
    if not remy_armature.animation_data or not remy_armature.animation_data.action:
        print(f"❌ Error: No se encontró action en Remy")
        return False
    
    remy_action = remy_armature.animation_data.action
    
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
    
    # Crear nueva acción para Ch12
    if not ch12_armature.animation_data:
        ch12_armature.animation_data_create()
    
    nueva_accion = bpy.data.actions.new(name=nombre_animacion)
    ch12_armature.animation_data.action = nueva_accion
    
    # Configurar rango de frames
    frame_inicio = int(remy_action.frame_range[0])
    frame_fin = int(remy_action.frame_range[1])
    
    # Copiar keyframes para cada hueso
    for frame in range(frame_inicio, frame_fin + 1):
        bpy.context.scene.frame_set(frame)
        
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
    
    # Eliminar modelo de Remy
    objetos_a_eliminar = []
    for obj in bpy.data.objects:
        if obj.parent == remy_armature or obj == remy_armature:
            objetos_a_eliminar.append(obj)
    
    for obj in objetos_a_eliminar:
        bpy.data.objects.remove(obj, do_unlink=True)
    
    # Exportar GLB
    bpy.ops.object.select_all(action='DESELECT')
    ch12_armature.select_set(True)
    
    # Seleccionar meshes hijos
    for obj in bpy.data.objects:
        if obj.parent == ch12_armature:
            obj.select_set(True)
    
    bpy.ops.export_scene.gltf(
        filepath=str(output_path),
        use_selection=True,
        export_animations=True,
        export_frame_range=True,
        export_current_frame=False,
        export_nla_strips=False,
        export_def_bones=False
    )
    
    return True

def procesar_todas_animaciones():
    """Procesar todas las animaciones de Remy y crear las de Carlos"""
    
    print("=" * 80)
    print("🎬 GENERANDO TODAS LAS ANIMACIONES DE CARLOS")
    print("=" * 80)
    
    base_path = Path("C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb")
    remy_path = base_path / "Remy"
    carlos_path = base_path / "Carlos"
    
    categorias = ['alfabeto', 'dias_semana', 'tiempo', 'pronombres', 
                  'saludos', 'cortesia', 'preguntas', 'expresiones']
    
    total_procesados = 0
    total_exitosos = 0
    total_fallidos = 0
    
    for categoria in categorias:
        remy_cat_path = remy_path / categoria
        carlos_cat_path = carlos_path / categoria
        
        if not remy_cat_path.exists():
            print(f"⚠️ No existe: {remy_cat_path}")
            continue
        
        archivos_remy = sorted(remy_cat_path.glob("Remy_resultado_*.glb"))
        
        print(f"\n📁 {categoria.upper()}: {len(archivos_remy)} archivos")
        print("-" * 80)
        
        for archivo_remy in archivos_remy:
            total_procesados += 1
            
            # Extraer nombre de la seña (sin "Remy_resultado_" y sin ".glb")
            nombre_sena = archivo_remy.stem.replace("Remy_resultado_", "")
            
            # Crear nombre para Carlos
            nombre_carlos = f"Carlos_resultado_{nombre_sena}.glb"
            archivo_carlos = carlos_cat_path / nombre_carlos
            
            print(f"\n   [{total_procesados}] Procesando: {nombre_sena}")
            print(f"   📥 Origen: {archivo_remy.name}")
            print(f"   📤 Destino: {nombre_carlos}")
            
            try:
                exito = aplicar_animacion_a_ch12(
                    archivo_remy,
                    archivo_carlos,
                    nombre_sena
                )
                
                if exito:
                    print(f"   ✅ ÉXITO: {nombre_carlos}")
                    total_exitosos += 1
                else:
                    print(f"   ❌ FALLÓ: {nombre_carlos}")
                    total_fallidos += 1
                    
            except Exception as e:
                print(f"   ❌ ERROR: {str(e)}")
                total_fallidos += 1
    
    print("\n" + "=" * 80)
    print("📊 RESUMEN FINAL")
    print("=" * 80)
    print(f"Total procesados: {total_procesados}")
    print(f"✅ Exitosos: {total_exitosos}")
    print(f"❌ Fallidos: {total_fallidos}")
    print(f"📈 Tasa de éxito: {(total_exitosos/total_procesados*100):.1f}%")
    print("=" * 80)

if __name__ == "__main__":
    procesar_todas_animaciones()
