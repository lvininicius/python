# Preencha um dicionario com as informações 5 pessoas.
# Utilize o cpf da pessoa como chave e o nome como valor
# Solicite os dados ao usuário

'''
dic={}

for i in range(5):
    dados=input("Digite seu nome:")
    cpf=int(input("Digite seu CPF: "))
    dic[cpf] = dados

print(dic)
'''

#Ex2
'''
Prencha um dicionario com as informações de 5 produtos
- Utilize o nome do proiduto chave e o preço como valor
- solicite os dados ao usuario
Percorra o dicionario e exiba o nome dos produtos com preço superior a R$50.00
'''
'''
dic={}

for i in range(2):
    produtos=input("Digite os produtos:")
    precos=float(input("Digite os preços : "))
    dic[produtos] = precos

print(dic)

for produtos, precos in dic.items():
    if precos>50:
        print (f"O produto {produtos} tem um preço superior a R$50,00")
'''   

#Ex3
'''
Preencha um dicionario com os dados de 5 alunos
- utilize o ra do aluno como chabe e uma lista de tres notras como valor.
- Solcite os dados ao usuários
Percorra o dicionario e exiba a média de cada aluno
'''
alunos = {}
while len(alunos) >5:
    ra = int(input('Seu RA: '))
    lista = []
    for i in range(3):
        n = float(input('Nota: '))
        lista.append(n)
    alunos[ra] = lista
print(alunos)
for ra, lista in alunos.items():
    media = sum(lista) / len(lista)
    print(f'{ra}, {media}')