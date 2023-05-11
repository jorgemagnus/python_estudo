#Aula 25 - Operadores lógicos:

renda_acima_5mil = True
nome_limpo = True

# Usando o and
if renda_acima_5mil and nome_limpo:
    print('Financiamento Aprovado')
else:
    print('Financiamente Negado')

# Usando o or
if renda_acima_5mil or nome_limpo:
    print('Financiamento Aprovado')
else:
    print('Financiamente Negado')