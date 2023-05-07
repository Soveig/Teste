lado1 = float(input('Primeira Medida: '))
lado2 = float(input('Segunda Medida: '))
lado3 = float(input('Terceira Medida: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1:
    print('As retas podem formar um triângulo', end='')
    if lado1 == lado2 == lado3:
        print('Equilátero')
    elif lado1 != lado2 != lado3 != lado1:
        print('Escaleno')
    else:
        print('Isoceles')
else:
    print('As retas não formam um triângulo')
