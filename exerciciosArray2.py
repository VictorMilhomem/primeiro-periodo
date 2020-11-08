"""
1) Elabore um programa que determine o tamanho t da maior sequência de números
iguais em uma lista A. Exemplo: Supor que sejam armazenados os seguintes
valores para a lista A: [1,1,6,6,7,7,7,7,1,1,1], então t=4

2) Dadas 2 listas com n números entre 0 e 9, interpretadas como dois números inteiros de
n dı́gitos, calcular uma lista que representa a somatória dos dois números. Exemplo:
Primeira lista:
                1 2 3 4
Segunda lista:
                9 9 0 0
Somatória
              1 1 1 3 4

"""


# Exercicio 1
def numIguais(lista):
    elemento = lista[0]
    comp_atual = 1
    t = 1
    for i in range(1,len(lista)):
        if lista[i] == elemento:
            comp_atual += 1
            if t < comp_atual:
                t = comp_atual
        else:
            elemento = lista[i]
            comp_atual = 1
    return t


# Exercicio 2
def somatoria(Lista1, Lista2):
    if len(Lista1)!=len(Lista2):
        return 'listas de tamanhos diferentes'
    Lista3 = []
    for i in range (0,len(Lista1)):
        Lista3.append(0)
    vai_um = 0
    i = len(Lista1)-1
    while i >= 0:
        soma = Lista1[i] + Lista2[i] + vai_um
        if soma >= 10:
            soma -= 10
            vai_um = 1
        else:
            vai_um = 0
        Lista3[i] = soma
        i -= 1
    if vai_um == 1:
        Lista3 = [1]+Lista3
    return Lista3
        



# Testando

lista1 = [1, 2, 3, 4]
lista2 = [9, 9, 0, 0]
lista = [2, 1, 3, 6, 6, 1, 2, 6,1, 1, 1, 1, 7, 8, 9, 7]

if __name__ == '__main__':

    print(numIguais(lista))
    print()

    print(somatoria(lista1, lista2))
    
