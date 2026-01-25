#!/usr/bin/env python3
"""
Servidor HTTP optimizado para velocidad con caché de archivos GLB
Usar: python server_rapido.py
"""
import http.server
import socketserver
from pathlib import Path

PORT = 8000

class CachedHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Handler con headers de caché para archivos GLB"""
    
    def end_headers(self):
        # Headers de caché agresivo para archivos GLB (1 hora)
        if self.path.endswith('.glb'):
            self.send_header('Cache-Control', 'public, max-age=3600')
            self.send_header('Access-Control-Allow-Origin', '*')
        # Headers de caché para JS/CSS (30 minutos)
        elif self.path.endswith('.js') or self.path.endswith('.css'):
            self.send_header('Cache-Control', 'public, max-age=1800')
        # Sin caché para HTML (siempre recargar)
        elif self.path.endswith('.html'):
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
        
        # CORS para todos los archivos
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), CachedHTTPRequestHandler) as httpd:
        print(f"⚡ Servidor HTTP RÁPIDO corriendo en puerto {PORT}")
        print(f"📁 Sirviendo archivos desde: {Path.cwd()}")
        print(f"🌐 URL local: http://localhost:{PORT}/test/prueba.html")
        print(f"📱 URL móvil: http://192.168.10.93:{PORT}/test/prueba.html")
        print(f"🚀 Caché activado para archivos GLB (1 hora)")
        print(f"\n✅ Presiona Ctrl+C para detener\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Servidor detenido")
