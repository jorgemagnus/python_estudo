'''

Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou
N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

'''
print('M - Matutino, V - Vespertino e N - Noturno.')
turno =  input('Informe o turno que você estuda: Digite M, V ou N ').upper()

if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite!.')
else:
    print('Valor inválido!.')
