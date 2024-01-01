'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
crescente.'''

numeros = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor duplicado portanto não foi adicionado')
    c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if c == 'N':
        break
numeros.sort()
print(numeros)
