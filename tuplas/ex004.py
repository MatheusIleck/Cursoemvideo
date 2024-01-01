'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''
cont = 0
tupla = (int(input('Digite um numero: ')),
         int(input('Digite outro numero: ')),
         int(input('Digite mais um numero: ')),
         int(input('Digite o ultimo numero: ')))

print(f"Tupla: {tupla}")
print(f"O numero 9 foi digitado {tupla.count(9)} vezes")
if 3 in tupla:
    print(f"O numero 3 esta na {tupla.index(3)+1}º posição")
else:
    print('O numero 3 não foi digitado')
print(f"Os numeros pares são: ", end='')

for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
