print("1 - soma")
print("2 - subrtração")
print("3 - multiplicação")
print("4 - Divisão")

opcao=int(input("escolha uma opção:"))

if opcao == 1:
    s=int(input("Ecolha os valores para somar: "))
    s2=int(input("Ecolha os valores para somar: "))
    r1=s+s2
    input(f"o resultado da sua soma {s}+{s2}={r1}: ")
elif opcao == 2:
    s1=int(input("Ecolha os valores para subtrair: "))
    s3=int(input("Ecolha os valores para subtrair: "))
    r2=s1-s3
    input(f"o resultado da sua soma {s1}+{s3}={r2} ")
elif opcao == 3:
    ss2=int(input("Ecolha os valores para multiplicar: "))
    si3=int(input("Ecolha os valores para multiplicar: "))
    r3=ss2*s2
    input(f"o resultado da sua soma {ss2}+{si3}={r3} ")
elif opcao == 4:
    ss3=int(input("Ecolha os valores para dividir: "))
    ss4=int(input("Ecolha os valores para dividir: "))
    r4=ss3/s2
    input(f"o resultado da sua soma {ss3}+{ss4}={r4} ")