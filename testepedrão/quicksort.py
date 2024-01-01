def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1  # Pega o ultimo elemento da lista
    if inicio < fim:
        p = partition(lista, inicio, fim)  # Pega a posição do pivo atraves de outra função
        quicksort(lista, inicio, p - 1)  # lista da esquerda
        quicksort(lista, p + 1, fim)  # lista da direita


def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i
