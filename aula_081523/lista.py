# listas
# Estruturas de dados (sequencia de itens)
#delimitadas por colchetes []

lista=[3,5,7,8]
print(lista)

# lista são heterogeneas (intens de tipos diferentes)
lista=[3,2.66,"abc",4,"paulo"]
print(lista)

# listas são mutáveis (podem ser alteradas)
lista=[3,5,7,8]
lista[0]=100
print(lista)

# listas são acessadas pelos indices (começa sempre no indice zero)
print(lista[0])

# indices negativos começam sempre em -1 (da partir do ultimo item)


#append - adiciona um item no final da lista
lista.append(300)
lista.append(400)
print(lista)

#insert - adiciona um item em uma posição especifica da lista

# pop() - remove o ultimo elemento da lista

lista = [3,7,5,10]
lista.pop()
print(lista)

#pop(indice) - remove o item do indice especifico
lista = [3,7,5,10] 
if 11 in lista:
    lista.remove(11)
else:
    print("numero 11 não está presente na lista")

# count - conta quatas vezes um item aparece na lista

lista=[3,7,5,10,5,5,5]
print(lista.count(5))

# index -retorna o indice de um elemento
print(lista.index(5))

#sort - ordem uma lista
lista=[3,7,5,10,5,5]
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)
lista=["Maria", "Ana", "Paulo", "Fernando"]
lista.sort()
print(lista)

#max - retorna o maior elemento da lista
lista=[3,5,10,1]
print(max(lista))

#min- retorna o menor elemento da lista
print(max(lista))

# sum - retorna somatorio da lista
print(sum(lista))

#media
media =sum(lista)/len(lista)
print(media)

#prencher lista com itens informados pelo usuarios
lista =[]
for i in range(5):
    n=int(input("Digite um número inteiro:"))
    lista.append(n)
print(lista)

lista=[]
while True:
    n=int(input("Digite um número inteiro, digite o numero -1 para sair:"))
    lista.append(n)
    if n==1:
        break
print(lista)

#percorrer itens da lista
lista = [4,6,2,3,10]
for item in lista: #for cada intem na lista
    print(item)
    if item % 2 ==0:
        count =+1
print(f"quantidade de pares {count}")

#percorrer indices da lista
for i in range (len(lista)):
    if lista[i]%2==0:
        lista[i]=0
print(lista)

#concatenação (juntar listas)
lista = [3,5,6]
lista2=["paulo","juliana","fernando"]
lista3=lista+lista2+lista
print(lista3)