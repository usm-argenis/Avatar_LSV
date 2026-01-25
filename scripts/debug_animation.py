import bpy
from pathlib import Path

# Limpiar escena
bpy.ops.wm.read_factory_settings(use_empty=True)

archivo = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nina\cortesia\Nina_resultado_cortesia.glb")

print(f"\n{'='*80}")
print(f"DIAGNÓSTICO: {archivo.name}")
print(f"{'='*80}")

# Importar archivo
bpy.ops.import_scene.gltf(filepath=str(archivo))

# Buscar armature
armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        armature = obj
        break

if not armature:
    print("❌ No se encontró armature")
else:
    print(f"✅ Armature encontrado: {armature.name}")
    
    # Verificar animation_data
    if not armature.animation_data:
        print("❌ No tiene animation_data")
    else:
        print("✅ Tiene animation_data")
        
        # Verificar action
        if not armature.animation_data.action:
            print("❌ No tiene action asignada")
        else:
            action = armature.animation_data.action
            print(f"✅ Action: {action.name}")
            print(f"   FCurves: {len(action.fcurves)}")
            
            if len(action.fcurves) > 0:
                # Obtener rango de frames
                frame_start = min([min([kf.co[0] for kf in fc.keyframe_points]) for fc in action.fcurves])
                frame_end = max([max([kf.co[0] for kf in fc.keyframe_points]) for fc in action.fcurves])
                print(f"   Frame range: {frame_start} - {frame_end}")
                
                # Mostrar algunos FCurves
                print(f"\n   Primeras 10 FCurves:")
                for i, fc in enumerate(action.fcurves[:10]):
                    bone_match = fc.data_path.split('"')[1] if '"' in fc.data_path else "?"
                    keyframes = len(fc.keyframe_points)
                    print(f"      {i+1}. {bone_match} - {fc.data_path.split('.')[-1]} ({keyframes} keyframes)")
            else:
                print("   ⚠️ No tiene FCurves")

# Verificar NLA tracks
if armature and armature.animation_data:
    nla_tracks = armature.animation_data.nla_tracks
    if len(nla_tracks) > 0:
        print(f"\n⚠️ Tiene {len(nla_tracks)} NLA tracks (esto podría ser el problema)")
        for track in nla_tracks:
            print(f"   Track: {track.name}")
            for strip in track.strips:
                print(f"      Strip: {strip.name} | Action: {strip.action.name if strip.action else 'None'}")
    else:
        print(f"\n✅ No tiene NLA tracks")

# Verificar acciones en bpy.data.actions
print(f"\n📋 Acciones disponibles en bpy.data.actions: {len(bpy.data.actions)}")
for action in bpy.data.actions:
    print(f"   - {action.name} ({len(action.fcurves)} FCurves)")

# Verificar texturas
print(f"\n🖼️ Texturas (bpy.data.images): {len(bpy.data.images)}")

print(f"\n{'='*80}\n")
