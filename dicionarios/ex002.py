'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado
.'''
import random
from time import sleep
from operator import itemgetter
dado = dict()
for v in range(0, 4):
    jogador = input(f'Insira o nome do {v+1} jogador: ')
    numero_aleatorio = random.randint(1, 6)
    dado[jogador] = numero_aleatorio
rankin = dict()
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
print('-' * 35)
print(f'{"ORDEM DO RANKING":^30}')
print('-' * 35)

for i, v in enumerate(ranking):
    print(f'{i+1} lugar: O player {v[0]} tirou {v[1]} no dado')
    sleep(2)

