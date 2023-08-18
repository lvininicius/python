#TUPLAS
#Sequencia de itens

#Tuplas são imutaveis (não podem ser modificadas)

#tuplas são delimitadas por parênteses
tupla=(1,2,3,10,5)

#Tuplas são heterogeneas (armazena difentes tipos de dado)
tupla=(3,"abc",3.5,6.99,"dfdf")

print(tupla[0])
print(tupla[1])

#index - retorna o indice de um determinado item
print(tupla.index(6.99))

#count - conta a quantidade de vezes que um item aparece na tupla
print(tupla.count(6.99))

#operador in - busca um item na tupla e retorna true e false
if 8 in tupla:
    print("Existe")
else:
    print("Não existe")

# concatenação
tupla1=(1,2,3)
tupla2=(20,30,60)
tupla3=tupla1+tupla2
print(tupla3)

def teste(a,b):
    soma=a+b
    subtração=a-b
    return soma, subtração

resultado=teste(30,7)
print(resultado)
print(resultado(0))
print(resultado[1])

#tupla com 1 unico item (tem uma virgula no final)
tupla=(1,)
print(tupla)

#list - copia os itens de uma tupla para uma lista
tupla=(4,5,6)
lista=list(tupla)
print(lista)

#tuple - copia os itens de uma lista para uma tupla
lista=[10,20,30]
tupla=tuple(lista)
print(tupla)

tupla=("Paula","Maria","Fernando")
lista=list(tupla)
lista.sort()
tupla=tuple(lista)
print(tupla)

# cópia de lista ou de tupla
lista=[1,2,3]
lista2=lista
lista2.append(100)
print(lista)