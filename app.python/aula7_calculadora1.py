# aula7 - calculadora parte 1) Data 26/07/2021
# métodos , funções e classes

class Calculadora:
    def __init__(self, num1,num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return  self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b


#instância a classe:
if  __name__ == '__main__':
    calculadora = Calculadora(10,2)
    print(f'soma: {calculadora.soma()}')
    print(f'subtração: {calculadora.subtracao()}')
    print(f'multiplicação: {calculadora.multiplicacao()}')
    print(f'divisão: {calculadora.divisao()}')