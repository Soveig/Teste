Distância = float(input('A viagem será de quantos km?'))
if Distância <= 200:
    preço = Distância * 0.50
else:
    preço = Distância * 0.45
print('O preço da viagem ficou em R${:.2f}'.format(preço))