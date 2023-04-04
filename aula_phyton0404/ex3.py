'''
Verifique se um número inteiro é múltiplo de 3
'''
numero = int(input("Informe um número inteiro: "))
resto=numero%3
match resto:
    case 0:
        print ("Múltiplo de 3")
    case _:
        print ("Não é multiplo de 3")