num = int(input('Informe um valor inteiro: '))
base = int(input("""Escolha uma das seguintes bases de conversão:
1 para binário
2 para octal
3 para hexadecimal
Informe a sua escolha: """))

if base == 1:
    bina = bin(num)
    print('O número {} convertido para binário será: {}'.format(num,bina))
elif base == 2:
    octa = oct(num)
    print('O número {} convertido para octal será: {}'.format(num, octa))
else:
    hexa = hex(num)
    print('O número {} convertido para octal será: {}'.format(num, hexa))