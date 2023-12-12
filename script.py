import pyautogui as bot
from datetime import timedelta
from functions import *

# Preencher mês, ano correspondentes e nome do arquivo
ano = 2023
mes = 12
arquivo = 'Folha Freq'
data = datetime(year=ano, month=mes, day=1)

bot.hotkey('win', 's')
bot.write(arquivo)
bot.press('enter')
bot.sleep(3)
# bot.hotkey('ctrl', '-')
# bot.hotkey('ctrl', '-')
bot.click(x=631, y=521)


for i in range(verificar_mes(data)):
    if verificar_feriado(data):
        for j in range(4):
            bot.press('tab')
        bot.write('Feriado')
        for j in range(4):
            bot.press('tab')
    elif verificar_fds(data):
        for j in range(4):
            bot.press('tab')
        bot.write('Final de Semana')
        for j in range(4):
            bot.press('tab')
    else:
        entrada_1, saida_1, entrada_2, saida_2 = preencher()
        bot.write(entrada_1)
        bot.press('tab')
        bot.write(saida_1)
        bot.press('tab')

        bot.write(entrada_2)
        bot.press('tab')
        bot.write(saida_2)
        bot.press('tab')
        
        bot.press('tab')
        bot.write('8')
        for j in range (3):
            bot.press('tab')

    data = data + timedelta(days=1)

bot.hotkey('ctrl', 's')
bot.sleep(1)
bot.write('folha_ponto')
bot.press('enter')
bot.press('tab')
bot.press('enter')

