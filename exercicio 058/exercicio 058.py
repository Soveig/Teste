from random import randint
computador = randint(1,10)
cont = 0
usuario = int(input('Qual número estou pensando? '))
while usuario != computador:
    if usuario > computador:
        print('Errou é menos, tente novamente!')
    else:
        print('Errou é mais, tente novamente')
    cont += 1
    usuario = int(input('Digite outro número: '))
print('Você acertou, eu realmente estava pensando no número {}'.format(computador))
print('Foram necessarios {} palpites para me vencer'.format(cont + 1))