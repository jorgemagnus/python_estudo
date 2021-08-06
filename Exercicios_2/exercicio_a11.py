'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo
o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5%
Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.

'''
def calcular_aumento(salario_inicial):
    if salario_inicial <= 280.00:
        return salario_inicial * 0.20
    elif salario_inicial > 280.00 and salario_inicial <= 700.00:
        return salario_inicial * 0.15
    elif salario_inicial > 700.00 and salario_inicial <= 1500.00:
        return salario_inicial * 0.10
    elif salario_inicial > 1500.00:
        return salario_inicial * 0.05


def informa_percentual(salario_inicial):
    if salario_inicial <= 280.00:
        return 0.20*100
    elif salario_inicial > 280.00 and salario_inicial <= 700.00:
        return 0.15*100
    elif salario_inicial > 700.00 and salario_inicial <= 1500.00:
        return 0.10*100
    elif salario_inicial > 1500.00:
        return 0.05*100


salario_atual = float(input('Informe Salário Atual do Colaborador: '))
percentual_aplicado = informa_percentual(salario_atual)
aumento_salario = calcular_aumento(salario_atual)

'''
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

print(f'Salário antes do reajuste R$: {salario_atual}\n'
      f'Percentual de aumento aplicado: {percentual_aplicado}%\n'
      f'Valor do aumento: R$ {aumento_salario}\n'
      f'Novo salário é R$ : {salario_atual + aumento_salario}')


