'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''
adulto = homem = mulher = 0
while True:
    idade = int(input('Digite a Idade: '))
    if idade > 18:
        adulto += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o Sexo [M/F]: ')).upper()
        if sexo == 'M':
            homem += 1
        elif sexo == 'F':
            mulher += 1
    c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar? [s/n]')).upper()
        if c == 'N':
            print(f"Apenas {adulto} tem 18 anos, foram cadastrados {homem} homens e {mulher} mulheres")
        break


