#FATIAMENTO /SLICE
#Seleciona um pedaço de uma string(ou lista, ou tupla)
nome="Paulo Vieira"
primeiro_nome=nome[0:5]
print(primeiro_nome)

segundo_nome=nome[6:12]
print(segundo_nome)

exemplo=nome[3:12:2]

#caso não seja informado o valor de inicio, é considerado zero
exemplo=nome[:10]
print(exemplo)

#Caso não seja informa o valor final, é considerado o ultimo indice
exemplo=nome[2:]
print(exemplo)

#Fatiamento em ordem inversa
exemplo=nome[::-1]
print(exemplo)

exemplo=nome[15:2:-2]
print(exemplo)

lista=[3,5,7,9]
lista2=lista[:2]
print(lista2)