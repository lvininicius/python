'''
Escreva um altoritmo que solicite 15 números e informe
o somatório de todos os números ímpares digitados
'''
cont=1 #contador
soma=0 #somador
while cont <=15:
    numero=int(input("numero: "))
    if numero % 2 !=0:
        soma+=numero
    cont +=1
print(f"Somatório dos impares {soma}")