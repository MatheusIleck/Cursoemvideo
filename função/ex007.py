'''Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou
não na tela o processo de cálculo do fatorial.'''


def fatorial(n, show=False):
    '''
    -> Calcula o Fatorial de um número.
    :param n: O numero a ser calculado.
    :param show: (opcional) Mostra ou não o processo.
    :return: O valor do fatorial de um número N
    '''
    f = 1
    for v in range(n, 0, - 1):
        if show:
            print(v, end='')
            if v > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= v
    return f


n = int(input('Digite o número: '))

print(fatorial(n, show=False))
