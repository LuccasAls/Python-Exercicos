n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2)/2
if media < 5:
    print('O aluno foi reprovado com a média{:.2f}'.format(media))
elif (media >= 5) and (media < 7):
    print('O aluno está  em recuperação {:.2f}'.format(media))
else:
    print('O aluno foi aprovado com a média {:.2f}'.format(media))
