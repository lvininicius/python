print("1 - linux")
print("2 - Banco de Dados")
print("3 - Windows Server")
print("4 - Lógica e Programação")

opcao = int(input("Informe a opçao desejada"))
match opcao:
    case 1:
        print("Auditorio 1")
    case 2:
        print("Banco de Dados")
    case 3:
        print("Windows Server")
    case 4:
        print(" Lógica e programação ")
    case _:
        print("Opção Invalida")