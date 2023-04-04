'''
Opção 1 - O Dobro
Opção 2 - metade
Opção 3 - 10% do numero
'''
numero=float(input("Número: "))
print("Opção 1 - O dobro")
print("Opção 2 - a metade")
print("Opção 3 - 10% do numero")
opcao= int(input("Escolha uma opção: "))

match opcao:
    case 1:
        resultado=numero*2
        print(f"O dobro do {numero} é {resultado}")
    case 2:
        resultado=numero/2
        print(f"A metade do {numero} é {resultado}")
    case 3:
        resultado = numero * 0.10
        print (f"10% DE {numero} é {resultado}")
    case _:
        print ("Opção invalida")

