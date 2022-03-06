km = int(input('Qual a distância da viagem: '))
if km <= 200:
    total = km*0.50
    print('O valor da sua viagem é R$ {:.2f}'.format(total))
else:
    total1 = km*0.45
    print('O valor da sua viagem é R$ {:.2f}'.format(total1))