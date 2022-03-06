import random
num = random.randint(0, 5)
dig = int(input('Digite um numero de 0 á 5, e tente a sorte: '))
print('O número sorteado foi {}, o numero digitado foi {}'.format(num, dig))
if num == dig:
    print('Você Ganhou, Parabéns!!!')
else:
    print('Você Perdeu, Tente Novamente!!')
