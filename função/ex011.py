'''Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando
e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.'''

def IHP(msg):
    help(msg)


while True:
    ajuda = str(input('Digite o comando que deseja visualizar: '))
    IHP(ajuda)
    if ajuda in 'fim':
        break

