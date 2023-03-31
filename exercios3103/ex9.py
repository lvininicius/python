'''
Faça um algoritmo que solicita ao usuário tres valores
correspondentes aos laos de um triangulo. Informe se o
triangulo é equitlareo (possui 3 lados iguais), isosceles
(possui dois lados iguais) ou escaleno (não possui lados iguais)
'''
lado1=float(input("Primeiro lado: "))
lado2= float(input("Segundo lado: "))
lado3- float(input("Terceiro lado: "))

if lado1 == lado2 and lado2 ==lado3:
    print("Equilátero")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Equilatero")
else:
    print("escaleno")