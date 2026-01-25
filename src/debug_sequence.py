from ai.motion_generator import MotionGenerator

g = MotionGenerator('data/keypoints')

print("\n1. Base de datos:")
print(f"   Señas: {list(g.sign_database.keys())}")

print("\n2. Datos de 'yo':")
yo = g.sign_database.get('yo')
print(f"   sign_name: {yo.get('sign_name')}")
print(f"   keyframes type: {type(yo.get('keyframes'))}")
print(f"   keyframes len: {len(yo.get('keyframes', []))}")

print("\n3. Llamando sequence_to_keyframes(['yo'])...")
result = g.sequence_to_keyframes(['yo'])

print(f"\n4. Resultado:")
print(f"   frames: {len(result.get('frames', []))}")
print(f"   duration: {result.get('duration')}")

if len(result.get('frames', [])) > 0:
    print(f"\n5. Primer frame:")
    print(f"   {result['frames'][0]}")
