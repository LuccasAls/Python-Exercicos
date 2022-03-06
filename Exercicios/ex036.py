print('{}==================================== {}'.format('\033[1;33m', '\033[m'))
print('         \033[1;34mAnálise de emprétimo!\033[m')
print('{}==================================== {}'.format('\033[1;33m', '\033[m'))
casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Qunato anos você deseja pagar: '))
total = casa / (anos*12)
print('O valor do imovél é R${:.2F}, e sua prestação em {} anos tera a presstação de R${:.2f}'.format(casa, anos, total))
if total <= salario*0.30:
    print('O Empréstimo será APROVADO!')
else:
    print('O Empréstimo será REPROVADO!')
