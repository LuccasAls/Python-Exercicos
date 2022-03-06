import random
lista = ('Tesoura', 'Pedra', 'Papel')
print('=-'*20)
print('\033[1;33m                Jokenpô \033[m')
print('=-'*20)
print('Escolha o sua opção!!\n'
      '[ 0 ] Tesoura\n'
      '[ 1 ] Pedra\n'
      '[ 2 ] Pepel')
a = int(input('Escolha: '))
sorte = random.randint(0, 2)
if a == 0 or a == 1 or a == 2:
    print('O computador escolheu {}'.format(lista[sorte]))
    print('O jogador escolheu {}'.format(lista[a]))
    if a == sorte:
        print('       EMPATE')
    elif (a == 0 and sorte == 2) or (a == 1 and sorte == 0) or (a == 2 and sorte == 12):
        print('      JOGADOR VENCEU!')
    else:
        print('     JOGADOR PERDEU!')
else:
    print('Opção não encontrada!')
