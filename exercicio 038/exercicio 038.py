from time import sleep
num1 = int(input('Digite um número: '))
num2 = int(input('digite outro número: '))
print('-=-' * 20)
print('COMPARANDO!')
print('-=-' * 20)
sleep(2)
if num1>num2:
    print('O primeiro valor é maior'.format(num1, num2))
elif num1<num2:
    print('O segundo valor é maior'.format(num2, num1))
else:
    print('{} e {} são números iguais'.format(num1, num2))
