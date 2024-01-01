###Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
# conversão: 1 para binário, 2 para octal e 3 para hexadecimal.###
numero = int(input('Digite o numero: '))
print('=' * 15, 'Menu de conversão', '=' * 15, '\n 1 - Binário \n 2 - octal \n 3 - hexadecimal \n', '=' * 485)
escolha = int(input('Selecione: '))
if escolha == 1:
    print(f"convertido para Binario é igual  a {bin(numero)[2:]}")

elif escolha == 2:
    print(f"Convertido para octal é igual a {oct(numero)[2:]}")

elif escolha == 3:
    print(f"Convertido para octal é igual a {hex(numero)[2:]}")





