import requests

print("***Consulta CEP***")
print()

cep_input = input("Digite somente os números do CEP: ")

if len(cep_input) != 8:
    print("Quantidade inválida de dígitos!")
    exit()

request = requests.get("https://viacep.com.br/ws/{}/json/".format(cep_input))

adress_data = request.json()

if "erro" not in adress_data:
    print(request.json())
else:
    print("CEP inválido")
    