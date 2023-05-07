
num = int(input('Digite um número: '))
base = str(input('Binário, Octal ou Hexadecimal? '))
if base == 'Binário':
    print('O número {} convertido para Binário fica {}'.format(num, bin(num)[2:]))
elif base == 'Octal':
    print('O número {} convertido para Octal fica {}'.format(num, oct(num)[2:]))
else:
    print('O numero {} convertido para hexadecimal fica {}'.format(num, hex(num)[2:]))


