'''
faça uma função que receba um numero inteiropor parametro retorna
true se for par e false se for impar
'''
def par_ou_impar(numero):
    if numero % 2 ==0:
        return True
    else:
        return False
numero=int(input("Informe um numero: "))
resultado=par_ou_impar(numero)
if resultado==True:
    print("O numero é par")
else:
    print("numero é impar")