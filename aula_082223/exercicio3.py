strg=input(str("Informe a palavra: "))
strg=strg.lower()
def vogais (strg):
    """Voagais"""
    numero_vogais=0
    for char in strg:
        if char in "aeiou":
            numero_vogais+=1
    print(f"O nome de {strg} tem {numero_vogais} vogais")
    return numero_vogais
vogais(strg)