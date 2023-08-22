def preenche_lista():
    '''
    Preencha uma lista com 10 numeros inteiros e retorna o maior, o menor
    e a média dos numeros
    '''
    lista=[]
    for i in range(10):
        numero=int(input("Numero:"))
        lista.append(numero)
    print(lista)

    maio=max(lista)
    menor=min(lista)
    media=sum(lista) / len(lista)

    return maio, menor, media

resultado=preenche_lista()
print(resultado)
print(f"Maior:{resultado[0]}")
print(f"Meno:{resultado[1]}")
print(f"Media:{resultado[2]}")
