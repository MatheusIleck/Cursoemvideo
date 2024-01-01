#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite o numero: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[35m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
if tot == 2:
    print(f"\nO numero {n} é primo")
else:
    print(f"\nO numero {n} não é primo")
