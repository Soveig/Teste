frase = "curso em video python"
#esse comando vai mostrar quantas letras contando com os espaços tem na frase
print(len(frase))
#aqui ele vai mostrar quantas vezes existe a letra 'o' na frase
print(frase.count('o'))
#aqui ele vai contar quantas letras 'o' existem da posição 0 até a 12
print(frase.count('o', 0, 13))
#aqui ele vai me dizer em que posição começa o 'deo' na string
print(frase.find('deo'))
#aqui ele vai me dizer se existe a palavra 'curso' na string
print('curso' in frase )
