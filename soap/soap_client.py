from zeep import Client

client = Client("http://localhost:8000/")

num1 = 5
num2 = 10
result_suma = client.service.Sumar(a=num1, b=num2)
print(result_suma)