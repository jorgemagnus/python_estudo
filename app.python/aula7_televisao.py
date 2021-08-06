# aula7 (televisão)- Data 26/07/2021
# métodos , funções e classes

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1


#instânciar classe

if  __name__ == '__main__':
    televisao = Televisao()

    print('Televisão está ligada {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada {}'.format(televisao.ligada))
    televisao.power()
    print(f'Televisão está ligada {televisao.ligada}')
    print(f'Canal: {televisao.canal}')
    televisao.power()
    print(f'Televisão está ligada {televisao.ligada}')
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print(f'Canal: {televisao.canal}')
    televisao.diminui_canal()
    print(f'Canal: {televisao.canal}')