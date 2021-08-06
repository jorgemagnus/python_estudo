'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o
rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que
o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa
de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a
quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.
'''
def multa_peixe(quantidade_peixe, limite, multa):
    if quantidade_peixe > limite:
        excesso = quantidade_peixe - limite
        return excesso * multa


peso = float(input('Informe a quantidade de peixe em quilos: '))
limite_maximo = 50.0
multa_passou = 4.0
if peso > limite_maximo:
   ultrapassou_limite = peso - limite_maximo
   print(f'Devido a ter Ultrapassado o limite de {limite_maximo} Kg dos Peixes,\n'
         f'Será cobrado multa de $ {multa_passou} Reais, sobre o execesso de {ultrapassou_limite} kg de Peixes,\n'
         f'O valor cobrado será de $ {multa_peixe(peso,limite_maximo,multa_passou)} Reais.')
else:
    print(f'Não vai ser necessário pagar multa pelos {peso} Kg de peixes informado.')