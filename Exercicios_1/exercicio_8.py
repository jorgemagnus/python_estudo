# Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês

def calcular_salario(v_por_hora,t_hora_mes):
    return v_por_hora*t_hora_mes

por_hora = float(input('Informe quanto você ganha por hora: '))
num_hora_mes = float(input('Informe número de horas trabalhadas no mês: '))

input(f'Meu salário do mês é $ {calcular_salario(por_hora,num_hora_mes)} Reais')

