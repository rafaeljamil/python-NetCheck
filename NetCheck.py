# NetCheck
# Version: 1.0
# Author: Jamil Pinheiro

# Imports necessários
import PySimpleGUI as sg  # Criador da GUI
import ctypes    # Lib pra acessar informações do sistema. Usei pra pegar resolução da tela
import checkFunc # Arquivo com a função de checar a conexão

getIp = checkFunc.myIp() # Salvando IP do computador

# Pegando a resolução da tela.
user32 = ctypes.windll.user32
x = user32.GetSystemMetrics(0)
y = user32.GetSystemMetrics(1)

sg.theme('DarkBlack')    # Aqui é o tema da janela

# Os 'widgets' que farão parte da janela. O segundo text é onde aparece o status da conexão.
layout = [  [sg.Text('Status:')],
            [sg.Text(size=(8,1), font=['Sans', 28], key='-OUTPUT-')],
            [sg.Text('IP: '), sg.Text(size=(16,1), key='-MYIP-')],      
            [sg.Button('Exit')]
]      

# A janela propriamente dita. Em 'location' eu usei a informação guardada sobre a resolução
window = sg.Window('Internet Status', layout, size=(200,150), location=((x - 210),(y - 210)))      

while True:     # O Event Loop da janela. Vai chamar o checkNet e 
                # mudar o valor de '-OUTPUT-' de acordo com o return da função
    
    checkNet = checkFunc.check() # Chamando a função e guardando o resultado na variável

    event, values = window.read(timeout=5) 
    #print(event, values)               # 'Descomenta' pra mostrar os eventos no console
    
    window['-MYIP-'].update(getIp) # Mostra o IP do computador na janela do app

    if event == sg.WIN_CLOSED or event == 'Exit':   # O break pra não dar loop infinito
        break  
    else:
        if checkNet == True: # Checando o resultado da função
            window['-OUTPUT-'].update('Online', text_color="White", background_color="green")
        else:
            window['-OUTPUT-'].update('Offline', text_color="White", background_color="red")  

window.close()