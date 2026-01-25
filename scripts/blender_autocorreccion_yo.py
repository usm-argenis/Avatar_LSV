"""
Script de Auto-Corrección para Blender
Generado automáticamente
Aplica correcciones de dedos y visibilidad
"""

import bpy
import math

def aplicar_correccion_dedo(bone_name, rotation_z_deg, frame_start, frame_end):
    """Aplica rotación a un hueso de dedo"""
    armature = bpy.context.active_object
    if armature.type != 'ARMATURE':
        print("⚠️  Por favor selecciona el Armature primero")
        return False
        
    pose_bone = armature.pose.bones.get(bone_name)
    if not pose_bone:
        print(f"⚠️  Hueso {bone_name} no encontrado")
        return False
        
    bpy.context.scene.frame_set(frame_start)
    
    # Rotar en Z
    rotation_rad = math.radians(rotation_z_deg)
    pose_bone.rotation_euler[2] += rotation_rad
    pose_bone.keyframe_insert(data_path="rotation_euler", frame=frame_start)
    
    bpy.context.scene.frame_set(frame_end)
    pose_bone.keyframe_insert(data_path="rotation_euler", frame=frame_end)
    
    print(f"✅ {bone_name}: {rotation_z_deg:+.1f}° (frames {frame_start}-{frame_end})")
    return True

def aplicar_correccion_visibilidad(bone_name, frame_start, frame_end, ajuste_Z):
    """Mueve el brazo hacia adelante para visibilidad"""
    armature = bpy.context.active_object
    if armature.type != 'ARMATURE':
        return False
        
    pose_bone = armature.pose.bones.get(bone_name)
    if not pose_bone:
        print(f"⚠️  Hueso {bone_name} no encontrado")
        return False
        
    bpy.context.scene.frame_set(frame_start)
    
    # Mover en Z (hacia adelante)
    pose_bone.location[2] += ajuste_Z
    pose_bone.keyframe_insert(data_path="location", frame=frame_start)
    
    bpy.context.scene.frame_set(frame_end)
    pose_bone.keyframe_insert(data_path="location", frame=frame_end)
    
    print(f"✅ {bone_name}: +{ajuste_Z}m adelante (frames {frame_start}-{frame_end})")
    return True

def detectar_nombres_huesos(armature):
    """Detecta automáticamente los nombres correctos de los huesos"""
    pose_bones = armature.pose.bones
    
    # Nombres exactos detectados del GLB Nancy
    nombres_exactos = {
        'thumb': 'RightHandThumb1',
        'index': 'RightHandIndex1',
        'middle': 'RightHandMiddle1',
        'ring': 'RightHandRing1',
        'pinky': 'RightHandPinky1'
    }
    
    # Verificar que existen
    nombres_encontrados = {}
    for dedo, nombre in nombres_exactos.items():
        if nombre in [bone.name for bone in pose_bones]:
            nombres_encontrados[dedo] = nombre
    
    # Si no se encuentran con nombres exactos, buscar con patrones
    if len(nombres_encontrados) < 5:
        patrones = {
            'thumb': ['Thumb1', 'thumb1', 'Pulgar1'],
            'index': ['Index1', 'index1', 'Indice1'],
            'middle': ['Middle1', 'middle1', 'Medio1'],
            'ring': ['Ring1', 'ring1', 'Anular1'],
            'pinky': ['Pinky1', 'pinky1', 'Little1']
        }
        
        for dedo, patrones_dedo in patrones.items():
            if dedo not in nombres_encontrados:
                for bone in pose_bones:
                    if 'Right' in bone.name or 'right' in bone.name:
                        for patron in patrones_dedo:
                            if patron in bone.name:
                                nombres_encontrados[dedo] = bone.name
                                break
                        if dedo in nombres_encontrados:
                            break
    
    return nombres_encontrados

def main():
    print("\n" + "="*60)
    print("🚀 INICIANDO AUTO-CORRECCIÓN")
    print("="*60 + "\n")
    
    # Verificar que hay un armature seleccionado
    if not bpy.context.active_object or bpy.context.active_object.type != 'ARMATURE':
        print("❌ ERROR: Por favor selecciona el Armature en la escena")
        return
    
    armature = bpy.context.active_object
    bpy.ops.object.mode_set(mode='POSE')
    
    # Detectar nombres de huesos automáticamente
    print("🔍 Detectando nombres de huesos...\n")
    huesos = detectar_nombres_huesos(armature)
    
    if not huesos:
        print("❌ ERROR: No se pudieron detectar los huesos de dedos")
        print("💡 Ejecuta primero: blender_listar_huesos.py")
        return
    
    print("✅ Huesos detectados:")
    for dedo, nombre in huesos.items():
        print(f"   • {dedo}: {nombre}")
    print()
    
    # CORRECCIONES DE DEDOS
    print("🔧 APLICANDO CORRECCIONES DE DEDOS\n")
    
    # Configuración de correcciones (grados)
    ajustes = {
        'thumb': 5,
        'index': -15,
        'middle': 10,
        'ring': 10,
        'pinky': 10
    }
    
    correcciones_aplicadas = 0
    for dedo, bone_name in huesos.items():
        if dedo in ajustes:
            if aplicar_correccion_dedo(bone_name, ajustes[dedo], 10, 50):
                correcciones_aplicadas += 1
    
    if correcciones_aplicadas == 0:
        print("⚠️  No se pudo aplicar ninguna corrección de dedos")
    else:
        print(f"\n✅ Se aplicaron {correcciones_aplicadas} correcciones de dedos")
        aplicar_correccion_dedo(
            corr['bone_name'],
            corr['rotation_z_degrees'],
            corr['frame_start'],
            corr['frame_end']
        )
    
    # CORRECCIONES DE VISIBILIDAD
    print("\n👁️  APLICANDO CORRECCIONES DE VISIBILIDAD\n")
    correcciones_vis = []
    
    for corr in correcciones_vis:
        aplicar_correccion_visibilidad(
            corr['bone_name'],
            corr['frame_start'],
            corr['frame_end'],
            corr['ajuste_Z']
        )
    
    # Suavizar curvas (solo si hay correcciones aplicadas)
    if correcciones_aplicadas > 0:
        print("\n✨ SUAVIZANDO ANIMACIÓN\n")
        try:
            # Seleccionar todos los huesos
            bpy.ops.pose.select_all(action='SELECT')
            # Interpolar las curvas F automáticamente
            for bone in armature.pose.bones:
                if bone.name in huesos.values():
                    bone.keyframe_insert(data_path="rotation_euler", frame=30)
            print("✅ Interpolación aplicada")
        except Exception as e:
            print(f"⚠️  No se pudo suavizar (no crítico): {e}")
    
    print("\n" + "="*60)
    print("✅ AUTO-CORRECCIÓN COMPLETADA")
    print("="*60)
    print("\n📤 Ahora exporta: File > Export > glTF 2.0 (.glb)")
    print(r"📁 Guardar como: C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy\pronombres\Nancy_resultado_yo_AUTOCORREGIDO.glb")
    print()

if __name__ == "__main__":
    main()
