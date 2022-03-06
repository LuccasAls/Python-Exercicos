from random import choice
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do primeiro aluno: '))
a3 = str(input('Digite o nome do primeiro aluno: '))
a4 = str(input('Digite o nome do primeiro aluno: '))
lista = [a1, a2, a3, a4]
sorteado = choice(lista)
print('O aluno sorteado foi {}'.format(sorteado))
