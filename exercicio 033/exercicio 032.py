num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num2 and num3>num1:
    maior = num3
print('O menor valor é {} e o maior é {}'.format(menor, maior))

