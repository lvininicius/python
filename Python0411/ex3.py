'''
Escreva um algoritmo que solicite a idade de 15 pessoas
e informe a quantidade de pessoas com idade inferios a 18 anos
'''
cont=1
quantidade=0
while cont <=15:
    idade=int(input("Iforme a idade: "))
    if idade < 18:
        quantidade +=1
    cont +=1
print(f"Quantidade com idade inferior a 18 é {quantidade}")