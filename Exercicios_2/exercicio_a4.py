#Faça um Programa que verifique se uma letra digitada é vogal ou consoante

letra = input('Informe uma letra do alfabeto: ')

if letra in ['a','e','i','o','u']:
    print(f'letra {letra} é uma vogal.')
else:
    print(f'letra {letra} é uma consoante.')
