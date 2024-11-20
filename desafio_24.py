cidade = str(input('Informe o nome da sua cidade: '))
cidade2 = cidade.upper()
lista = cidade2.split()
if lista[0] == 'SANTO':
    print('A cidade começa com SANTO')
else:
    print('A cidade não começa com SANTO')