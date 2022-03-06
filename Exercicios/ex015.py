km = float(input('Qual a quantidade de kilometros percoridos: '))
dia = int(input('Qual a quantidade de dais percoridos: '))
pagar = (dia*60)+(km*0.15)
print('O total que irá ter que pagar é R${:.2f}'.format(pagar))