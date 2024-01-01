###Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

idade = int(input('Digite sua idade: '))
if idade <= 9:
    print(f"Você tem {idade} anos, sua categoria é: Mirim.")
elif 9 < idade <= 14:
    print(f"Você tem {idade} anos, sua categoria é: Infantil.")
elif 14 < idade <= 19:
    print(f"Você tem {idade} anos, sua categoria é: Júnior")
elif 19 < idade <= 25:
    print(f"Você  tem {idade} anos, sua categoria é: senior")
else:
    print(f"Você tem {idade} anos, sua categoria é: Master")