import json

with open('notas.csv','r',encoding="utf-8") as file:
    dicionario={}
    conta_linha=1
    for linha in file:
        if conta_linha>1:
            lista=linha.split(",")
            rm=lista[0]
            nome=lista[1]
            notas=[float(lista[2]),float(lista[3])]
            dicionario[rm] = {'nomes': nome, 'notas': notas}
        conta_linha+=1

with open('notas.json','w',encoding='utf-8') as file:
    json.dump(dicionario,file, indent=4, ensure_ascii=False)