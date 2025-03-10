# Aula 17 - Calculando a idade com o input

ano_nascimento = input('Informe o ano do seu nascimento no formato AAAA: ')
print(f'O tipo de dado informado no input é {type(ano_nascimento)}')
idade = 2025 - int(ano_nascimento)
print(f'O tipo de dado para idade é {type(idade)}')
print(f'Sua idade é {idade}')