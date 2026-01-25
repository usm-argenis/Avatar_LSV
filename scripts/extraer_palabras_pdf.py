"""
Script para extraer palabras del PDF de Curso LSV Básico 1
Extrae el texto y genera una lista de palabras/señas para el sistema
"""

import PyPDF2
import re
from pathlib import Path

def extraer_texto_pdf(pdf_path):
    """Extrae todo el texto del PDF"""
    texto_completo = []
    
    try:
        with open(pdf_path, 'rb') as archivo:
            lector = PyPDF2.PdfReader(archivo)
            num_paginas = len(lector.pages)
            
            print(f"📄 Procesando PDF: {pdf_path.name}")
            print(f"📊 Total de páginas: {num_paginas}\n")
            
            for i, pagina in enumerate(lector.pages, 1):
                texto = pagina.extract_text()
                texto_completo.append(texto)
                print(f"Página {i}/{num_paginas} procesada")
            
            return '\n'.join(texto_completo)
    
    except Exception as e:
        print(f"❌ Error al leer PDF: {e}")
        return None

def extraer_palabras_lsv(texto):
    """Extrae palabras relevantes del texto"""
    if not texto:
        return []
    
    # Dividir en líneas y limpiar
    lineas = texto.split('\n')
    palabras_encontradas = set()
    
    # Patrones comunes en cursos LSV
    patrones_sena = [
        r'Seña[:\s]+(.+)',
        r'Palabra[:\s]+(.+)',
        r'Vocabulario[:\s]+(.+)',
        r'^\s*[•\-]\s*(.+)',  # Listas con viñetas
    ]
    
    for linea in lineas:
        linea = linea.strip()
        
        # Buscar patrones específicos
        for patron in patrones_sena:
            match = re.search(patron, linea, re.IGNORECASE)
            if match:
                palabra = match.group(1).strip().lower()
                palabra = re.sub(r'[^\w\sáéíóúñ]', '', palabra)
                if palabra and len(palabra) > 1:
                    palabras_encontradas.add(palabra)
        
        # También agregar palabras individuales relevantes
        palabras = linea.split()
        for palabra in palabras:
            palabra_limpia = re.sub(r'[^\w\sáéíóúñ]', '', palabra.lower())
            # Filtrar palabras muy cortas o comunes que no son señas
            if (len(palabra_limpia) > 2 and 
                palabra_limpia not in ['el', 'la', 'los', 'las', 'un', 'una', 'de', 'del', 'al', 'con', 'por', 'para']):
                palabras_encontradas.add(palabra_limpia)
    
    return sorted(palabras_encontradas)

def guardar_palabras(palabras, output_file):
    """Guarda las palabras en un archivo de texto"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Palabras extraídas del PDF Curso LSV Básico 1\n")
        f.write(f"# Total: {len(palabras)} palabras\n\n")
        
        for palabra in palabras:
            f.write(f"{palabra}\n")
    
    print(f"\n✅ Palabras guardadas en: {output_file}")

def generar_codigo_python(palabras, output_file):
    """Genera código Python listo para agregar al optimizador"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Código para agregar a lsv_optimizer.py\n\n")
        f.write("# Agregar estas palabras al set de señas disponibles:\n")
        f.write("senas_curso_basico = {\n")
        
        for i, palabra in enumerate(palabras):
            if i < len(palabras) - 1:
                f.write(f"    '{palabra}',\n")
            else:
                f.write(f"    '{palabra}'\n")
        
        f.write("}\n\n")
        f.write("# Luego en cargar_senas_disponibles():\n")
        f.write("# senas.update(senas_curso_basico)\n")
    
    print(f"✅ Código Python generado en: {output_file}")

def main():
    # Ruta al PDF (está en la raíz del proyecto)
    base_path = Path(__file__).resolve().parent.parent
    pdf_path = base_path / "Modulo CursoLSV Basico 1 con fondo.pdf"
    
    if not pdf_path.exists():
        print(f"❌ No se encontró el archivo: {pdf_path}")
        return
    
    # Extraer texto
    print("=" * 60)
    print("🔍 EXTRACTOR DE PALABRAS LSV - PDF CURSO BÁSICO 1")
    print("=" * 60 + "\n")
    
    texto = extraer_texto_pdf(pdf_path)
    
    if texto:
        # Guardar texto completo para revisión
        texto_output = base_path / "data" / "pdf_texto_completo.txt"
        texto_output.parent.mkdir(exist_ok=True)
        with open(texto_output, 'w', encoding='utf-8') as f:
            f.write(texto)
        print(f"\n✅ Texto completo guardado en: {texto_output}")
        
        # Extraer palabras
        print("\n" + "=" * 60)
        print("🔤 EXTRAYENDO PALABRAS...")
        print("=" * 60 + "\n")
        
        palabras = extraer_palabras_lsv(texto)
        
        print(f"\n📊 Total de palabras encontradas: {len(palabras)}")
        print("\n🔍 Primeras 20 palabras:")
        for i, palabra in enumerate(palabras[:20], 1):
            print(f"  {i}. {palabra}")
        
        if len(palabras) > 20:
            print(f"  ... y {len(palabras) - 20} más")
        
        # Guardar resultados
        palabras_output = base_path / "data" / "palabras_lsv_curso_basico.txt"
        guardar_palabras(palabras, palabras_output)
        
        codigo_output = base_path / "data" / "codigo_palabras_lsv.py"
        generar_codigo_python(palabras, codigo_output)
        
        print("\n" + "=" * 60)
        print("✅ EXTRACCIÓN COMPLETADA")
        print("=" * 60)
        print("\nArchivos generados:")
        print(f"  1. {texto_output} (texto completo)")
        print(f"  2. {palabras_output} (lista de palabras)")
        print(f"  3. {codigo_output} (código Python)")
        
    else:
        print("❌ No se pudo extraer texto del PDF")

if __name__ == "__main__":
    main()
