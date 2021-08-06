#aula 10 - datas (02/08/2021)

from datetime import date, time, datetime, timedelta


def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())
    tupla_dias_semana = ('Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo')
    print(tupla_dias_semana[data_atual.weekday()])
    data_criada = datetime(2018,6,20,15,30,20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_string,'%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
    nova_data2 = data_convertida + timedelta(days=365, hours=2, minutes=15)
    print(nova_data)
    print(nova_data2)


def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%A %B %y'))

def trabalhando_com_time():
    horario = time(hour=15, minute=16, second=30)
    print(horario)
    print(horario.strftime('%H:%M:%S'))



if __name__ == '__main__':

    opcao = int(input('1(date), 2(time), 3(datetime)'))

    if opcao == 1:
        trabalhando_com_date()
    elif opcao == 2:
        trabalhando_com_time()
    elif opcao == 3:
        trabalhando_com_datetime()
    else:
        print('Informe uma opção válida!')
