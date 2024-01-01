import random
n1 = str(input('Digite um Nome: '))
n2 = str(input('Digite outro Nome '))
n3 = str(input('Digite outro nome: '))
n4 = str(input('Digite o ultimo nome '))
lista = [n1, n2, n3, n4]

print('O aluno escolhido é {}'.format(random.choice(lista)))
