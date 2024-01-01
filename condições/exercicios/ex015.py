# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos
# de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input('Digite a frase: ')).strip().upper()
separa = frase.split() #separei em uma lista
junta = ''.join(separa) #juntei as palavras eliminando os espaços
inverso = ''

for c in range(len(junta) - 1, -1, -1): #Aqui a gente faz um for correndo de forma inverso na frase
    inverso += junta[c] #eu jogo tudo na variavel inverso

if inverso == junta:
    print(f"A frase {frase} é um pálindromo")
else:
    print('A frase não é um pálindromo')

#existe também uma outra forma de resolver que seria pegando
#inverso = junto[::-1] definindo que ele é igual ao junto so que começando de tras pra frente
