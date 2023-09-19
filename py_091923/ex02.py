matriz=[]
for i in range(6):
    lista=[]
    for j in range(6):
        if i == j:
            lista.append(1)
        else:
            lista.append(0)
    matriz.append(lista)
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end='\t')
    
    print()

