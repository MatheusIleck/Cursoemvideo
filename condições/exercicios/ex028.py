'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
 mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
import random
contwin = soma = 0
while True:
    p = str(input('Você deseja jogar como par ou impar? '))
    if p == "par":
        x = random.randrange(1, 100)
        j = int(input('Digite um numero: '))
        soma = x + j
        if soma % 2 == 0:
            print(f"Você venceu! o numero {soma} par")
            contwin += 1
        else:
            print(f"você perdeu, o numero {soma} é impar, você ganhou {contwin} vezes")
            break
    if p == "impar":
        x = random.randrange(1, 100)
        j = int(input('Digite um numero: '))
        soma = x + j
        if soma % 2 == 0:
            print(f"Você perdeu! o numero {soma} par, você ganhou {contwin} vezes")
            break
        else:
            print(f"você venceu, o numero {soma} é impar")
            contwin += 1
