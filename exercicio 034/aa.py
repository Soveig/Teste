s = float(input("Digite o valor do Solário: "))
if s <= 1250:
    print("O valor do aumento foi de 15% e passou a receber {}".format(((s * 15)/100) + s))
else:
    print(" O valor de aumento foi de 10% e agora recebe {}".format(((s * 10)/100) + s))