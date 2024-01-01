'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze'
                , 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    seletorDeNumero = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= seletorDeNumero <= 20:
        break
    print('Burro é ate 20')

print(F"O numero é {numeros[seletorDeNumero]}")
