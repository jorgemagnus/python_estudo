'''
 Aula 19 - Utilizando Formatos string
'''

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
profissao = input('Digite sua profissão: ')

texto = f'     o {nome} {sobrenome} e um excelente [{profissao}]'

print(f'texto com tudo minusculo {texto.lower()}')
print(f'texto com tudo maiúsculo {texto.upper()}')
print(f'Coloca a primeira letra do texto em maiúsculo {texto.capitalize()}')
print(f'Localiza no texto a letra m {texto.find("m")}')
print(f'Localizar e trocar caractere {texto.replace("a", "c")}')
print(f'Localizar e trocar palavra {texto.replace("antunino", "grande mestre")}')
print(f'Removendo espaços {texto.strip()}')



'''
    Aula 20 - Metódos para strings.
'''


