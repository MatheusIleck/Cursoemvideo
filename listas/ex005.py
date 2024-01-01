'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
listas geradas.'''
lista = []
listapar = []
listaimpar = []
while True:
    lista.append(int(input('Digite o valor: ')))
    contador = ' '
    while contador not in 'SsNn':
        contador = str(input('Deseja continuar? [S/N] ')).upper()
    if contador == 'N':
        break
for valores in range(0, len(lista)):
    if lista[valores] % 2 == 0:
        listapar.append([lista[valores]])
    else:
        listaimpar.append([lista[valores]])

print(f"A lista completa é {lista}")
print(f"A lista par é {listapar}")
print(f"A lista par é {listaimpar}")

