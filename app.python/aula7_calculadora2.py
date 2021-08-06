# aula7 (calculadora parte 2) - Data 26/07/2021
# métodos , funções e classes

class Calculadora:

    def soma(self,valor_a,valor_b):
        return valor_a + valor_b

    def subtracao(self,valor_a,valor_b):
        return valor_a - valor_b

    def multiplicacao(self,valor_a,valor_b):
        return  valor_a * valor_b

    def divisao(self,valor_a,valor_b):
        return valor_a / valor_b


#instância a classe:
if  __name__ == '__main__':
    calculadora = Calculadora()
    print(f'soma: {calculadora.soma(10,2)}')
    print(f'subtração: {calculadora.subtracao(10,2)}')
    print(f'multiplicação: {calculadora.multiplicacao(10,2)}')
    print(f'divisão: {calculadora.divisao(100,2)}')