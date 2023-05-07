#crie um programa que leia o cateto oposto, cateto adjascente e calcule o comprimento da hipotenusa
import math
num1 = float(input('digite um número: '))
num2 = float(input('digite outro número: '))
hipotenusa = math.hypot(num1, num2)
print('o cateto oposto vale {}, o cateto adjascente {} e a hipotenusa {:.2f}'.format(num1, num2, hipotenusa))
