# aula 2 - 21/07/2021

a = int(input('Entre com o primeiro valor:'))
b = int(input('Entre com o segundo valor :'))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
#Forma 1
resultado = ('Soma:{soma}'
      '\nSubtração:{subtracao}'
      '\nMultiplicação:{multiplicacao}'
      '\nDivisão:{divisao}'
      '\nResto:{resto}'.format(soma = soma,
                             subtracao=subtracao,
                             multiplicacao=multiplicacao,
                             divisao=divisao,
                             resto=resto))
print(resultado)

print('\n-----------------------------------\n')

#Forma 2
print(f'Soma:{soma}'
      f'\nSubtração:{subtracao}'
      f'\nMultiplicação:{multiplicacao}'
      f'\nDivisão:{divisao}'
      f'\nResto:{resto}')

print('\n-----------------------------------\n')
#outros exemplos:

x = '1'
soma = int(x)+5
print(f'total da soma : {soma}')