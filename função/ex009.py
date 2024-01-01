'''Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função
input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)'''
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        número = str(input(msg))
        if número.isnumeric():
            valor = int(número)
            ok = True
        else:
            print('\033[0;31mErro, por favor digite um numero Valido. \033[m')
        if ok:
            return valor


# Programa principal
n = leiaInt('Digite um valor: ')
print(f'Você acabou de digitar o numero {n}')
