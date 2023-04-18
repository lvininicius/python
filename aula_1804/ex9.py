n=int(input("Informe a quantidade de numeros?"))
cont=1
somapar=0
somaimpar=0
contapar=0
contaimpar=0
while cont <=n:
    numero=int(input("Numero: "))
    if numero % 2 ==0:
        somapar +=numero # somatotrio dos pares
        contapar +=1
    else:
        somaimpar +=numero # somatorio dos impares
        contaimpar +=1     # conta a quantidade de impares
        cont+=1
if contapar > 0:
    mediapar=somapar/contapar
    print(f"A medua dis oares :{mediapar}")

else:
    print("Não há numeros pares")

if contaimpar >0:
    mediaimpar=somaimpar/contaimpar
    print(f"A media dos impares: {mediaimpar}")
else:
    print("Não há numeros impares")
mediaimpar=somaimpar/contaimpar
print(f"A media dos numeros pares : {mediapar}")
print(f"A media dos numeros impares {mediaimpar}")                 