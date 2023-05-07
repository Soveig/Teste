salário = float(input('Qual o seu salário? '))
if salário <= 1.250:
    novo = salário + (salário * 0.15)
else:
    novo = salário + (salário * 0.10)
print('seu salário fica {}'.format(novo))

