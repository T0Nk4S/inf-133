from zeep import Client

client = Client("http://localhost:8000/")

palabra = "reconocer"
result_palindromo = client.service.EsPalindromo(palabra=palabra)
if result_palindromo:
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")