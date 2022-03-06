km = float(input('Qual a quantidade de Kiometros que você atingiu km/h: '))
if km > 80:
    print('Você Ultrapassaou 80.0km/h irá pagar R${:.2f} de multa'.format((km-80)*7))
else:
    print('Você não ultrapassou limite, Parabéns  não irá pagar multa')

