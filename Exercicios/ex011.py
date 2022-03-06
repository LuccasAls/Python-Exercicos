largura = float(input("Qual a largura da parede: "))
altura = float(input("Qual a altura da parede: "))
area = largura * altura
print("Numa parede com {:.2f} de área serão necessário {:.2f} litrtos de tinta".format(area, area/2))