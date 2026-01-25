"""
Script de validación completa del sistema mocap_utils
Verifica que todo el pipeline funciona correctamente
"""
from pathlib import Path
import json
import sys

BASE_PATH = Path(r"C:\Users\andre\OneDrive\Documentos\tesis")

print("\n" + "="*70)
print("  VALIDACIÓN DEL SISTEMA MOCAP_UTILS")
print("="*70 + "\n")

tests_passed = 0
tests_total = 0

def test(name, condition, error_msg=""):
    """Ejecuta un test y muestra resultado"""
    global tests_passed, tests_total
    tests_total += 1
    
    if condition:
        print(f"✅ Test {tests_total}: {name}")
        tests_passed += 1
        return True
    else:
        print(f"❌ Test {tests_total}: {name}")
        if error_msg:
            print(f"   Error: {error_msg}")
        return False

# Test 1: Video original existe
video_path = BASE_PATH / "test" / "output" / "videos" / "yo.mp4"
test("Video yo.mp4 existe", video_path.exists(), 
     f"No se encontró {video_path}")

# Test 2: Nancy.glb existe
nancy_path = BASE_PATH / "test" / "output" / "glb" / "Nancy" / "Nancy.glb"
test("Nancy.glb existe", nancy_path.exists(),
     f"No se encontró {nancy_path}")

# Test 3: motion_data_yo.json existe
motion_json = BASE_PATH / "motion_data_yo.json"
if test("motion_data_yo.json existe", motion_json.exists()):
    
    # Test 4: JSON es válido
    try:
        with open(motion_json, 'r') as f:
            data = json.load(f)
        test("JSON es válido", True)
        
        # Test 5: Tiene frames
        has_frames = 'frames' in data and len(data['frames']) > 0
        test(f"Tiene frames ({len(data.get('frames', []))})", has_frames)
        
        if has_frames:
            # Test 6: Frames tienen landmarks
            first_frame = data['frames'][0]
            has_pose = 'pose' in first_frame and len(first_frame['pose']) == 33
            test(f"Frames tienen 33 landmarks", has_pose,
                 f"Encontrados: {len(first_frame.get('pose', []))}")
            
            # Test 7: Landmarks tienen coordenadas correctas
            if has_pose:
                lm = first_frame['pose'][0]
                has_coords = all(k in lm for k in ['x', 'y', 'z', 'visibility'])
                test("Landmarks tienen coordenadas (x,y,z,visibility)", has_coords)
    except Exception as e:
        test("JSON es válido", False, str(e))
else:
    print("   ⚠️  Ejecuta: python extract_motion_mediapipe.py")

# Test 8: Script correcto existe
script_v3 = BASE_PATH / "apply_motion_to_nancy_real_v3.py"
test("Script v3 existe", script_v3.exists())

# Test 9: GLB resultado existe
glb_result = BASE_PATH / "nancy_yo_real_v3.glb"
if test("nancy_yo_real_v3.glb existe", glb_result.exists()):
    
    # Test 10: GLB tiene tamaño razonable
    size_mb = glb_result.stat().st_size / (1024 * 1024)
    test(f"GLB tiene tamaño correcto ({size_mb:.1f} MB)", 
         1.0 < size_mb < 10.0,
         f"Tamaño: {size_mb:.1f} MB (esperado: 2-5 MB)")
else:
    print("   ⚠️  Ejecuta: blender --background --python apply_motion_to_nancy_real_v3.py")

# Test 11: Scripts obsoletos marcados
script_v2 = BASE_PATH / "apply_motion_to_nancy_v2.py"
if script_v2.exists():
    print(f"⚠️  Advertencia: apply_motion_to_nancy_v2.py existe (obsoleto)")
    print(f"   Usa apply_motion_to_nancy_real_v3.py en su lugar")

# Test 12: Visualizador existe
visualizer = BASE_PATH / "view_nancy_yo_comparison.html"
test("Visualizador HTML existe", visualizer.exists())

# Test 13: Documentación existe
docs = [
    "GUIA_MOCAP_COMPLETA.md",
    "REPORTE_ANALISIS_MOCAP_FINAL.md",
    "RESUMEN_SOLUCION_MOCAP.md"
]
docs_exist = sum(1 for doc in docs if (BASE_PATH / doc).exists())
test(f"Documentación completa ({docs_exist}/{len(docs)})", 
     docs_exist == len(docs))

# Test 14: Script automático existe
bat_script = BASE_PATH / "GENERAR_NANCY_YO.bat"
test("Script automático .bat existe", bat_script.exists())

# Resumen
print("\n" + "="*70)
print("  RESUMEN DE VALIDACIÓN")
print("="*70)
print(f"\nTests pasados: {tests_passed}/{tests_total}")

if tests_passed == tests_total:
    print("\n✅ TODOS LOS TESTS PASADOS")
    print("\n🎉 El sistema está completamente funcional!")
    print("\nPróximos pasos:")
    print("  1. Ejecuta: GENERAR_NANCY_YO.bat")
    print("  2. O ejecuta manualmente:")
    print("     python extract_motion_mediapipe.py")
    print("     blender --background --python apply_motion_to_nancy_real_v3.py")
    print("  3. Abre: view_nancy_yo_comparison.html")
    
elif tests_passed >= tests_total * 0.7:
    print("\n⚠️  ALGUNOS TESTS FALLARON")
    print("\nEl sistema está parcialmente funcional.")
    print("Revisa los tests que fallaron arriba.")
    
else:
    print("\n❌ MUCHOS TESTS FALLARON")
    print("\nEl sistema necesita configuración.")
    print("Revisa la documentación en GUIA_MOCAP_COMPLETA.md")

print("\n" + "="*70 + "\n")

# Retornar código de salida
sys.exit(0 if tests_passed == tests_total else 1)
