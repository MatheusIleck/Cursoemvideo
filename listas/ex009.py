'''Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo
teclado. No final, mostre a matriz na tela, com a formatação correta.'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linhas in range(0, 3):
    for colunas in range(0, 3):
        matriz[linhas][colunas]= int(input(f'Digite o valor: '))

for linhas in range(0, 3):
    for colunas in range(0, 3):
        print(f'{matriz[linhas][colunas]:^5}', end=' ')
    print()