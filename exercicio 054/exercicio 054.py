from datetime import date
atual = date.today().year
cont = 0
cont2 = 0
print(atual)
for c in range(1, 7):
    nascimento = int(input('Qual ano a {}º pessoa nasceu? '.format(c)))
    idade = atual - nascimento
    if idade >= 18:
        cont += 1
    else:
        cont2 += 1
print('{} pessoas atingiram a maioridade'.format(cont))
print('e {} ainda são menores de idade'.format(cont2))