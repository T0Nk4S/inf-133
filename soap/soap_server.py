from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def sumar(a, b):
    try:
        result = int(a) + int(b)
        return "La suma de {} y {} es: {}".format(a, b, result)
    except ValueError:
        return "Error: deben ser números naturales"

dispatcher = SoapDispatcher(
    "Ejemplo-Soap-Server", location="http://localhost:8000/", action="http://localhost:8000/", namespace="http://localhost:8000/", trace=True, ns=True
)

dispatcher.register_function("Sumar", sumar, returns={"resultado": str}, args={"a": str, "b": str})

server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher

print("Servidor SOAP Iniciando en http://localhost:8000/")

server.serve_forever()