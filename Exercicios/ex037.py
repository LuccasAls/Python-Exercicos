num = int(input('Digite um número: '))
print(''''\033[1;31;15m Escolha a base de conversão \033[m
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
a = int(input('Sua Opção é: '))
if a == 1:
    print('O número {} em Binário é {}'.format(num, bin(num)[2:]))
elif a == 2:
    print('O número {} em Octal é {} '.format(num, oct(num)[2:]))
elif a == 3:
    print('O número {} em Hexadecinal {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválido, Tente novamente!')
