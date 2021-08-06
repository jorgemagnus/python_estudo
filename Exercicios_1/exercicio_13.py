'''Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

def calcular_peso_ideal(altura,sexo):
    if sexo == 'M':
        return (72.7 * altura) - 58
    else:
        return (62.1 * altura) - 44.7

pessoa_altura = float(input('Informe sua Altura :'))
pessoa_sexo = input('Informe seu Sexo (F ou M): ')

print(f'Seu peso ideal é: {calcular_peso_ideal(pessoa_altura,pessoa_sexo)}')