#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
print(f"A Progressão Aritmetica é")
for c in range(pt, pt + 10 * r, r):
     print(c, end=' -> ')
