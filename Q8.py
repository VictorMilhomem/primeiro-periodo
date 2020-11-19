"""
Elabore um programa que leia para uma lista o cpf, o nome e o time de futebol de preferência de um grupo indeterminado de pessoas. Esta entrada deve ser validada.
O aluno poderá estabelecer um mínimo de 4 dos principais times podendo ser do Rio de Janeiro (flamengo, fluminense,vasco, botafogo)
usando ou não abreviatura ou de outro estado/pais que deseja.

Usando pesquisa binária verifique se um determinado nome se encontra neste grupo de pessoas.

O programa deverá ser modularizado com no mínimo 3 funções. Estas funções devem ter um objetivo que deve constar de um comentário.

Na saída devem aparecer os dados lidos e se a pessoa se encontra ou não no grupo. o nome do time de futebol deve aparecer por extenso.

"""

def pesquisa_binaria(lista, busca):
    inicio = 0
    final = len(lista)-1
    dado_encontrado = False
    while inicio <= final and not dado_encontrado:
        meio = (inicio+final) // 2  # encontrando o indice do elemento do meio
        if lista[meio] == busca:  # se o elemento do meio for igual a busca, retorna true
            dado_encontrado = True
        elif lista[meio] > busca: 
            final = meio -1  # se o elemento do meio for maior que o procurado o loop se repetira so desta vez ate o elemento anterior ao indice do meio da lista
        else:
            inicio = meio + 1  # se o elemento do meio for menor que o procurado o loop se repetira so desta vez a partir do elemento seguinte ao indice do meio da lista
    return dado_encontrado  # retorna o valor booleano 


def ler_lista():
    times_validos = ['flamengo', 'fluminense', 'vasco', 'botafogo']
    lista = []
    cont = 1 # adicionando um contador
    while True:
        try:
            print('Pessoa {}:\n'.format(cont)) # utilizando o contador para o usuario identificar as pessoas que estão sendo digitadas
            nome = input('Digite o nome: ').lower()
            # flag do programa
            if nome == '': break
            cpf = input('Digite o cpf: ')
        
            time = input('Digite o time: ').lower()
            if time not in times_validos: raise
            print()
            registrar = nome + ',' + cpf + ',' + time # unindo em uma unica string
            lista.append(registrar) # adicionando a lista
            cont += 1 # muda para a pessoa seguinte
        except:
            print('\nTime invalido\n')
    return lista

def ordenar(lista):
    lista.sort()  # ordenando lista para aplicar a pesquisa binaria e ainda conseguir identificar o indice correspondente de cada pessoa
                  # quando separados em novas listas no proximo passo 
    # separando em outras listas
    cpf = []
    nomes = []
    times = []
    for i in lista: # iterando por todas as strings da lista
        sep = i.split(',') # separando cada string no formato csv pela virgula
        nomes.append(sep[0]) # adicionando a string cpf a lista de nomes
        cpf.append(sep[1]) # adicionando a string nome a lista de cpf
        times.append(sep[2]) # adicionando a string time a lista de times
    return cpf, nomes, times


def imprimir(cpf, nomes, times, buscar):
    # aplicando a pesquisa binaria e armazenando o valor booleano na variavel encontrou
    encontrou = pesquisa_binaria(nomes, buscar.lower())
    
    # imprimindo dados informados em forma de tabela
    print ('\n{:*^50}\n'.format('Informações Recebidas'))
    print('Cpf | Nome| Time')
    for i in range(len(nomes)):
        print (('{} | {} | {}').format(cpf[i], nomes[i], times[i], sep=''))
    print()
    print('\n{:*^50}\n'.format('*'))

    if encontrou:
        # encontrando o time correspondente a pessoa procurada
        for i in range(len(nomes)):
            if nomes[i] == buscar:
                time = times[i].capitalize()
                break
        print('\nEncontrei o nome {} e seu time é {}'.format(buscar.capitalize(), time))
    else:
        print('\nNão encontrei o nome {}'.format(buscar.capitalize()))
    

# programa 

lista = ler_lista()

cpf, nomes, times = ordenar(lista)
while True:
    try:
        buscar = input('Qual nome deseja buscar? ')
        if buscar == '': raise
        else: break
    except:
        print('Digite um nome para buscar')
imprimir(cpf, nomes, times, buscar)





