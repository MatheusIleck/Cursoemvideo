#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai
#tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
n = int(random.randrange(0, 10))
r = int(input('O computador escolheu um numero de 0 a 10, qual o numero que ele escolheu? '))
contador = 0
while r != n:
    r = int(input('Tente novamente: '))
    contador += 1
print(f"O numero escolhido era {n} você acertou em {contador} tentativas!")