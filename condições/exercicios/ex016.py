#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
#maioridade e quantas já são maiores.
import datetime

# Obtendo o ano atual
ano_atual = datetime.datetime.now().year
print(f"Ano atual:{ano_atual}")

data = []
maior = []
menor = []
for c in range(0, 7, 1):
     valor = int(input('Digite o ano de nascimento: '))
     data.append(valor)
     if ano_atual - data[c] > 18:
          maior.append(data[c])
     else:
          menor.append(data[c])

print(f"A quantidade de pessoas que ja são maior de idade é de {len(maior)} e são os anos: {maior}")
print(f"E a quantiadade de pessoas que ainda não sao maiores de idade é de {len(menor)} e são os anos:{menor}")
