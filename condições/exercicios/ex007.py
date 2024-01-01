# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
# a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
# Calculo de média é a soma das notas divida pela quantidade de notas, como vamos ter duas notas eu vou dividir por dois
media = (n1 + n2) / 2
if media < 5.0:
    print(f"A media do aluno é {media:.1f}")
    print('\033[;31;40mREPROVADO BURRO!!!\033[m')
elif media >= 7.0:
    print(f"A media do aluno é {media:.1f}")
    print('\033[;30;42mAPROVADO GENIO!!!\033[m')
elif media >= 5.0 and media <= 6.9:
    print(f"A media do aluno é {media:.1f}")
    print('Você esta de recuperação')




