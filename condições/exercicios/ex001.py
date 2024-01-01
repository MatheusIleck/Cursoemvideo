import random
n = int(random.randrange(0, 10))
r = int(input('O computador escolheu um numero de 0 a 10, qual o numero que ele escolheu? '))
if r == n:
    print('Parabénsss você acertou!! o numero era {} '.format(n))
else:
    print('Você errou, muito burro! o numero era {}'.format(n))
