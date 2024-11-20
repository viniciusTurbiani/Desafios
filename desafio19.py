# import random
# nome1 = str(input('Informe o primeiro nome: '))
# nome2 = str(input('Informe o segundo nome: '))
# nome3 = str(input('Informe o tereiro nome: '))
# nome4 = str(input('Informe o quarto nome: '))
# lista = [nome1,nome2,nome3,nome4]
# nome = random.choices(lista)
# print('O nome sorteado é: {}'.format(nome))

import random
nome1 = str(input('Informe o primeiro nome: '))
nome2 = str(input('Informe o segundo nome: '))
nome3 = str(input('Informe o tereiro nome: '))
nome4 = str(input('Informe o quarto nome: '))
lista = [nome1,nome2,nome3,nome4]
random.shuffle(lista)
print('A ordem é: {}'.format(lista))


