'''
calculo do ipva.
fórmula: valor do carro x aliquota do seu estado  = resultado / 100 = valor do seu ipva.

'''


valorCarro = float(input('informe valor do carro:'))# valor do carro em Setembro/2021 Tabela fipe: 51.332,00
AliquotaUF = float(input('Aliquota do seu Estado:'))# aliquota do RN 3%

def calcularIPVA_2022(valorCarro,AliquotaUF):
    return (valorCarro * AliquotaUF)/100

MeuIpva = calcularIPVA_2022(valorCarro,AliquotaUF)

print(f'O valor do seu IPVA é : {MeuIpva}')
