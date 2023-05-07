preço = float(input('Qual o preço do produto: R$'))
pagamento = int(input('''Qual a forma de pagamento:
[ 1 ] A vísta dinheiro/cheque: 10% de desconto
[ 2 ] A vísta no cartão: 5% de desconto
[ 3 ] Em até 2x no cartão: preço formal
[ 4 ] 3x ou mais no cartão: 20% de juros
Digite o número da opção: '''))
if pagamento == 1:
    desconto = (10 * preço) / 100
    print('O preço ficou em R$: {}'.format(preço - desconto))
elif pagamento == 2:
    desconto = (5 * preço) / 100
    print('O preço ficou em R$: {}'.format(preço - desconto))
elif pagamento == 3:
    parcela = preço / 2
    print('O preço ficou em 2 parcelas de R$: {:.2f}'.format(parcela))
elif pagamento == 4:
    parcela = int(input('Quantas parcelas vão ser? '))
    juros = preço + (preço * 20 / 100)
    valor = juros / parcela
    print('Parcelado em {}x, seu produto ficou {}'.format(parcela, valor))
    print('O preço final com 20% de juros ao todo foi de R$:{}'.format(juros) )
else:
    print('OPÇÂO INVALIDA')