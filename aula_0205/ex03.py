'''
Crie uma função que recebe como parametro um número inteiro
e retorna o seu dobro
'''
def dobro(numero):
    x=5

    d=numero *2
    return d

numero=int(input("Numero : "))
d= dobro(numero)
print(f"O dobro de {numero} é {d}")