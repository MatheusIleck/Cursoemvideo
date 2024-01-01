'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
para cada palavra, quais são as suas vogais.'''

palavras = ('aprender', 'progamar', 'linguagem', 'python', 'eu', 'sou', 'muito', 'bom', 'no', 'valorant')

for posição in palavras:
    print(f"\nNa palavra {posição.upper()} temos: ", end='')
    for letra in posição: #Ele passa em cada letra da palavra
        if letra.lower() in 'aeiou': #ele verifica se tem as vogais na palavra
            print(letra, end=' ')
