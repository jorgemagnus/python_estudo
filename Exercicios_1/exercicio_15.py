'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
'''


def calcular_salario(v_por_hora,t_hora_mes):
    return v_por_hora*t_hora_mes

def calcular_ir(salario_b):
    return salario_b * 0.11

def calcular_inss(salario_b):12
    return salario_b * 0.08

def calcular_sindicato(salario_b):
    return salario_b * 0.05

def calcular_salario_liquido(sal_bruto,ir,inss,sindicato):
    return  sal_bruto - (ir + inss + sindicato)


por_hora = float(input('Informe quanto você ganha por hora: '))
num_hora_mes = float(input('Informe número de horas trabalhadas no mês: '))

# Variáveis para receber os calculos das funções:
salario_bruto = calcular_salario(por_hora,num_hora_mes)
imposto_renda = calcular_ir(salario_bruto)
imposto_inss  = calcular_inss(salario_bruto)
imposto_sindicato = calcular_sindicato(salario_bruto)
salario_liquido = calcular_salario_liquido(salario_bruto,imposto_renda,imposto_inss,imposto_sindicato)

#Visualizar resultados:
input(f'Meu salário bruto é $ {salario_bruto} Reais\n'
      f'Imposto de renda: ${imposto_renda} Reais\n'
      f'Inss: ${imposto_inss} Reais\n'
      f'Sindicato: ${imposto_sindicato} Reais\n'
      f'Salário Liquido a Receber: ${salario_liquido} Reais.')
