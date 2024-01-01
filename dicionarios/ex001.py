'''Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um
dicionário. No final, mostre o conteúdo da estrutura na tela.'''
cadastro = dict()

cadastro['nome'] = str(input('Digite o nome do aluno: '))
cadastro['media'] = float(input('Digite a media do aluno: '))
if cadastro['media'] < 5.0:
    cadastro['situação final'] = 'reprovado'
else:
    cadastro['situação final'] =  'aprovado'

print('-' * 35)
for v in cadastro:
    print(cadastro[v])
