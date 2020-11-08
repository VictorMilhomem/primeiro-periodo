"""1) Elabore um programa que leia o vetor A com 5 valores inteiros. Determine um
vetor com a seguinte lei de formação: Os termos de ordem impar de A são
multiplicados por 3 Os termos de ordem par de A são multiplicados por 2

2) Elabore um programa que leia dois vetores e determine o número de elementos
em comum entre 2 listas dadas como parâmetro. Exemplo: L1=[1,2,3,4,5] e
L2=[2,4]tem 2 elementos em comum

"""

# Exercicio 1
def changeArray(array):
    for i in range(0, len(array)-1):
        if array[i] % 2 == 0:
            array[i] *= 2

        else:
            array[i] *= 3

    return array

# Exercicio 2
def pesquisa_binaria(lista, busca):
    inicio = 0
    final = len(lista)-1
    dado_encontrado = False
    while inicio <= final and not dado_encontrado:
        meio = (inicio+final) // 2
        if lista[meio] == busca:
            dado_encontrado = True
        elif lista[meio] > busca:
            final = meio -1
        else:
            inicio = meio + 1
    return dado_encontrado


# Exercicio 2
def sameElements(arrayA, arrayB):
    quickSort(arrayB)
    find = False
    lista = []
    for i in range(0, len(arrayA)):
        find = pesquisa_binaria(arrayB, arrayA[i])
        if find:
            lista.append(arrayA[i])
    return lista


# Exercicio 2
def quickSort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1

    if inicio < fim:
        pivot = particao(lista, inicio, fim)
        quickSort(lista, inicio, pivot-1)
        quickSort(lista, pivot+1, fim)

def particao(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio

    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i += 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i


# Testando
import random

listaAleatoria = []
listaAleatoria2 = []

for i in range(10):
    listaAleatoria.append(random.randrange(1, 10))
    listaAleatoria2.append(random.randrange(1, 10))

listaA = ['a','b','c','d','e','f','g']
listaB = [1, 2, 3, 4, 5, 6, 7]
listaC = [2,5,3,8,20,1,12]
if __name__ == "__main__":


    print(sameElements(listaAleatoria, listaAleatoria2))
    print()
    print(sameElements(listaB, listaC))
    print()

