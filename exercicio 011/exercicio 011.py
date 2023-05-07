#faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e s quantidade de tinta necessaria para pinta -lo
#sabendo que cada  litro pinta uma area de 2m²
largura = int(input('Largura: '))
altura = int(input('Altura: '))
área = largura * altura
litros = área/2
print('a área da parede é {}m²'.format(área))
print('será usado {} litros de tinta para pintar a parede'.format(litros))