import bpy
import sys

print("\n" + "="*70)
print("VERIFICANDO ANIMACIÓN TRANSFERIDA: Leonard_con_animacion_b.fbx")
print("="*70)

# Limpiar escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Importar Leonard transferido
fbx_path = r"C:\Users\andre\OneDrive\Documentos\tesis\output\Leonard_con_animacion_b.fbx"
print(f"\n📥 Importando {fbx_path}...")
bpy.ops.import_scene.fbx(filepath=fbx_path)

# Encontrar armature
armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        armature = obj
        break

if not armature:
    print("❌ NO SE ENCONTRÓ ARMATURE")
    sys.exit(1)

print(f"✅ Armature: {armature.name}\n")

# Encontrar action
if armature.animation_data and armature.animation_data.action:
    action = armature.animation_data.action
    print(f"✅ Action: {action.name}")
    print(f"   Frames: {int(action.frame_range[0])} - {int(action.frame_range[1])}")
    print(f"   FCurves: {len(action.fcurves)}\n")
    
    # Buscar RightArm
    bone_names = ["RightArm", "mixamorig9:RightArm", "mixamorig:RightArm"]
    right_arm = None
    
    for bone_name in bone_names:
        if bone_name in armature.pose.bones:
            right_arm = bone_name
            break
    
    if not right_arm:
        print("❌ NO SE ENCONTRÓ HUESO RightArm")
        sys.exit(1)
    
    print(f"🔍 Analizando {right_arm}:\n")
    
    # Analizar rotation_quaternion[0] (componente W)
    for fc in action.fcurves:
        if right_arm in fc.data_path and "rotation_quaternion" in fc.data_path and fc.array_index == 0:
            valores = [kf.co[1] for kf in fc.keyframe_points]
            unicos = len(set([round(v, 6) for v in valores]))
            
            print(f"   rotation_quaternion[0] (w):")
            print(f"   Keyframes: {len(valores)}")
            print(f"   Min: {min(valores):.6f}, Max: {max(valores):.6f}")
            print(f"   Valores únicos: {unicos}")
            
            if unicos > 10:
                print(f"   ✅ HAY VARIACIÓN ({unicos} valores únicos)\n")
            else:
                print(f"   ❌ SIN VARIACIÓN (solo {unicos} valores únicos)\n")
            break
    
    # Test visual - comparar frames
    print("🎬 TEST VISUAL - Cambio de pose:\n")
    
    bone = armature.pose.bones[right_arm]
    
    bpy.context.scene.frame_set(1)
    rot_f1 = bone.rotation_quaternion.copy()
    
    bpy.context.scene.frame_set(45)
    rot_f45 = bone.rotation_quaternion.copy()
    
    print(f"   Frame 1:  {rot_f1}")
    print(f"   Frame 45: {rot_f45}")
    
    # Calcular diferencia
    diff = sum(abs(rot_f45[i] - rot_f1[i]) for i in range(4))
    
    if diff > 0.01:
        print(f"   ✅ LA ANIMACIÓN FUNCIONA! (diferencia: {diff:.4f})")
    else:
        print(f"   ❌ LA ROTACIÓN NO CAMBIÓ (diferencia: {diff:.6f})")
else:
    print("❌ NO HAY ANIMATION DATA")

print("\n" + "="*70)
