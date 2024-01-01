'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a
digitar valores.'''
menu = ''
cont = 0
aux = 0
soma = 0
maiorNumero = 0
menorNumero = 0
while menu != "N":
    n = int(input('Digite o numero: '))
    cont += 1
    soma += n
    if aux == 0:
        aux = n
        menorNumero = aux
    elif n > aux or n == aux:
        maiorNumero = n
    elif n < aux:
        menorNumero = n
    menu = str(input('Deseja continuar? [S/N]: ')).upper()
soma = soma / cont
print(F"{cont} numeros foram digitados, O maior numero é {maiorNumero} e o menor é {menorNumero} e a media é {soma}")