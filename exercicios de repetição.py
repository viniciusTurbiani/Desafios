# nota = int(input('Informe a nota do aluno: '))
# while nota > 10 or nota < 0:
#     nota=int(input('Informe uma nota válida entre 0 e 10: '))

# usuario = str(input('Informe o usuário: '))
# senha = str(input('Informe a senha de acesso: '))
# while usuario == senha:
#     print('Erro! Usuário e senha não devem ser iguais!')
#     usuario = str(input('Informe o usuário: '))
#     senha = str(input('Informe a senha de acesso: '))
# print('Usuário e senha cadastrados com sucesso!')

# nome = str(input('Informe o nome: '))
# tamanhonome = len(nome)
# while tamanhonome <= 3:
#     tamanhonome = 0
#     nome = str(input('Informe um nome válido (com mais de 3 caracteres): '))
#     tamanhonome = len(nome)
# idade = int(input('Informe a idade (anos): '))
# while idade < 0 or idade > 150:
#     idade = int(input('Informe uma idade válida entre 0 e 150: '))
# salario = float(input('Informe o salário: '))
# while salario <= 0:
#     salario = float(input('Informe um salário válido maior que 0: '))
# sexo = str(input('Informe o sexo utilizando a letra inicial: '))
# while sexo != 'm' and sexo != 'M' and sexo != 'f' and sexo != 'F':
#     sexo = str(input('Informe o sexo utilizando a letra inicial utilize m para masculino e f para feminino: '))
# if sexo == 'm' or 'M':
#     sexo ='Masculino'
# else:
#     sexo='Feminino'
# estado = str(input('Informe o estado civil utilizando apenas a letra inicial: '))
# while estado != 's' and estado != 'c' and estado !='d' and estado != 'v' and estado != 'C' and estado !='S' and estado != 'V' and estado != 'D':
#     estado = str(input('Informe o estado civil utilizando apenas a letra inicial / S - SOLTEIRO / C - CASADO / D - DIVORCIADO / V - VIÚVO: '))
# if estado == 's' or estado == 'S':
#     estado = 'Solteiro'
# elif estado == 'd' or estado == 'D':
#     estado = 'Divorciado'
# elif estado == 'c' or estado == 'C':
#     estado = 'Casado'
# else:
#     estado = 'Viúvo'
# print('O nome é: {}'.format(nome))
# print('A idade é: {}'.format(idade))
# print('O salário é: {}'.format(salario))
# print('O sexo é: {}'.format(sexo))
# print('O estado civil é: {}'.format(estado))

# a = 10000
# b = 10147
# count = 0
# while a < b:
#     a = a+a*0.03
#     b = b+b*0.015
#     count = count + 1
# print('A quantidade de anos para a alcançar b é: {} anos'.format(count))
# print(a)
# print(b)

# fazer = 0
# count = 0
# while fazer == 0:
#     continuar = str(input('Você deseja fazer uma nova projeção (sim ou não)? '))
#     if continuar == 'não':
#         fazer = 1
#     else:
#         while continuar == 'sim':
#             a = int(input('Informe a população da primeira cidade: '))
#             b = int(input('Informe a população da segunda cidade: '))
#             c = float(input('Informe a taxa de crescimento da primeira cidade: '))
#             d = float(input('Informe a taxa de crescimento da segunda cidade: '))
#             while a != b:
#                 count = count + 1
#                 a = a + a * (c/100)
#                 b = b + b * (d/100)
#                 print('A quantidade de anos para as cidades terem a mesma população é de aproximadamente {} anos'.format(count))
#                 print('A população da primeira cidade será de {}'.format(a))
#                 print('A população da segunda cidade será de {}'.format(b))
#                 pergunta = str(input('Você deseja realiza uma nova projeção? sim ou não? '))


# count = 0
# soma = 0
# while count < 5:
#     num = int(input('Informe um valor: '))
#     count = count + 1
#     if num > soma:
#         soma = num
#     elif num <= soma:
#         soma = soma
# print('O maior número é: {}'.format(soma))
#

# count = 0
# soma = 0
# while count < 5:
#     num = int(input('Informe um valor: '))
#     count = count + 1
#     soma = soma + num
#     media = soma / 5
# print('A soma dos números é: {}'.format(soma),'a média dos números é: {}'.format(media))

# for x in range(1,51):
#     if x % 2 != 0:
#         print(x)

# fazer = 0
# while fazer == 0:
#     a = int(input('Informe o primeiro valor: '))
#     b = int(input('Informe o segundo valor: '))
#     if a > b:
#         for x in range(b+1,a):
#             print(x)
#             fazer = 1
#     elif b > a:
#         for x in range(a+1,b):
#             print(x)
#             fazer = 1
#     else:
#         print('Operação inválida os números são iguais!')

# fazer = 0
# soma = 0
# while fazer == 0:
#     a = int(input('Informe o primeiro valor: '))
#     b = int(input('Informe o segundo valor: '))
#     if a > b:
#         for x in range(b+1,a):
#             print(x)
#             fazer = 1
#             soma = soma + x
#     elif b > a:
#         for x in range(a+1,b):
#             print(x)
#             fazer = 1
#             soma = soma + x
#     else:
#         print('Operação inválida os números são iguais!')
# print('A soma dos numéros do intervalo é: {}'.format(soma))

# a = int(input('Informe o número que deseja saber a tabuada: '))
# multiplicador = 1
# while multiplicador <= 10:
#     resultado = a * multiplicador
#     print(a,' X ',multiplicador, ' = ', resultado)
#     multiplicador = multiplicador + 1

# count = 0
# par = 0
# impar = 0
# while count < 10:
#     a = int(input('Informe o primeiro valor: '))
#     if a % 2 == 0:
#         par = par + 1
#     else:
#         impar = impar + 1
#     count = count + 1
# print('A quantidade de números impares é: {}'.format(impar))
# print('A quantidade de números pares é: {}'.format(par))

for x in range(1, 1001):
    a = x + x - 1
    print(a)
