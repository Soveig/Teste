#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preço = float(input('qual o preço do produto? '))
desconto = (5*preço) / 100
print('seu preço com desconto fica R$:{}'.format(preço-desconto))

