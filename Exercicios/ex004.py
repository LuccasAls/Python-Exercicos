a = input('Digite algo: ')
print('O seu tipo primitivo é', type(a))
print('Só tem espaço: ', a.isspace())
print('É alpha númerico: ', a.isalnum())
print('É númerico: ', a.isnumeric())
print('É alfabético: ', a.isalpha())
print('Está escrito em Maiúsculo', a.isupper())
print('Está escrito em Minúsculo', a.islower())
print('Está escrito capitaizada ', a.istitle())