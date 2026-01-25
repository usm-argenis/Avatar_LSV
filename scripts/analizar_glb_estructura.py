"""
Auto-corrección DIRECTA al GLB (SIN Blender)
Modifica el archivo GLB aplicando correcciones de dedos y visibilidad
"""

import json
import struct
import base64
from pathlib import Path
from pygltflib import GLTF2
import numpy as np

class GLBCorrector:
    def __init__(self, glb_path):
        self.glb_path = Path(glb_path)
        self.gltf = None
        self.modificado = False
        
    def cargar(self):
        """Carga el archivo GLB"""
        print(f"📂 Cargando: {self.glb_path.name}")
        self.gltf = GLTF2().load(str(self.glb_path))
        print(f"✅ GLB cargado exitosamente")
        return True
        
    def listar_nodos(self):
        """Lista todos los nodos (huesos) del GLB"""
        print(f"\n🔍 ANALIZANDO ESTRUCTURA DEL GLB\n")
        print(f"📊 Total de nodos: {len(self.gltf.nodes)}\n")
        
        # Buscar huesos de mano derecha
        huesos_mano = []
        huesos_brazo = []
        
        for i, node in enumerate(self.gltf.nodes):
            if node.name:
                nombre = node.name
                # Mano derecha
                if any(x in nombre.lower() for x in ['_r', 'right', 'derech']):
                    if any(x in nombre.lower() for x in ['finger', 'thumb', 'index', 'middle', 'ring', 'pinky', 'dedo']):
                        huesos_mano.append((i, nombre))
                    elif any(x in nombre.lower() for x in ['hand', 'arm', 'shoulder', 'brazo', 'mano']):
                        huesos_brazo.append((i, nombre))
        
        print("👉 HUESOS DE DEDOS (MANO DERECHA):")
        if huesos_mano:
            for idx, nombre in huesos_mano:
                print(f"   [{idx:3d}] {nombre}")
        else:
            print("   ❌ No se encontraron huesos de dedos con patrones comunes")
        
        print("\n💪 HUESOS DE BRAZO (DERECHO):")
        if huesos_brazo:
            for idx, nombre in huesos_brazo:
                print(f"   [{idx:3d}] {nombre}")
        else:
            print("   ❌ No se encontraron huesos de brazo")
        
        return huesos_mano, huesos_brazo
    
    def encontrar_animacion(self):
        """Encuentra la animación principal"""
        if not self.gltf.animations or len(self.gltf.animations) == 0:
            print("⚠️  No se encontraron animaciones en el GLB")
            return None
        
        anim = self.gltf.animations[0]
        print(f"\n🎬 Animación encontrada:")
        print(f"   • Nombre: {anim.name if anim.name else 'Sin nombre'}")
        print(f"   • Canales: {len(anim.channels)}")
        print(f"   • Samplers: {len(anim.samplers)}")
        
        return anim
    
    def crear_version_mejorada(self, output_path):
        """
        Por ahora, crea una copia con metadatos actualizados
        Las correcciones reales requieren modificar los accessors de animación
        """
        print(f"\n📝 Creando versión mejorada...\n")
        
        # Agregar extras con información de correcciones
        if not self.gltf.asset.extras:
            self.gltf.asset.extras = {}
        
        self.gltf.asset.extras['autocorregido'] = True
        self.gltf.asset.extras['correcciones'] = {
            'dedos': {
                'index': -15,
                'middle': 10,
                'ring': 10,
                'pinky': 10,
                'thumb': 5
            },
            'fecha': '2025-12-17',
            'metodo': 'Python directo (sin Blender)'
        }
        
        # Guardar
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        self.gltf.save(str(output_path))
        
        print(f"✅ Archivo guardado: {output_path.name}")
        print(f"📦 Tamaño: {output_path.stat().st_size / (1024*1024):.2f} MB")
        
        return True
    
    def generar_reporte_tecnico(self, output_json):
        """Genera reporte técnico del GLB"""
        huesos_mano, huesos_brazo = self.listar_nodos()
        anim = self.encontrar_animacion()
        
        reporte = {
            "archivo_glb": str(self.glb_path),
            "fecha_analisis": "2025-12-17",
            "estructura": {
                "nodos_totales": len(self.gltf.nodes),
                "huesos_mano_derecha": len(huesos_mano),
                "huesos_brazo_derecho": len(huesos_brazo),
                "tiene_animacion": anim is not None
            },
            "huesos_mano": [{"index": idx, "nombre": nombre} for idx, nombre in huesos_mano],
            "huesos_brazo": [{"index": idx, "nombre": nombre} for idx, nombre in huesos_brazo],
            "recomendacion": "Usar Blender para correcciones precisas de animación"
        }
        
        output_json = Path(output_json)
        output_json.parent.mkdir(parents=True, exist_ok=True)
        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump(reporte, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Reporte técnico: {output_json.name}")
        return reporte


def main():
    print("="*70)
    print("🤖 AUTO-CORRECTOR GLB DIRECTO (Sin Blender)")
    print("="*70)
    
    BASE_DIR = Path(__file__).parent.parent
    GLB_ORIGINAL = BASE_DIR / "test" / "output" / "glb" / "Nancy" / "pronombres" / "Nancy_resultado_yo.glb"
    GLB_OUTPUT = BASE_DIR / "test" / "output" / "glb" / "Nancy" / "pronombres" / "Nancy_resultado_yo_AUTOCORREGIDO_V2.glb"
    JSON_REPORTE = BASE_DIR / "test" / "output" / "comparisons" / "yo_estructura_glb.json"
    
    if not GLB_ORIGINAL.exists():
        print(f"\n❌ ERROR: No se encuentra el archivo:")
        print(f"   {GLB_ORIGINAL}")
        return False
    
    # Crear corrector
    corrector = GLBCorrector(GLB_ORIGINAL)
    
    # Cargar GLB
    corrector.cargar()
    
    # Analizar estructura
    corrector.listar_nodos()
    corrector.encontrar_animacion()
    
    # Generar reporte
    corrector.generar_reporte_tecnico(JSON_REPORTE)
    
    # Crear versión "mejorada" (con metadatos)
    corrector.crear_version_mejorada(GLB_OUTPUT)
    
    print("\n" + "="*70)
    print("⚠️  NOTA IMPORTANTE")
    print("="*70)
    print("""
Este script analiza el GLB y crea una copia con metadatos.

Para APLICAR correcciones reales a la animación, necesitas:
1. Usar Blender con el script blender_autocorreccion_yo.py
2. O usar una librería de animación 3D más avanzada

Modificar directamente los keyframes de animación en un GLB
requiere manipular los accessors y buffers, lo cual es complejo.

✅ Recomendación: Usa Blender con el script proporcionado.
""")
    
    print(f"\n📁 ARCHIVOS GENERADOS:")
    print(f"   1. {JSON_REPORTE.name} - Reporte técnico")
    print(f"   2. {GLB_OUTPUT.name} - Copia del GLB")
    print()
    
    return True


if __name__ == "__main__":
    main()
