"""
Diagnóstico profundo de los archivos buenos dias
"""

import bpy
from pathlib import Path

print("="*80)
print("DIAGNÓSTICO: BUENOS DIAS")
print("="*80)

BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\blend")

def analizar_archivo(categoria, animacion):
    print(f"\n{'='*80}")
    print(f"📝 ANALIZANDO: {categoria}/{animacion}")
    print(f"{'='*80}")
    
    blend_file = BASE_DIR / categoria / f"Nancy_{animacion}.blend"
    
    if not blend_file.exists():
        print(f"❌ No existe: {blend_file}")
        return
    
    bpy.ops.wm.open_mainfile(filepath=str(blend_file))
    
    # Armatures
    armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
    print(f"\n🦴 Armatures encontrados: {len(armatures)}")
    for arm in armatures:
        print(f"   - {arm.name} ({len(arm.pose.bones)} bones)")
    
    if not armatures:
        return
    
    armature = armatures[0]
    
    # Acciones
    actions = list(bpy.data.actions)
    print(f"\n🎬 Acciones encontradas: {len(actions)}")
    
    for action in actions:
        print(f"\n   📌 Acción: {action.name}")
        print(f"      Frames: {action.frame_range[0]:.0f} - {action.frame_range[1]:.0f}")
        print(f"      FCurves: {len(action.fcurves)}")
        
        # Asignar acción
        if not armature.animation_data:
            armature.animation_data_create()
        
        armature.animation_data.action = action
        armature.animation_data.use_nla = False
        
        frame_start, frame_end = action.frame_range
        
        # Probar varios huesos
        bones_to_test = ['Hips', 'Spine', 'Head', 'LeftArm', 'RightArm', 
                        'LeftHand', 'RightHand', 'LeftLeg', 'RightLeg']
        
        print(f"      Movimiento por hueso:")
        max_movement = 0
        best_bone = None
        
        for bone_name in bones_to_test:
            if bone_name in armature.pose.bones:
                bpy.context.scene.frame_set(int(frame_start))
                bpy.context.view_layer.update()
                
                pos_start = armature.pose.bones[bone_name].matrix.translation.copy()
                rot_start = armature.pose.bones[bone_name].matrix.to_euler()
                
                bpy.context.scene.frame_set(int(frame_end))
                bpy.context.view_layer.update()
                
                pos_end = armature.pose.bones[bone_name].matrix.translation.copy()
                rot_end = armature.pose.bones[bone_name].matrix.to_euler()
                
                pos_movement = (pos_start - pos_end).length
                rot_movement = sum(abs(rot_start[i] - rot_end[i]) for i in range(3))
                
                total_movement = pos_movement + rot_movement
                
                print(f"         {bone_name:12s}: pos={pos_movement:.4f}, rot={rot_movement:.4f}, total={total_movement:.4f}")
                
                if total_movement > max_movement:
                    max_movement = total_movement
                    best_bone = bone_name
        
        if max_movement > 0.001:
            print(f"      ✅ Tiene movimiento! Mejor hueso: {best_bone} (mov={max_movement:.4f})")
        else:
            print(f"      ❌ Sin movimiento detectado (max={max_movement:.6f})")

# Analizar ambos archivos
analizar_archivo("cortesia", "buenos dias")
analizar_archivo("saludos", "buenos dias")

print(f"\n{'='*80}")
print(f"DIAGNÓSTICO COMPLETADO")
print(f"{'='*80}")
