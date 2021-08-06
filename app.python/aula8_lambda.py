# usando lambda 29/07/2021

contador_letras = lambda lista:[len(x) for x in lista]
soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
calculadora = {
    'soma':lambda a,b:a+b,
    'subtracao':lambda a,b:a-b,
    'multiplicacao':lambda a,b:a*b,
    'divisao':lambda a,b:a/b,
}

if  __name__ == '__main__':
    lista_animais = ['cachorro', 'gato', 'elefante']
    print(contador_letras(lista_animais))
    print(soma(5,10))
    print(subtracao(10,5))
    print(type(calculadora))
    soma_ = calculadora['soma']
    multiplicacao_ = calculadora['multiplicacao']
    print(f' O resultado da soma é: {soma_(10,5)}')
    print(f' O resultado da multiplicação é: {multiplicacao_(10,2)}')