#Faça um Programa que leia três números e mostre o maior deles.

num1 = float(input('Informe primeiro número: '))
num2 = float(input('Informe segundo número: '))
num3 = float(input('Informe terceiro número: '))

if (num1 > num2) and (num1 > num3):
    print(f'O Primeiro número digitado é o maior: {num1}.')
elif (num2 > num3):
    print(f'O Segundo número digitado é o maior: {num2}.')
else:
    print(f'O terceiro número é o maior {num3}.')