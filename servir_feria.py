"""Sirve la feria por HTTP en la compu y la abre en el navegador.

Uso: en una terminal dentro de esta carpeta, `python servir_feria.py`
(los navegadores no cargan la escena 3D ni los videos abriendo el HTML con doble clic).
"""
import http.server
import os
import socketserver
import threading
import webbrowser

PUERTO = 8766
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Manejador(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map,
                      ".js": "text/javascript", ".json": "application/json",
                      ".mp4": "video/mp4", ".ogg": "audio/ogg", ".glb": "model/gltf-binary"}

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()


url = f"http://127.0.0.1:{PUERTO}/visita_virtual.html"
with socketserver.ThreadingTCPServer(("127.0.0.1", PUERTO), Manejador) as srv:
    print(f"Feria en {url}  (Ctrl+C para cerrar)")
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
