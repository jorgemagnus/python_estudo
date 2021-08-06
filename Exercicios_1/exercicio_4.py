# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def calcular_media(n1,n2,n3,n4):
    return (n1+n2+n2+n4)/4

nota1 = float(input('Informe Primeira nota: '))
nota2 = float(input('Informe Segunda nota: '))
nota3 = float(input('Informe Terceira nota: '))
nota4 = float(input('Informe Quarta nota: '))

print(f'A média das notas é: {calcular_media(nota1,nota2,nota3,nota4)}')