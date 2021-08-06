'''calculo de folha'''
import math


def hora_extra_50(salario_base,qtdHoraExtras):
    hora_normal = salario_base/220.00
    hora_extra = hora_normal*1.5
    valor_hora = qtdHoraExtras*hora_extra
    return  round(valor_hora,2)


salario_mes= float(input('Informe salário do Mês:'))
horasExtra = float(input('Informe total de horas extras:'))

print(f'total de horas extras é {hora_extra_50(salario_mes,horasExtra)}')