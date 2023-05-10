import PySimpleGUI as sg

layout = [
    [sg.Text('Inserire password per accedere al reattore della centrale nucleare')],
    [sg.Input(key='-IN-', expand_x=True, password_char='•')],
    [sg.Button('Accedi'), sg.Button('Chiudi')],
    [sg.Text('', key='-OUTPUT-')]
]

window = sg.Window('Accesso reattore nucleare', layout)

while True:  # Event Loop
    event, values = window.read()
    # print(event, values)
    if event == sg.WIN_CLOSED or event == 'Chiudi':
        break
    if event == 'Accedi':
        window['-OUTPUT-'].update('Accesso effettuato' if values['-IN-'] == 'passwordsupersegreta' else 'Accesso negato')
            

window.close()