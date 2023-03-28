# Obter as entradas do usuário para o primeiro jogo
input("RESULTADO JOGO 1 (PRESSIONE ENTER):\n")
a = int(input("Digite o valor-1 de 0 a 99:"))
b = int(input("Digite o valor-2 de 0 a 99:"))
r1 = a + b

# Obter as entradas do usuário para o segundo jogo
input("RESULTADO JOGO 2 (PRESSIONE ENTER):\n")
c = int(input("Digite o valor-1 de 0 a 99:"))
d = int(input("Digite o valor-2 de 0 a 99:"))
r2 = c + d

# Exibir os resultados inseridos
print(f"o resultado do primeiro jogo é {a}+{b} = {r1}")
print(f"o resultado do segundo jogo é {c}+{d} = {r2}")

# Envenenar os resultados
input("Deseja envenenar os resultados 💀 PRESSIONE (ENTER):")

# Criar uma lista com os resultados para o envenenamento das variáveis
z = [a, b, c, d, r1, r2]

# Substituir os números 7 por 0 em todas as operações
for k in range(len(z)):
    if z[k] == 7:
        z[k] = 0
    elif z[k] % 10 == 7:
        z[k] -= 7
        z[k] += 0
    elif z[k] // 10 == 7:
        z[k] -= 70
        z[k] += 0

# Calcular os resultados envenenados
z4 = z[0] + z[1]
z5 = z[2] + z[3]
z6 = z[4] + z[5]

# Substituir os números 7 por 0 nos resultados envenenados
if z4 == 7 or z4 % 10 == 7 or z4 // 10 == 7:
    z4 = 0
if z5 == 7 or z5 % 10 == 7 or z5 // 10 == 7:
    z5 = 0
if z6 == 7 or z6 % 10 == 7 or z6 // 10 == 7:
    z6 = 0

# Exibir os resultados envenenados
print(f"SPOOFING RESULTADOS JOGO 1 {z[0]}+{z[1]}={z4}")
print(f"SPOOFING RESULTADOS JOGO 2 {z[2]}+{z[3]}={z5}")