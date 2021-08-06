# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

def fahrenheit_para_ceusios(temp_fah):
    return  5 * ((temp_fah - 32) /9)

temperatura = float(input('Informe temperatura em Fahrenheit: '))
print(f'A temperatura informada em Farenheit de {temperatura}\n'
      f' , corresponde a {fahrenheit_para_ceusios(temperatura)} em Ceusius.')

