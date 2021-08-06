# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
def calcular_area_circulo(raio_):
    return 3.14 * (raio_ * raio_)

raio = float(input('Informe o raio do círculo: '))
print(f'A área do circulo é: {calcular_area_circulo(raio)}')


