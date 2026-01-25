"""
Script para aplicar una animación de Remy a Justin
Analiza los nombres de los huesos y mapea las animaciones
"""
import bpy
import sys
import argparse
from pathlib import Path

def limpiar_escena():
    """Limpiar toda la escena"""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    # Limpiar datos huérfanos
    for block in bpy.data.meshes:
        if block.users == 0:
            bpy.data.meshes.remove(block)
    
    for block in bpy.data.materials:
        if block.users == 0:
            bpy.data.materials.remove(block)
    
    for block in bpy.data.textures:
        if block.users == 0:
            bpy.data.textures.remove(block)
    
    for block in bpy.data.images:
        if block.users == 0:
            bpy.data.images.remove(block)

def listar_huesos(armature, nombre_modelo):
    """Listar todos los huesos de un armature"""
    print(f"\n🦴 Huesos de {nombre_modelo}:")
    print("=" * 60)
    
    huesos = {}
    for bone in armature.data.bones:
        huesos[bone.name.lower()] = bone.name
        print(f"   - {bone.name}")
    
    return huesos

def analizar_compatibilidad(huesos_destino, huesos_origen):
    """Analizar compatibilidad entre esqueletos"""
    print(f"\n🔍 ANÁLISIS DE COMPATIBILIDAD")
    print("=" * 60)
    
    compatibles = []
    incompatibles = []
    
    for hueso_origen_lower, hueso_origen_name in huesos_origen.items():
        if hueso_origen_lower in huesos_destino:
            compatibles.append(hueso_origen_name)
        else:
            # Intentar mapeo aproximado
            encontrado = False
            for hueso_destino_lower, hueso_destino_name in huesos_destino.items():
                if hueso_origen_lower in hueso_destino_lower or hueso_destino_lower in hueso_origen_lower:
                    compatibles.append(f"{hueso_origen_name} → {hueso_destino_name}")
                    encontrado = True
                    break
            
            if not encontrado:
                incompatibles.append(hueso_origen_name)
    
    print(f"\n✅ Huesos compatibles: {len(compatibles)}")
    for hueso in compatibles[:10]:  # Mostrar primeros 10
        print(f"   ✓ {hueso}")
    if len(compatibles) > 10:
        print(f"   ... y {len(compatibles) - 10} más")
    
    print(f"\n⚠️  Huesos incompatibles: {len(incompatibles)}")
    for hueso in incompatibles[:10]:
        print(f"   ✗ {hueso}")
    if len(incompatibles) > 10:
        print(f"   ... y {len(incompatibles) - 10} más")
    
    porcentaje = (len(compatibles) / len(huesos_origen)) * 100
    print(f"\n📊 Compatibilidad: {porcentaje:.1f}%")
    
    return compatibles, incompatibles

def probar_animacion_en_justin():
    """Probar aplicar animación de Remy a Ch12_nonPBR"""
    
    print("=" * 80)
    print("🎬 PRUEBA DE ANIMACIÓN: CH12_NONPBR + REMY")
    print("=" * 80)
    
    # Rutas absolutas
    base_path = Path("C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb")
    ch12_path = base_path / "cc" / "Ch12_nonPBR (1).fbx"
    remy_animacion_path = base_path / "alfabeto" / "Remy_resultado_b.glb"
    output_path = base_path / "cc" / "Ch12_con_animacion_b.fbx"
    
    # Verificar archivos
    if not ch12_path.exists():
        print(f"❌ Error: No se encuentra {ch12_path}")
        return
    
    if not remy_animacion_path.exists():
        print(f"❌ Error: No se encuentra {remy_animacion_path}")
        return
    
    print(f"\n📁 Ch12: {ch12_path}")
    print(f"📁 Animación: {remy_animacion_path}")
    
    # Limpiar escena
    limpiar_escena()
    
    # Cargar Ch12
    print("\n📥 Cargando Ch12...")
    bpy.ops.import_scene.fbx(filepath=str(ch12_path))
    
    # Buscar armature de Ch12
    ch12_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            ch12_armature = obj
            break
    
    if not ch12_armature:
        print("❌ Error: No se encontró armature en Ch12")
        return
    
    print(f"✅ Armature de Ch12: {ch12_armature.name}")
    
    # Listar huesos de Ch12
    huesos_ch12 = listar_huesos(ch12_armature, "Ch12")
    
    # Cargar animación de Remy
    print(f"\n📥 Cargando animación de Remy...")
    bpy.ops.import_scene.gltf(filepath=str(remy_animacion_path))
    
    # Buscar armature de Remy
    remy_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE' and obj != ch12_armature:
            remy_armature = obj
            break
    
    if not remy_armature:
        print("❌ Error: No se encontró armature de Remy en la animación")
        return
    
    print(f"✅ Armature de Remy: {remy_armature.name}")
    
    # Listar huesos de Remy
    huesos_remy = listar_huesos(remy_armature, "Remy")
    
    # Analizar compatibilidad
    compatibles, incompatibles = analizar_compatibilidad(huesos_ch12, huesos_remy)
    
    # Intentar transferir animación
    print(f"\n🔄 Intentando transferir animación...")
    
    if not remy_armature.animation_data or not remy_armature.animation_data.action:
        print("❌ Error: No se encontró animación en Remy")
        return
    
    remy_action = remy_armature.animation_data.action
    print(f"✅ Acción encontrada: {remy_action.name}")
    print(f"   Frames: {int(remy_action.frame_range[0])} → {int(remy_action.frame_range[1])}")
    
    # Método 1: Copiar action directamente (si los huesos son compatibles)
    if len(compatibles) / len(huesos_remy) > 0.8:  # 80% compatible
        print(f"\n🎯 Esqueletos son {(len(compatibles) / len(huesos_remy) * 100):.1f}% compatibles")
        print("   Intentando copia directa de animación...")
        
        if not ch12_armature.animation_data:
            ch12_armature.animation_data_create()
        
        ch12_armature.animation_data.action = remy_action.copy()
        
        print("✅ Animación copiada exitosamente!")
    else:
        print(f"\n⚠️  Esqueletos son solo {(len(compatibles) / len(huesos_remy) * 100):.1f}% compatibles")
        print("   Se requiere retargeting manual o uso de NLA")
    
    # Guardar resultado
    print(f"\n💾 Guardando resultado en: {output_path}")
    
    # Seleccionar solo Ch12 para exportar
    bpy.ops.object.select_all(action='DESELECT')
    ch12_armature.select_set(True)
    
    # También seleccionar meshes hijos de Ch12
    for obj in bpy.data.objects:
        if obj.parent == ch12_armature:
            obj.select_set(True)
    
    bpy.ops.export_scene.fbx(
        filepath=str(output_path),
        use_selection=True,
        bake_anim=True
    )
    
    print("✅ Exportación completada!")
    
    print("\n" + "=" * 80)
    print("✅ PRUEBA COMPLETADA")
    print("=" * 80)
    print(f"\n📁 Archivo generado: {output_path}")
    print(f"📊 Compatibilidad: {(len(compatibles) / len(huesos_remy) * 100):.1f}%")

if __name__ == "__main__":
    probar_animacion_en_justin()
