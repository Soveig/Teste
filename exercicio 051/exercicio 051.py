from time import sleep
termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
print('-'*30)
print('GERANDO PROGRESÃO ARITIMÉTICA')
print('-'*30)
sleep(1)
for c in range(1, 11):
    c2 = c - 1
    termo1 = termo + (c2 * razão)
    print(termo1, end = ' ')
print('ACABOU!')