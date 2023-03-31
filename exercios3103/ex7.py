'''
Faça um algoritmo que solicite dois números ao usuario e exiba
apenas o maior deles. Caso eles seja iguais exiba a mensagem
"Números Iguais"
'''
a=int(input("Primeiro numero"))
b=int(input("Segundo numero"))

if a > b:
    print(f"Maior número é {a}")
elif b > a:
    print(f"Maior numero é {b}")
else:
    print("Numero iguais")