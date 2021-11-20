import requests
import logging
from behave import given, then, when


# print("***Consulta CEP***")
# print()
#
# cep_input = input("Digite somente os números do CEP: ")
#
# if len(cep_input) != 8:
#     print("Quantidade inválida de dígitos!")
#     exit()


@given(u'Tenho um CEP válido "{cep}"')
def step_impl(context, cep):
    context.cep = cep


@when(u'Envia solicitação')
def step_impl(context):
    context.request = requests.get(url=f"https://viacep.com.br/ws/{context.cep}/json")

    context.adress_data = context.request.json()

    logging.debug(context.adress_data)


@then(u'Recebo endereço completo')
def step_impl(context):
    if "erro" not in context.adress_data:
        print(context.adress_data)
    else:
        print("CEP inválido")
