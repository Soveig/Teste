#faça um programa que leia um ângulo e diga o valor em radianos de cosseno, seno e tangente
import math
Ang = float(input('digite um ângulo: '))
cos = math.cos(math.radians(Ang))
sen = math.sin(math.radians(Ang))
tan = math.tan(math.radians(Ang))
print('o cosseno de {} é {:.2f}'.format(Ang,cos))
print('o seno de {} é {:.2f}'.format(Ang, sen))
print('a tangente de {} é {:.2f}'.format(Ang, tan))