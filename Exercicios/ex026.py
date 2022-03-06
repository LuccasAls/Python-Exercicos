nome = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {}'.format(nome.count('A')))
print('A letra "A" apareceu na {}º colocação'.format(nome.find('A')+1))
print('A letra "A" apareceu pela última vez na {}º colocação'.format(nome.rfind('A')+1))
