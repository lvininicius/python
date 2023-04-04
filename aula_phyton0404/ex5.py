print("1 Picanha R$ 25,00")
print("2 lasanha R$20,00")
print("3 strogonoff R$20,00")
print("4 Bife acebolado R$15,00")
print("5 Pão com ovo R$5,00")
opcao=int(input("escolha a opção desejada : "))

match opcao:
    case 1:
        valor=25.00
    case 2:
        valor=20.00
    case 3:
        valor=23.00
    case 4:
        valor=15.00
    case 5:
        valor=5.00
    case _:
        input("Opção invalida")
        valor=0
gorjeta=input("Deseja pagar os 10% (sim/nao): ")
match gorjeta:
    case "sim":
        valor= valor + valor * 10/100
        print(f"Valor total: {valor}")
    case "nao":
        print(f"Valor total:{valor}")