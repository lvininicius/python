'''
Solicite a quantidade de alunos de uma turma e a quantidade de notas.
Para cada aluno, solicite as suas notas e exiba a sua respectiva média
(a média deve ser arredondada para duas casas decimais)
'''
alunos=int(input("informe a quantidade de alunos: "))
notas=int(input("Informe a quantidade de notas: "))

for a in range(alunos):
    soma=0
    for b in range(notas):
        n=int(input("Informe a nota: "))
        soma += n
    media = soma /  notas
    print(f"Média:{media}")
