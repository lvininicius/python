def primo_proximo():
    # Função que verifica se um número é primo
    def eh_primo(num):
        # Se num é menor que 2, não é primo
        # all() retorna True se todos os elementos do iterável forem verdadeiros
        # Verifica se num não é divisível por nenhum número entre 2 e a raiz quadrada de num
        return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

    while True:
        # Solicita a entrada do usuário
        num = int(input("Digite (0) para sair ou digite um número entre 1 e 1000 para encontrar o número primo próximo: "))
        if num == 0:
            print("Saindo do programa... Byeee!")
            break
        # Verifica se o número digitado é primo
        if eh_primo(num):
            primo_prox = num
        else:
            i = 1
            # Verifica se num - i ou num + i são primos, incrementando i até encontrar um que seja primo
            while not eh_primo(num - i) and not eh_primo(num + i):
                i += 1
            # Se num - i for primo, atribui o valor de num - i a primo_prox, senão atribui num + i
            primo_prox = num - i if eh_primo(num - i) else num + i
        # Imprime o resultado
        print(f"O número primo mais próximo de {num} é {primo_prox}")
primo_proximo()
