a = float(input('informe o primeiro lado: '))
b = float(input('informe o segundo lado: '))
c = float(input('informe o terceiro lado: '))
if a < b + c and b < a + c and c < a + b:
    print('os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos acima não podem formar um triângulo')
