"""
PASO 2: Aplicar rotaciones al modelo GLB en Blender
Este script se ejecuta DENTRO de Blender y lee el JSON generado por el PASO 1
"""
import bpy
import json
import mathutils
from pathlib import Path

# ==================== CONFIGURACIÓN ====================
ROTATIONS_JSON = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\temp_hand_rotations.json")
GLB_INPUT = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_mal.glb")
GLB_OUTPUT = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_mal_optimizado.glb")

# Mapeo de dedos a huesos del modelo
FINGER_BONES_MAP = {
    'left': {
        'thumb': ['LeftHandThumb1', 'LeftHandThumb2', 'LeftHandThumb3'],
        'index': ['LeftHandIndex1', 'LeftHandIndex2', 'LeftHandIndex3'],
        'middle': ['LeftHandMiddle1', 'LeftHandMiddle2', 'LeftHandMiddle3'],
        'ring': ['LeftHandRing1', 'LeftHandRing2', 'LeftHandRing3'],
        'pinky': ['LeftHandPinky1', 'LeftHandPinky2', 'LeftHandPinky3']
    },
    'right': {
        'thumb': ['RightHandThumb1', 'RightHandThumb2', 'RightHandThumb3'],
        'index': ['RightHandIndex1', 'RightHandIndex2', 'RightHandIndex3'],
        'middle': ['RightHandMiddle1', 'RightHandMiddle2', 'RightHandMiddle3'],
        'ring': ['RightHandRing1', 'RightHandRing2', 'RightHandRing3'],
        'pinky': ['RightHandPinky1', 'RightHandPinky2', 'RightHandPinky3']
    }
}

# ==================== FUNCIONES ====================

def import_glb():
    """Importa el GLB en Blender"""
    print(f"\n{'='*70}")
    print(f"📥 IMPORTANDO GLB")
    print(f"{'='*70}")
    print(f"Archivo: {GLB_INPUT.name}")
    
    # Limpiar escena
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    
    # Importar GLB
    bpy.ops.import_scene.gltf(filepath=str(GLB_INPUT))
    
    # Buscar armature
    armature = None
    for obj in bpy.context.scene.objects:
        if obj.type == 'ARMATURE':
            armature = obj
            break
    
    if not armature:
        raise RuntimeError("❌ No se encontró armature en el GLB")
    
    print(f"✅ Armature encontrado: {armature.name}")
    
    # Listar huesos de manos
    hand_bones = []
    for bone in armature.pose.bones:
        bone_lower = bone.name.lower()
        if any(kw in bone_lower for kw in ['hand', 'thumb', 'index', 'middle', 'ring', 'pinky']):
            hand_bones.append(bone.name)
    
    print(f"🦴 Huesos de manos encontrados: {len(hand_bones)}")
    for bone_name in sorted(hand_bones):
        print(f"   - {bone_name}")
    
    return armature

def load_rotations():
    """Carga las rotaciones del JSON"""
    print(f"\n📂 Cargando rotaciones: {ROTATIONS_JSON.name}")
    
    if not ROTATIONS_JSON.exists():
        raise FileNotFoundError(f"❌ No se encontró el archivo de rotaciones: {ROTATIONS_JSON}")
    
    with open(ROTATIONS_JSON, 'r') as f:
        data = json.load(f)
    
    print(f"✅ Rotaciones cargadas: {len(data['frames'])} frames")
    return data

def apply_rotations(armature, rotations_data):
    """Aplica las rotaciones SOLO a los huesos de las manos"""
    print(f"\n{'='*70}")
    print(f"🔧 APLICANDO ROTACIONES")
    print(f"{'='*70}")
    
    if not armature.animation_data or not armature.animation_data.action:
        action = bpy.data.actions.new(name="HandsOptimized")
        armature.animation_data_create()
        armature.animation_data.action = action
    else:
        action = armature.animation_data.action
    
    print(f"📊 Acción: {action.name}")
    
    frame_start = bpy.context.scene.frame_start
    modified_bones = set()
    warnings = []
    
    # Procesar cada frame
    for frame_data in rotations_data['frames']:
        frame_number = frame_start + frame_data['frame']
        bpy.context.scene.frame_set(frame_number)
        
        # Mano izquierda
        for finger_name, rotations in frame_data['left_hand'].items():
            bone_names = FINGER_BONES_MAP['left'].get(finger_name, [])
            
            for i, bone_name in enumerate(bone_names):
                if i >= len(rotations):
                    continue
                
                if bone_name not in armature.pose.bones:
                    if bone_name not in warnings:
                        warnings.append(f"⚠️ Hueso no encontrado: {bone_name}")
                    continue
                
                bone = armature.pose.bones[bone_name]
                euler_rot = rotations[i]
                
                # Aplicar rotación Euler
                bone.rotation_mode = 'XYZ'
                bone.rotation_euler = mathutils.Euler(euler_rot, 'XYZ')
                bone.keyframe_insert(data_path="rotation_euler", frame=frame_number)
                modified_bones.add(bone_name)
        
        # Mano derecha
        for finger_name, rotations in frame_data['right_hand'].items():
            bone_names = FINGER_BONES_MAP['right'].get(finger_name, [])
            
            for i, bone_name in enumerate(bone_names):
                if i >= len(rotations):
                    continue
                
                if bone_name not in armature.pose.bones:
                    if bone_name not in warnings:
                        warnings.append(f"⚠️ Hueso no encontrado: {bone_name}")
                    continue
                
                bone = armature.pose.bones[bone_name]
                euler_rot = rotations[i]
                
                # Aplicar rotación Euler
                bone.rotation_mode = 'XYZ'
                bone.rotation_euler = mathutils.Euler(euler_rot, 'XYZ')
                bone.keyframe_insert(data_path="rotation_euler", frame=frame_number)
                modified_bones.add(bone_name)
    
    # Mostrar advertencias
    if warnings:
        print(f"\n⚠️ Advertencias ({len(warnings)}):")
        for warning in warnings[:10]:  # Mostrar solo las primeras 10
            print(f"   {warning}")
        if len(warnings) > 10:
            print(f"   ... y {len(warnings) - 10} más")
    
    print(f"\n✅ Huesos modificados: {len(modified_bones)}")
    for bone_name in sorted(modified_bones):
        print(f"   ✓ {bone_name}")
    
    return len(modified_bones) > 0

def export_glb():
    """Exporta el GLB optimizado"""
    print(f"\n{'='*70}")
    print(f"💾 EXPORTANDO GLB")
    print(f"{'='*70}")
    
    # Crear directorio
    GLB_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    
    # Asegurar Object Mode
    if bpy.context.active_object and bpy.context.active_object.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    
    # Seleccionar todo
    bpy.ops.object.select_all(action='SELECT')
    
    # Exportar
    bpy.ops.export_scene.gltf(
        filepath=str(GLB_OUTPUT),
        export_format='GLB',
        export_animations=True,
        export_apply=False,
        export_rest_position_armature=False,
        export_frame_range=True
    )
    
    print(f"✅ GLB exportado: {GLB_OUTPUT.name}")
    
    # Tamaño del archivo
    size_mb = GLB_OUTPUT.stat().st_size / (1024 * 1024)
    print(f"📊 Tamaño: {size_mb:.2f} MB")
    
    return GLB_OUTPUT

def main():
    """Función principal"""
    print(f"\n{'#'*70}")
    print(f"# PASO 2: APLICACIÓN DE ROTACIONES EN BLENDER")
    print(f"{'#'*70}")
    
    try:
        # Cargar rotaciones
        rotations_data = load_rotations()
        
        # Importar GLB
        armature = import_glb()
        
        # Aplicar rotaciones
        success = apply_rotations(armature, rotations_data)
        
        if not success:
            print("\n⚠️ No se aplicaron rotaciones (posible problema con nombres de huesos)")
            return False
        
        # Exportar
        output_file = export_glb()
        
        # Limpiar archivo temporal
        if ROTATIONS_JSON.exists():
            ROTATIONS_JSON.unlink()
            print(f"\n🗑️ Archivo temporal eliminado")
        
        print(f"\n{'='*70}")
        print(f"✅ PASO 2 COMPLETADO")
        print(f"{'='*70}")
        print(f"📁 Archivo generado: {output_file}")
        print(f"\n💡 Abre el archivo en tu visualizador 3D para ver las manos optimizadas")
        
        return True
        
    except Exception as e:
        print(f"\n{'='*70}")
        print(f"❌ ERROR")
        print(f"{'='*70}")
        print(f"{type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
