
home = float(input('Valor da casa: '))
wage = float(input('Salário: '))
years = int(input('Quantos anos de financiamento: '))
home2 = home / (years * 12)
if (wage/100) * 30 >= home2:
    print('Para pagar uma casa de R$:{} a prestação será de R$:{:.2f} \nEmpréstimo Aprovado'.format(home, home2))
else:
    print('Para pagar uma casa de R$:{} a prestação será de R$:{:.2f} \nEmprestimo Negado'.format(home, home2))

