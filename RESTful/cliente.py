import requests

url = "http://localhost:8000/"
ruta_estudiantes = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_estudiantes)
print("Mostrar todos los estudiantes:")
print(get_response.text)


params = {"carrera": "Economia"}
estudiantes_economia_response = requests.request(method="GET", url=ruta_estudiantes, params=params)
print("\nEstudiantes de Economia:")
print(estudiantes_economia_response.text)


ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Perez",
    "carrera": "Ingenieria Agronomica",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print("\nAgregar nuevo estudiante:")
print(post_response.text)

ruta_carreras = url + "estudiantes"
carreras_response = requests.request(method="GET", url=ruta_carreras)
print("\nMostrar todas las carreras:")
print(carreras_response.text)

ruta_estudiantes_economia = url + "estudiantes"
estudiantes_economia_response = requests.request(method="GET", url=ruta_estudiantes_economia, params={"carrera": "Economia"})
print("\nEstudiantes de Economia:")
print(estudiantes_economia_response.text)

nuevo_estudiante_economia1 = {
    "nombre": "EstudianteEco1",
    "apellido": "Apellido1",
    "carrera": "Economia",
}

nuevo_estudiante_economia2 = {
    "nombre": "EstudianteEco2",
    "apellido": "Apellido2",
    "carrera": "Economia",
}

ruta_post_economia1 = url + "estudiantes"
post_response_economia1 = requests.request(method="POST", url=ruta_post_economia1, json=nuevo_estudiante_economia1)
print("\nAgregar estudiante de Economia 1:")
print(post_response_economia1.text)

post_response_economia2 = requests.request(method="POST", url=ruta_post_economia1, json=nuevo_estudiante_economia2)
print("\nAgregar estudiante de Economia 2:")
print(post_response_economia2.text)

estudiantes_economia_response_nueva = requests.request(method="GET", url=ruta_estudiantes_economia, params={"carrera": "Economia"})
print("\nEstudiantes de Economia después de agregar nuevos estudiantes:")
print(estudiantes_economia_response_nueva.text)

ruta_actualizar = url + "estudiantes"
estudiante_actualizado = {
    "id": 1,
    "nombre": "Juan",
    "apellido": "Perez",
    "carrera": "Ingenieria Agronomica",
}

put_response = requests.request(method="PUT", url=ruta_actualizar, json=estudiante_actualizado)
print("\nActualizar estudiante de ID 1:")
print(put_response.text)
