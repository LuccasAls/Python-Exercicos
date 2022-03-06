n1 = float(input('Digite o Número 1: '))
n2 = float(input('Digite o Número 2: '))
n3 = float(input('Digite o Número 3: '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O número maior entre eles é {}'.format(maior))
print('O número menor entre eles é {}'.format(menor))
