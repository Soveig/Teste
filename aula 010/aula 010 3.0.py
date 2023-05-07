n1 = float(input('digite sua primeira nota: '))
n2 = float(input('digite sua segunda nota: '))
m = (n1+n2)/2
print('sua média é {:.1f}'.format(m))
print('Parabéns' if m >= 6.0 else 'Estude mais')
