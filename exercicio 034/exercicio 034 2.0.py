salário = float(input('Qual o seu salário? '))
if salário <= 1250:9
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('seu salário ficou: {} '.format(novo))


