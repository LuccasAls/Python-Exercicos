ano = int(input('Qual o ano do seu nascimento: '))
atual = int(input('Qual o ano Atual: '))
idade = atual - ano
if idade <= 9:
    print('Sua categoria é MARIM')
elif (idade > 9) and (idade <= 14):
    print('Sua categoria é  INFANTIL')
elif (idade > 14) and (idade <= 19):
    print('Sua categoria é JUNIOR')
elif (idade == 20):
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')
