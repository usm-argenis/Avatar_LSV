import bpy
import sys

# Obtener el archivo a inspeccionar
file_path = sys.argv[-1]

print(f"\n{'='*80}")
print(f"DIAGNÓSTICO COMPLETO DE REPRODUCCIÓN")
print(f"Archivo: {file_path}")
print(f"{'='*80}\n")

# Limpiar escena
bpy.ops.wm.read_factory_settings(use_empty=True)

# Importar el archivo
print("📥 Importando archivo...")
bpy.ops.import_scene.gltf(filepath=file_path)

# Buscar el armature
armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        armature = obj
        break

if not armature:
    print("❌ No se encontró armature")
    sys.exit(1)

print(f"✅ Armature encontrado: {armature.name}")

# Verificar animation_data
if not armature.animation_data:
    print("❌ El armature NO tiene animation_data")
    sys.exit(1)

print(f"✅ El armature tiene animation_data")

# Verificar acción activa
action = armature.animation_data.action
print(f"\n📋 Acción activa: {action.name if action else 'NINGUNA'}")
if action:
    print(f"   FCurves: {len(action.fcurves)}")
    print(f"   Frame range: {action.frame_range[0]} - {action.frame_range[1]}")

# Verificar NLA tracks
nla_tracks = armature.animation_data.nla_tracks
print(f"\n📊 NLA Tracks: {len(nla_tracks)}")
for track in nla_tracks:
    print(f"   Track: {track.name} | Mute: {track.mute} | Active: {track.is_solo}")
    for strip in track.strips:
        print(f"      Strip: {strip.name} | Frame: {strip.frame_start}-{strip.frame_end}")
        print(f"         Action: {strip.action.name if strip.action else 'None'}")
        print(f"         Influence: {strip.influence}")

# Verificar modo de uso de NLA
print(f"\n🎭 Use NLA: {armature.animation_data.use_nla}")

# Verificar todas las acciones disponibles
print(f"\n📚 Acciones en bpy.data.actions: {len(bpy.data.actions)}")
for act in bpy.data.actions:
    print(f"   - {act.name} ({len(act.fcurves)} FCurves)")

# PRUEBA: Configurar para reproducción
print(f"\n🔧 CONFIGURANDO PARA REPRODUCCIÓN...")

# Si hay NLA tracks, desactivar uso de NLA
if len(nla_tracks) > 0:
    print("   Desactivando uso de NLA...")
    armature.animation_data.use_nla = False
    
    # Tomar la acción del primer strip
    if len(nla_tracks[0].strips) > 0:
        strip_action = nla_tracks[0].strips[0].action
        if strip_action:
            print(f"   Asignando acción del strip como activa: {strip_action.name}")
            armature.animation_data.action = strip_action
            
            # Configurar timeline
            bpy.context.scene.frame_start = int(strip_action.frame_range[0])
            bpy.context.scene.frame_end = int(strip_action.frame_range[1])
            bpy.context.scene.frame_current = int(strip_action.frame_range[0])

# Verificar estado final
print(f"\n📋 ESTADO FINAL:")
print(f"   Use NLA: {armature.animation_data.use_nla}")
print(f"   Acción activa: {armature.animation_data.action.name if armature.animation_data.action else 'NINGUNA'}")
print(f"   Timeline: {bpy.context.scene.frame_start} - {bpy.context.scene.frame_end}")

print(f"\n{'='*80}")
print(f"CONCLUSIÓN:")
if armature.animation_data.action and not armature.animation_data.use_nla:
    print(f"✅ La animación DEBERÍA reproducirse correctamente")
else:
    print(f"❌ La animación NO se reproducirá")
    if armature.animation_data.use_nla:
        print(f"   Problema: use_nla=True está interfiriendo")
    if not armature.animation_data.action:
        print(f"   Problema: No hay acción activa")
print(f"{'='*80}\n")
