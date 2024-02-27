from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")  # Convertir a minúsculas y quitar espacios
    return palabra == palabra[::-1]

dispatcher = SoapDispatcher( "Ejemplo-Soap-Server", location="http://localhost:8000/", action="http://localhost:8000/", namespace="http://localhost:8000/", trace=True, ns=True)

dispatcher.register_function("EsPalindromo", es_palindromo, returns={"resultado": bool}, args={"palabra": str})

server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher

print("Servidor SOAP Iniciando en http://localhost:8000/")

server.serve_forever()