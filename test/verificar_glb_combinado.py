"""
Verificación programática del GLB combinado
Analiza el archivo GLB para confirmar que tiene la animación correcta
"""

import json
import struct
import os

glb_path = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_brazos_combinado.glb"

print("="*80)
print("VERIFICACIÓN PROGRAMÁTICA DEL GLB COMBINADO")
print("="*80)
print(f"\nArchivo: {glb_path}")
print(f"Tamaño: {os.path.getsize(glb_path) / (1024*1024):.2f} MB\n")

# Leer el archivo GLB
with open(glb_path, 'rb') as f:
    # Header GLB (12 bytes)
    magic = struct.unpack('I', f.read(4))[0]
    version = struct.unpack('I', f.read(4))[0]
    length = struct.unpack('I', f.read(4))[0]
    
    print(f"GLB Header:")
    print(f"  Magic: 0x{magic:X} (esperado: 0x46546C67)")
    print(f"  Version: {version}")
    print(f"  Length: {length} bytes")
    
    # Chunk 0: JSON (metadata)
    chunk_length = struct.unpack('I', f.read(4))[0]
    chunk_type = struct.unpack('I', f.read(4))[0]
    
    json_data = f.read(chunk_length).decode('utf-8')
    gltf = json.loads(json_data)
    
    print(f"\n📊 Análisis del contenido:")
    print(f"  Nodos: {len(gltf.get('nodes', []))}")
    print(f"  Meshes: {len(gltf.get('meshes', []))}")
    print(f"  Materiales: {len(gltf.get('materials', []))}")
    print(f"  Texturas: {len(gltf.get('textures', []))}")
    print(f"  Skins: {len(gltf.get('skins', []))}")
    print(f"  Animaciones: {len(gltf.get('animations', []))}")
    
    # Analizar animaciones
    if 'animations' in gltf and len(gltf['animations']) > 0:
        print(f"\n🎬 Animaciones encontradas:")
        
        for idx, anim in enumerate(gltf['animations']):
            anim_name = anim.get('name', f'Animación {idx}')
            channels = anim.get('channels', [])
            samplers = anim.get('samplers', [])
            
            print(f"\n  Animación: {anim_name}")
            print(f"    Canales: {len(channels)}")
            print(f"    Samplers: {len(samplers)}")
            
            # Analizar qué huesos están animados
            animated_bones = set()
            arm_bones_animated = []
            
            arm_bone_keywords = ['Shoulder', 'Arm', 'ForeArm', 'Hand']
            
            for channel in channels:
                target = channel.get('target', {})
                node_idx = target.get('node')
                
                if node_idx is not None and node_idx < len(gltf['nodes']):
                    node_name = gltf['nodes'][node_idx].get('name', f'Node{node_idx}')
                    animated_bones.add(node_name)
                    
                    # Verificar si es un hueso de brazo
                    if any(keyword in node_name for keyword in arm_bone_keywords):
                        property_type = target.get('path', 'unknown')
                        arm_bones_animated.append(f"{node_name} ({property_type})")
            
            print(f"    Huesos animados: {len(animated_bones)}")
            
            if arm_bones_animated:
                print(f"\n    ✅ HUESOS DE BRAZOS ANIMADOS ({len(arm_bones_animated)} canales):")
                # Agrupar por hueso
                bone_channels = {}
                for entry in arm_bones_animated:
                    bone_name = entry.split(' (')[0]
                    prop = entry.split('(')[1].rstrip(')')
                    if bone_name not in bone_channels:
                        bone_channels[bone_name] = []
                    bone_channels[bone_name].append(prop)
                
                for bone, props in sorted(bone_channels.items()):
                    print(f"      • {bone}: {', '.join(props)}")
            else:
                print(f"\n    ⚠️  NO SE DETECTARON HUESOS DE BRAZOS ANIMADOS")
            
            # Verificar rango de tiempo
            if samplers:
                print(f"\n    Detalles de samplers:")
                for s_idx, sampler in enumerate(samplers[:3]):  # Mostrar solo los primeros 3
                    accessor_idx = sampler.get('input')
                    if accessor_idx is not None:
                        accessor = gltf['accessors'][accessor_idx]
                        min_time = accessor.get('min', [0])[0] if 'min' in accessor else 0
                        max_time = accessor.get('max', [0])[0] if 'max' in accessor else 0
                        print(f"      Sampler {s_idx}: {min_time:.2f}s - {max_time:.2f}s (duración: {max_time-min_time:.2f}s)")
    
    else:
        print("\n❌ NO SE ENCONTRARON ANIMACIONES EN EL GLB")

print("\n" + "="*80)
print("RESULTADO DE LA VERIFICACIÓN")
print("="*80)

if 'animations' in gltf and len(gltf['animations']) > 0:
    has_arm_animation = False
    for anim in gltf['animations']:
        for channel in anim.get('channels', []):
            node_idx = channel.get('target', {}).get('node')
            if node_idx is not None and node_idx < len(gltf['nodes']):
                node_name = gltf['nodes'][node_idx].get('name', '')
                if any(keyword in node_name for keyword in ['Shoulder', 'Arm', 'ForeArm', 'Hand']):
                    has_arm_animation = True
                    break
        if has_arm_animation:
            break
    
    if has_arm_animation:
        print("✅ VERIFICACIÓN EXITOSA")
        print("   El archivo GLB contiene animación de brazos")
        print("   Listo para visualizar en navegador")
    else:
        print("⚠️  ADVERTENCIA")
        print("   El archivo tiene animación pero no se detectaron brazos")
else:
    print("❌ VERIFICACIÓN FALLIDA")
    print("   El archivo NO contiene animaciones")

print("="*80)
