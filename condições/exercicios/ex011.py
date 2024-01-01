#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite o numero da tabuada: '))
for c in range(1, 11, 1):
    print(f"{n} X {c} = {n * c}")

