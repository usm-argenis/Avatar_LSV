#!/usr/bin/env python3
"""
Script para inspeccionar archivos GLB y detectar problemas de orientación
"""
import json
import struct
from pathlib import Path

def leer_glb(ruta_glb):
    """Lee y analiza un archivo GLB"""
    with open(ruta_glb, 'rb') as f:
        # Leer header GLB
        magic = f.read(4)
        if magic != b'glTF':
            print(f"❌ No es un archivo GLB válido")
            return None
        
        version = struct.unpack('<I', f.read(4))[0]
        length = struct.unpack('<I', f.read(4))[0]
        
        print(f"📦 Archivo GLB válido")
        print(f"   Versión: {version}")
        print(f"   Tamaño: {length} bytes ({length/1024:.2f} KB)")
        
        # Leer chunk JSON
        chunk_length = struct.unpack('<I', f.read(4))[0]
        chunk_type = f.read(4)
        
        if chunk_type != b'JSON':
            print(f"❌ Chunk JSON no encontrado")
            return None
        
        json_data = f.read(chunk_length).decode('utf-8')
        gltf = json.loads(json_data)
        
        return gltf

def analizar_animaciones(gltf, nombre_archivo):
    """Analiza las animaciones en el archivo GLTF"""
    print(f"\n{'='*70}")
    print(f"🔍 ANÁLISIS DE: {nombre_archivo}")
    print(f"{'='*70}")
    
    # Información general
    if 'asset' in gltf:
        print(f"\n📄 Asset Info:")
        print(f"   Generator: {gltf['asset'].get('generator', 'N/A')}")
        print(f"   Version: {gltf['asset'].get('version', 'N/A')}")
    
    # Nodos y transformaciones
    if 'nodes' in gltf:
        print(f"\n🔗 Nodos: {len(gltf['nodes'])}")
        for i, node in enumerate(gltf['nodes']):
            if 'rotation' in node or 'scale' in node or 'translation' in node:
                print(f"\n   Node {i}: {node.get('name', 'Sin nombre')}")
                if 'rotation' in node:
                    rot = node['rotation']
                    print(f"      Rotación: [{rot[0]:.4f}, {rot[1]:.4f}, {rot[2]:.4f}, {rot[3]:.4f}]")
                if 'scale' in node:
                    scale = node['scale']
                    print(f"      Escala: [{scale[0]:.4f}, {scale[1]:.4f}, {scale[2]:.4f}]")
                    # Detectar escala negativa (causa de volteo)
                    if any(s < 0 for s in scale):
                        print(f"      ⚠️ ESCALA NEGATIVA DETECTADA - Causa volteo!")
                if 'translation' in node:
                    trans = node['translation']
                    print(f"      Posición: [{trans[0]:.4f}, {trans[1]:.4f}, {trans[2]:.4f}]")
    
    # Animaciones
    if 'animations' in gltf:
        print(f"\n🎬 Animaciones: {len(gltf['animations'])}")
        for i, anim in enumerate(gltf['animations']):
            print(f"\n   Animación {i}: {anim.get('name', 'Sin nombre')}")
            print(f"      Channels: {len(anim.get('channels', []))}")
            print(f"      Samplers: {len(anim.get('samplers', []))}")
            
            # Analizar channels
            for j, channel in enumerate(anim.get('channels', [])):
                target = channel.get('target', {})
                path = target.get('path', 'N/A')
                node_idx = target.get('node', -1)
                print(f"         Channel {j}: path={path}, node={node_idx}")
    
    # Meshes
    if 'meshes' in gltf:
        print(f"\n🎭 Meshes: {len(gltf['meshes'])}")
        for i, mesh in enumerate(gltf['meshes']):
            print(f"   Mesh {i}: {mesh.get('name', 'Sin nombre')}")
            print(f"      Primitives: {len(mesh.get('primitives', []))}")
    
    # Skins (armature)
    if 'skins' in gltf:
        print(f"\n🦴 Skins: {len(gltf['skins'])}")
        for i, skin in enumerate(gltf['skins']):
            print(f"   Skin {i}: {skin.get('name', 'Sin nombre')}")
            print(f"      Joints: {len(skin.get('joints', []))}")
            print(f"      Skeleton root: {skin.get('skeleton', 'N/A')}")
    
    # Scenes
    if 'scenes' in gltf:
        print(f"\n🎨 Scenes: {len(gltf['scenes'])}")
        default_scene = gltf.get('scene', 0)
        print(f"   Escena por defecto: {default_scene}")
        for i, scene in enumerate(gltf['scenes']):
            print(f"   Scene {i}: {scene.get('name', 'Sin nombre')}")
            print(f"      Nodes: {scene.get('nodes', [])}")
    
    return gltf

def detectar_problemas(gltf):
    """Detecta problemas comunes que causan volteo"""
    print(f"\n{'='*70}")
    print(f"🔎 DETECCIÓN DE PROBLEMAS")
    print(f"{'='*70}")
    
    problemas = []
    
    # 1. Escala negativa
    if 'nodes' in gltf:
        for i, node in enumerate(gltf['nodes']):
            if 'scale' in node:
                scale = node['scale']
                if any(s < 0 for s in scale):
                    problemas.append(f"⚠️ Node {i} ({node.get('name', 'N/A')}): Escala negativa {scale}")
    
    # 2. Rotaciones inusuales en root
    if 'scenes' in gltf and 'nodes' in gltf:
        default_scene = gltf.get('scene', 0)
        root_nodes = gltf['scenes'][default_scene].get('nodes', [])
        for node_idx in root_nodes:
            node = gltf['nodes'][node_idx]
            if 'rotation' in node:
                rot = node['rotation']
                # Verificar rotación de 180 grados en X o Z (causa volteo)
                if abs(rot[0]) > 0.7 or abs(rot[2]) > 0.7:  # ~90-180 grados
                    problemas.append(f"⚠️ Root node {node_idx}: Rotación inusual {rot}")
    
    # 3. Múltiples escenas
    if 'scenes' in gltf and len(gltf['scenes']) > 1:
        problemas.append(f"ℹ️ Múltiples escenas detectadas: {len(gltf['scenes'])}")
    
    if problemas:
        print("\n🚨 Problemas encontrados:")
        for problema in problemas:
            print(f"   {problema}")
    else:
        print("\n✅ No se detectaron problemas evidentes")
    
    return problemas

def sugerir_solucion(problemas):
    """Sugiere soluciones basadas en los problemas encontrados"""
    if not problemas:
        return
    
    print(f"\n{'='*70}")
    print(f"💡 SOLUCIONES SUGERIDAS")
    print(f"{'='*70}")
    
    if any("Escala negativa" in p for p in problemas):
        print("\n1. ESCALA NEGATIVA:")
        print("   • En Blender: Apply Scale (Ctrl+A > Scale)")
        print("   • Verificar que todas las escalas sean positivas")
        print("   • Re-exportar el GLB")
    
    if any("Rotación inusual" in p for p in problemas):
        print("\n2. ROTACIÓN INUSUAL:")
        print("   • En Blender: Apply Rotation (Ctrl+A > Rotation)")
        print("   • Verificar eje forward/up en opciones de exportación")
        print("   • Probar diferentes combinaciones de ejes (Y forward, Z up)")

# Programa principal
if __name__ == "__main__":
    archivo = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.glb")
    
    if not archivo.exists():
        print(f"❌ Archivo no encontrado: {archivo}")
        exit(1)
    
    print(f"📂 Analizando: {archivo.name}")
    print(f"📍 Ruta: {archivo.parent}")
    print(f"📏 Tamaño: {archivo.stat().st_size / 1024:.2f} KB")
    
    # Leer GLB
    gltf = leer_glb(archivo)
    
    if gltf:
        # Analizar contenido
        analizar_animaciones(gltf, archivo.name)
        
        # Detectar problemas
        problemas = detectar_problemas(gltf)
        
        # Sugerir soluciones
        sugerir_solucion(problemas)
        
        # Guardar JSON para inspección manual
        json_output = archivo.parent / f"{archivo.stem}_analisis.json"
        with open(json_output, 'w', encoding='utf-8') as f:
            json.dump(gltf, f, indent=2)
        
        print(f"\n💾 JSON guardado en: {json_output.name}")
    
    print(f"\n{'='*70}")
    print("✅ Análisis completado")
    print(f"{'='*70}")
