a = float(input('Digite o valor do Lado 1 do triângulo: '))
b = float(input('Digite o valor do Lado 2 do triângulo: '))
c = float(input('Digite o valor do Lado 3 do triângulo: '))
if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print('O triângulo é Equilátero')
    elif (a == b) or (b == c) or (c == a):
        print('O triângulo é Isósceles')
    else:
        print('O triângulo é Escaleno')
else:
    print('Os lados não forma um triângulo')
