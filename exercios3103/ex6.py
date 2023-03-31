'''
Faça um algoritmo que solicita ao usuario dois numeros inteiros
O primeiro é o alor das horas e  segundo dos minutos
Verufuqye se a hora é  valida ou invalida e exia uma mensagem
correspondente ()
'''
horas=int(input("Informe as horas"))
minutos=int(input("Informe os minutos"))
#Se "if" variaveis {horas} for maior igual a 0 e "and" variavel {horas}  for menor igual a 23 e variavel {minutos}
if horas >= 0 and horas <=23 and minutos >= 0 and minutos <= 59:
    print("Horas e minutos válidos")
else:
    print("Horas e minutos válidos")