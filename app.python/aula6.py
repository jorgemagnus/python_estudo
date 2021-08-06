# aula6 - conjuntos - 23/07/2021

conjunto = {1,2,3,4,5}
print(type(conjunto))
print(f'conjunto {conjunto}')

# conjuntos não aceita repetição:
conjunto_ = {1,2,3,4,4,2}
print('Os valores do conjunto são {1,2,3,4,4,2}')
print('conjunto não aceita repetiçaõ de valores: {}'.format(conjunto_))

conjunto2 = {5,6,7,8}
conjunto2.add(9)
print('conjunto2 {}'.format(conjunto2))

conjunto_uniao = conjunto.union(conjunto2)
print('União do conjunto e conjunto2 {}' .format(conjunto_uniao))

conjunto_diferenca = conjunto.difference(conjunto2)
print(f'Diferença do conjunto e conjunto2 {conjunto_diferenca}')

conjunto2_diferenca = conjunto2.difference(conjunto)
print('Diferença do conjunto2 e conjunto {}'.format(conjunto2_diferenca))

conjunto_interseccao = conjunto.intersection(conjunto2)
print(f'Intersecçao conjunto e conjunto2 {conjunto_interseccao}')

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print(f'Diferença simétrica : {conjunto_diff_simetrica}')

print('--------------------------')
conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}

conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B: {}'.format(conjunto_subset))

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {}'.format(conjunto_superset))

lista = ['cachorro','cachorro','gato','gato','elefante']
conjunto_animais = set(lista)
print(f'Lista antes de usar o comando set {lista}')
print(f'usando set(lista) para tirar as repetições e transformando em um conjunto {conjunto_animais}')
lista_animais = list(conjunto_animais)
print(f'Usando o comando list para transformar de conjunto para lista {lista_animais}')


conjunto_test = {1,2,2,1,4,5}
print(conjunto_test)
# print(type(conjunto))
# conjunto.add(5)
# print(f'sendo usado o o add(5) {conjunto}')
# conjunto.discard(2)
# print(f'sendo usado o discard(2) {conjunto}')
