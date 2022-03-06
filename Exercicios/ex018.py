import math
ang = float(input('Digite o valor do ângulo: '))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O valor do seno é {:.2f}'.format(sen))
print('O valor do cosseno é {:.2f}'.format(cos))
print('O valor da tangente é {:.2f}'.format(tan))
