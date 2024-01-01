'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o
menor valor digitado e as suas respectivas posições na lista.'''
numeros = []
maior = menor = 0
for cont in range(0, 5):
    numeros.append(int(input('Digite um numero: ')))
    if cont == 0:
        maior = menor = numeros[cont]
    else:
        if numeros[cont] > maior:
            maior = numeros[cont]
        if numeros[cont] < menor:
            menor = numeros[cont]
print(f"O maior numero foi {maior} na posição ", end="")
for index, valor in enumerate(numeros):
    if valor == maior:
        print(f"{index + 1}...", end="")
print()
print(f"O menor numero foi {menor} na posição ", end="")
for index, valor in enumerate(numeros):
    if valor == menor:
        print(f"{index + 1}...", end="")


