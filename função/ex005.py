'''Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a
soma entre todos os valores pares sorteados pela função anterior.'''
import random
from time import sleep


def sorteia(números):
    print(f'Numeros gerados: ', end='')
    for v in range(0, 5):
        num = random.randint(0, 100)
        números.append(num)
        print(num, end=' ', flush=True)
        sleep(1.0)
    print(números)


def somaPar(números):
    soma = 0
    for v in números:
        if v % 2 == 0:
            soma += v

    print(f'A soma dos numeros pares é: {soma}')


números = list()
sorteia(números)
somaPar(números)
