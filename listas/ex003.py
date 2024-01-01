''' Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
numeros = []
for c in range(0, 5):
    valor = int(input(f"Digite o {c + 1} valor: ")) #digita os valores
    if c == 0 or valor > numeros[-1]: #verifica se é o começo do laço e adiciona na lista  ou verifica se o valor digitado é maior que o ultimo argumento da lista
        numeros.append(valor) #adiciona o valor ao final da lista
    else:
        posiçao = 0 #começa uma variavel pra varrer a lista
        while posiçao < len(numeros): #define o limite do while ate o final da lista
            if valor <= numeros[posiçao]: #verifica se o valor é menor ou igual ao valor que esta naa variavel posição
                numeros.insert(posiçao, valor) #adiciona o valor na variavel posição
                break
            posiçao +=1

print(numeros)

