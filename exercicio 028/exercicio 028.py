import random
from time import sleep

num = random.randint(0,5)
question = int(input('qual número eu estou pensando? '))
print('-'* 20)
print('VERIFICANDO...')
print('-' * 20)
sleep(2)
if question == num:
    print('Parabéns você ganhou')
    print('eu realmente pensei no número {}'.format(num))
else:
    print('você perdeu, eu pensei no número {}'.format(num))
