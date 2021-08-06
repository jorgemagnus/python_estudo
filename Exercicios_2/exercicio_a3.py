#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Informe o sexo: (M ou F): ')

if sexo =='F':
    print('SEXO FEMININO')
elif sexo =='M':
    print('SEXO MASCULINO')
else:
    print('SEXO INVÁLIDO!')