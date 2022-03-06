valor = float(input('Digite o valor do Podruto: '))
print('''Qual sera a forma de pagamento?
[ 1 ] à vista dinheiro/cheque.
[ 2 ] à vista no cartão.
[ 3 ] 2 x no cartão.
[ 4 ] 3 x ou mais. ''')
a = str(input('Escolha sua opção: '))
if a == "1" or a == "2" or a == "3" or a == "4":
    if a == 1:
        total = valor * 0.9
        print('terá 10% de desconto R${:.2f}'.format(total))
    elif a == 2:
        total = valor * 0.95
        print('Terá 5% de desconto R${:.2f}'.format(total))
    elif a == 3:
        total = valor / 2
        print('O valor a saer pago em 2x é R${:.2f}'.format(total))
    else:
        parcela = int(input('Digite a quantidade de pacelas: '))
        total = valor * 1.20 / parcela
        print('O valor total ficará {:.2f} e dividido em {} x será {:.2f}'.format(total * parcela, parcela, total))
else:
    print('Opção não encontrada!')