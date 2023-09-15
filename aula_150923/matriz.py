matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]
print(matriz)
print(matriz[1][2])


matriz[0][1]=100
print(matriz)

linhas=int(input("Quantidade de linhas: "))
colunas=int(input("Quantidade de colunas: "))
matriz=[]
for linha in range(linhas):
    lista=[]

    for coluna in range(colunas):
        n=int(input("numero:"))
        lista.append(n)
    matriz.append(lista)
print(matriz)

for linha in matriz:
    for item in linha:
        print(item,end='\t')

#percorrer os itens da matriz
cont=0
for linha in matriz:
    for item in linha:
        if item % 2 ==0:
            cont+=1
print(cont)

#percorre os indices da matriz
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] % 2 ==0:
            matriz[i][j] = 100