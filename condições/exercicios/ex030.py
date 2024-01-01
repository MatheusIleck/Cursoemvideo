'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
 ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
soma = produtoAcimaDeMil = menorPreco = cont = 0
produtoMaisBarato = ''
while True:
    nomeDoProduto = str(input('Digite o nome do Produto:'))
    precoProduto = float(input('Digite o preço do produto:'))
    cont += 1
    if cont == 1 or precoProduto < menorPreco:
        menorPreco = precoProduto
        produtoMaisBarato = nomeDoProduto
    if precoProduto >= 1000:
        produtoAcimaDeMil += 1
    soma += precoProduto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print(f"O total gasto foi de RS{soma}, Apenas {produtoAcimaDeMil} produtos custam acima de R$1000 reais")
print(f"E o produto mais barato é {produtoMaisBarato}")
