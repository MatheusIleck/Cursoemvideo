''' Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram
digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    continua = ' '
    while continua not in 'SsNn':
        continua = str(input('Deseja continuar? [S/N]')).upper()
    if continua == 'N':
        break

lista.sort(reverse=True)
if 5 in lista:
    print(f"O numero 5 esta na lista na posição: {lista.index(5) + 1}")
print(f"A lista na forma invertida fica: {lista}")
print(f"{len(lista)} numeros foram digitados. ")
