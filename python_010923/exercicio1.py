alunos=[("Lucas",20,8),("Riqueto",18,5),("Oliveira",31,10)]

def alunos_aprovados(alunos):
    aprovados=[]
    for tupla in alunos:
        if tupla[2] >=7:
            t = (tupla[0], tupla[2])
            aprovados.append(t)
    return aprovados

alunos_aprovados(alunos)

def idad_media(alunos):
    print(alunos_aprovados(alunos))
    alunos2 = alunos[0][1], alunos[1][1], alunos[2][1] 
    media=sum(alunos2)/len(alunos2)
    return media

print(idad_media(alunos))