# aula 04 - 22/07/2021

# Usando o while
# a = 0
# while a <= 10:
#     print(a)
#     a+=1

# código da aula3 corrigido.
a = int(input('Entre com nota do primeiro bimestre: '))
while a > 10 or a < 0:
     a = int(input('Você digitou um valor errado, digite o valor correto para o primeiro bimestre: '))
b = int(input('Entre com nota do segundo bimestre: '))
while b > 10 or b < 0:
     b = int(input('Você digitou um valor errado, digite o valor correto para o segundo bimestre: '))
c = int(input('Entre com terceiro bimestre: '))
while c > 10 or c < 0:
     c = int(input('Você digitou um valor errado, digite o valor correto para o terceiro bimestre: '))
d = int(input('Entre com quarto bimestre: '))
while d > 10 or d < 0:
     d = int(input('Você digitou um valor errado, digite o valor correto para o quarto bimestre: '))
media = (a+b+c+d)/4
print(f'Média do Aluno é: {media}')
#outra forma é:
print('Média do aluno é: {}'.format(media))




# usando o for:
for a in range(11):
    print(a)

# Todos os números primos informado pelo usuário
# a = int(input('Informe o número:'))
#
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)