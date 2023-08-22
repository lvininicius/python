def lista_palavras(frase):
    '''
    Recebe uma frase como entrada e retorne uma lista das palavras presentes na
    frase
    '''
    return frase.split (" ") # divide a frase onde houver um espaço em branco
def conta_palavras(frase):
    '''
    Retorna a quantidade de palabras existentes em uma string
    '''
    lista=frase.split(" ")
    return len(lista)

frase=input("informe uma frase: ")
print(lista_palavras(frase))
print(f"Quantidade de palavras> {conta_palavras(frase)}")