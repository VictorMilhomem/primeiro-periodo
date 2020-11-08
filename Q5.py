"""
Gere para uma lista uma quantidade de "n" nomes alfanuméricos ALEATÓRIOS  todos com 7 caracteres cada, cada qual composto de 4 letras  e 3 algarismos. Por exemplo ; AAAA012
O código ascii para a letra A é 65 e Z é 90.
Usando bubble sort ou outro algoritmo conhecido classifique os nomes gerados em ordem alfabética da A até Z;
Imprima os valores na ordem em que forem gerados e depois de ordenados.
Não pode usar sort(), max(), min() nem outras bibliotecas do python tipo numpy, scipy etc
Vc deverá colocar comentários com seu nome e explicando a lógica de seu programa
"""

# Nome: Victor Milhomem Losada López

from random import *


listaPalavras = []
# gerando 100 palavras aleatorias
for i in range(100): 
    palavra = '' 
    for j in range(4): # gerando 4 caracteres aleatorios
        letra = chr(randint(65, 90))
        palavra += letra  # adiocionando a string palavra
    for k in range(3): # gerando 3 numeros aleatorios
        num = str(randint(0, 9)) # gera o numero aleatorio e transforma em string para ser incorporado a palavra
        palavra += num 
    listaPalavras.append(palavra) # adicionando a lista

print('Valores gerados:\n{}'.format(listaPalavras))
# utilizando o bubble sort para ordenar a lista
troca = True
n = len(listaPalavras)-1

while n > 0 and troca:
    troca = False
    for i in range(n):
        if listaPalavras[i] > listaPalavras[i+1]:
            troca = True
            # troca os elementos de posição
            listaPalavras[i], listaPalavras[i+1] = listaPalavras[i+1], listaPalavras[i]
    n -= 1

print('\nValores ordenados:\n{}'.format(listaPalavras))

