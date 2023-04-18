'''
Solicite um númweo inteiro ao usuario e calcule o fatorial desse numero.
O fatorial de um numweo N é a multiplicação de N por seus antecessores
maioores ou iguais a 1.
Por exemplo: o fatorial de 5 é igual 5*4*3*2*1=120
'''
numero=int(input("Informe um número: "))
fatorial =1
while numero >=1:
    fatorial *=numero
    numero -=1
print (f"Fatorial: {fatorial}")