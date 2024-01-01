'''Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
nas eleições.'''


def voto(idade):
    '''
    Essa função verifica se você ja tem idade para votar
    :param idade: O ano de nascimento
    :return: retorna a sua idade atual
    '''
    from datetime import date
    idade = date.today().year - ano
    if idade > 18:
        return f'Você tem {idade} anos e é obrigatorio votar!!'
    elif 16 <= idade < 18:
        return f'Você tem {idade} anos e pode votar porem não é obrigatorio!'
    elif idade < 16:
        return f'Você tem {idade} anos e não pode votar'


# Programa Principal
ano = int(input('Digite o ano: '))

print(voto(ano))
