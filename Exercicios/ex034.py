sal = float(input('Digite o valor do seu salário: '))
if sal >= 1250:
    novosal = sal*1.10
else:
    novosal = sal*1.15
print('seu novo sálario é {}'.format(novosal))
