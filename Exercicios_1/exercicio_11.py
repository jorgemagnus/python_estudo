'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''

num1 = int(input('Informe Primeiro Número INTEIRO: '))
num2 = int(input('Informe Segundo Número INTEIRO: '))
num3 = float(input('Informe Terceiro Numéro, sendo esse REAL :'))

print(f'O produto do dobro do primeiro com a metade do segundo é: {(num1*2)*2 + (num2/2)}')
print(f'A soma do triplo do primeiro com o tercerio é {(num1*3)+num3}')
print(f'O terceiro elevado ao cubo é: {num3**3}')