import random
import PySimpleGUI as sg


def pass_gen(length, char_list):
    password = ''
    for i in range(length):
        password += random.choice(char_list)
    return password

# Create the GUI
layout = [[sg.Text('Password Generator')],
          [sg.Text('How complex do you want your password?')],
          [sg.Checkbox('Add Numbers', default=True), sg.Checkbox('Add Uppercase Letters', default=True),
           sg.Checkbox('Add Lowercase Letters', default=True), sg.Checkbox('Add Special Characters', default=True)],
          [sg.Text('Password Length'), sg.Slider(range=(6, 32), default_value=8, orientation='h')],
          [sg.Text('Password Count'), sg.Slider(range=(0, 32), default_value=3, orientation='h')],
          [sg.Button('Generate'), sg.Output(size=(32, 32), key='-OUTPUT-')]]

window = sg.Window('Password Generator', layout)

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