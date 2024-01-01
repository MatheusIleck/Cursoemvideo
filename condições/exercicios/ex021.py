'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite o segundo valor: '))
menu = 0
while menu == 0:
    menu = int(input('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\n'))
    if menu == 1:
        print(f"A soma dos dois numeros é: {n1 + n2}")
    elif menu == 2:
        print(f"A multiplicação dos numeros é: {n1 * n2}")
    elif menu == 3:
        if n1 > n2:
            print(f"O numero {n1} é maior que {n2}")
        elif n2 > n1:
            print(f"O numero {n2} é maior que {n1}")
        else:
            print('Os numeros são iguais')
    elif menu == 4:
        n1 = float(input('Digite o novo valor: '))
        n2 = float(input('Digite o segundo valor: '))
        menu = 0
    elif menu == 5:
        print("Programa finalizado")
    else:
        menu = int(input('Por favor digite um numero valido'))
