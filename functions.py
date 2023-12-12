from datetime import datetime
import holidays
import calendar
import random

def verificar_feriado(data):
    '''
    Verifica se a data passada é um feriado e retorna True ou False

    Parameters:
        data (datetime.datetime): data a ser verificada

    Returns:
        True or False
    '''
    feriados = holidays.Brazil()
    feriados.update({
        datetime(year=2023, month=12, day=31):'Ano novo',
        datetime(year=2023, month=2, day=20):'Carnaval',
        datetime(year=2023, month=2, day=21):'Carnaval',
        datetime(year=2023, month=2, day=22):'Carnaval',
        datetime(year=2023, month=5, day=1):'Dia do Trabalho',
        datetime(year=2023, month=12, day=8):'Dia de Nossa Senhora da Imaculada Conceição',
    })
    for feriado in feriados['2023-01-01':'2023-12-31']:
        if data in feriados:
            return True

def verificar_mes(data):
    '''
    Recebe uma data e verifica qual o mês, retornando a quantidade de dias

    Parameters:
        data (datetime.datetime): data do mês a ser verificado

    Returns:
        qtde_dias (int): Quantidade de dias do mês, levando em consideração fevereiro e ano bissexto
    '''
    odd_months = [
        'Jan',
        'Mar',
        'May',
        'Jul',
        'Aug',
        'Oct',
        'Dec'
    ]
    if data.month == 2:
        if calendar.isleap(data.year):
            return 29
        else: 
            return 28

    if data.strftime('%b') in odd_months:
        return 31
    else:
        return 30
    
def verificar_fds(data):
    '''
    Recebe uma data e verifica se é final de semana

    Parameters:
        data (datetime.datetime): data do dia a ser verificado

    Returns:
        True or False
    '''
    dia = data.strftime('%A')
    if dia == 'Saturday' or dia == 'Sunday':
        return True

def preencher():
    '''
    Preenche os campos com os horários
    
    Returns:
        Horário de entrada e horário de saída
    '''
    seletor = random.randint(1, 3)
    if seletor == 1:
        hora_entrada_1 = '07:0'
        hora_saida_1 = '13:0'
        hora_entrada_2 = '14:0'
        hora_saida_2 = '16:0'
        texto = str(random.randint(0, 8))
    elif seletor == 2:
        hora_entrada_1 = '06:5'
        hora_saida_1 = '13:1'
        hora_entrada_2 = '14:1'
        hora_saida_2 = '16:0'
        texto = str(random.randint(0, 6))
    else:
        hora_entrada_1 = '07:0'
        hora_saida_1 = '13:1'
        hora_entrada_2 = '14:0'
        hora_saida_2 = '16:1'
        texto = str(random.randint(0, 4))
    hora_entrada_1 += texto
    hora_saida_1 += texto
    hora_entrada_2 += texto
    hora_saida_2 += texto
    return hora_entrada_1, hora_saida_1, hora_entrada_2, hora_saida_2

