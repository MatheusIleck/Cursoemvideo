#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o.
soma = 0
for c in range(1, 7, 1):
    n = int(input('Digite o numero: '))
    if n % 2 == 0:
        soma += n
print(f"A soma de todos os numeros digitados é {soma}")
