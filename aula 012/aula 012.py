nome = str(input('qual é o seu nome? '))
if nome == 'Gabriel':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria'or nome == 'Paulo':
    print('seu nome é bem popular')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome Feminino')
else:
    print('seu nome é bem normal, {}'.format(nome))
print('tenha um bom dia, {}'.format(nome))