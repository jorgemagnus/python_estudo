#Aula5 Data 22/07/2021 - tuplas, listas

#Atenção : na lista usamos o []
# na tupla usamos o ()

#lista é mutável ou seja pode mudar, retirar...valores.
lista = [1,3,5,7]
print(lista)
print(f'soma de uma lista com o sum(lista) {sum(lista)}')
print(f'Maior de uma lista com o max(lista) {max(lista)}')
print(f'menor de uma lista com o min(lista) {min(lista)}')

lista_animal = ['cachorro','gato','elefante']

#tupla é imutável, ou seja não pode ser modificada.
print('Imprimindo tupla')
tupla = (1,10,12,14)
print(tupla)
print(f'total de itens na tupla: {len(tupla)}')
print('Total de itens na lista:{}'.format(len(lista)))
print('Converte uma lista em tupla:')
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

print('-----------------------')

print('converte uma tupla em lista:')
lista_numerica = list(tupla)
lista_numerica[0]=100
print(type(lista_numerica))
print(lista_numerica)

print('--------------------')

print(lista_animal[1])

print('--------------------')

for x in lista_animal:
    print(x)

print('--------------------')

if 'gato' in lista_animal:
    print('Existe um gato na lista.')
else:
    print('não existe um gato na lista.')

print('--------------------')

nova_lista = lista_animal * 3
print(nova_lista)

print('--------------------')

nova_lista2 = lista * 2
print(nova_lista2)

print('--------------------')

if 'lobo' in lista_animal:
    print('Existe um lobo na lista.')
else:
    print('Não existe um lobo na lista, Será incluido.')
    lista_animal.append('lobo')
    print(lista_animal)

print('Usando o pop que elimina o último valor, mas pode também especificar a posição')
# lista_animal.pop()
# print(lista_animal)

print('usando o remove')
# lista_animal.remove('elefante')
# print(lista_animal)

print('Ordenando os valores com o Sort')
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)
lista_animal.reverse()
print(lista_animal)