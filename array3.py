"""
1) Elabore um programa que leia uma matriz quadrada A de tamanho m, calcule o
número de zeros contidos na matriz.Imprimir a matriz lida sob a forma de tabela
e o resultado obtido.

2) Elabore um programa que leia uma matriz quadrada de tamanho mxm e
determine o somatório de todos os números presentes na diagonal principal da
matriz. Imprimir a matriz lida sob a forma de tabela e o resultado obtido

3) Elabore um programa que leia uma matriz quadrada de tamanho mxm e
determine o somatório de todos os números presentes na diagonal secundária
da matriz. Imprimir a matriz lida sob a forma de tabela e o resultado obtido.
"""

# Exercicio 1
def contZeros(matriz):
    quadrada = False
    cont = 0
    for i in range(0, len(matriz)):
        if len(matriz) == len(matriz[i]):
            quadrada = True
        
    if quadrada:
        for i in range(0, len(matriz)):
            for j in range(0, len(matriz[i])):
                if matriz[i][j] == 0:
                    cont += 1
        return cont
    return 'A matriz não é quadrada!'


def imprimirMatriz(matriz, n):
    print ('\n{:*^30}\n'.format('Matriz Lida'))
    for i in range(n):
        for j in range (n):
            print (('{:>10d}').format(matriz[i][j]),end='')
        print()

# EXercicio 2
def somaDPrincipal(matriz):
    quadrada = False
    soma = 0
    for i in range(0, len(matriz[0])):
        if len(matriz) == len(matriz[i]):
            quadrada = True
    if quadrada:
        for i in range(0, len(matriz)):
            for j in range(0, len(matriz[0])):
                if i == j:
                    soma += matriz[i][j]
        return soma
    return 'A matriz não é quadrada!'

# Exercicio 3
def somaDSecundaria(matriz):
    quadrada = False
    soma = 0
    for i in range(0, len(matriz[0])):
        if len(matriz) == len(matriz[i]):
            quadrada = True
    if quadrada:
        for i in range(0, len(matriz)):
            for j in range(0, len(matriz[0])):
                if i + j == len(matriz[0])-1:
                    soma += matriz[i][j]
        return soma
    return 'A matriz não é quadrada!'

# Testando
matriz = [[1, 2, 3], [0, 0, 1], [5, 0, 2]]

if __name__ == "__main__":
    imprimirMatriz(matriz, 3)
    print()
    print('Contém {} zeros'.format(contZeros(matriz)))
    print()

    print(somaDPrincipal(matriz))
    print()
    print(somaDSecundaria(matriz))
