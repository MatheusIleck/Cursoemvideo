'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:
– Quantidade de notas
- A maior nota
- menor nota
- media da turma
- situação (opcional)'''


def notas(*notas, sit=False):
    totalNotas = len(notas)
    maiorNota = 0
    menorNota = notas[0]
    mediaTurma = 0
    turma = dict()
    situação = ''
    for v in notas:
        if v > maiorNota:
            maiorNota = v
        if v < menorNota:
            menorNota = v
        mediaTurma += v / totalNotas
    turma['Total'] = totalNotas
    turma['Maior Nota'] = maiorNota
    turma['Menor nota'] = menorNota
    turma['Media Turma'] = round(mediaTurma, 3)
    if mediaTurma > 6.0:
        situação = 'Aprovado'
    else:
        situação = 'Reprovado'
    if sit:
        turma['Situação'] = situação
        return turma
    else:
        return turma

# Programa Principal
resp = notas(5.5, 8.5, 1.5, sit=True)
print(resp)
