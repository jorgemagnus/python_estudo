'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
'''
def dia_semana(dia):
    if dia == 1:
      return 'Domingo'
    elif dia == 2:
      return 'Segunda - Feira'
    elif dia == 3:
      return 'Terça - Feira'
    elif dia == 4:
      return 'Quarta - Feira'
    elif dia == 5:
        return 'Quinta - Feira'
    elif dia == 6:
        return 'Sexta - Feira'
    elif dia == 7:
        return 'Sábado'
    else:
        return 'Inválido'


dia_informado = int(input('Informe o dia da Semana: '))
print(f'O dia da semana informado é {dia_semana(dia_informado)}')