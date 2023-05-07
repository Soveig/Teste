n1 = float(input('digite sua primeira nota: '))
n2 = float(input('digite sua segunda nota: '))
m = (n1+n2)/2
print('sua média é {:.1f}'.format(m))
if m >=6.0:
    print('Parabéns, você tirou nota azul!')
else:
    print('Estude mais! sua nota foi vermelha')
