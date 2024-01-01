#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
#h = (co ** 2 + ca ** 2) ** (1/2) da pra fazer dessa forma ou
h = math.hypot(co, ca)
print('A hipotenusa vai medir: {:.2f} '.format(h))
