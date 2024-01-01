'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.'''

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A area de um terreno {comprimento} x {largura} é de {a}m²')

# Programa Principal
largura = float(input('Digite a Largura: '))
comprimento = float(input('Digite o comprimento: '))

area(largura,comprimento)