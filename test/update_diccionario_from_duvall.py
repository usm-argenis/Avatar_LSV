from pathlib import Path
import re

"""
Genera y actualiza la constante DICCIONARIO en animation_mobile.html
usando los GLB ubicados en test/output/glb/Duvall.

- Preserva las entradas existentes (aliases manuales) y suma las nuevas.
- Detecta el nombre de la categoría a partir de la carpeta que contiene el GLB
  (incluye subcarpetas como "medios transporte/terrestre").
- Usa el nombre del archivo sin prefijo "Duvall_resultado_" como clave y valor
  de "archivo".
"""

AVATAR = "Duvall"
PROJECT_ROOT = Path(__file__).resolve().parent
HTML_PATH = PROJECT_ROOT / "animation_mobile.html"
GLB_ROOT = PROJECT_ROOT / "output" / "glb" / AVATAR

BLOCK_RE = re.compile(r"const DICCIONARIO = \{(.*?)\n\s*\};", re.S)
ENTRY_RE = re.compile(r"'([^']+)'\s*:\s*\{\s*categoria:\s*'([^']+)'\s*,\s*archivo:\s*'([^']+)'\s*\}")


def load_html() -> str:
    return HTML_PATH.read_text(encoding="utf-8")


def parse_existing(html: str) -> dict[str, dict[str, str]]:
    match = BLOCK_RE.search(html)
    if not match:
        raise SystemExit("No se encontró la constante DICCIONARIO en animation_mobile.html")

    entries: dict[str, dict[str, str]] = {}
    for key, categoria, archivo in ENTRY_RE.findall(match.group(1)):
        entries[key] = {"categoria": categoria, "archivo": archivo}
    return entries


def collect_from_glb() -> dict[str, dict[str, str]]:
    if not GLB_ROOT.exists():
        raise SystemExit(f"No existe la carpeta de GLB: {GLB_ROOT}")

    generated: dict[str, dict[str, str]] = {}
    prefix = f"{AVATAR}_resultado_"

    for glb in GLB_ROOT.rglob("*.glb"):
        # Evitar el GLB base del avatar
        if glb.name.lower() == f"{AVATAR.lower()}.glb":
            continue

        rel = glb.relative_to(GLB_ROOT)
        categoria = rel.parent.as_posix()

        archivo = glb.stem
        if archivo.startswith(prefix):
            archivo = archivo[len(prefix):]

        palabra = archivo.lower()
        generated[palabra] = {"categoria": categoria, "archivo": archivo}

    return generated


def render_block(entries: dict[str, dict[str, str]]) -> str:
    lines = [
        "        const DICCIONARIO = {",
        "            // 📌 Generado automáticamente por update_diccionario_from_duvall.py",
    ]

    for key in sorted(entries):
        cat = entries[key]["categoria"]
        archivo = entries[key]["archivo"]
        lines.append(f"            '{key}': {{ categoria: '{cat}', archivo: '{archivo}' }},")

    lines.append("        };")
    return "\n".join(lines)


def write_html(html: str, block: str) -> None:
    new_html, count = BLOCK_RE.subn(block, html, count=1)
    if count != 1:
        raise SystemExit("No se pudo reemplazar la constante DICCIONARIO")

    if not new_html.endswith("\n"):
        new_html += "\n"

    HTML_PATH.write_text(new_html, encoding="utf-8")


def main() -> None:
    html = load_html()
    existentes = parse_existing(html)
    generados = collect_from_glb()

    merged = existentes.copy()
    merged.update(generados)

    block = render_block(merged)
    write_html(html, block)

    nuevos = len(set(generados) - set(existentes))
    print(f"DICCIONARIO actualizado: {len(merged)} entradas (nuevas: {nuevos})")


if __name__ == "__main__":
    main()
