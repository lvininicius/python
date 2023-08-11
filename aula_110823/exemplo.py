# PARÂMETRO DEFAUT
def calcular_media(matematica:float =0,fisica:float=0, quimica:float=0):
    print(f"Matemática:{matematica}")
    print(f"Fisica:{fisica}")
    print(f"Quimica:{quimica}")
    media=(matematica+fisica+quimica)/3
    return media
print (f"Média{calcular_media(10,8,6)}")
print (f"Média{calcular_media(10,8)}")
print (f"Média{calcular_media()}")