#verifica qual o tipo de valor do resultado
n1 = int(input('digite um número'))
print(type(n1))

#como somar dois números
n1 = int(input('digite um número'))
n2 = int(input('digite outro número'))
s = n1 + n2
print('a soma vale', s)

#e se for a soma entre x e y é z
n1 = int(input('digite um número'))
n2 = int(input('digite outro número'))
s = n1 + n2
#print('a soma entre', n1, 'e', n2, 'vale', s)
print('a soma entre {} e {} vale {}'.format(n1, n2, s))
