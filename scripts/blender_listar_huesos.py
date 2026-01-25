"""
Script para Listar Huesos del Armature
Ejecutar primero para ver los nombres reales de los huesos
"""

import bpy

def listar_huesos():
    print("\n" + "="*70)
    print("🔍 LISTANDO TODOS LOS HUESOS DEL ARMATURE")
    print("="*70 + "\n")
    
    # Verificar que hay un armature seleccionado
    if not bpy.context.active_object or bpy.context.active_object.type != 'ARMATURE':
        print("❌ ERROR: Por favor selecciona el Armature en la escena")
        return
    
    armature = bpy.context.active_object
    print(f"📦 Armature encontrado: {armature.name}\n")
    
    # Cambiar a Pose Mode
    bpy.ops.object.mode_set(mode='POSE')
    
    pose_bones = armature.pose.bones
    print(f"📊 Total de huesos: {len(pose_bones)}\n")
    
    # Buscar huesos de dedos mano derecha
    print("👉 HUESOS DE MANO DERECHA (_r o _R):\n")
    mano_derecha = []
    for bone in pose_bones:
        if '_r' in bone.name.lower() or '_R' in bone.name:
            mano_derecha.append(bone.name)
    
    if mano_derecha:
        for bone_name in sorted(mano_derecha):
            print(f"   • {bone_name}")
    else:
        print("   ⚠️ No se encontraron huesos con '_r' o '_R'")
    
    # Buscar huesos específicos de dedos
    print("\n\n🔍 BUSCANDO HUESOS DE DEDOS (patrones comunes):\n")
    
    patrones_dedos = {
        'Pulgar (Thumb)': ['thumb', 'pulgar', 'Thumb'],
        'Índice (Index)': ['index', 'indice', 'Index'],
        'Medio (Middle)': ['middle', 'medio', 'Middle'],
        'Anular (Ring)': ['ring', 'anular', 'Ring'],
        'Meñique (Pinky)': ['pinky', 'menique', 'little', 'Pinky', 'Little']
    }
    
    for nombre_dedo, patrones in patrones_dedos.items():
        print(f"\n{nombre_dedo}:")
        encontrados = []
        for bone in pose_bones:
            for patron in patrones:
                if patron in bone.name:
                    encontrados.append(bone.name)
                    break
        
        if encontrados:
            for bone_name in sorted(set(encontrados)):
                print(f"   ✅ {bone_name}")
        else:
            print(f"   ❌ No encontrado")
    
    # Buscar huesos de brazo
    print("\n\n💪 HUESOS DE BRAZO DERECHO:\n")
    patrones_brazo = ['arm', 'shoulder', 'forearm', 'hand', 'upper', 'lower', 'brazo', 'hombro']
    
    brazos = []
    for bone in pose_bones:
        if '_r' in bone.name.lower() or '_R' in bone.name:
            for patron in patrones_brazo:
                if patron.lower() in bone.name.lower():
                    brazos.append(bone.name)
                    break
    
    if brazos:
        for bone_name in sorted(set(brazos)):
            print(f"   • {bone_name}")
    else:
        print("   ⚠️ No se encontraron huesos de brazo")
    
    print("\n\n" + "="*70)
    print("✅ LISTADO COMPLETADO")
    print("="*70)
    print("\n💡 INSTRUCCIONES:")
    print("   1. Copia los nombres exactos de los huesos que necesitas")
    print("   2. Actualiza el script blender_autocorreccion_yo.py")
    print("   3. Reemplaza los nombres en la lista 'correcciones_dedos'")
    print("\n")

if __name__ == "__main__":
    listar_huesos()
