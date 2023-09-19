matriz=[]   
import random
def prencher(linha,coluna):

    matriz=[]   
    for i in range(linha):
        lista=[]
        for j in range(coluna):
            n=random.randint
            lista.append(n)
        matriz.append(lista)
def exibir(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] >=100:
                matriz[i][j]=0   
    print(matriz)       

def soma_diagonal_principal(matriz):
    
    soma=0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j:
                soma +=matriz[i][j]
    return soma

def soma_diagonal_secundaria(matriz):
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i + j ==len(matriz) -1:

                soma +=matriz[i][j]
    return soma

matriz=prencher(5,5)
print(matriz)
print(soma_diagonal_principal(matriz))
print(soma_diagonal_secundaria(matriz))
