#STRINGS, SEQUENCIAS DE CARACTERES
texto="Exemplo de texto"
a=texto[0]
print(a)
b=texto[1]
print(b)

#tamanho da string

for c in texto:
    print(c)

print(len(texto))

#operador in (busca)

if "a" in texto:
    print("o caracter x exite na string")

# upper (converte para maiusculo)
print(texto.upper())

#lower (converte para minusculo)
print(texto.lower())

#title
print(texto.title())

#strip (remove espaços em branco no inicio e do final)
texto="exemplo de texto"
print(texto.strip())

#count (conta a quantidade de vees que um caracter a aparece na string)
texto="Exemplo de texto"
print(texto.count("texto"))

#replace(susbtitui uma substring por outra)
texto="banana, laranja, maça"
texto=texto.replace("laranja","melancia")
print(texto)

#split (divide uma string de acordo com um separador)
texto="Banana,laranja,maça,laranja,laranja"
frutas=texto.split(",") # retorna lista
print(frutas)