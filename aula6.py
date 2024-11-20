# conjunto = {1, 2, 3, 4, 4, 2}
# conjunto.add(5)
# conjunto.discard(2)
# print(type(conjunto))
# print(conjunto)

conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print('União entre os dois conjuntos: {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção entre os dois conjuntos: {}'.format(conjunto_interseccao))
conjunto_diferenca = conjunto.difference(conjunto2)
print('Diferença do conjunto 1 e 2: {}'.format(conjunto_diferenca))
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença do conjunto 2 e 1: {}'.format(conjunto_diferenca2))

conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simetrica: {}'.format(conjunto_dif_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)
