salario=2500
nome=str(input("Digite o nome do vendedor:"))
vendas=int(input("digite a quantidade de carros vendidos:"))
valor=float(input("valor total das vendas:"))

comissao=200*vendas
acrescimo=valor*2/100
d=salario+comissao+acrescimo
print(f"Salario do vendedor {nome} é {d}")