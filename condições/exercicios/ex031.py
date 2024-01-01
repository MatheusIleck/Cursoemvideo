'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
contCinquenta = contVinte = contDez = contUm = 0

nota = int(input('Digite o valor que deseja sacar: '))
while True:
    if nota <= 0:
        break
    while nota - 50 >= 0:
        nota -= 50
        contCinquenta += 1
    while nota - 20 >= 0:
        nota -= 20
        contVinte += 1
    while nota - 10 >= 0:
        nota -= 10
        contDez += 1
    while nota - 1 >= 0:
        nota -= 1
        contUm += 1

print(f"R$50: {contCinquenta}\nR$20: {contVinte}\nR$10: {contDez}\nR$1: {contUm}")