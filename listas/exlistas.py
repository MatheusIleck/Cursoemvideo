'''valores = []
valores.append(1)
valores.append(2)
valores.append(3)

for c, v in enumerate(valores): #enumarate pega tanto o valor quanto o indice da lista
    print(f"Na posição {c} encontrei o valor {v}.")
    '''

a = [2, 3, 4, 7]
#b = a Se eu usar somente o simbolo "=" ele vai fazer uma ligação entre as duas listas, ou seja, se eu alterar uma ele
      #vai alterar a outra

b = a[:] #ele vai fazer uma copia da lista A sem essa ligação, ou seja, eu vou conseguir alterar a Lista B sem afetar A
         #lista A
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
