# Faça um Programa que converta metros para centímetros.
def metros_centimetros(metros):
    return metros*100

v_metros = float(input('Informe o valor em metros'))
print(f'O valor digitado {v_metros} metro(s) corresponde a {metros_centimetros(v_metros)} em centimetro(s)')