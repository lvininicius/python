salario=float(input("Informe o salário do vendedor: "))
if salario <= 1500:
    aumento = salario * 3 /100
    total = salario + aumento
    print(f"salario Final: {total}")
else:
    aumento1=1500 * 3/100
    aumento2=(salario - 1500) * 5 / 100
    total2=salario + aumento1 + aumento2
    print(f"Salario Final:{total}")