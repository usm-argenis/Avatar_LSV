"""
Script de Blender para convertir GLB a FBX sin animación (modelo base)
Ejecutar en Blender
"""

import bpy
from pathlib import Path

# CONFIGURACIÓN
GLB_INPUT = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Remy_resultado_r.glb")
FBX_OUTPUT = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\convertidor\avatar\Remy_base.fbx")

def limpiar_escena():
    """Limpia la escena"""
    print("🧹 Limpiando escena...")
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    print("✅ Escena limpiada")

def importar_glb():
    """Importa el GLB"""
    print(f"\n📥 Importando GLB: {GLB_INPUT}")
    
    if not GLB_INPUT.exists():
        print(f"❌ No se encuentra: {GLB_INPUT}")
        return None
    
    bpy.ops.import_scene.gltf(filepath=str(GLB_INPUT))
    
    # Buscar armature
    armature = None
    for obj in bpy.context.scene.objects:
        if obj.type == 'ARMATURE':
            armature = obj
            break
    
    if armature:
        print(f"✅ Armature encontrado: {armature.name}")
    else:
        print("❌ No se encontró armature")
    
    return armature

def eliminar_animacion(armature):
    """Elimina la animación existente"""
    print("\n🗑️ Eliminando animación...")
    
    if armature.animation_data:
        if armature.animation_data.action:
            print(f"   📊 Acción actual: {armature.animation_data.action.name}")
            armature.animation_data.action = None
            print("   ✅ Animación eliminada")
        
        # Limpiar animation data completamente
        armature.animation_data_clear()
        print("   ✅ Animation data limpiado")
    else:
        print("   ℹ️ No hay animación que eliminar")
    
    return True

def resetear_pose(armature):
    """Resetea la pose a T-pose"""
    print("\n🧍 Reseteando a T-pose...")
    
    # Seleccionar armature
    bpy.ops.object.select_all(action='DESELECT')
    armature.select_set(True)
    bpy.context.view_layer.objects.active = armature
    
    # Entrar en pose mode
    bpy.ops.object.mode_set(mode='POSE')
    
    # Seleccionar todos los huesos
    bpy.ops.pose.select_all(action='SELECT')
    
    # Limpiar transformaciones
    bpy.ops.pose.transforms_clear()
    
    # Volver a object mode
    bpy.ops.object.mode_set(mode='OBJECT')
    
    print("✅ Pose reseteada a T-pose")
    
    return True

def exportar_fbx():
    """Exporta como FBX"""
    print(f"\n💾 Exportando FBX: {FBX_OUTPUT}")
    
    # Crear directorio
    FBX_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    
    # Exportar
    bpy.ops.export_scene.fbx(
        filepath=str(FBX_OUTPUT),
        use_selection=False,
        bake_anim=False,  # NO incluir animación
        add_leaf_bones=False
    )
    
    print("✅ FBX exportado")
    
    # Verificar tamaño
    if FBX_OUTPUT.exists():
        tamaño_mb = FBX_OUTPUT.stat().st_size / (1024 * 1024)
        print(f"📊 Tamaño: {tamaño_mb:.2f} MB")
    
    return FBX_OUTPUT

def main():
    print("=" * 60)
    print("🔄 CONVERTIR GLB A FBX BASE (SIN ANIMACIÓN)")
    print("=" * 60)
    
    # 1. Limpiar escena
    limpiar_escena()
    
    # 2. Importar GLB
    armature = importar_glb()
    if not armature:
        return
    
    # 3. Eliminar animación
    eliminar_animacion(armature)
    
    # 4. Resetear pose
    resetear_pose(armature)
    
    # 5. Exportar FBX
    exportar_fbx()
    
    print("\n" + "=" * 60)
    print("✅ CONVERSIÓN COMPLETADA")
    print("=" * 60)
    print(f"\n📁 Archivo FBX base: {FBX_OUTPUT}")
    print("\n💡 Siguiente paso:")
    print("   1. Abre MotionBuilder")
    print("   2. Ejecuta: scripts\\crear_animacion_r.py")

if __name__ == "__main__":
    main()
