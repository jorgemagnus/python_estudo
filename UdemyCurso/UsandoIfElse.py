#Aula 24 - Controle de fluxo

velocidade = int(input("Informe sua velocidade: "))

if velocidade > 110:
    print('Acima da Velocidade Permitida.')
    print('Favor Reduzir a sua velociade.')
elif velocidade < 60:
    print('Favor dirigir acima de 80km/h')
else:
    print('Velocidade ok')