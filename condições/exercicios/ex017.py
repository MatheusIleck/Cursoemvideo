#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
peso = []
for c in range(0, 5, 1):
    valor = float(input(f'Digite o Peso da {c+1}º pessoa: '))
    peso.append(valor)

peso.sort(reverse=True)
print(f"O maior peso é de {peso[0]} e o menor é de {peso[-1]}")