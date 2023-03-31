'''
Faça um algoritmo que solicita ao usuário uma letra e exiba
uma mensagem informando se é uma vogal ou uma consoante
'''
letra = input("Digite uma letra: ")
#função declarada para transformar letras maiusculas em minusculas
letra = letra.lower()
if letra == "a" or letra == "e" or letra == "i" or letra == "u":
    print("Vogal")
else:
        print ("Consoante")
#__________________________________________________________________
vogais="aeiouAEIOU"
# "if" alguma letra estar presente "in" varivel vogais, então inicie o bloco "if" senão inicia
# o bloco "else"
if letra in vogais:
    print("Vogal")
else:
        print("Consoante")