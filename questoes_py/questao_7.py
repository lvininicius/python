#Escreva um progama que recaba o preço de um produto e calcule o seu preço final com um desconto de 10%
valor1=float(input("Insira o valor do produto:"))
valor2=float(10/100)*valor1
valor3=float(valor1-valor2)
print(f"O seu produto com 10% de desconto é:{valor3}")