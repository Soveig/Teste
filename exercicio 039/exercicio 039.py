from datetime import date
ano = int(input('Qual o ano do seu nascimento? '))
atual = date.today().year
diferença = atual - ano
if diferença < 18:
    alistamento = ano + 18
    prazo = 18 - diferença
    print('Ainda não é tempo de você se alistar')
    print('Você se alistará daqui {} anos no ano de {}'.format(prazo, alistamento))
elif diferença == 18:
    print('Está na hora de se alistar!')
elif diferença > 18:
    prazo = diferença - 18
    alistamento = ano + 18
    print('Já passou do tempo de se alistar!')
    print('seu alistamento foi em {} e você está {} anos atrasado'.format(alistamento, prazo))
