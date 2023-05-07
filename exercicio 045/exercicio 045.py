import random
escolha = int(input('''
[ 1 ]Pedra
[ 2 ]Papel 
[ 3 ]Tesoura
Escolha um número: '''))
computador = random.choice(['Pedra', 'Papel', 'Tesoura'])
if escolha == 1 and computador == 'Tesoura':
    print('Você ganhou, minha escolha foi {}'.format(computador))
elif escolha == 1 and computador == 'Papel':
    print('Você perdeu, minha escolha foi {}'.format(computador))
elif escolha == 2 and computador == 'Pedra':
    print('Você ganhou, minha escolha foi {}'.format(computador))
elif escolha == 2 and computador == 'Tesoura':
    print('Eu ganhei, minha escolha foi {}'.format(computador))
elif escolha == 3 and computador == 'Pedra':
    print('Eu ganhei, minha escolha foi {}'.format(computador))
elif escolha == 3 and computador == 'Papel':
    print('Você ganhou, minha escolha foi escolhi {}'.format(computador))
else:
    print('Empatamos, pois eu escolhi {}'.format(computador))