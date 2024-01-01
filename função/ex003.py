'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
fim e passo.'''
from time import sleep
def contador(inicio,fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        contador = inicio
        while contador <= fim:
            print(contador, end=' ', flush=True)
            contador += passo

            sleep(1.0)
    else:
        contador = inicio
        while contador >= fim:
            print(contador, end=' ', flush=True)
            sleep(1.0)
            contador -= passo
        print('FIM')


inicio = int(input('Agora é sua vez de personalizar, digite o Inicio da Lista: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))


contador(inicio,fim, passo)