'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''
numeros = [[], []]

for v in range(1, 8):
    n = int(input(f'Digite o {v} numero: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

numeros[0].sort()
numeros[1].sort()
print(f'A lista de numeros pares é {numeros[0]}')
print(f'E a lista de numeros impares é {numeros[1]}')