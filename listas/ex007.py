'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
dados = list()
pessoas = list()
maior = menor = 0
verificador = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break
    if verificador == 0:
        maior = menor = pessoas[verificador][1]
    if pessoas[verificador][1] > menor:
        maior = pessoas[verificador][1]
    else:
        menor = pessoas[verificador][1]
    verificador += 1

print(f"As pessoas com o maior peso são: ", end='')
for nomes in range(0, len(pessoas)):
    if maior == pessoas[nomes][1]:
        print(pessoas[nomes][0], end=' ')

print(f"\nAs pessoas com o menor peso são: ", end='')
for nomes in range(0, len(pessoas)):
    if menor == pessoas[nomes][1]:
        print(pessoas[nomes][0], end=' ')
print(f"\nApenas {len(pessoas)} foram cadastradas")
