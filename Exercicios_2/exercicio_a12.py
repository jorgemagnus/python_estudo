'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11%
do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário
Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme
o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''
pago_hora_valor = float(input('Valor pago por hora ao Colaborador: '))
hora_trabalha_mes = float(input('Informe o total de horas Trabalhadas no Mês: '))

salario_bruto = (pago_hora_valor * hora_trabalha_mes)
ir_valor = (salario_bruto * 0.05)
inss_valor = (salario_bruto * 0.10)
fgts_valor = (salario_bruto * 0.11)
total_desconto = (ir_valor + inss_valor)
salario_liquido = (salario_bruto - total_desconto)

print(f'Sálario bruto: ({pago_hora_valor} * {hora_trabalha_mes}) : R$ {salario_bruto}\n'
      f'(-) IR (5%)                  : R$ {ir_valor}\n'
      f'(-) INSS (11%)               : R$ {inss_valor}\n'
      f'FGTS (11%)                   : R$ {fgts_valor}\n'
      f'Total de Descontos           : R$ {total_desconto}\n'
      f'Salário líquido              : R$ {salario_liquido}')

