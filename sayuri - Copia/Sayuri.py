import pyautogui
from time import sleep
from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Text('Todas as Respostas do mundo estão aqui')],
    [sg.Button('Quem é a mulher mais bonita do mundo?')],
    [sg.Button('Pagina Saradora')],
    [sg.Button('Mistério')],
]

# Criando a janela
janela = sg.Window('Tela de todas as respostas', layout)

# Loop de eventos para capturar os eventos da janela
while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break
    if evento == 'Quem é a mulher mais bonita do mundo?':
        pyautogui.click(417,742,duration=1)
        pyautogui.write('google chrome')
        pyautogui.click(491,183, duration=4)
        pyautogui.click(989,323, duration=2) 
        pyautogui.click(524,454 )
        pyautogui.write('https://www.instagram.com/sym4hiz/',)
        pyautogui.press('enter')
        pyautogui.click(420,465, duration=6)
    elif evento == 'Pagina Saradora':
        sg.popup('Página Saradora')  
    elif evento == 'Mistério':
        sg.popup('O mistério continua...')  

# Fechando a janela ao sair do loop de eventos
janela.close()
