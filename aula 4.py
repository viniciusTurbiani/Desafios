# a = int(input('Informe um número: '))
# b = 0
# for x in range(1,a+1):
#     resto = a % x
#     if resto == 0:
#         print('O número {}'.format(a),'é divisivel por: {}'.format(x))
#         b = b+1
# if b == 2:
#     print('O número {}'.format(a),'é primo')
# else:
#     print('O número {}'.format(a), 'não é primo')
####################################################
# a = int(input('Informe um valor: '))
# for i in range(a+1):
#     b = 0
#     for x in range(1,i+1):
#         resto = i % x
#         if resto == 0:
#             b = b+1
#     if b == 2:
#         print('O número {}'.format(i),'é primo')
#     else:
#         print('O número {}'.format(i), 'não é primo')

# nota = int(input('Informe a nota do primeiro bimestre: '))
# while nota > 10:
#     nota = int(input('Nota infromada incorretamente! Por gentileza informar nota correta do primeiro bimestre: '))
# # a = 0
# while a <= 10:
#     print(a)
#     a=a+1

# nota1 = int(input('Informe a nota do primeiro bimestre: '))
# while nota1 > 10:
#     nota1 = int(input('Você digitou um valor incorreto, por favor revisar! informe a nota correta do primeiro bimestre: '))
# nota2 = int(input('Informe a nota do segundo bimestre: '))
# while nota2 > 10:
#     nota2 = int(input('Você digitou um valor incorreto, por favor revisar! informe a nota correta do segundo bimestre: '))
# nota3 = int(input('Informe a nota do terceiro bimestre: '))
# while nota3 > 10:
#     nota3 = int(input('Você digitou um valor incorreto, por favor revisar! informe a nota correta do terceiro bimestre: '))
# nota4 = int(input('Informe a nota do quarto bimestre: '))
# while nota4 > 10:
#     nota4 = int(input('Você digitou um valor incorreto, por favor revisar! informe a nota correta do quarto bimestre: '))
# media = (nota1+nota2+nota3+nota4)/4
# print('A média é: {}'.format(media))


b = 0
while b != 2:
    print(b)
    a = int(input('Informe um número primo: '))
    for x in range(1, a + 1):
        resto = a % x
        if resto == 0:
            b = b + 1
if b == 2:
    print('O número {}'.format(a), 'é primo')
else:
    print('O número {}'.format(a), 'não é primo')
