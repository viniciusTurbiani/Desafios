a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print('Soma: ', soma)
print('Subtração: ', subtracao)
print('Multiplicação: ', multiplicacao)
print('Divisão: ', divisao)
print('Resto da divisão: ', resto)
print('Soma: ' + str(soma))
print('Subtração: ' + str(subtracao))
print('Multiplicação: ' + str(multiplicacao))
print('Divisão: ' + str(divisao))
print('Resto da divisão: ' + str(resto))
soma = str(soma)
subtracao = str(subtracao)
multiplicacao = str(multiplicacao)
divisao = str(divisao)
resto = str(resto)
print('Soma: ' + soma)
print('Subtração: ' + subtracao)
print('Multiplicação: ' + multiplicacao)
print('Divisão: ' + divisao)
print('Resto da divisão: ' + resto)

print('Soma: {}'.format(soma))
print('Subtração: {}'.format(subtracao))
print('Multiplicação: {}'.format(multiplicacao))
print('Divisão: {}'.format(divisao))
print('Resto da divisão: {}'.format(resto))

print('Soma: {a}. \nsubtracao: {b}. \nmultiplicacao: {c}. \ndivisao: {d}. \nresto: {e}'.format(a=soma, b=subtracao,
                                                                                               c=multiplicacao,
                                                                                               d=divisao,
                                                                                               e=resto))  # a ordem nesse caso não importa pois derá definido pelo apelido
