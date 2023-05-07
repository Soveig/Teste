sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmfF':
    sexo = str(input('Dados invalidos, digite novamente: '))
print('Sexo {} registrado com sucesso'.format(sexo))