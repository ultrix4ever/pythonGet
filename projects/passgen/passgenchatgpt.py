import random
import PySimpleGUI as sg

# Create the GUI
layout = [[sg.Text('Password Generator')],
          [sg.Text('How complex do you want your password?')],
          [sg.Checkbox('Add Numbers', default=True), sg.Checkbox('Add Uppercase Letters', default=True),
           sg.Checkbox('Add Lowercase Letters', default=True), sg.Checkbox('Add Special Characters', default=True)],
          [sg.Text('Password Length'), sg.Slider(range=(8, 32), default_value=12, orientation='h')],
          [sg.Button('Generate'), sg.Output(size=(20, 10))]]

window = sg.Window('Password Generator', layout)

# Create the password based on user input
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Generate':
        break
    length = values[4]

    # Create the list of characters that will be used in the password
    char_list = []
    if values[0] is True:
        char_list.extend(list('1234567890'))
    if values[1] is True:
        char_list.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if values[2] is True:
        char_list.extend(list('abcdefghijklmnopqrstuvwxyz'))
    if values[3] is True:
        char_list.extend(list('!@#$%^&*()_+-='))

    # Generate the password
    password = ''
    for i in range(length):
        password += random.choice(char_list)

    # Output the password
    print(password)

# Close the GUI
window.close()