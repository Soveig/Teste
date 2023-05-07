num = int(input('Digite um número: '))
num2 = num % 2
if num2 == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é impar'.format(num))