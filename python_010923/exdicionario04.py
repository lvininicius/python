quantidade = {}
texto= input("Digite um frase")
for letra in texto:
    if letra in 'aeiou':
        if letra in quantidade:
            quantidade[letra]+=1 # incrementa
        else:
            quantidade[letra] = 1 # insere            
print(quantidade)
