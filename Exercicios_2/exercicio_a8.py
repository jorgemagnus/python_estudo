'''
Faça um programa que pergunte o preço de três produtos e informe qual produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''

produto_a = float(input('Informe o preço da unidade da Panela de Pressão: '))
produto_b = float(input('Informe o preço da unidade da máquina de lavar louças: '))
produto_c = float(input('Informe o preço da unidade do conjunto de facas: '))


if produto_a < produto_b and produto_a < produto_c:
   print(f'Você deve comprar a Penela de Pressão por $: {produto_a}')
elif produto_b < produto_a and produto_b < produto_c:
   print(f'Você deve comprar a Máquina de lavar louça por $: {produto_b}')
elif produto_c < produto_b and produto_c < produto_a:
   print(f'Você deve comprar o Conjunto de facas por $: {produto_c}')

