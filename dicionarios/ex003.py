'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime
cadastro = dict()

cadastro['nome'] = str(input('Digite seu nome: '))
ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = datetime.now().year - ano_nascimento
cadastro['idade'] = idade
ctps = int(input('Digite o numero da carteira de trabalho: (0 não tem)'))
if ctps > 0:
    cadastro['ctps'] = ctps
else:
    cadastro['ctps'] = 'não possui'
cadastro['contratação'] = int(input('Digite o ano de contratação: '))
cadastro['salario'] = float(input('Digite o seu ultimo salario: '))
cadastro['aposentadoria'] = cadastro['idade']+ ((cadastro['contratação'] + 35) - datetime.now().year)

print(f'-' * 35)
print(f'{"Aposentadoria":^35}')
print(f'-' * 35)

for k, v in cadastro.items():
    print(f'- {k} do usuario tem o valor {v}')

