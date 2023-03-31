'''
Faça um algoritmo que solicita ao usuario tres numeros e exibe
na tela apenas o menor deles, ou uma mensagem informando que 
os números são iguais.
'''
a=int(input("primeiro numero: "))
b=int(input("primeiro numero: "))
c=int(input("primeiro numero: "))
if a < b and a < c:
    print(f"menor número é {a}")
elif b < a and b < c:
    print(f"menor número é {b}")
elif c < a and c <b:
    print(f"menor número é {c}")
elif a==b and b==c:
    print("Tres numeros iguais")
else:
    print("Dois numeros iguais")    