# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a>c:
#     print('O maior número é: {}'.format(a))
#     print('Os menores números são: {b} e {c}'.format(b=b,c=c))
# elif b > a and b > c:
#     print('O maior número é: {}'.format(b))
#     print('Os menores números são: {a} e {c}'.format(a=a, c=c))
# else:
#     print('O maior número é: {}'.format(c))
#     print('Os menores números são: {a} e {b}'.format(a=a, b=b))
# print('Final do programa')

# a = int(input('Digite o primeiro valor: '))
# b = int(input('Digite o segundo valor: '))
# resto_a = a%2
# resto_b = b%2
#
# if resto_a==0:
#     print('O número {}'.format(a),'é par')
# if resto_b==0:
#     print('O número {}'.format(b),'é par')
# else:
#     print('Os números {}'.format(a),'são ímpares')

nota1 = int(input('Informe a nota do primeiro bimestre: '))
if nota1 > 10:
    nota1 = int(
        input('Você digitou um valor incorreto, por favor revisar! informe a nota correta do primeiro bimestre: '))
nota2 = int(input('Informe a nota do segundo bimestre: '))
if nota2 > 10:
    nota2 = int(
        input('Você digitou um valor incorreto, por favor revisar! informe a nota correta do segundo bimestre: '))
nota3 = int(input('Informe a nota do terceiro bimestre: '))
if nota3 > 10:
    nota3 = int(
        input('Você digitou um valor incorreto, por favor revisar! informe a nota correta do terceiro bimestre: '))
nota4 = int(input('Informe a nota do quarto bimestre: '))
if nota4 > 10:
    nota4 = int(
        input('Você digitou um valor incorreto, por favor revisar! informe a nota correta do quarto bimestre: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print('A média é: {}'.format(media))
# if nota1 <= 10 and nota2 <= 10 and nota3 <= 10 and nota4 <= 10:
#     print('A média do aluno é: {}'.format(media))
# else:
#     print('Alguma nota foi informada incorretamente! Por favor revisar os valores inseridos')
