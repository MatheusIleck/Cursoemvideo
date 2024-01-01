'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
 programa será interrompido quando o número solicitado for negativo.'''
while True:
    tabuada = int(input('Digite a tabuada que deseja: '))
    if tabuada < 0:
        break

    for c in range(1, 11):
        print(f"{c} X {tabuada} = {c * tabuada}")

