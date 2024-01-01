km = int(input('Digite a velocidade do carro: '))
if km > 80:
    multa = (km - 80) * 7
    print(f"multa é de {multa}")
else:
    print('Você esta na velocidade normal')
