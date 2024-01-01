###Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
# Km para viagens de até 200Km e R$0,45 parta viagens mais longas.###

km = float(input('Digite a distância em km: '))
if km <= 200:
    preço = km * 0.50
    print(f"O preço da viagem é de R${preço}")
else:
    preço = km * 0.45
    print(f"O preço da viagem é de R${preço:.2f}")
