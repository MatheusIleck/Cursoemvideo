'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
jogadores = list()
dados = dict()
gols = list()
totaljogos = 0
continuar = 'S'

while continuar in 'Ss':
    dados['nome'] = str(input('Digite o nome do jogador: '))
    jogos = int(input('Digite a quantidade de jogos: '))
    for g in range(0, jogos):
        gols.append(int(input(f'Digite a quantidade de gols do {g+1}º jogo:')))
    dados['gols'] = gols.copy()
    dados['total'] = sum(gols)
    gols.clear()
    jogadores.append(dados.copy())
    continuar = str(input('Deseja continuar? [S/N]: '))
    while continuar not in 'SsNn':
        continuar = input('Digite apenas [S/N]: ')

for k, v in enumerate(jogadores):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()


numeroJogador = int(input('Digite o numero do jogador para acessar suas estatisticas [999 para sair]: '))
while numeroJogador != 999:
    print(jogadores[numeroJogador])
    for v in range(0, len(dados['gols'])):
        print(f'O jogo {v + 1} teve {dados["gols"][v]} gols')
    print('-=' * 35)

    numeroJogador = int(input('Digite o numero do jogador para acessar suas estatisticas [999 para sair]: '))
    if numeroJogador == 999:
        break

