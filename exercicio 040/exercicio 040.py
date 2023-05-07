nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
média = (nota1 + nota2) / 2
if média > 7.0:
    print('Sua média foi de {}'.format(média))
    print('Você foi aprovado!')
elif média >= 5.0 and média <= 6.9:
    print('Sua média foi de {}'.format(média))
    print('Você ficou de recuperação!')
else:
    print('Sua média foi de {}'.format(média))
    print('Você foi reprovado!')