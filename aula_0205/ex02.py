'''
'''
def poligno(lados):
    if lados ==3:
        print("Triangulo")
    elif lados ==4:
        print("Quadrilatero")
    elif lados ==5:
        print("Pentâgono")
    else:
        print("Valor invalido")
lados =int(input("Informe a quantidade de lados"))
poligno(lados)