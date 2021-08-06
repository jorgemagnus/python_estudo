import math

# Estudando o uso do f no string.

nome = 'Python Academy'
print(f'Qual o melhor blog sobre python {nome}!')

#-------------------------------------------------

ex_nome = 'Python Academy'
print(f"Qual o melhor blog sobre python {nome.upper() +'!' *3}")

#--------------------------------------------------

x = 0.5
print(f'cos({x}) = {math.cos(x)}')

#-------------------------------------------------
# Em dicionários:

dicionario =dict({'nome':'vinicius','ocupacao':'sofware engineer'})
print(f"Nome: {dicionario['nome']} é sua ocupação é:{dicionario['ocupacao']}")

#Em multilinhas:

site = 'Python Academy'
titulo = 'f-string no Python'
dificuldade = 'Básico'

print(
    f"Site :{site}\n"
    f"Título :{titulo}\n"
    f"Dificuldade :{dificuldade}\n"
)
