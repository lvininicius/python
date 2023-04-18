'''
Escreca yn orgrama que solicita ao usuario o valor de N e calcule o valor de S na seriei abaixo:
Calcule o valor de S na serie abaixo:
s=1/1 + 1/2 + 1/3 + ... 1/N
'''
n=int(input("informe o valor de N: "))
cont=1
s=0
while cont <=n:
    s+=1/cont
    cont +=1
print(f"A soma é {round(s,2)}")