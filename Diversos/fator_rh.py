'''
tipos sanguineos:
a+,a-, b+, b- , ab+, ab- , o+ e o-
'''

meu_tipo_rh = input('Informe o seu tipo de sangue(Fator rh) : ').upper()
lista_rh = ['A+','A-','B+','B-','AB+','AB-','O+','O-']

if meu_tipo_rh == lista_rh[6]:
   print(f'O fator rh informado : {meu_tipo_rh}, pode doa para O+, A+, B+, AB+\n'
         f'E só pode receber de O+ e O-')
elif meu_tipo_rh == lista_rh[7]:
    print(f'O fator rh informado : {meu_tipo_rh}, pode doa para O+, A+, B+, AB+, A-, B-, AB-, O-\n'
          f'E só pode receber de O-')
elif meu_tipo_rh == lista_rh[0]:
    print(f'O fator rh informado : {meu_tipo_rh}, pode doa para A+ e AB+\n'
          f'E só pode receber de A+, A-, O+ e O-')
elif meu_tipo_rh == lista_rh[1]:
    print(f'O fator rh informado : {meu_tipo_rh}, pode doa para A+, AB+, A-, AB-\n'
          f'E só pode receber de A- e O-')
elif meu_tipo_rh == lista_rh[2]:
    print(f'O fator rh informado : {meu_tipo_rh}, pode doa para B+ e AB+\n'
          f'E só pode receber de B+, B-, O+ e O-')
elif meu_tipo_rh == lista_rh[3]:
    print(f'O fator rh informado : {meu_tipo_rh}, pode doa para B+, AB+, B-, AB-\n'
          f'E só pode receber de B- e O-')
elif meu_tipo_rh == lista_rh[4]:
    print(f'O fator rh informado : {meu_tipo_rh}, pode doa para AB+\n'
          f'E só pode receber de A+, B+, O+, AB+, A-, B-, O- e AB-')
elif meu_tipo_rh == lista_rh[5]:
    print(f'O fator rh informado : {meu_tipo_rh}, pode doa para AB+ e AB-\n'
          f'E só pode receber de A-, B-, O- e AB-')
else:
    print(f'Fator rh ({meu_tipo_rh}) informado não é válido!.')