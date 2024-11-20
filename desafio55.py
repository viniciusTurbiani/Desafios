peso2 = 0
for count in range (0,5):
    peso = float(input('Informe o peso de uma pessoa: '))
    if peso2 < peso:
        peso2 = 0
        peso2 += peso
print('O maior peso informado é: {}'.format(peso2))
