'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a
quantidades de latas de tinta a serem compradas e o preço total.
'''

#variaveis
litro = 3  # 1 litro e que da para 3 metros quadrados.
lata = 18  # uma lata de tinta que tem 18 litros.
lata_area = 54
lata_preco = 80

def quantidade_lata_pintar(area):
    litros_necessarios = area / 3
    if litros_necessarios == 18:
        return 1
    elif litros_necessarios > 18:
        qtd_latas = litros_necessarios /18
        return qtd_latas
    elif litros_necessarios < 18:
        return 1

area = float(input('Informe em metros quadrados a aéra a ser pintada: '))
qtd_lata_pintar = quantidade_lata_pintar(area)
valor_pagar = qtd_lata_pintar * lata_preco

print(f'A área que você quer pintar é de {area} metros quadrados.')
print(f'uma lata da para pintar {lata_area} metros quadrados.')
print(f'O preço da lata é $ {lata_preco} Reais.')
print(f'A quantidade de latas para pintar é {round(quantidade_lata_pintar(area))}\n'
      f'e o valor a pagar é: $ {round(valor_pagar)} Reais.')
