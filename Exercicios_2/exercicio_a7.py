#Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = float(input('Informe primeiro número: '))
num2 = float(input('Informe segundo número: '))
num3 = float(input('Informe terceiro número: '))

def retorna_o_maior(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    elif n3 > n1 and n3 > n2:
        return n3


def retorna_o_menor(n1_,n2_,n3_):
    if n1_ < n2_ and n1_ < n3_:
        return n1_
    elif n2_ < n1_ and n2_ < n3_:
        return n2_
    elif n3_ < n1_ and n3_ < n2_:
        return n3_


print(f'O Maior número digitado foi: {retorna_o_maior(num1,num2,num3)}.')
print(f'O Menor número digitado foi: {retorna_o_menor(num1,num2,num3)}.')

