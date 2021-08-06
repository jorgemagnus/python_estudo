# aula 03 - 21/07/2021
a = int(input('Entre com nota do primeiro bimestre: '))
if a > 10 or a < 0:
     a = int(input('Você digitou um valor errado, digite o valor correto para o primeiro bimestre: '))
b = int(input('Entre com nota do segundo bimestre: '))
if b > 10 or b < 0:
     b = int(input('Você digitou um valor errado, digite o valor correto para o segundo bimestre: '))
c = int(input('Entre com terceiro bimestre: '))
if c > 10 or c < 0:
     c = int(input('Você digitou um valor errado, digite o valor correto para o terceiro bimestre: '))
d = int(input('Entre com quarto bimestre: '))
if d > 10 or d < 0:
     d = int(input('Você digitou um valor errado, digite o valor correto para o quarto bimestre: '))
media = (a+b+c+d)/4
print(f'Média do Aluno é: {media}')
#outra forma é:
print('Média do aluno é: {}'.format(media))


# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#      print(f'Média do Aluno é: {media}')
#      #outra forma é:
#      print('Média do aluno é: {}'.format(media))
# else:
#      print('Foi informado alguma nota errada.')



# a = int(input('Entre com primeiro valor'))
# b = int(input('Entre com segundo valor'))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or not resto_b > 0:
#      print('foi digitado um número par!')
# else:
#      print('não foi digitado nem um número par!')



# a = int(input('Entre com um valor'))
# # resto = a % 2
# # if resto == 0:
# #     print('O número informado {} é Par, o resto é {}'.format(a,resto))
# # else:
# #     print('O número informado {} é Impar, o resto é {}'.format(a,resto))


# a = int(input('Informe o primeiro valor:'))
# b = int(input('informe o segundo valor:'))
# c = int(input('Informe o terceiro valor:'))
#
# if a > b and a > c:
#      print('O maior número é {}'.format(a))
#
# elif b > a and b > c:
#     print('O maior número é {}'.format(b))
# else:
#    print(f'O maior número é {c}')
#
#print("Final do Programa!.")