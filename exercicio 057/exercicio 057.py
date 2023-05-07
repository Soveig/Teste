nome = str(input('''Qual o seu gênero
[M] Masculino
[F] Feminino
Digite aqui: ''')).upper()
while nome != 'M' and nome != 'F':
    nome = str(input('Dados invalidos! Digite novamente: ')).upper()
if nome == 'M':
    nome = 'Masculino'
else:
    nome = 'Feminino'
print('OK! seu gênero é {}'.format(nome))
