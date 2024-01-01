''' Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).'''
n = contador = soma = 0
n = int(input('Digite um valor: '))
while n != 999:
    soma += n
    contador += 1
    n = int(input('Digite outro numero: '))
print(f"{contador} numeros foram digitados e a soma total é de: {soma}")
