from math import tan, sin, cos, radians
valor = float(input('Informe um valor: '))
seno = sin(radians(valor))
cosseno = cos(radians(valor))
tangente = tan(radians(valor))
print('O seno é: {:.2f}\no cosseno é: {:.2f}\na tangente é: {:.2f}'.format(seno,cosseno,tangente))
