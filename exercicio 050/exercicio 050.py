soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('A soma dos {} termos pares resulta em {}'.format(cont, soma))
