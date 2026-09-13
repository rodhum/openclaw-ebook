import http.server
import socketserver
import json
import sqlite3
import os
import urllib.parse
from datetime import datetime

PORT = 8080
DB_FILE = "leads.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            whatsapp TEXT NOT NULL,
            email TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            source TEXT DEFAULT 'Web Lead Magnet'
        )
    """)
    conn.commit()
    conn.close()
    print(f"✅ Base de datos SQLite inicializada: {DB_FILE}")

class LeadHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        
        # Route: Serve landing page as default index
        if parsed.path in ["/", "/index.html"]:
            self.path = "/landing.html"
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

        # Route: API list leads (JSON)
        elif parsed.path == "/api/leads":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, whatsapp, email, created_at, source FROM leads ORDER BY id DESC")
            rows = cursor.fetchall()
            conn.close()
            
            leads = [
                {
                    "id": r[0],
                    "name": r[1],
                    "whatsapp": r[2],
                    "email": r[3],
                    "created_at": r[4],
                    "source": r[5]
                }
                for r in rows
            ]
            self.wfile.write(json.dumps(leads, ensure_ascii=False).encode("utf-8"))
            return

        # Route: API export CSV
        elif parsed.path == "/api/export-csv":
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, whatsapp, email, created_at, source FROM leads ORDER BY id DESC")
            rows = cursor.fetchall()
            conn.close()
            
            self.send_response(200)
            self.send_header("Content-Type", "text/csv; charset=utf-8")
            self.send_header("Content-Disposition", 'attachment; filename="leads_ebook_openclaw.csv"')
            self.end_headers()
            
            csv_content = "ID,Nombre,WhatsApp,Email,Fecha_Registro,Origen\n"
            for r in rows:
                csv_content += f'"{r[0]}","{r[1]}","{r[2]}","{r[3]}","{r[4]}","{r[5]}"\n'
            
            self.wfile.write(csv_content.encode("utf-8-sig"))
            return

        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        
        # Route: Register new lead
        if parsed.path == "/api/leads":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            
            try:
                data = json.loads(body)
                name = data.get("name", "").strip()
                whatsapp = data.get("whatsapp", "").strip()
                email = data.get("email", "").strip()
                source = data.get("source", "Web Lead Magnet")
                
                if not name or not whatsapp or not email:
                    self.send_response(400)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.end_headers()
                    self.wfile.write(json.dumps({"status": "error", "message": "Todos los campos son obligatorios"}).encode("utf-8"))
                    return

                # Save into SQLite
                conn = sqlite3.connect(DB_FILE)
                cursor = conn.cursor()
                cursor.execute("INSERT INTO leads (name, whatsapp, email, source) VALUES (?, ?, ?, ?)", (name, whatsapp, email, source))
                conn.commit()
                new_id = cursor.lastrowid
                conn.close()
                
                print(f"📥 [NUEVO LEAD GUARDADO] ID: {new_id} | {name} | WA: {whatsapp} | {email}")

                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                response = {
                    "status": "success",
                    "message": "Lead registrado con éxito",
                    "lead_id": new_id,
                    "redirect_url": "/ebook_interactivo.html"
                }
                self.wfile.write(json.dumps(response).encode("utf-8"))
                return
                
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode("utf-8"))
                return

        self.send_response(404)
        self.end_headers()

if __name__ == "__main__":
    init_db()
    with socketserver.TCPServer(("", PORT), LeadHandler) as httpd:
        print(f"🚀 Servidor Web de Captura activo en: http://localhost:{PORT}")
        print(f"📖 e-Book Interactivo: http://localhost:{PORT}/ebook_interactivo.html")
        print(f"📊 Panel de Administración: http://localhost:{PORT}/admin.html")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor detenido.")
