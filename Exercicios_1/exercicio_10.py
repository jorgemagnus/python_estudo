# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

def celsius_para_farenheit(temp_celsius):
    return (1.8 * temp_celsius) + 32

temperatura = float(input('Informe a temperatura em Celsius: '))
print(f'Temperatura em Celsius informada {temperatura},\n'
      f'corresponde em Farenheit a {celsius_para_farenheit(temperatura)}.')