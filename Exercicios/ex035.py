print('-='*20)
print('Analisador de triângulo')
print('-='*20)
a = float(input('Qual o valor das reta 1: '))
b = float(input('Qual o valor da reta 2: '))
c = float(input('Qual o valor da reta 3: '))
# if a < b + c and b < a + c and c < a + b
if (b-c) <a  < (b + c):
    if (a- c) <b < (a + c):
        if (a - b) <c < (a +b):
            print('O triângulo é Verdadeiro!')
        else:
            print('O triângulo é Falso!')