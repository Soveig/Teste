#crie o programa que leia o nome de 4 alunos e mostre a ordem sorteada
import random
aluno1 = str(input('digite o nome do primeiro aluno: '))
aluno2 = str(input('digite o nome do segundo aluno: '))
aluno3 = str(input('digite o nome do terceiro aluno: '))
aluno4 = str(input('digite o nome do quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('a lista sorteada foi:di')
print(lista)