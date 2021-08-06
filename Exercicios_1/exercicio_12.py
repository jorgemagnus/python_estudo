'''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58'''

def calcular_peso_ideal(altura):
    return (72.7 * altura) - 58

pessoa_altura = float(input('Informe sua Altura :'))
print(f'Seu peso ideal é: {calcular_peso_ideal(pessoa_altura)}')