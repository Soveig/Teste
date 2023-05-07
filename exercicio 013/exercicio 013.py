#faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salário = float(input('Informe o salário: '))
acréscimo = (15*salário) / 100
print('seu salário ficará {:.2f} com 15% de aumento'.format(salário+acréscimo))