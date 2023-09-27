"""
Para cada elemento i no array de tamanho n
    para cada elemento j no array do tamanho n - 1
    Se o valor da posição i for maior que a posição j, troque os elementos i e j
    exiba o array ordenado
"""

# Considere a lista como exemple de ordenação
lista = [9, 3, 5, 8, 1]

# primeira lista do algoritmo (troca os elementos 6 e 3)
lista2 = [3, 6, 12, 7]

# segunda lista do algoritmo (troca os elementos 6 e 12)
lista3 = [3, 6, 12 ,7]


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(bubble_sort(lista))
print(bubble_sort(lista2))
print(bubble_sort(lista3))