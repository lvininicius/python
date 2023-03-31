'''
Nome:Lucas Vinicius de Almeida Brigida
RM:99094

TAREFA: Escrever um programa em Python que solicite dois números inteiros positivos e calcule a soma entre eles, considerando o vírus que torna todos os numero 7 em 0.
'''
# função para remover o dígito 7 de um número
def r_7(n):
    # variável para guardar o número sem os dígitos 7
    r7 = 0
    # variável que ajuda a posicionar os dígitos corretamente
    mult = 1

    # enquanto ainda houver dígitos no número
    while n > 0:
        # pega o último dígito do número
        digito = n % 10
        # remove o último dígito do número
        n //= 10

        # se o dígito for 7, não adiciona nada ao resultado
        if digito == 7:
            r7 += 0
        # se o dígito não for 7, adiciona o dígito multiplicado pela posição correta
        else:
            r7 += digito * mult

        # atualiza o multiplicador
        mult *= 10

    # retorna o número sem os dígitos 7
    return r7

# solicita que o usuário digite dois números
x = int(input("Digite o primeiro valor do jogo : "))
y = int(input("Digite o segundo valor do jogo: "))

# remove os dígitos 7 de cada número, caso o numero x e y
x_r7 =r_7(x)
y_r7=r_7(y)

# soma os números sem os dígitos 7
resulta_soma = x_r7 + y_r7

# remove os dígitos 7 da soma dos números
resulta_soma_r7 =r_7(resulta_soma)

# exibe os resultados
print(f"Resultado: {resulta_soma_r7}")