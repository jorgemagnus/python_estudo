'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa
deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez
'''

nota1 = float(input('Informe primeira nota: '))
nota2 = float(input('Informe segunda nota: '))

media = (nota1 + nota2) /2

if media == 10:
    print(f'Nossa!! com essa média {media}, você está APROVADO COM DISTINÇÃO!.')
elif media >= 7:
    print(f'Parabéns, sua média foi {media}, você está APROVADO!.')
elif media < 7:
    print(f'Desculpe, mas com essa média {media}, você está REPROVADO!.')

