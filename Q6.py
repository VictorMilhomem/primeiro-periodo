"""
Elabore um programa Python que leia uma matriz quadrada de m xm valores inteiros. Usando pesquisa sequencial verificar se um determinado valor digitado pelo usuário se encontra na diagonal principal.
Exibir a matriz lida sob a forma de tabela e legendas: "Matriz Lida" e "O valor se encontra (ou não) na diagonal principal".
Não pode usar os métodos index(), count() ou as bibliotecas numpy, scipy ou outra não integrante ao curso.
Vc deverá colocar comentários com seu nome e explicando a lógica de seu programa
"""

# Nome: Victor Milhomem Losada López


matriz = [None]
while True:
    try:
        ordem = int(input('Digite a ordem da matriz: ')) 
        if ordem <= 0: raise # eveitando erro de uma matriz de ordem 0
        
        matriz *= ordem # dando a matriz criada o quantidade de elementos dada pelo usuario
        for i in range(ordem):
            matriz[i] = [None] * ordem # gerando a matriz quadrada (m x m)

        # input para o usuario criar cada elemento da matriz
        # dados sendo tratados para evitar valores não inteiros e evitando outros tipos de entrada de dados
        for i in range(ordem):
            for j in range(ordem):  
                matriz[i][j] = int(input('Digite o elemento A [{}, {}]: '.format(i+1, j+1)))

        buscar = int(input('Qual valor deseja verificar se está diagonal principal? '))
        break
    except:
        print('Valor invalido!')



encontrado = False
# fazendo a busca sequencial pela matriz
for k in range(0, ordem):
    for j in range(0, ordem):
        if k == j: # verificando os valores da diagonal principal 
            if matriz[k][j] == buscar:
                encontrado = True


# Imprimindo a matriz em forma de tabela
print ('\n{:*^50}\n'.format('Matriz Lida'))
for i in range(ordem):
    for j in range (ordem):
        print (('{:>10d}').format(matriz[i][j]),end='')
    print()


if encontrado:
    print('\nO valor {} foi encontrado na diagonal principal '.format(buscar))
else:
    print('\nO valor {} não foi encontrado na diagonal principal '.format(buscar))
