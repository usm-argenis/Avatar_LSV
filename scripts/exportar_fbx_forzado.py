import bpy
import sys

print("\n" + "="*70)
print("EXPORTAR FBX CON CONFIGURACIÓN MANUAL COMPLETA")
print("="*70)

# Abrir el archivo .blend
blend_path = r"C:\Users\andre\OneDrive\Documentos\tesis\output\Leonard_con_animacion_b.blend"
bpy.ops.wm.open_mainfile(filepath=blend_path)

print(f"\n✓ Archivo abierto: {blend_path}")

# Verificar animación
arm = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        arm = obj
        break

if not arm or not arm.animation_data or not arm.animation_data.action:
    print("\n❌ ERROR: No hay animación")
    sys.exit(1)

action = arm.animation_data.action
frame_start = int(action.frame_range[0])
frame_end = int(action.frame_range[1])

print(f"\n✓ Animación: {action.name}")
print(f"  Frames: {frame_start} - {frame_end}")
print(f"  FCurves: {len(action.fcurves)}")

# Configurar escena
bpy.context.scene.frame_start = frame_start
bpy.context.scene.frame_end = frame_end
bpy.context.scene.frame_set(frame_start)

# Seleccionar todo
bpy.ops.object.select_all(action='SELECT')
arm.select_set(True)
bpy.context.view_layer.objects.active = arm

# SOLUCIÓN: Guardar como un .blend temporal con configuración de exportación
# y luego usar addon de exportación con preset

fbx_path = r"C:\Users\andre\OneDrive\Documentos\tesis\output\Leonard_con_animacion_b.fbx"

print(f"\n📦 Intentando exportar FBX con configuración forzada...")

# Intentar con TODOS los parámetros posibles
try:
    bpy.ops.export_scene.fbx(
        filepath=fbx_path,
        # Selección
        use_selection=False,
        use_visible=False,
        use_active_collection=False,
        
        # Escala y transformación
        global_scale=1.0,
        apply_unit_scale=True,
        apply_scale_options='FBX_SCALE_NONE',
        use_space_transform=True,
        bake_space_transform=False,
        
        # Tipos de objetos
        object_types={'ARMATURE', 'MESH'},
        use_mesh_modifiers=True,
        use_mesh_modifiers_render=True,
        mesh_smooth_type='FACE',
        colors_type='SRGB',
        
        # Armature
        use_armature_deform_only=False,
        armature_nodetype='NULL',
        add_leaf_bones=False,
        primary_bone_axis='Y',
        secondary_bone_axis='X',
        bake_anim_use_nla_strips=False,
        bake_anim_use_all_actions=False,
        
        # ANIMACIÓN - LA CLAVE
        bake_anim=True,
        bake_anim_use_all_bones=True,
        bake_anim_force_startend_keying=True,
        bake_anim_step=1.0,
        bake_anim_simplify_factor=0.0,
        
        # Otros
        path_mode='AUTO',
        embed_textures=True,
        batch_mode='OFF',
        use_batch_own_dir=False,
        use_metadata=True,
        
        # Eje y unidades
        axis_forward='-Z',
        axis_up='Y'
    )
    
    print(f"\n✓ FBX exportado a: {fbx_path}")
    
    # Verificar el archivo exportado
    print("\n" + "="*70)
    print("VERIFICANDO FBX EXPORTADO...")
    print("="*70)
    
    # Limpiar escena
    bpy.ops.wm.read_homefile(use_empty=True)
    
    # Importar el FBX recién exportado
    bpy.ops.import_scene.fbx(filepath=fbx_path)
    
    # Buscar armature
    arm_imported = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            arm_imported = obj
            break
    
    if arm_imported and arm_imported.animation_data and arm_imported.animation_data.action:
        action_imported = arm_imported.animation_data.action
        print(f"\n✓ Animación importada: {action_imported.name}")
        print(f"  Frames: {int(action_imported.frame_range[0])} - {int(action_imported.frame_range[1])}")
        print(f"  FCurves: {len(action_imported.fcurves)}")
        
        # Verificar un hueso específico
        for fc in action_imported.fcurves:
            if "RightArm" in fc.data_path and "rotation_quaternion" in fc.data_path and fc.array_index == 0:
                valores = [kf.co[1] for kf in fc.keyframe_points]
                unicos = len(set([round(v, 6) for v in valores]))
                print(f"\n  RightArm rotation_quaternion[0]:")
                print(f"    Keyframes: {len(valores)}")
                print(f"    Min: {min(valores):.6f}, Max: {max(valores):.6f}")
                print(f"    Valores únicos: {unicos}")
                
                if unicos > 10:
                    print(f"\n  ✓✓✓ LA ANIMACIÓN SE EXPORTÓ CORRECTAMENTE! ✓✓✓")
                else:
                    print(f"\n  ❌ La animación NO tiene variación (solo {unicos} valores únicos)")
                break
    else:
        print("\n❌ El FBX exportado NO tiene animación")
    
except Exception as e:
    print(f"\n❌ Error al exportar: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*70)
