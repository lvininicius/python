'''
Escreva um altoritmo que solicite 10 numeros e exiba o dobro
de cada número digitado.
'''
cont=1
while cont <=10:
    numero = float(input("numero: "))
    dobro = numero*2
    print(f"O dobro de {numero} é {dobro}")
    cont +=1