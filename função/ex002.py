'''Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
parâmetro e mostre uma mensagem com tamanho adaptável.'''
def escreva(msg):
    print('-' * len(msg))
    print(msg)


msg = str(input('Digite a mensagem: '))


escreva(msg)
