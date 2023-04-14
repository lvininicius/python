'''
Escreva um algoritmo qye solicite 10 numeros
e informe qual foi o menor número digitado.
'''
cont=1
numero= int(input("Numero"))
menor = numero 
while cont <=9:
    numero = int(input("Numero"))
    if numero < menor:
        menor=numero 
    cont +=1
    print(menor)