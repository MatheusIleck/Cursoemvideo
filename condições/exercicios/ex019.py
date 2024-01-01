#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a
#digitação novamente até ter um valor correto.

sexo = str(input('Digite o sexo [M/F]: ')).upper()
while sexo not in "MmFf":
    sexo = str(input('Por favor Digite o seu sexo: '))
print(f"O sexo é {sexo}")

