from math import pow, sqrt

cateto_o = float(input('Informe o comprimento do cateto oposto: '))
cateto_a = float(input('Informe o comprimento do cateto adjacente: '))
hipotenusa = sqrt(pow(cateto_o, 2) + pow(cateto_a, 2))
print('A hipotenusa é: {}'.format(hipotenusa))
