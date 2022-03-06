ano = int(input('Digite o ano que você nasceu: '))
atual = int(input('Digite o ano atual: '))
idade = atual - ano
if idade > 18:
    idade = idade - 18
    print('Já passou da hora do seu alistamento, está {} anos atrazados'.format(idade))
elif idade == 18:
    print('Está na hora de você fazer seu alistamento')
else:
    idade = 18 - idade
    print('Ainda falta {} anos para seu alistamento'.format(idade))
