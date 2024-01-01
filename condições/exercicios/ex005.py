###Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da
# casa, o Salario do comprador e em quantos anos ele vai pagar. ###
casa = float(input('Digite o Valor da casa: '))
salario = float(input('Digite o seu Salário: '))
parcelas = int(input('Quantos anos você vai pagar: '))
pm = casa / (parcelas * 12)
if pm >= salario * 30 / 100:
    print('\033[0;31;40mEmprestimo Negado!\033[m.')
else:
    print('\033[;30;42mEmprestimo Aprovado!\033[m.')
