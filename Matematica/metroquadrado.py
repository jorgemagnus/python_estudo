'''
 Calculando o metro quadrado.
 formula: m = comprimento * largura
'''

largura = float(input('Informe a largura:'))
comprimento = float(input('Informe o comprimento:'))

def calcularMetroQuadrado(x,y):
    return (x * y)


m = calcularMetroQuadrado(largura,comprimento)

print(f'O valor em metros quadrados é: {m}')