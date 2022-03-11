'''
calculo do combustível - vantagem ou não usar etanol.
'''
from multiprocessing.managers import Value

valorgasolina = float(input("Valor da Gasolina:"))
valoretanol = float(input("Valor do Etanol:"))

def valorCombustivel(VGasolina):
    return VGasolina * 0.7

if valorCombustivel(valorgasolina) < valoretanol:
    print(f'Melhor colocar Gasolina, pois o valor do etanol {valoretanol} não compensa.')
else:
    print(f'Melhor colocar Etanol.')