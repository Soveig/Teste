num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0 :
        print(c,end=' ')
        tot += 1
if tot == 2:
    print('\nO número digitado é primo')
else:
    print('\nSeu número não é primo')