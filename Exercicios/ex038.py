n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O número {} e maior que o número {}'.format(n1, n2))
elif n2 > n1:
    print('O número {} e maior que o número {}'.format(n2, n1))
else:
    print('o número {} e {} são iguais'.format(n2, n1))
