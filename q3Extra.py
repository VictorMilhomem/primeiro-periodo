"""
Dado um triangulo qualquer verifique se ele é equilatero, isosceles ou retangulo
"""


while True:
    try:
        lado1 = int(input("Lado 1: "))
        if lado1 <= 0: raise
        lado2 = int(input("Lado 2: "))
        if lado2 <= 0: raise
        lado3 = int(input("Lado 3: "))
        if lado3 <= 0: raise

        # Lógica do programa

        if lado1 > (lado2 + lado3) or lado2 > (lado1 + lado3) or lado3 > (lado1 + lado2):
            print('Não é um triangulo.')

        elif lado1 == lado2 == lado3:
            print('Triangulo equilátero.')

        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print('Triangulo isósceles.')

        elif lado1 > lado2 and lado1 > lado3:
            if lado1 **2 == (lado2**2) + (lado3**2):
                print('Triangulo retangulo.')
            else:
                print('Triangulo escaleno')
        elif lado2 > lado3 and lado2 > lado1:
            if lado2 **2 == (lado1**2) + (lado3**2):
                print('Triangulo retangulo.')
            else:
                print('Triangulo escaleno')
        elif lado3 > lado2 and lado3 > lado1:
            if lado3 **2 == (lado2**2) + (lado1**2):
                print('Triangulo retangulo.')
            else:
                print('Triangulo escaleno')

        # Flag do programa
        stop = str(input('Deseja continuar(s/n)? '))
        if stop == 'n': break
        elif stop != 's':
            print('Resposta invalida / parando o programa...')
            break
        

        
    except:
        print('Valor invalido!')

    
        
