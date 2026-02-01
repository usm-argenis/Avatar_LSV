#!/usr/bin/env python3
"""
Script para servir la aplicación LSV localmente y probarla
"""

import http.server
import socketserver
import os
import webbrowser
import time
from pathlib import Path

PORT = 8000
DIRECTORY = Path(__file__).parent.absolute()

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)
    
    def end_headers(self):
        # Agregar headers para CORS (en caso de que llames a otra API)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Logs más coloridos
        print(f"[{time.strftime('%H:%M:%S')}] {format % args}")

def main():
    os.chdir(DIRECTORY)
    
    print("╔════════════════════════════════════════════╗")
    print("║   🌐 Servidor LSV - GitHub Pages Local   ║")
    print("╚════════════════════════════════════════════╝\n")
    
    print(f"📁 Directorio: {DIRECTORY}")
    print(f"🔗 URL: http://localhost:{PORT}/")
    print(f"📄 Archivo: http://localhost:{PORT}/index.html\n")
    
    print("ℹ️  Presiona Ctrl+C para detener el servidor\n")
    
    # Crear servidor
    handler = MyHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"✅ Servidor iniciado en puerto {PORT}")
        print("⏳ Abriendo navegador en 2 segundos...\n")
        
        # Abrir navegador automáticamente
        time.sleep(2)
        try:
            webbrowser.open(f'http://localhost:{PORT}/')
        except:
            print(f"⚠️  No se pudo abrir el navegador automáticamente.")
            print(f"   Abre manualmente: http://localhost:{PORT}/")
        
        # Servir
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Servidor detenido")
            print("✅ ¡Hasta luego!")

if __name__ == "__main__":
    main()
