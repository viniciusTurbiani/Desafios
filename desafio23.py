num = int(input('Informe um número entre 0 e 9999: '))
while num > 9999 or num < 0:
    num = int(input('Número inválido! Informe um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))