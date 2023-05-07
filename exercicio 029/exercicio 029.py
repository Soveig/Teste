veloc = float(input('Quantos Km está seu carro? '))
multa = float(veloc - 80) * 7
if veloc > 80:
    print('Você foi multado! Terá que pagar R$:{:.2f}'.format(multa))
else:
    print('Você não foi multado! Parabéns')