#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input('Informe um número, seja ele positivo ou negativo: '))

if num < 0:
    print(f'O número informado é negativo: {num}')
else:
    print(f'O número informado é positivo: {num}')