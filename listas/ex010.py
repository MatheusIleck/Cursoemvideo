'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
import random
jogos = list()
numeros = list()
quantidade_Jogos = int(input('Digite a quantidade de jogos que você deseja: '))

for jogo in range(0, quantidade_Jogos):
    numeros = [random.randint(0,  60), random.randint(0,  60),random.randint(0,  60),random.randint(0,  60)
        ,random.randint(0,  60),random.randint(0,  60),random.randint(0,  60)]
    jogos.append(numeros[:])
    numeros.clear()

for jogos_gerados in range(0, quantidade_Jogos):
    print(f'Jogo {jogos_gerados + 1}: {jogos[jogos_gerados]}')
