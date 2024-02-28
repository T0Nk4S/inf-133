from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes = [{"id": 1, "nombre": "Pedrito", "apellido": "Garcia", "carrera": "Ingenieria de Sistemas"},
               {"id": 2, "nombre": "Juanito", "apellido": "Perez", "carrera": "Ingenieria Agronomica"}]

class RESTRequestHandler(BaseHTTPRequestHandler):
    def send_json_response(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        if self.path == "/lista_estudiantes":
            self.send_json_response(estudiantes)
        elif self.path == "/buscar_nombre":
            nombres_con_P = [estudiante["nombre"] for estudiante in estudiantes if estudiante["nombre"].startswith("P")]
            self.send_json_response({"nombres_con_P": nombres_con_P})
        elif self.path == "/contar_carreras":
            carreras_contadas = {}
            for estudiante in estudiantes:
                carrera = estudiante["carrera"]
                carreras_contadas[carrera] = carreras_contadas.get(carrera, 0) + 1
            self.send_json_response({"estudiantes_por_carrera": carreras_contadas})
        elif self.path == "/total_estudiantes":
            total_estudiantes = len(estudiantes)
            self.send_json_response({"total_estudiantes": total_estudiantes})
        else:
            self.send_json_response({"Error": "Ruta no existente"}, status=404)

    def do_POST(self):
        if self.path == "/agrega_estudiante":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode("utf-8"))
            post_data["id"] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.send_json_response(estudiantes, status=201)
        else:
            self.send_json_response({"Error": "Ruta no existente"}, status=404)

def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Servidor web iniciado en http://localhost:{port}/lista_estudiantes")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando el servidor web")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
