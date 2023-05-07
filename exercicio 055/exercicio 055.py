maior = 0
menor = 0
for c in range(1, 5+1):
    peso = float(input('Digite seu peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < maior:
            menor = peso

print(maior)
print(menor)