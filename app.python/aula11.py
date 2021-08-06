#aula 11 - (Tratamento de erros) - 02/08/2021

lista = [1,10]
try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritimética.')
except IndexError:
    print('Erro ao acessar um índice inválido da lista!')
except Exception as ex:
    print(f'Erro desconhecido. Erro: {ex}')
else:
    print('Executa quando não ocorre exceção!.')
finally:
    print('Sempre executa o código no finally')
    print('fechando arquivo!')
    arquivo.close()
