# programa simples de calculadora:

# Essa função soma dois números:
def add(x, y):
    return x + y


# Essa função subtrai dois números:
def subtract(x, y):
    return x - y


# Essa função multiplica dois números:
def multipliy(x, y):
    return x * y


# Essa função divide dois números:
def divide(x, y):
    return x / y


print("Selecione operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

while True:
    opcao = input("Entre com a opção(1/2/3/4): ")

    if opcao in ('1', '2', '3', '4'):
        num1 = float(input("Entre com o primeiro número:"))
        num2 = float(input("Entre com o segundo número: "))

        if opcao == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif opcao == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif opcao == '3':
            print(num1, "*", num2, "=", multipliy(num1, num2))

        elif opcao == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
else:
    print("Entrada inválida")