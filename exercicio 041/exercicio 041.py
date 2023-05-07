from datetime import date
nascimento = int(input('Qual o seu ano de nascimento? '))
idade = date.today().year - nascimento
print('Você tem {} anos'.format(idade))
if idade >= 0 and idade <= 9:
    print('Sua categoria é Mirim')
elif idade > 9 and idade <=14:
    print('Sua categoria é Infantil')
elif idade > 14 and idade <= 19:
    print('Sua categoria é Júnior')
elif idade > 19 and idade <= 25:
    print('Sua categoria é Sênior')
else:
    print('Sua categoria é Master')