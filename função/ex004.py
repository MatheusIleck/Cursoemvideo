'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
 inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
def maior(num, teste):
    teste.append(num)
    contador = maior = 0
    for v in teste:
        if contador == 0:
            maior == v
            contador += 1
        if v > maior:
            maior = v
    print(f'O maior numero é {maior}')



teste = list()
while True:
    num = int(input('Teste: '))
    if num == 999:
        break
    maior(num, teste)