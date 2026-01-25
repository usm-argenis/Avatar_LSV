from pathlib import Path
p=Path(r"C:\Users\andre\OneDrive\Documentos\tesis\output\Leonard_resultado_b.fbx")
if not p.exists():
    print('FBX not found:', p)
    raise SystemExit(1)

data=p.read_bytes()
strings=[b'Ch31_1001_Diffuse.png', b'Ch31_1001_Glossiness.png', b'Ch31']
for s in strings:
    print(s.decode(errors='ignore'), 'found' if data.find(s)!=-1 else 'not found')
