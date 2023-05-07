maior = 0
maior2 = 0
cont = 0
cont2 = 0
for c in range(1,5):
    nome = str(input('Qual o seu nome? '))
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual o seu sexo? '))
    cont = cont + idade
    if c == 1 and sexo == 'Masculino'.upper().lower():
        idade = maior
        nome = maior2
    else:
        if idade > maior and sexo == 'Masculino'.upper().lower():
            maior = idade
            maior2 = nome

        # contador feminino
        if idade < 20 and sexo == 'Feminino'.upper().lower():
            cont2 = cont2 + 1
média = cont / 4
print('A média das idades foi {}'.format(média))
print('A maior idade foi do {} de {} anos'.format(maior2, maior))
print('E existem {} mulheres com menos de 20 anos '.format(cont2))


