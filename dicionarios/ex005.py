''''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B)
A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média'''
continuar = 'S'
dados = dict()
cadastro = list()
mediaIdade = 0
while continuar in 'S':
    dados['nome'] = str(input('Digite o nome: '))
    dados['idade'] = int(input('Digite a idade: '))
    dados['sexo'] = str(input('Digite o Sexo [M/F]:'))
    while dados['sexo'] not in 'MmFf':
        dados['sexo'] = str(input('ERRO! Por favor digite apenas [M/F]:'))
    cadastro.append(dados.copy())
    mediaIdade += dados['idade']
    continuar = input('Deseja continuar [S/N]: ').upper()
    while continuar not in 'SsNn':
        continuar = input('Erro! Digite apenas [S/N]: ').upper()

print()

print(f'A quantidade de pessoas cadastradas é {len(cadastro)}')
mediaIdade = mediaIdade / len(cadastro)
print(f'A media é {mediaIdade:.2f}')
print(f'As listas de mulheres são: ')
for p in cadastro:
    if p['sexo'] in 'Ff':
        print(p['nome'])
print(f'As listas de pessoas acima da media são: ')
for media in cadastro:
    if media['idade'] > mediaIdade:
        print(media['nome'])



