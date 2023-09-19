matriz=[]
for i in range(3):
    linha=[]
    for j in range(5):
        n=int(input("numero: "))
        linha.append(n)
    matriz.append(linha)

print(matriz)

for i in range(len(matriz)): #quantidade de linhas
    for j in range(len(matriz[0])): #colunas
        print(matriz[i][j], end=' ')
    print()