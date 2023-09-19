matriz=[]   

for i in range(3):
    lista=[]
    for j in range(5):
        n=int(input("Numero: "))
        lista.append(n)
    matriz.append(lista)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] >=100:
            matriz[i][j]=0   
print(matriz)       
