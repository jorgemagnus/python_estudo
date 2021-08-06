# estudo de variáveis

nome = input('Entre com seu nome Completo:')
sexo = input('Informe seu Sexo: F ou M:')
idade = int(input('Informe sua idade:'))

if sexo == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'


if idade >= 60:
    covid = 'Risco de Covid'
else:
    covid = 'Risco baixo de Covid'


print(f'Meu nome é {nome} , meu sexo é {sexo} e minha idade é {idade} - {covid}.')