'''
Ecreva um programa para solicitar as notras de duas provas. Faça uma função que receba as duas notas por parametros
e exibe a mensagem "Voce foi Aprovado!" ou "Voce foi Reprovado!. Considere 6.0 a média minima para aprovação.
'''
def aprovacao(nota1, nota2):
    media=(nota1+nota2)/2
    if media >=6:
        print(f"sua media é {media}")
        print("Aluno Aprovado")
    else:
        print("reprovado")
nota1=float(input("Digite a primeira nota"))
nota2=float(input("Digite a segunda nota"))     
aprovacao(nota1,nota2)
