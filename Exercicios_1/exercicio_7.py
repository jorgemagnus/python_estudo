# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
def area_quadrado(lado):
    return lado*lado

lado_quadrado = float(input('Informe altura do quadrado em centimétros: '))
input(f'A área do quadrado é: {area_quadrado(lado_quadrado)} em centimetros.')
input(f'Porém para o usuário a área do quadrado é {area_quadrado(lado_quadrado)*2}')