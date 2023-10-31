'''
Exercicio 1:
Ultilizar a API viacep para buscar um CEP a partir de um enderço digitado
'''
import requests

ESTADO=input("Insira um Estado: ")
CIDADE=input("Insira um Cidade: ")
RUA=input("Insita o nome da rua: ")
api=requests.get(f'https://viacep.com.br/ws/{ESTADO}/{CIDADE}/{RUA}/json/')
cep=api.json()

a=input("Desja inserir um complementpo ?:")

if a == "s" or "sim":
    COMP=input("Insira o complemento: ")

else:
    print(cep)

for i in cep:
    if i['complemento'] == COMP:
        print("------------------------")
        print (f"{RUA}\n{COMP}\nCEP:{i['cep']}")
        print("------------------------")