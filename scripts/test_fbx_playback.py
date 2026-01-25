import bpy
import sys

# Obtener el archivo a inspeccionar
file_path = sys.argv[-1]

print(f"\n{'='*80}")
print(f"VERIFICACIÓN FBX")
print(f"Archivo: {file_path}")
print(f"{'='*80}\n")

# Limpiar escena
bpy.ops.wm.read_factory_settings(use_empty=True)

# Importar el archivo FBX
print("📥 Importando FBX...")
bpy.ops.import_scene.fbx(filepath=file_path)

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

print(f"✅ El armature TIENE animation_data")

# Verificar acción activa
action = armature.animation_data.action
if not action:
    print("❌ No hay acción activa")
else:
    print(f"\n✅ Acción activa: {action.name}")
    print(f"   FCurves: {len(action.fcurves)}")
    print(f"   Frame range: {action.frame_range[0]} - {action.frame_range[1]}")

# Verificar NLA tracks
nla_tracks = armature.animation_data.nla_tracks
print(f"\n📊 NLA Tracks: {len(nla_tracks)}")

# Verificar texturas
print(f"\n🖼️ Texturas: {len(bpy.data.images)}")

print(f"\n{'='*80}")
if action and len(action.fcurves) > 0:
    print(f"✅ LA ANIMACIÓN FUNCIONA EN FBX!")
else:
    print(f"❌ FBX tampoco tiene animación")
print(f"{'='*80}\n")
