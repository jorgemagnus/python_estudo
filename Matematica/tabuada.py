'''
Criando uma tabuada.
'''

numero = int(input('Informe número para gerar tabuada: '))

for x in range(0,11):
    print(f'{x} x {numero} = {x * numero}')