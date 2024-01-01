''' lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
c = 0
while c < 10:
    pt += r
    print(pt)
    c += 1
