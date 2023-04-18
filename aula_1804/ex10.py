'''
Chico tem 1,5m cresce 2 cemntimeros por ano, equanto juca tem 1,10 e cresce 5 centimetros por anos
considerando que Chico e Juca continuem crescendo constantemente,
quantos anos seriam nescessario para Juca ser mais alto que chico
'''
alturachico=1.5
alturajuca=1.1
anos=0 # contadora
while alturajuca <= alturachico:
    alturachico +=0.02
    alturajuca +=0.05
    anos +=1
print(f"A quantidade de anos para que o Juca seja mais alto {anos}")