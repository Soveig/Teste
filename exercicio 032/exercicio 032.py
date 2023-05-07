ano = int(input('Digite qualquer ano: '))
#'and' vai atuar como uma cola, pra colocar mais de um comando e '!=" significa difenrente, 'or' coloca um terceiro comando
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))

