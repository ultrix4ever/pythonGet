import random
import PySimpleGUI as sg


def pass_gen(length, char_list):
    password = ''
    for i in range(length):
        password += random.choice(char_list)
    return password

# Create the GUI
layout = [[sg.Text('Генератор паролей')],
          [sg.Text('Укажите сложность пароля:')],
          [sg.Checkbox('Добавить цифры', default=True), sg.Checkbox('Добавить прописные буквы', default=True),
           sg.Checkbox('Добавить строчные буквы', default=True), sg.Checkbox('Добавить символы', default=True)],
          [sg.Text('Длина пароля'), sg.Slider(range=(6, 32), default_value=8, orientation='h')],
          [sg.Text('Колличество паролей'), sg.Slider(range=(0, 32), default_value=3, orientation='h')],
          [sg.Button('Генерировать'), sg.Output(size=(35, 33), key='-OUTPUT-')]]

window = sg.Window('Targem games', layout)

# Create the password based on user input
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    length = int(values[4])
    Count = int(values[5])
    pass_list= []

    # Create the list of characters that will be used in the password
    char_list = []
    if values[0]:
        char_list.extend(list('1234567890'))
    if values[1]:
        char_list.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if values[2]:
        char_list.extend(list('abcdefghijklmnopqrstuvwxyz'))
    if values[3]:
        char_list.extend(list('!@#$%^&*()_+-='))

    # Generate the password
    for i in range(Count):
        pass_list.append(pass_gen(length, char_list))


    # Output the password
    window['-OUTPUT-'].update(print(*pass_list, sep='\n'))

# Close the GUI
window.close()