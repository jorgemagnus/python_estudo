'''
calculo do imc.
fórmula: altura / peso x peso.

'''


peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

def calcular_imc(peso, altura):
    return  peso/(altura * altura)

imc = round(calcular_imc(peso,altura),1)

if imc < 18.5:
     print(f'Seu imc = {imc} -> resultado -> Abaixo do Peso.')
elif imc >= 18.5 and imc <= 24.9:
     print(f'Seu imc = {imc} -> resultado -> Peso Normal.')
elif imc >= 25.0 and imc <= 29.9:
     print(f'Seu imc = {imc} -> resultado -> Sobrepeso.')
elif imc >= 30.0 and imc <= 34.9:
     print(f'Seu imc = {imc} -> resultado -> Obesidade Grau 1.')
elif imc >= 35.0 and imc <= 39.9:
     print(f'Seu imc = {imc} -> resultado -> Obesidade Grau 2.')
elif imc >= 40.0:
     print(f'Seu imc = {imc} -> resultado -> Obesidade Grau 3.')