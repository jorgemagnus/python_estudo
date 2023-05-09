nome = input('Qual é o seu nome: ')
idade = input('Qual a sua idade: ')
idade = str(idade)
cidade = input('Onde você mora? ')

print('O ' + nome + ' tem ' + str(idade) + ' anos de idade e mora em '+ cidade + '.')
#ou
print('O ' + nome + ' tem ' + idade + ' anos de idade e mora em '+ cidade + '.')
#ou
print(f'O {nome} tem {idade} anos de idade e mora em {cidade}.')