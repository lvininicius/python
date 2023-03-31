'''
Faça um algoritmo que solicita um número inteiro e exibe uma
mensagem indicando se ele é positvo, negativo ou zero
'''
#Digite um numero positivo ou negativo

numero = int(input("numero: "))
#se "if" numero for maior que 0 então inicie o bloco de codigo "if"
if numero > 0:
    print("Positivo")
# senão "elif" inicie o bloco "elif"
elif numero < 0:
    print("Negativo")