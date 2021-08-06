'''
Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''
lista = []

for x in range(1,4):
   num = int(input('informe um número: '))
   lista.append(num)
   lista.sort(reverse=True)

print(f'Números em ordem decrescente: {lista}')