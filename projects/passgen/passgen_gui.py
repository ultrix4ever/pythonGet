import PySimpleGUI as sg
import random

digits = list('0123456789')
lowercase_letters = list('abcdefghijklmnopqrstuvwxyz')
uppercase_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
punctuation = list('!#$%&*+-=?@^_')
chars = []
passwd = []    
count = 0

def pass_gen():
    passwd = []
    for i in range(int(values['Pass_len'])):
        passwd += random.choice(chars) 
    return passwd

layout =   [[sg.Text('Выберите сложность пароля')],
            [sg.Checkbox('Включать цифры', enable_events=True, key='add_digits_in_chars')], 
            [sg.Checkbox('Включить прописные буквы', enable_events=True, key='add_upper_letters_in_chars')], 
            [sg.Checkbox('Включить строчные буквы', enable_events=True, key='add_lower_leters_in_chars')],
            [sg.Checkbox('Включить символы', enable_events=True, key='add_punctuation_leters_in_chars')],
            [sg.InputText('Укажите длину пароля', key='Pass_len')],
            [sg.InputText('Укажите колличество паролей', key='Pass_count')],
            [sg.Button('Генерировать')]]


window = sg.Window('Password generator by Targem', layout)

while True:
    event, values = window.read()
    print(event, values) 
    if event == 'add_digits_in_chars':
            chars += digits
    if event == 'add_upper_leters_in_chars':
            chars += uppercase_letters
    if event == 'add_lower_leters_in_chars':
            chars += lowercase_letters
    if event == 'add_punctuation_leters_in_chars':
            chars += punctuation

    if event == 'Генерировать':
        while True:
            pass_gen()
            count +=1
            if count > int(values['Pass_count']):
#                sg.popup_scrolled(passwd)
#                window.close()
                break
#    break 

event, values = window.read()
print(event, values)

       
            
            